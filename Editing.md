If you want write access, please ask for it at [#xonotic on FreeNode](https://webchat.freenode.net/), we'll gladly give it to you. There is no way to allow anonymous editing on GitLab.

The official version is on [GitLab](https://gitlab.com/xonotic/xonotic/wikis/home) but we also sync it to [GitHub](https://github.com/xonotic/xonotic/wiki). Please, follow this guide when editing to make sure the wiki works properly on both.

Filenames
---------

Use dashes in page names, not underscores - dashes get converted to spaces in page titles so we have a nice title on every page

Interestingly, spaces seem to work fine in filenames for both GitHub and GitLab but I am sure they'd break *something somewhere* so let's stick to dashes.

Subdirectories
--------------

Ok to use for images and other assets

Don't use for pages (the `.md` files) - GitHub doesn't support them properly (it flattens everything - this can cause collisions, plus there is no way to link from subdir to another subdir that works on both GitLab and GitHub)

 - Put all `.md` files in root

Links to pages
-------------

Use standard markdown links: `[Text](link)` (e.g. `[Back to index](Home)` to get [Back to index](Home))

 - Don't prefix `link` with either `../link` or `/link` - both break on GitHub. Using `./link` seems to work ok but is unnecessary since we have to put everything in root anyway.

Links don't seem to be case sensitive but it's probably best to use proper capitalization just in case it breaks in some edge case somewhere.
