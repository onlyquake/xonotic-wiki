Compiling and Contributing
==========================

Xonotic uses [several Git repositories](Git). The `all` script in the main repo manages them, builds Xonotic and runs it. Each repo can also contain feature branches next to the stable `master` branch, check them out for WIP features.

Build Requirements
------------------

Make sure you have at least 2GB memory to compile.  This is enough for a git server, but 6GB is required to play using a git client.

[About 12GB of disk space is required for the git repositories.](Git)

### Linux

Note: `curl` isn't required but it's strongly recommended for downloading maps when playing online, `wget` is not supported for this.  

Note: The `all` script requires either `wget` or `curl`.


**Ubuntu** dependencies:

    sudo apt-get install autoconf build-essential curl git libtool libgmp-dev libjpeg-turbo8-dev libsdl2-dev libxpm-dev xserver-xorg-dev zlib1g-dev unzip

Note: On Debian, use `libjpeg62-turbo-dev` if `libjpeg-turbo8-dev` isn’t available in the package repositories.

Note: `libasound2-dev libxext-dev libxxf86vm-dev p7zip-full unzip wget x11proto-xf86vidmode-dev` might be needed but are probably already installed. `libclalsadrv-dev libsdl2-image-dev libxcb-xf86dri0-dev libxxf86dga-dev x11proto-xf86dga-dev x11proto-xf86dri-dev` should no longer be needed.

**Fedora** and other **RPM based** distro dependencies:

    autoconf automake gcc-c++ gmp-devel libjpeg-turbo-devel libtool SDL2-devel curl

Note: `x11-proto-devel` or `xorg-x11-proto-devel` might be needed but might be already installed.

**Archlinux** dependencies:

    sudo pacman -S alsa-lib curl git libjpeg-turbo libmodplug libpng libvorbis libxpm xorgproto libxxf86vm sdl2 unzip

### Windows

By default, Windows has no real environment to handle the necessary scripting and compiling tools for building Xonotic. So, what we have to do is install something called [MSYS2](http://www.msys2.org) to allow us to have a similar environment as on Linux. Download 64 bit version of MSYS2 (msys2-x86_64-xxxxxx.exe) and follow installation instructions.

Once you have completed the installation, close the current MSYS2 shell and launch a MSYS2 MINGW64 shell by running mingw64.exe (instead of the default msys2.exe) located at C:\msys64 and install the needed dependencies with this command:

    pacman --needed -S git curl zip unzip p7zip make automake autoconf libtool gcc gmp-devel mingw-w64-x86_64-{toolchain,gmp,SDL2,libjpeg-turbo,libpng,libogg}

It is recommended that you make a shortcut to MSYS2 MINGW64 shell (simply right click mingw64.exe and hit “Create Shortcut”) for easier access on your desktop or in your start menu.

You can now use this shell to continue on with the guide and clone the Xonotic repositories.

### macOS

You must first install **XCode** which comes on your installation DVD or can be downloaded from the Apple website. This package provides tools like **Git and GCC**, which are needed for successful checkout and compilation of Xonotic. Some versions of XCode come with Git and others don’t - if you don’t have Git after installing XCode get it here: [XCode installer](http://sourceforge.net/projects/git-osx-installer/files/)

Cloning the Repository and Compiling
------------------------------------

To begin downloading:

    git clone git://git.xonotic.org/xonotic/xonotic.git  # download main repo
    cd xonotic
    ./all update -l best  # download all other repos (data + game logic, maps, etc.)

The **git://** protocol uses port **9418**, which may be a problem if you’re behind a **strict firewall**. You may instead use the clone url http://git.xonotic.org/xonotic/xonotic.git (however, using the git protocol directly is preferred for performance reasons).

Now the game can be compiled and run with the following commands:

    ./all compile -r
    ./all run

**Note:** if you encounter en error similar to darkplaces#111, try `./all clean && ./all compile -r -0`.

You can use `./all compile -d` to create a slower unoptimized build with debug symbols but usually you want `-r` (which is also the new default).

The `./all run` or `./all compile` line can be followed by `dedicated` to build or run the executable for server hosting. E.g. `./all compile -r dedicated`.

The `run` command can also be followed by standard DarkPlaces commandline arguments:

    ./all run +vid_fullscreen 0

To update your Git clone:

    cd xonotic
    ./all checkout  # switch to main branch on all repos (usually master)
    ./all update  # pull and prune
    ./all compile -r  # recompile what changed

**Note:** If you intend to play on public servers, you should probably also enable the nexcompat repo to download additional textures that are used on some older unofficial maps. Use `touch data/xonotic-nexcompat.pk3dir.yes` and `./all update`. For mappers: these textures should NOT be used on new maps.

***

If you run into issues with the latest version you can easily revert to an older one. Since most bugs are caused by the game code rather that the engine, you just need to downgrade that repository. Inside the main xonotic repository, use `cd data/xonotic-data.pk3dir` and then `git checkout <some older commit>`. After that go back `cd -` and `./all compile` (with the optional `-r` flag).

Contributing and Getting Write Access
-------------------------------------

Cloning (one of) our repos and submitting MRs from there (as in any other project) works but you won't be able to use our CI setup for the data repo (which seems to need a custom runner). It's therefore a good idea to join the Xonotic group and get push access - then you can create branches in our repos and use our CI.

A condition for write (push) access is that you agree that any code or data you push will be licensed under the General Public License, version 2, with or without the “or any later version” clause. In case the directory the changes apply to contains a LICENSE or COPYING file indicating another license, then your pushed code has to be dual licensed appropriately. Subdirectories currently having a dual license:

* `data/xonotic-data.pk3dir/qcsrc/lib/warpzone` - dual licensed as “GPLv2 or later” or MIT license.

In case the code you pushed was not written by you, it is your responsibility to ensure proper licensing.

To apply for write access, add your SSH key to your GitLab account and ask for access in #xonotic on the FreeNode IRC network or [request access](https://docs.gitlab.com/ce/user/group/index.html#request-access-to-a-group) using the GitLab interface.

### Windows/Linux/macOS

Get a checkout (see above), and do:

    ./all keygen

and follow the instructions that are shown. Be sure that you've done:

    ./all update -p

After that, you can write to the repositories using the usual git commands (commit, push, ...).

Alternatively, you can use the helper script `all`.
It supports the following commands:

    ./all update

This command updates all the Xonotic repositories.

    ./all branch

Lists the branches you are currently on, in the respective repositories.

    ./all branches

Lists all the branches known for all the respective repositories.

    ./all compile

Compiles the game, assuming that you have the required libs installed.

    ./all checkout BRANCH

Switch to that branch in all repositories where its available.

    ./all commit

This command commits and pushes your local changes.

    ./all run

Starts the Xonotic client

    ./all run dedicated

Starts a Xonotic dedicated server

General Contributor Guidelines
------------------------------

1.  Before creating your local branch and committing to it, make sure you’ve configured your user settings such as your name which will display in the logs (in TortoiseGit: Settings > Git > Config).
2.  Try naming your branch myname/mychange for each patch. For instance, if your name is Alex and the change you are committing is a menu fix, use something like alex/menufix.

Further Git Information
-----------------------

About tracking remote branches:
http://git-scm.com/book/en/v2/Git-Branching-Remote-Branches

This wiki’s [Git](Git) page.

A tutorial to Git for SVN users:
http://git-scm.org/course/svn.html
