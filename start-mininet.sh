#!/bin/bash

SWITCHES=5
re='^[0-9]+$' # regex is number
if [[ $1 =~ $re ]]; then
   SWITCHES=$1
fi
echo "Using $SWITCHES switches in chain topology"

if [ $1 = "--pingall" ]; then
   PINGALL="--test pingall"
fi

if [ $2 = "--pingall" ]; then
   PINGALL="--test pingall"
fi

cd src
echo "Running sudo mn --custom topo.py --topo chaintopo,$SWITCHES --mac --switch ovsk --controller remote $PINGALL"
sudo mn --custom topo.py --topo chaintopo,$SWITCHES --mac --switch ovsk --controller remote $PINGALL