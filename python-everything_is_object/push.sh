#!/bin/bash

if [ -z "$1" ]; then
  exit 1
fi

msg="$1"

git add .
git commit -m "$msg"
git push
