FROM tensorflow/tensorflow:2.7.0-gpu-jupyter
#TODO: install openssh-client
RUN \
    apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    openssh-client \
    libopenmpi-dev && \
    pip install \
    tqdm \
    mpi4py \
    keras-tuner \ 
    scikit-learn \
    transformers \ 
    datasets \
    tensorboard-plugin-profile==2.4.0 \
    gitpython==3.1.17
