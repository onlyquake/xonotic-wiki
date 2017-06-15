#!/usr/bin/env python3

# Run in wiki root

# Well, this wasn't supposed to be so long and complicated.
# Anyway, it makes sure the wiki works on both Gitlab and Github by moving
# stuff around and fixing links. Then it reports all remaining broken links
# and unused files. Since the wiki is in git, you can use `git status`
# and `git diff` to see the changes. You can also use the `--dry-run` flag
# to print all changes the script would make without actually making them.

# See Editing.md for more information.

# Some stuff that could have been done better:
#  - Not parsing Markdown with regex. Currently, we for example report
#    broken links even though they're inside code blocks (e.g. Irclog.md)
#  - Using the type system (and mypy) to distinguish different link types
#    to make sure the right functions are called with the right link types
#    (e.g. page links, file links, links with headers, urls, ...)
#  - Checking outbound links for 404s.

import sys
import os
import glob
import regex  # sudo pip3 install regex
import functools
from typing import *
from os.path import normpath, join, dirname, basename


# yeah, well, this is ugly but sure beats putting the regex on one line
def compile_regex(rgx: str):
    # regex (unlike re) supports non-constant length look-behinds
    return regex.compile(
        "".join(
            [line.strip() for line in rgx]))


# examples:
# [Page link](Some_Page)
# [Url link](http://example.com)
# ![Image](image_1.png)
# [![Image link to image](image_inner.png)](image_outer.png)
# [![Image link to page](image_inner.png)](Archive/Some_Page)

# regex.sub doesnt support overlapping - we have to use lookbehinds.
# Practically, the inner link will never be a page so we don't need to
# sub it, but later we can reuse the regex to go through all the links
# and check that they're valid.
LINK_REGEX = compile_regex("""
(?<=
    \[
        (?:
            [^\[\]]*
        |
            \!\[
                [^\[\]]*
            \]
            \(
                [^()]*
            \)
        )
    \]
)
\(
    ([^()]*)
\)
""")


fix = False


def strip_header_link(link: str) -> str:
    "remove links to headers inside the file"

    header_index = link.rfind('#')
    if header_index != -1:
        link = link[:header_index]
    return link


def convert_page_name(path: str) -> str:
    "path can be with or without .md"

    if path.startswith("_"):
        # ignore header, footer etc
        return path

    if "-" in path:
        # don't wanna break stuff like mapping-entity-func_door
        return path

    headerless = strip_header_link(path)
    # don't reformat these links because they're often linked to from outside
    for exc in ["Repository_Access", "Halogenes_Newbie_Corner"]:
        if headerless == exc or headerless == exc + ".md":
            return path

    return basename(path).replace("_", "-")


def convert_page_link(link: str) -> str:
    header_index = link.rfind('#')
    if header_index != -1:
        header = link[header_index + 1:]
        if "_" in header:
            print("warning: underscore in header: {}".format(link))
    return convert_page_name(link)


def find_paths() -> Tuple[List[str], List[str]]:
    all_paths = sorted(filter(
        os.path.isfile,
        [name for name in glob.iglob('**', recursive=True)]))
    md_paths = sorted(filter(lambda s: s.endswith(".md"), all_paths))
    return all_paths, md_paths


def fix_dir_structure():
    _, md_paths = find_paths()
    for path in md_paths:
        fixed = convert_page_name(path)
        if fixed == path:
            continue

        if os.path.exists(fixed):
            print("warning: collision: {}".format(path))
        elif fix:
            os.rename(path, fixed)
        else:
            print("would rename {} to {}".format(path, fixed))


def is_between_files(link: str) -> bool:
    if "://" in link or link.startswith("#"):
        # http(s) link or link to header on the same page
        return False
    else:
        return True


def is_page_link(link: str) -> bool:
    # this is a best guess, i don't think there is a foolproof way to tell

    if link.startswith("assets") or link.startswith("img"):
        # hopefully nobody adds more directories
        return False
    if "." in basename(link):
        # hopefully it's an extension
        return False
    # files in root without extension will fail

    return True


def replace_link(changes: List[str], match) -> str:
    text = match.group()
    link_start = match.start(1) - match.start()
    link_end = match.end(1) - match.start()

    link = text[link_start:link_end]

    if is_between_files(link) and is_page_link(link):
        new_link = convert_page_link(link)
        new_text = text[:link_start] + new_link + text[link_end:]
        if text != new_text:
            changes.append("\t{} -> {}".format(text, new_text))
        return new_text
    else:
        return text


def fix_links():
    _, md_paths = find_paths()
    for path in md_paths:
        with open(path, 'r+') as f:
            contents = f.read()

            changes = []
            replacer = functools.partial(replace_link, changes)
            contents_new = LINK_REGEX.sub(replacer, contents)
            if fix and contents != contents_new:
                f.seek(0)
                f.write(contents_new)
                f.truncate()
            elif not fix and any(changes):
                print("would convert these links in {}:".format(path))
                for change in changes:
                    print(change)


def link_to_path(current_file: str, link: str) -> str:
    #           nothing     .           ..          /
    # gitlab    root        current     current     root
    # gollum    current     current     current     root
    # github    ok          ok          broken      broken

    # when not using subdirs, nothing or "." works for all 3

    if link.startswith("..") or link.startswith("/"):
        print("file: {} bad link: {}", link)

    # path relative to wiki root, not curent file
    current_dir = dirname(current_file)
    link = normpath(join(current_dir, link))

    link = strip_header_link(link)

    # page links don't have an extension - add it
    extension_index = link.rfind('.')
    if extension_index == -1:
        link = link + '.md'

    return link


def get_file_links(path: str) -> Generator[str, None, None]:
    with open(path, 'r') as f:
        contents = f.read()
        for match in LINK_REGEX.finditer(contents):
            link = match.group(1)

            if is_between_files(link):
                yield link


def canonicalize(path: str) -> str:
    # spaces and capitalization don't seem to matter for pages
    if path.endswith(".md"):
        return path.replace(" ", "-").casefold()
    else:
        return path


def find_broken(all_paths: List[str], md_paths: List[str]):
    canonical_paths = [canonicalize(path) for path in all_paths]

    for path in md_paths:
        if path == "Irclog.md":
            continue  # TODO need to parse MD properly to avoid false posiives
        for link in get_file_links(path):
            link_target = canonicalize(link_to_path(path, link))
            if not link_target in canonical_paths:
                #print("broken link in {}: {} -> {}".format(path, link, link_target))
                print("broken link in {}: {}".format(path, link))


def walk_links(canonical_to_real: Dict[str, str], is_linked: Dict[str, bool], current_path: str):
    canonical = canonicalize(current_path)
    if canonical not in canonical_to_real:
        # broken link - nothing to do here, we check broken links elsewhere
        # because here we're not guaranteed to walk through all files
        #print("not in known paths: {}".format(current_path))
        return

    current_path = canonical_to_real[canonical]

    if is_linked[current_path]:
        return

    is_linked[current_path] = True
    if current_path.endswith(".md"):
        for link in get_file_links(current_path):
            link_target = link_to_path(current_path, link)
            walk_links(canonical_to_real, is_linked, link_target)


def find_unlinked(all_paths: List[str]):
    canonical_to_real = {canonicalize(path): path for path in all_paths}
    is_linked = {path: False for path in all_paths}

    # ignore these 2 - currently they don't show on GitLab but do on GitHub
    is_linked["_Footer.md"] = True
    is_linked["_Sidebar.md"] = True

    walk_links(canonical_to_real, is_linked, "Home.md")

    for path, linked in sorted(is_linked.items()):
        if not linked:
            print("not reachable from Home: {}".format(path))


def check_links():
    all_paths, md_paths = find_paths()
    find_broken(all_paths, md_paths)
    find_unlinked(all_paths)


def main():
    global fix
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        fix = True

    # convert file paths - put everything into root
    fix_dir_structure()

    # convert links on all pages
    fix_links()

    # look for broken links and unlinked files
    check_links()


if __name__ == '__main__':
    main()
