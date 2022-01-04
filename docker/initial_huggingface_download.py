import importlib
import argparse


import numpy as np
import tensorflow as tf

from transformers import pipeline

classifier = pipeline("zero-shot-classification", device=0)