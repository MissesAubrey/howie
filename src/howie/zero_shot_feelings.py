"""
Guesses feelings and needs as described by nonviolent communication using huggingface pipelines

    Copyright (C) 2022  Sioan Zohar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import importlib
import argparse


import numpy as np
import tensorflow as tf

from transformers import pipeline

from howie import feelings, needs


#boiler plate for limiting allocated GPU memory
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)


class feeling_need_guesser():
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="roberta-large-mnli",device=0)
        #self.summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
        self.num_feelings = 5
        self.num_needs = 3

    
    #def summarize(self, input_string):
    #    my_string = self.summarizer(input_string, min_length=5, max_length=30)
    #    return my_string[0]["summary_text"]

    def get_feelings(self, input_string):

        num_feelings = self.num_feelings
        num_needs = self.num_needs

        feelings_list = list(feelings.base_feelings)

        hypothesis_template = "Am I feeling {}?"
        feelings_results = self.classifier(input_string, feelings_list, hypothesis_template=hypothesis_template, multi_label=True)

        #nuanced_feelings_results = self.classifier(input_string, feelings_list, hypothesis_template=hypothesis_template, multi_label=True)

        used_needs = set()
        updated_needs = needs.needs

        my_string = "When I hear '"+input_string+"' I wonder if you're feeling "

        for idx, feeling in enumerate(feelings_results['labels'][:num_feelings]):
            sequence = "When I hear "+input_string+" do I feel "+feeling
            hypothesis_template = "because I have a need for {}?"
            need_results = self.classifier(sequence, list(updated_needs), hypothesis_template=hypothesis_template,multi_label=True)
            used_needs = used_needs.union(need_results['labels'][:num_needs])
            updated_needs = set(needs.needs).difference(used_needs)
            my_string += "\n"+feeling + " because you have a need for " 
            for need in need_results['labels'][:num_needs]:
                my_string += need+", "
            
            my_string+="?"

        my_string+="\n\n\n"
        return my_string

def parse_args():
    parser = argparse.ArgumentParser(description="Guess feelings and needs")
    parser.add_argument("input_text", help="The file or text. ")
    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    input_string = args.input_text

    too_many_guessers = feeling_need_guesser()

    result_message = too_many_guessers.get_feelings(input_string)

    print(result_message)

if __name__ =="__main__":
    main()