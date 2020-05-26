#!/usr/bin/env bash

docker-compose down
# Removes db volume to remove seed data.
docker volume rm selfhelpprograms_postgres
