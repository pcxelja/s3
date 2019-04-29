#!/bin/bash

apt-get install python-mysqldb
apt-get install python-setuptools
apt-get install python-dev

pip install --upgrade pip
pip install --upgrade setuptools
#pip install mysqlclient

#pip install mysql-python
#pip install mysqldb

python ./app/app.py
