Repository Access and Compiling
===============================

Xonotic uses several Git repositories. There’s a helper script in the main repository to aid in checking out all relevant repositories and help you with building and running Xonotic.
The repository also contains several branches next to the stable “master” branch. So if you’re interested in the progress of a certain feature, or want to help or create a new one, you can checkout the appropriate branch.
For information on how to obtain write access, skip down to the “[Getting write access](Repository_Access#contributing-and-getting-write-access)” section.

For more information about the project's structure, see [git](Git).

***

Setting up the development environment
--------------------------------------

The first thing you must do in order to begin with development is to set up your system to be able to download and compile the Xonotic game data. Make sure you have enough memory to compile. 1GB is likely to fail. Consider setup the environment to have at least 2G free memory for the job.

### Linux

Linux already has an adequate base for development, all we really need to do here is to install the **dependencies** for the download/compilation process and then we can move right along to cloning the data.

**Ubuntu Dependencies** (independent package `x11-proto-devel` dependencies fill the rest of the Debian package dependencies):

    sudo apt-get install build-essential xserver-xorg-dev x11proto-xf86dri-dev x11proto-xf86dga-dev x11proto-xf86vidmode-dev libxxf86dga-dev libxcb-xf86dri0-dev libxpm-dev libxxf86vm-dev libsdl1.2-dev libsdl2-dev libsdl2-image-dev libclalsadrv-dev libasound2-dev libxext-dev libjpeg-turbo8-dev git-core unzip wget zlib1g-dev

Note: If using **i386** architecture, you can replace `libdsl1.2debian` with `libsdl1.2debian:i386` in the list above. On Debian, use `libjpeg8-dev` if `libjpeg-turbo8-dev` isn’t available in the package repositories. To be able to download maps from game servers when using Xonotic for online gaming, you will also need `curl` installed on your system.

For **Fedora** and other **RPM based** distro’s, compiling dependencies are as follows:

    x11-proto-devel libalsa2-static-devel libjpeg62-devel libjpeg62-static-devel libSDL2-devel

For **Archlinux** the dependencies can be installed via the following command:

    sudo pacman -S alsa-lib curl libjpeg-turbo libmodplug libpng libvorbis libxpm libxxf86dga libxxf86vm sdl2 unzip

### Windows

By default, Windows has no real environment to handle the necessary scripting and compiling tools for building Xonotic. So, what we have to do is install something called [`msysgit`](https://github.com/msysgit/msysgit/releases) to allow us to have a similar environment as on Linux. In this case, we want the download which is entirely self contained (including **build-essentials** and other core required dependencies), which at the time of writing this is called `msysGit-netinstall-1.9.5-preview20150319.exe`. Simply follow the instructions on screen at this point. **NOTE: Unless you know what you’re doing, install with default settings/directories.**

Once you have completed the installation, you should be able to launch the msysgit shell by simply finding `msys.bat` - by default, it is located at `C:`, and you can use this shell to continue on with the guide and clone and compile the Xonotic repositories. It is recommended that you make a shortcut to msysgit (simply right click the shell and hit “Create Shortcut”) for easier access on your desktop or in your start menu.

### Mac OSX

You must first install **XCode** which comes on your installation DVD or can be downloaded from the Apple website. This package provides tools like **Git and GCC**, which are needed for successful checkout and compilation of Xonotic. Some versions of XCode come with Git and others don’t - if you don’t have Git after installing XCode get it here: [XCode installer](http://sourceforge.net/projects/git-osx-installer/files/)

After your development environment is all set up, you can continue on to cloning the git repository and compiling Xonotic.

***

Cloning the repository and compiling
------------------------------------

Making sure that your environment is set up properly, you can do the following to begin downloading and compilation (execute the first line only to download):

    git clone git://git.xonotic.org/xonotic/xonotic.git
    cd xonotic
    ./all update -l best

Take care to do these steps as a **normal user** on Linux (not as superuser(aka root)), otherwise you’ll have to take care about the file permissions later on.

The **git://** protocol uses port **9418**, which may be a problem if you’re behind a **strict firewall**. You may instead use the clone url http://git.xonotic.org/xonotic/xonotic.git (however, using the git protocol directly is preferred for performance reasons).

After that, you have a working checkout of the repository. The game can be compiled and run with the following commands:

    ./all compile -r
    ./all run

**Note:** if you encounter en error similar to darkplaces#111, try `./all clean && ./all compile -r -0`.

You can use just `./all compile` to create a slower build with debug symbols but usually you want `-r`.

The `./all run` line can be followed by one of `glx` (Linux native), `sdl` (input/sound managed by SDL), `agl` (OSX native), `wgl` (Windows native), or `dedicated` (for server hosting) to choose which executable to run or compile. Seen as follows:

    ./all compile -r dedicated
    ./all run wgl
    ./all run sdl

The `run` command can also be followed by standard DarkPlaces commandline arguments:

    ./all run +vid_fullscreen 0

To update your Git clone, you can repeat the commands above without the first “git clone” line- And don’t forget to compile after you update- Like this:

    cd xonotic
    ./all checkout
    ./all update
    ./all compile -r

**Note:** The compiled binary will have a faint watermark with the git revision. To remove it completely put `set menu_watermark ""` into your `autoexec.cfg`.

***

If you run into issues with the latest version you can easily revert to an older one. Since most bugs are caused by the game code rather that the engine, you just need to downgrade that repository. Inside the main xonotic repository, use `cd data/xonotic-data` and then `git checkout <some older commit>`. After that go back `cd -` and `./all compile` (with the optional `-r` flag).

***

Contributing and getting write access
-------------------------------------

A condition for write (push) access is that you agree that any code or data you push will be licensed under the General Public License, version 2, with or without the “or any later version” clause. In case the directory the changes apply to contains a LICENSE or COPYING file indicating another license, then your pushed code has to be dual licensed appropriately. Subdirectories currently having a dual license:
\* data/qcsrc/warpzonelib - dual licensed as “GPLv2 or later” or MIT license.
In case the code you pushed was not written by you, it is your responsibility to ensure proper licensing.

To apply for write access, make an issue of type “Support” in the category “Repository” and attach your public SSH key to it. (Windows users: see the Windows section below for more on SSH keys)

### Windows/Linux/OS X

Get a checkout (see above), and do:

    ./all keygen

and follow the instructions that are shown. Be sure that you've done:

    ./all update -p

After that, you can write to the repository using the usual git commands (commit, push).

Alternatively, you can use the helper script `all`.
It supports the following commands:

    ./all update

This command updates all the Xonotic repositories.

    ./all branch

Lists the branches you are currently on, in the respective repositories.

    ./all branches

Lists all the branches known for all the respective repositories.

    ./all compile

Compiles the game, assuming that you have the required libs installed. Don't forget `-r` if you wanna actually play the game with decent fps.

    ./all checkout BRANCH

Switch to that branch in all repositories where its available.

    ./all commit

This command commits and pushes your local changes.

    ./all run xonotic

Starts the Xonotic client

    ./all run dedicated xonotic

Starts a Xonotic dedicated server

General contributor guidelines
------------------------------

1.  Before creating your local branch and committing to it, make sure you’ve configured your user settings such as your name which will display in the logs (in TortoiseGit: Settings > Git > Config).
2.  Try naming your branch myname/mychange for each patch. For instance, if your name is Alex and the change you are committing is a menu fix, use something like alex/menufix.

Further git information
-----------------------

About tracking remote branches:
http://git-scm.com/book/en/v2/Git-Branching-Remote-Branches

This wiki’s [Git](Git) page.

A tutorial to Git for SVN users:
http://git-scm.org/course/svn.html
