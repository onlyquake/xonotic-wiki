If you want write access, please ask for it at [#xonotic on FreeNode](https://webchat.freenode.net/), we'll gladly give it to you. There is no way to allow annoynmous editing on GitLab.

Filenames
---------

Use dashes, not underscores - dashes get converted to spaces in titles

Subdirectories
--------------

Ok to use for images and other assets
Don't use for pages (the .md files) - GitHub doesn't support them properly (it flattens everything - this can cause collisions, plus there is no way to link from subdir to another subdir that works on both GitLab and GitHub)

Links
-----

Use standard markdown links: `[Text](link)`, don't prefix `link` with either ".." or "/" - both break on GitHub. Using "." seems ok but is unnecessary since we have to put everything in root anyway.

TODO(martin-t): check that this renders properly everywhere
