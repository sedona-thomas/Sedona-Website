#!/bin/sh

read -p "Email: " email
read -p "Host (user@host): " host
read -p "User (user@host): " user
read -p "Nickname (for host-user login): " nickname

echo "For RSA File use (copied to clipboard): ~/.ssh/id_rsa_$nickname"
pbcopy "~/.ssh/id_rsa_$nickname"
ssh-keygen -t rsa -b 4096 -C $email
ssh-copy-id -i ~/.ssh/id_rsa_$nickname.pub $user@$host

echo "\n" >> ~/.ssh/config
echo "HOST $host" >> ~/.ssh/config
echo "\tHostName $host" >> ~/.ssh/config
echo "\tUser $user" >> ~/.ssh/config
echo "\tIdentityFile ~/.ssh/id_rsa_$nickname" >> ~/.ssh/config

echo "alias $nickname=\"ssh $user@$host\"" >> ~/.zsh_aliases
echo "alias $nickname=\"ssh $user@$host\"" >> ~/.bash_aliases

source ~/.zshrc

