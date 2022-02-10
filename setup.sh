echo ""

rm -rf ~/public_html/*
cp -r ~/Sedona-Website/* ~/public_html/
echo "Clear Directory: ~/public_html/"

IGNORE='README.md setup.sh'
for file in $IGNORE; do
    rm -f ~/public_html/$file
done
echo "Ignore Files: ${IGNORE}"
unset IGNORE

find ~/public_html/ -type d | xargs chmod 711
find ~/public_html/ -type f | xargs chmod 644
echo "Change Permissions: directories 711, files 644"
