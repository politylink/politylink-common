#!/bin/bash

python3 -m sgqlc.introspection \
     --exclude-deprecated \
     --exclude-description \
     http://localhost:4000 \
     schema.json
echo "generated schema.json"
sgqlc-codegen schema.json schema.py
echo "generated schema.py"
rm schema.json
echo "removed schema.json"