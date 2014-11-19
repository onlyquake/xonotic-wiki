#!/bin/sh
# Textile to Markdown in-place conversion
for file in `ls *.md`; do
	[ -f ${file} ] && [ ! -h ${file} ] || continue
	pandoc -f textile -t markdown_github ${file} > ${file}.bak
	mv ${file}.bak ${file}
done
