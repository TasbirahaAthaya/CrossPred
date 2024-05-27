#!/bin/bash

python -m venv ./pythonEnv
source ./pythonEnv/bin/activate

python -V
which python

python -m pip install -r requirements.txt

Rscript ./R_packages/limmaPkg.R

echo 'Done setting up R and Python environments'
