#!/bin/bash

POXPATH=$HOME/pox
if [ -n "$1" ]; then
  POXPATH=$1
fi

echo "Using $POXPATH as pox installation folder"
cd src
if [[ ! -f $POXPATH/ext/policies.json ]]; then
  ln -s $PWD/policies.json $POXPATH/ext/policies.json
fi

if [[ ! -f $POXPATH/ext/policies.py ]]; then
  ln -s $PWD/policies.py $POXPATH/ext/policies.py
fi

if [[ ! -f $POXPATH/pox/samples/firewall.py ]]; then
  ln -s $PWD/firewall.py $POXPATH/pox/samples/firewall.py
fi

echo "Running $POXPATH/pox.py --verbose firewall"
$POXPATH/pox.py --verbose samples.firewall