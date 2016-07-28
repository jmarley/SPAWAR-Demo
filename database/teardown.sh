#!/bin/bash

docker stop snifferdb
docker rm snifferdb
docker run -p 3306:3306 \
--name snifferdb \
-e MYSQL_USER=admin \
-e MYSQL_ROOT_PASSWORD=sniffered \
-e MYSQL_PASSWORD=pungent \
-d mysql
