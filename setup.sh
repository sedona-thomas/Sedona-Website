rm -rf ~/public_html/*
cp -r ~/Personal-Website/* ~/public_html/

IGNORE='README.md setup.sh'
for file in $IGNORE; do
    rm -f ~/public_html/$file
done
unset IGNORE

find ~/public_html/ -type d | xargs chmod 711
find ~/public_html/ -type f | xargs chmod 7644

# FOLDERS = 'config img resume shell_scripts social_media templates'
# for folder in $FOLDERS; do
# done
# unset FOLDERS
