FROM tensorflow/tensorflow:2.7.0-gpu-jupyter
COPY initial_huggingface_download.py /tf/
RUN \
    apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
    openssh-client \
    libopenmpi-dev && \
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
    tensorboard-plugin-profile==2.4.0 \
    gitpython==3.1.17 && \ 
    python /tf/initial_huggingface_download.py

