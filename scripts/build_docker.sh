#!/bin/bash

set -euo pipefail

IMAGE="ghcr.io/bigchunguz24/fields"
TAGS="${1:-latest}"

# The caller passes tags as a whitespace-separated string, for example: "latest sha-abc1234".
read -r -a TAG_ARRAY <<< "$TAGS"

if [ "${#TAG_ARRAY[@]}" -eq 0 ]; then
    echo "No Docker tags were provided." >&2
    exit 1
fi

echo "Using tags: ${TAG_ARRAY[*]}"

VERSION="${TAG_ARRAY[-1]}"
BUILD_TAGS=()

for TAG in "${TAG_ARRAY[@]}"; do
    BUILD_TAGS+=(--tag "${IMAGE}:${TAG}")

    # A missing cache image is expected on a first build.
    docker pull "${IMAGE}:${TAG}" 2>/dev/null || true
done

docker build \
    --cache-from "${IMAGE}:latest" \
    --build-arg "VERSION=${VERSION}" \
    "${BUILD_TAGS[@]}" \
    --file Dockerfile .

for TAG in "${TAG_ARRAY[@]}"; do
    docker push "${IMAGE}:${TAG}"
done
