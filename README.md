# HOWIE

A feelings and needs guessing AI.

## Tested on:

Ubuntu 20.04.1

Docker version 20.10.6, build 370c289 

NVIDIA-SMI 460.80       Driver Version: 460.80       CUDA Version: 11.2 

MODEL: DELL XPS 8940
RAM: 64GB, 2x32GB, DDR4, 2933Mhz
CPU: 10th Gen Intel(R) Core(TM) i7-10700 processor(8-Core, 16M Cache, 2.9GHz to 4.8GHz) 
GPU: NVIDIA(R) GeForce(R) RTX 2060 SUPER(TM) 8GB GDDR6

## Quick Start:

    make build-docker
    make start-docker-container
    make log-into-continer

    #outside the docker container
    docker run -p 6379:6379 -d redis:5

    #inside the docker container
    giraffe_ears "My pup was biting my sleeve while I was working because it was dinner time"

    #inside docker container, start the web app to allow other people to eventually use
    cd mysite
    python manage.py runserver 0:8000
    
    

    # the jupyter port is 8888
    # inspect the contents of jupyter_token.txt for the token to log-in
    cat jupyter_token.txt

development workflow follows numpy approach https://numpy.org/devdocs/dev/development_workflow.html

## Pip Installation:
A conda or python virtual environment can be used instead of the docker container.
    pip install -r requirements.txt
