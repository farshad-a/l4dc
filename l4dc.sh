#!/bin/bash

mode=$1

function run()
{
  echo 'Starting custom image and container build for l4dc...'
  docker-compose up -d
}

function rm()
{
  echo 'Removing custom image and container build for l4dc...'
  docker-compose down --rmi all -v
}

if [ $mode == 'run' ]
then
  run
  exit
fi

if [ $mode == 'rm' ]
then
  rm
  exit
fi

if [ $mode == 'reload' ]
then
  rm
  run
  exit
fi

echo 'sim.sh: Invalid argument!'