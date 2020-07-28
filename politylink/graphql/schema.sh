#!/bin/bash

python3 -m sgqlc.introspection \
     --exclude-deprecated \
     --exclude-description \
     http://localhost:4000 \
     schema.json
sgqlc-codegen schema.json schema.py
rm schema.json