Docker runtime for videoanalytics applications
==============================================

Docker based in the [official Tensorflow GPU image](tensorflow/tensorflow:latest-gpu-jupyter) that includes all requirements for [videoanalytics](https://github.com/nhorro/videoanalytics) applications.

Instructions to build:

~~~bash
docker build -t nhorro/videoanalytics-gpu:latest -f Dockerfile.gpu ../
~~~

Example configuration to run applications interactively:

~~~bash
export IMAGE_NAME=nhorro/videoanalytics-gpu:latest
xhost +
docker run --gpus all \
		   --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 \
           -it --rm \
		   --net=host \		   
		   -p 10000:8888 \
		   -v $PWD:"/app" \
		   --workdir="/app" \           
		   --device=/dev/video0:/dev/video0 \
		   -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY \
		   --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
		   $IMAGE_NAME 
~~~           

Considerations:

- Access to camera 0.
- X11 Desktop (for OpenCV visualizations, etc.)
- Jupyter is redirected to 10000.
