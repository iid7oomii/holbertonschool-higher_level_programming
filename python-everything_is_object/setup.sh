#!/bin/bash

sudo apt update
sudo apt install -y tmux

read -p "Git email: " email
read -p "Git username: " username

git config --global user.email "$abdulrahman18alghamdi@gmail.com"
git config --global user.name "$iid7oomii"
git config --global credential.helper store
