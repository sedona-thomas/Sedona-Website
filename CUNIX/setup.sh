#!/usr/bin/env bash

echo "Move website files to ~/public_html/"

find ~/public_html/ -type d | xargs chmod 711
find ~/public_html/ -type f | xargs chmod 644
echo "Changed permissions: directories 711, files 644"
