#!/bin/bash

# 1. تثبيت البرامج الضرورية
echo "Installing pycodestyle..."
pip install pycodestyle

echo "Installing tmux..."
sudo apt install tmux -y
apt update
apt install -y mysql-server

# 2. إعدادات Git (بياناتك الشخصية)
echo "Configuring Git..."
git config --global user.email "abdulrahman18alghamdi@gmail.com"
git config --global user.name "iid7oomii"
git config --global credential.helper store

echo "✅ All Done! Environment is ready."
