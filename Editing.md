If you want write access, please ask for it at [#xonotic on FreeNode](https://webchat.freenode.net/), we'll gladly give it to you (unfortunately, there is no way to allow anonymous editing on GitLab). After that, you can edit the wiki online (there is an Edit button when logged in) or clone it to your machine using git (`git clone git@gitlab.com:xonotic/xonotic.wiki.git`).

The official version is on [GitLab](https://gitlab.com/xonotic/xonotic/wikis/home) but we also sync the wiki to [GitHub](https://github.com/xonotic/xonotic/wiki). Please, follow this guide when editing to make sure everything works properly on both.

- Try to keep things short and to the point
- Avoid creating lists of stuff that people will need to keep up to date, it doesn't work
- Don't duplicate information, there should be a single up-to-date source of truth, everything else should link to it
    - Improve things instead of starting from scratch, if the previous author didn't finish, you're not likely to do better if you start from nothing
    - Low hanging fruit: obliterate docs from `Docs/` subdirectory, move it to wiki, link to it instead


Links to pages
--------------

Use standard markdown links: `[Text](link)` (e.g. `[Back to main page](Home)` to get [Back to main page](Home))

- Don't prefix `link` with either `../link` or `/link` - both break on GitHub. Using `./link` seems to work ok but is unnecessary since we have to put everything in root anyway.

Links don't seem to be case sensitive but it's probably best to use proper capitalization just in case it breaks in some edge case somewhere. Also, spaces and dashes seem to be freely interchangeable on GH and GL but again, probably best to use dashes.


New files
---------

For pages, capitalize at least the first letter of the filename (GitHub doesn't capitalize titles automatically, GitLab will do what it wants anyway).

Use dashes in page names, not underscores - dashes get converted to spaces in page titles so we have a nice title on every page. Some pages might have underscores in names for historical reasons - they already have many outside links (from forums, etc.) pointing to them.

Interestingly, spaces in filenames and links seem to work fine for both GitHub and GitLab, not sure if they break somewhere else, it might still be best to avoid them.

It's ok (and preferred) to put images and other assets into subdirectories but we have to **put pages in root** because GitHub doesn't support subdirs properly (it flattens everything - this can cause collisions, plus there is no way to link from subdir to another subdir that works on both GitLab and GitHub).


Automated checking
-------------------

Neither GL not GH support red links (highlighting broken links) so there's a script in [`assets/check-and-fix.py`](assets/check-and-fix.py) that finds broken links and unreachable files. To use it, clone the wiki and run the script in its root. It can also automatically move or rename files that don't follow the above guidelines if you run it with `--fix`.
