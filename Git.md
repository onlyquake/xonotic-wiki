Git
===

Cloning the repository
----------------------

Expected time (~2.5MiB/s): ~2m (initial checkout) + ~35m (./all update)  
Expected size: 8.6 GiB

|Repository |Size   |
|:--        |:--    |
|data       |1 GiB  |
|music      |225 MiB|
|darkplaces |17 MiB |
|netradiant |19 MiB |
|d0_blind_id|145 KiB|
|maps       |2.1 GiB|
|gmqcc      |3.3 MiB|

    git clone https://gitlab.com/xonotic/xonotic.git
    cd xonotic
     ./all update -l best

After cloning the repository
----------------------------

After you cloned the repository (using `git clone <url>`) you are ready to start creating a branch to start working.
Please check [Repository Access](Repository_Access) to make sure you checked out **all** of the repositories. `data/` for example resides in its own repository.

Compiling
---------

Run `./all compile` to compile the engine and gamecode. Add -r for a faster release build without debugging symbols.

Running
-------

Run `./all run` launch the game after compiling. `./all run dedicated` to start a dedicated server instead.

Project structure
-----------------

The game content can be divided into several distinct parts, like the `data/` directory, and some of its subdirectories. This is why there are several repositories, and a helper script to fetch and update them all. This is described in [Repository Access](Repository_Access) under “Working with the helper script ./all”

The current structure looks as follows:

| Directory | Repository |
| --------- | ---------- |
|`/`|git://git.xonotic.org/xonotic/xonotic.git|
|`/d0_blind_id`|git://git.xonotic.org/xonotic/d0_blind_id.git|
|`/darkplaces`|git://git.xonotic.org/xonotic/darkplaces.git|
|`/data/xonotic-data.pk3dir`|git://git.xonotic.org/xonotic/xonotic-data.pk3dir.git|
|`/data/xonotic-maps.pk3dir`|git://git.xonotic.org/xonotic/xonotic-maps.pk3dir.git|
|`/data/xonotic-music.pk3dir`|git://git.xonotic.org/xonotic/xonotic-music.pk3dir.git|
|`/data/xonotic-nexcompat.pk3dir`|git://git.xonotic.org/xonotic/xonotic-nexcompat.pk3dir.git|
|`/gmqcc`|git://git.xonotic.org/xonotic/gmqcc.git|
|`/mediasource`|git://git.xonotic.org/xonotic/mediasource.git|
|`/netradiant`|git://git.xonotic.org/xonotic/netradiant.git|
|`/netradiant-xonoticpack`|git://git.xonotic.org/xonotic/netradiant-xonoticpack.git|

When using the ssh protocol, the xonotic/ directory is skipped, so it’s just: git.xonotic.org/xonotic.git

You can still use the `data/` directory as base for the game since darkplaces now supports `.pk3dir` directories natively.

Creating a new branch
---------------------

By convention, branches are usually called <yourname>/<branch>.
Before creating a branch, you first have to choose a base of your branch. Then you can create your branch:
Let’s assume your name is `me`, your branch will be called `feature1` and your base will be `master`.
There are several ways of creating a branch:
You can simply create it by doing this from the xonotic directory and selecting where to branch:

    ./all branch me/feature1

This will create the branch locally and nothing else. It will not checkout the branch. You can do this now with:

    git checkout me/feature1

Another possibility would be to checkout your base, and then use `git checkout -b me/feature1`. This is usually nice if you already are on your base branch because it is a single command.

In case you want to make it available publicly, the most efficient way would be to first push the base branch as your branch on the remote:

    git push origin master:refs/heads/me/feature1
    git branch --track me/feature1 origin/me/feature1
    git checkout me/feature1

The reason for this are tracking branches.

#### Tracking branches

Whenever you are working with a branch that is available to the public, you want to know the state of your branch on the remote repository.
You can either do this manually by getting diffs and logs from `origin/me/feature1..me/feature1` using

    git log origin/me/feature1..me/feature1
    git diff origin/me/feature1..me/feature1

Or you make sure you have tracking branches.
This can be done by using `git branch —track ...` to create the branch.

#### Making a non-tracking branch a tracking branch

Most of git's magic is done in the config file. A tracking branch simple has merge information in the config. If your branch is not a tracking one and you wish to make it one, you can either push it, then remove the local version, and use `git branch —track me/feature1 origin/me/feature1` to recreate it as a tracking one, or you add the necessary config lines:

    git config branch.me/feature1.remote origin
    git config branch.me/feature1.merge refs/heads/me/feature1

Committing changes
------------------

After editing the code, you need to commit your changes. Since in git all your changes are local and you usually push to the repository after you added a set of changes, it is usually a good idea to make small commits with a good commit-message, instead of committing huge chunks of changes.

Some useful commands:

-   To add new files to the index to be committed on git commit: `git add file1 [file2...]`
-   To commit the files which have been added using `git add`: `git commit` or `git commit -m "message"`
-   To commit ALL changed files (without adding new files): `git commit -a` or again: `git commit -am "message"`

In git all your changes are local. This includes your commits! If you want your branch to be updated on the remote repository, you have to push it.

-   Usually, you can push your changes doing: `git push me/feature1`
-   If your branch is not a tracking branch: `git push origin me/feature1` or if you have an older git version you may have to do `git push origin me/feature1:refs/heads/me/feature1`

Reverting
---------

Remember that `git revert` creates a **new commit** which reverts the changes of the commit you are reverting.
This is important to avoid conflicts for others who pull from your branch.
If the change you are reverting is not yet pushed to any repository, you can also try to erase it from the history.

TODO: Add information about removing a commit from the history, and about how to remove the last commit by checkout out the previous one.

Merging and rebasing
--------------------

In git you have two ways of combining two branches: You can either merge them, which does exactly what its name suggests: it merges the commits together. Or you can rebase the branch.

Rebasing means that all your changes will be put at the end. This works by first collecting and removing all your changes, then replacing your branch with the base branch, then applying all your changes to it. Whenever something fails to apply you’ll be asked to fix it, and then issue a `git rebase —continue`

-   Merging master into me/feature1:

        git checkout me/feature1
        git merge master

-   Merging some other branches into me/feature1:

        git checkout me/feature1
        git merge branch1 branch2 brnach3

-   Rebasing my branch - you should only do this when the branch is not pushed to a remote repository regularly:

        git checkout me/feature1
        git rebase master

    in case of conflicts, edit the conflicting files, then do:

        git add conflicting_file1 [conflicting_file2...]
        git rebase --continue

TODO...
