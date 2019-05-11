#!/usr/bin bash

# NOTE: This script must reside in the main xonotic repo directory

prev_dir="$PWD"

cd $(dirname "$0")

cscope_cmd="cscope -bc"

# Windows: mingw version of cscope can't be used as it writes code path
# in Unix format to the index, making it broken for Windows apps that use it
if [ -e cscope.exe ] ; then
	cscope_cmd="$PWD""/cscope.exe -bcX"
fi


echo 
echo Updating qcsrc index...

cd data/xonotic-data.pk3dir/qcsrc
find -name '*.inc' -or -name '*.q[ch]' > cscope.files
$cscope_cmd
cd ../../..
echo " Done!"


echo 
echo Updating DP index...
cd darkplaces
$cscope_cmd
cd ..
echo " Done!"


cd $prev_dir

echo 
read -n1 -r -p 'Press any key to exit.' key
