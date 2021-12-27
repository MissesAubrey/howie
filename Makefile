IMAGE_NAME = tensorflow/tensorflow:2.7.0-gpu-jupyter

PROJECT_NAME = howie
CWD = $(shell pwd)

.PHONY: start-docker-container stop-docker-container log-into-container start-tensorboard

build-docker: docker/Dockerfile
	docker build -t $(IMAGE_NAME) docker
	docker image inspect --format='{{.Id}}' $(IMAGE_NAME)  > .build-docker
start-docker-container:
	docker run -d --shm-size=1024m --name ${PROJECT_NAME} --gpus all -p 8888:8888 -p 6006:6006 \
	--rm -it --mount type=bind,source="$(CWD)",target=/tf/${PROJECT_NAME} $(IMAGE_NAME)
	docker exec -it ${PROJECT_NAME} bash -c 'cd /tf/${PROJECT_NAME} ; pip install -e . ; jupyter notebook list > jupyter_token.txt '
stop-docker-container:
	docker exec -it ${PROJECT_NAME} bash -c 'cd /tf/${PROJECT_NAME} ; rm -rf src/${PROJECT_NAME}.egg-info/'
	docker kill ${PROJECT_NAME}
log-into-container:
	docker exec -w /tf/${PROJECT_NAME} -it ${PROJECT_NAME} bash
start-tensorboard:
	docker exec ${PROJECT_NAME} bash -c 'tensorboard --logdir /tf/${PROJECT_NAME}/work_dir/ --bind_all --load_fast=false'
