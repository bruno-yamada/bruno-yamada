# Docker

## Build image
docker build -t my-image .

## Tag image
docker tag my-image my-image:latest

## Troubleshooting
docker stats
docker ps -a
docker images -a

## Remove unused images, networks, volumes
docker rmi `docker images | awk '{ print $3; }'`
docker system prune -a
docker image prune -a
docker volume prune -a

## List reclaimable space
docker system df
