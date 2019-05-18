#!/usr/bin bash

##########################################
###   user setting, change if needed   ###

compress=false

##########################################



# NOTE: This script must reside in the main xonotic repo directory

prev_dir="$PWD"

cd $(dirname "$0")


cscope_args=" -b"

# don't compress
if ! $compress; then
	cscope_args="$cscope_args"" -c"
fi

cscope_cmd="cscope"

# Windows: mingw version of cscope can't be used as it writes code path
# in Unix format to the index, making it broken for Windows apps that use it
if [ -e cscope.exe ] ; then
	cscope_cmd="$PWD""/cscope.exe "
	cscope_args="$cscope_args"" -X"
fi


echo 
echo Updating qcsrc index...

cd data/xonotic-data.pk3dir/qcsrc
find -name '*.inc' -or -name '*.q[ch]' > cscope.files
$cscope_cmd$cscope_args
if $compress; then
	$cscope_cmd -L
fi
cd ../../..
echo " Done!"


echo 
echo Updating DP index...
cd darkplaces
$cscope_cmd$cscope_args
if $compress; then
	$cscope_cmd -L
fi
cd ..
echo " Done!"


cd $prev_dir

echo 
read -n1 -r -p 'Press any key to exit.' key
