# 🐳 Docker Image

## Build the image
docker build -t <image-name> .

## Run the container
docker run <image-name>

## Optional (run in background)
docker run -d --name <container-name> <image-name>

## Check running containers
docker ps

## Stop and remove
docker stop <container-name>
docker rm <container-name>

---

💡 **Quick Start Example**
git clone https://github.com/Jack17kdb/docker-images.git
cd docker-images

docker build -t <image> .
docker run <image>
