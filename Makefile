IMAGE_NAME = tensorflow/tensorflow:2.7.0-gpu-jupyter

CWD = $(shell pwd)

.PHONY: start-docker-container stop-docker-container log-into-container start-tensorboard

build-docker: docker/Dockerfile
	docker build -t $(IMAGE_NAME) docker
	docker image inspect --format='{{.Id}}' $(IMAGE_NAME)  > .build-docker
start-docker-container:
	docker run -d --shm-size=1024m --name bcvae --gpus all -p 8888:8888 -p 6006:6006 \
	--rm -it --mount type=bind,source="$(CWD)",target=/tf/bcvae $(IMAGE_NAME)
	docker exec -it bcvae bash -c 'cd /tf/bcvae ; pip install -e . ; jupyter notebook list > jupyter_token.txt '
stop-docker-container:
	docker exec -it bcvae bash -c 'cd /tf/bcvae ; rm -rf src/bcvae.egg-info/'
	docker kill bcvae
log-into-container:
	docker exec -w /tf/bcvae -it bcvae bash
start-tensorboard:
	docker exec bcvae bash -c 'tensorboard --logdir /tf/bcvae/work_dir/ --bind_all --load_fast=false'
