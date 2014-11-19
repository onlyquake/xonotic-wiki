Compiling in Windows
====================

**THIS IS OUTDATED**: the versions of MinGW and MSYS are not recent enough to compile Xonotic. **Do not use xonpatch.** If you want to set up a build environment, you will need the tools mentioned in this deprecated article in more recent versions. Feel free to ask for assistance on the forums or on ouc IRC channels. If you succeed, please consider updating this page.

**NOTE**: there is an experimental automated building pack for Windows that uses a portable version of the tools mentioned in this article.
If you are planning on contributing to the project, it is best to follow the tutorial. If you are just interested in running and testing the game, you can find the build system [here](http://forums.xonotic.org/showthread.php?tid=666).

Prerequisites
-------------

### MinGW / MSYS

You first need to install a compiler and a shell environment to run the build scripts. On windows, we use MinGW and MSYS. Those two work together, so you have to install MinGW first.
It can be found [here](http://sourceforge.net/projects/mingw/files/) . Run the automated installer, and do not check any of the optional components, all you need from MinGW is its C compiler, which is always installed.
**Important**: install MinGW in a path containing no spaces. The default path is good: c:

Next, you need to install MSYS. The recent versions don’t have an installer, so it is easier to install [version 1.0.11](http://downloads.sourceforge.net/mingw/MSYS-1.0.11.exe) .
**Important**: again, the installation path should contain no spaces. The default is c:After it is done installing, a terminal will pop up, asking you to run the post-install script. Answer yes, and when it asks for the MinGW install path, input it as c:/mingw .
**Note**: If the terminal window instantly closed it self and you never got a chance to input the mingw path etc (And if you’re on Vista or Win7). Then go to c:.0\\postinstalland right-click pi.bat and choose ‘Run as administrator’.

### msysGit

You will need msysGit to download the Xonotic source files from the repositories and keep them up to date. You can get msysGit [here](http://code.google.com/p/msysgit/) . Download the “Full installer for official Git” file.
The default install options should be good.

Downloading the Xonotic sources
-------------------------------

Open git bash, and type those two commands:

    cd /c/msys/1.0
    git clone git://git.xonotic.org/xonotic/xonotic.git

(Tip: you can paste text in the console with the Shift-Insert keyboard shortcut)

This will install the Xonotic root repository in c:.0\\xonotic

When the download is done, type

    cd xonotic
    ./all update -l best

This will download approximately 2 gigabytes of data, and use 4 gigabytes in disk space.
This will take a while, but you can already get started on the next step.

Setting up the environment
--------------------------

To run and compile Xonotic, the “all” script must be able to access msysGit from MSYS, as well as wget and unzip. The xonpatch bundle patches your MSYS installation to sort this out.

**Important**: if you have followed a previous version of this guide where the “profile” file had to be edited manually, download the original msys1.0.11 profile file from the attachments on this page (or from [this link](http://dev.xonotic.org/attachments/84/profile.zip)), and unzip it in c:.0\\etc before applying the xonpatch.

The process is simple: download the latest xonpatch from the attachments (or from [this link](http://dev.xonotic.org/attachments/91/xonpatch_1-2.zip)), and extract it in c:.0 . Then, launch xonpatch.bat. This will make msysGit visible from MSYS, and add wget as well as unzip.

Compiling and running the game
------------------------------

When the cloning of all the repositories is done, open **MSYS** (not git bash this time) and type:

    cd /xonotic
    ./all compile

This will compile the engine, QC compiler, and game progs. When this is done, you can then run the game with:

    ./all run

Updating
--------

To update, all you need to do is open MSYS and:

    cd /xonotic
    ./all update
    ./all compile

The most recent Xonotic development version is then ready to run.

