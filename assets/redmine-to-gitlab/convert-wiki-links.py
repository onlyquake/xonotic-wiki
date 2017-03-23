#!/usr/bin/env python
# -*- coding: utf-8 -*-

# not a simple sed script because I can do non-greedy easier here :x

# changing gollum/wiki links to markdown/markup syntax (no redlinks support... fuuu gitlab)
# but not the other way around...
# since external links and images are better left using portable markdown syntax

import os
import re

FILES = ('.md',)
RX = [
#	(re.compile(r''), ''),
	# I'm sure this could be cleaner... but it works (order is important (with \W for french chars), or [[a|b]] is matched to [a|b](a|b) !)
	(re.compile(r'(?u)\[\[([\w\W \\/\.#\(\)_-]+?)\|([\w\W \\/\.#\(\)_-]+?)\]\]'), r'[\1](\2)'), # [[This|that#top]] -> [This](that#top)
	(re.compile(r'(?u)\[\[([\w\W \\/\.#\(\)_-]+?)\]\]'), r'[\1](\1)'), # [[This]] -> [This](This)
]

path = '.'
lsdir = os.listdir(path)
for f in lsdir:
	file_name, file_extension = os.path.splitext(f)
	new_f = file_name + file_extension + '.rx'

	if file_extension in FILES:
		i = os.path.join(path, f)
		o = os.path.join(path, new_f)
		with open(i, "r") as inf, open(o, "w") as outf:
			for line in inf:
				for search, replace in RX:
					#line = search.sub(replace, line)
					line = re.sub(search, replace, line)
				outf.write(line)
		os.rename(o, i)
