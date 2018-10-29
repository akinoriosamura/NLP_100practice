#! /usr/bin/bash

# get commit message
read -p "commit message: " str

# update github
git add .
git commit -m $str
