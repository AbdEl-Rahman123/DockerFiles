#!/bin/bash

# Define the container name and output directory
CONTAINER_NAME=welcome-to-docker
OUTPUT_DIR=/home/abdo/bd-a1/service-result/

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# List of files to copy
FILES_TO_COPY=(
  "res_dpre.csv"
  "eda-in-1.txt"
  "eda-in-2.txt"
  "eda-in-3.txt"
  "vis.png"
  "k.txt"
)

# Copy the output files from the container to the local machine
for file in "${FILES_TO_COPY[@]}"; do
  if docker exec "$CONTAINER_NAME" test -e "/home/doc-bd-a1/$file"; then
    docker cp "$CONTAINER_NAME:/home/doc-bd-a1/$file" "$OUTPUT_DIR"
  else
    echo "File $file does not exist in the container."
  fi
done

# Stop the container
docker stop "$CONTAINER_NAME"
