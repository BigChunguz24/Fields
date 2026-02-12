#!/bin/bash

IMAGE="ghcr.io/bigchunguz24/fields"
TAGS=latest
VERSION=none

# Override tags with param1
if [ ! -z "$1" ] ; then
    TAGS="$1"
fi

echo "Using tags: ${TAGS}"

BUILD_TAGS=""
for TAG in ${TAGS} ; do
    BUILD_TAGS="${BUILD_TAGS} --tag ${IMAGE}:${TAG} "
    docker pull ${IMAGE}:${TAG} 2>/dev/null || true

    # last part of TAGS is commit SHA, if available
    VERSION=${TAG}
done

docker build \
    --cache-from ${IMAGE}:build \
    --cache-from ${IMAGE}:build-venv \
    --cache-from ${IMAGE}:latest \
    --build-arg VERSION=${VERSION} \
    ${BUILD_TAGS} \
    --file Dockerfile .

for TAG in ${TAGS} ; do
    docker push ${IMAGE}:${TAG}
done
