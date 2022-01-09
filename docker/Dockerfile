FROM tensorflow/tensorflow:2.7.0-gpu-jupyter
COPY initial_huggingface_download.py /tf/
RUN \
    apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    openssh-client \
    libopenmpi-dev && \
    python -m pip install --upgrade pip && \ 
    python -m pip install \
    tqdm \
    mpi4py \
    keras-tuner \ 
    scikit-learn \
    transformers \ 
    Flask \ 
    Django \
    channels \
    channels_redis \
    datasets \
    tensorboard-plugin-profile \
    gitpython && \ 
    python /tf/initial_huggingface_download.py

