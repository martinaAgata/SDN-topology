#!/bin/bash

POXPATH=$HOME/pox
if [ -n "$1" ]; then
  POXPATH=$1
fi

echo "Using $POXPATH as pox installation folder"
cd src
cp policies.json $POXPATH/ext/policies.json
cp policies.py $POXPATH/ext/policies.py
cp firewall.py $POXPATH/ext/firewall.py

echo "Running $POXPATH/pox.py --verbose firewall"
$POXPATH/pox.py --verbose firewall