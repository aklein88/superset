#!/bin/bash

#compose_file="docker-compose.yml"
compose_file="docker-compose-custom.yml"
#compose_file="docker-compose-non-dev.yml"
#compose_file="docker-compose-image-tag-custom.yml"
#compose_file="docker-compose-build.yml"

start() {
  echo "Starting Apache Superset..."
  #export TAG=5.0.0  
  docker compose -f $compose_file up -d
}

stop() {
    echo "Stopping Apache Superset..."
    docker compose -f $compose_file down
}

logs() {
    echo "Stopping Apache Superset..."
    docker compose -f $compose_file logs -f
}

build() {
    echo "Building Apache Superset..."
    docker compose -f $compose_file build
}

init() {
    current_dir=$(dirname "$0")
    sudo sh -c "cd $current_dir/superset-frontend && npm install && npm run dev"
}

reset() {
    echo "Deleting Apache Superset volumes..."
    docker volume rm -f superset_db_home
    docker volume rm -f superset_redis
    docker volume rm -f superset_superset_home
}

reset_test() {
    echo "Deleting Apache Superset volumes..."
    docker volume rm -f superset_db_home_test
    docker volume rm -f superset_redis_test
    docker volume rm -f superset_superset_home_test
}

strUsage="Usage: $0 {start|stop|logs|build|init}"

if [ ! $# -eq 1 ]; then
    echo $strUsage
    exit 1
fi

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    logs)
        logs
        ;;
    build)
        build
        ;;
    init)
        init
        ;;
    delete-volumes)
        reset
        ;;
    delete-volumes-test)
        reset_test
        ;;
    *)
        echo "Invalid option: $1"
        echo $strUsage
        exit 1
        ;;
esac
