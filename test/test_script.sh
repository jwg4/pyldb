#!/bin/bash

python3 setup.py sdist

mkdir temp
cp -R test/ temp
cp dist/pyLDB-*.tar.gz temp

cd temp/
virtualenv venv -p python3
. venv/bin/activate

pip install pyLDB-*.tar.gz
pip install requests
python -m unittest discover test