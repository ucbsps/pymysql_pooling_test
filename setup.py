#!/bin/bash

python -m pip install virtualenv

virtualenv -p python3.7 venv

venv/bin/pip install pymysql
# venv/bin/pip install pymysql-pooling # conflicts with pymysql-pool
venv/bin/pip install DBUtils
venv/bin/pip install pymysql-pool
