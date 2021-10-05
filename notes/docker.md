# Docker

## Docker mem/cpu/disk usage
docker stats

## Remove unused images
docker rmi `docker images | awk '{ print $3; }'`
docker image prune -a

## List reclaimable space
docker system df
