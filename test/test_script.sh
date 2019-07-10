#!/bin/bash

mkdir temp
cp -R test/ temp

cd temp/
virtualenv venv
. venv/bin/activate

pip install ../
python -m unittest discover test