#!/bin/sh
# optimizing binary file size

SRC_DIR="images-prep"
DST_DIR="images"
OLD_DIR="images-old"


SELF=`basename $0`;
if ! [ -f ./$SELF ]; then
	echo "Cannot find myself."
	exit 1
fi
d=`pwd`
SELF="$d/$SELF"
cd $d

mkdir -p ${OLD_DIR}

cd ${SRC_DIR}
for image in `ls *.png`; do
	pngcrush -oldtimestamp ${image} $d/${DST_DIR}/${image} #|| echo "error processing $image - fix it" && exit 1
	mv ${image} $d/${OLD_DIR}/${image}
done
for image in `ls *.jp*g`; do
	jpegoptim --preserve -d $d/${DST_DIR}/ ${image} #|| echo "error processing $image - fix it" && exit 1
	mv ${image} $d/${OLD_DIR}/${image}
done
cd $d
