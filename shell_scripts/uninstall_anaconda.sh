#! /bin/sh

conda install anaconda-clean --yes

anaconda-clean --yes

rm -rf ~/opt                   2> /dev/null
rm -rf ~/anaconda3             2> /dev/null
rm -rf ~/anaconda2             2> /dev/null
rm -rf ~/.anaconda_backup      2> /dev/null
rm -rf ~/.anaconda             2> /dev/null
rm -rf ~/.conda                2> /dev/null

