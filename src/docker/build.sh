#!/usr/bin/env bash


# how to enter an intermediate image and debug what is going on:
# docker run --rm -it <id_last_working_layer> bash -il

# start new (detached) container with port forwarding (--rm removes the container after shutdown of the container):
# docker run --rm --name <container_name> -d -v /<host_path>:/<container_path> -p 5000:5000 <image_id>

# enter a running container as root user:
# sudo docker exec -it -u root <container_id> bash



SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CONTEXT_DIR="${SCRIPT_DIR}/../.."
echo "Script dir: ${SCRIPT_DIR}"
echo "Build context dir: ${CONTEXT_DIR}"


sudo docker build -t groceries_list -f ${SCRIPT_DIR}/Dockerfile ${CONTEXT_DIR}
