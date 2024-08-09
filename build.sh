#!/bin/bash

docker build -t ghcr.io/miguensone/github-gitlab-sync:latest .
docker push ghcr.io/miguensone/github-gitlab-sync:latest
