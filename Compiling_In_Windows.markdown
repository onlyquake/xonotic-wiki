Compiling In Windows
====================

{{\>toc}}

**This guide has been replaced by a shorter alternative.** This guide should still work, and get you a standalone MinGW/MSYS environment with access to msysgit. The new method only makes use of msysgit and is therefore easier and faster to set up. See the [Repository Access\#Windows][Repository Access\#Windows] page.

This is an unofficial updated version of the outdated [[Outdated Compiling in Windows|Compiling in Windows]] page. There are no more automated tools in this version of the guide.

You will need about 10 gigabytes of disk space to keep the sources (the uncompressed texture files are quite large and git keeps a backup copy, doubling the actual size of the sources).

Step 1: installing the prerequisites
------------------------------------

To compile and run Xonotic in Windows, you will need to download the following. Do not install anything yet, this is covered in the next section.
\* The latest version of [MinGW](http://sourceforge.net/projects/mingw/files/). At the time of writing this guide, mingw provides an installer (mingw-get-inst). More up-to-date information on how to get MinGW can be found on http://mingw.org
\* [msysgit](https://code.google.com/p/msysgit/downloads/list). Make sure you get the latest **full installer for official Git** (not the self-contained packages). At the time of writing this, the latest installer is called Git-1.7.11-preview20120710.exe.

### Installing MinGW

These instructions apply to mingw-get-inst. Run the installer. When setting up the path, if you do not pick the default, make at least sure that the installation path you choose contains no space in it. Thus, Program Files is out of question.

When you reach the “select components” section, you need to check “MSYS Basic System” (**not** “MinGW Developer Toolkit”). You will also need the C compiler, which should be selected by default.

When the setup is complete, you will get a “MinGW Shell” in your start menu. This is a Unix-like shell that you will soon use to manage and compile the Xonotic source files. It will also be used to launch the game.

### Installing msysgit

Run the installer. At the component selection screen (screenhsot: attachment:“git-1-components.png”), uncheck the “Associate .sh files” option. Windows Explorer Integration can also optionnally be unselected — it is only useful if you plan on contributing and do not like using git purely from the command line to do so. When you get to the PATH adjusting screen (screenshot: attachment:git-2-path.png), you need to select the second option (Run Git from the Windows Command Prompt). This ensures that git can be run from the MinGW shell, as we will not use the shell that comes with msysgit for this. Finally, in the line ending screen (screenshot: attachment:git-3-crlf.png), keep the first option selected unless you know what you’re doing.

### Installing the dependencies in MinGW

Xonotic requires a few more packages in MinGW that are not provided by default. Installing them is quite simple, just open a MinGW Shell and type the following line:

    mingw-get install msys-wget msys-unzip mingw32-libiconv mingw32-libintl msys-libopenssl

You can paste text in the shell by right-clicking the title bar and selecting *Edit* \> *Paste*. But be careful with this, mistakes can happen!

To close a MinGW Shell, just type

    exit

But keep this one open, we’re going to use it some more.

To close a MinGW Shell, just type

    exit

But keep this one open, we’re going to use it some more.

Step 2: downloading the Xonotic source files
--------------------------------------------

In this step, we will clone the Xonotic git repositories inside MinGW’s install directory.

In your MinGW Shell, type

    git clone git://git.xonotic.org/xonotic/xonotic.git

This will clone the base repository, which contains a script called “`all`” that will manage the subrepositories. I will call this script `./all` to avoid confusion, as this is how we will be using it in the terminal.

Next, type

    cd xonotic
    ./all update -l best

The `cd` line tells the Shell to go inside the `xonotic` directory, where `./all` is located. In the second line, the `-l best` part asks `./all` to pick the best available mirror. This step will dowload several gigabytes of data, so expect it to take a while.

Step 3: compiling
-----------------

Compiling the game is quite simple. In your MinGW Shell, just type

    ./all compile

This will compile fteqcc (which is a compiler for the QuakeC language), then the game code using fteqcc, then the DarkPlaces engine.

This step can take a few minutes, so be patient! When it’s over, check the last few lines to see if it reports any errors.

Step 4: running the game!
-------------------------

To run the game, you have to use `./all` again:

    ./all run

If you ever need to start the game in windowed mode, you can launch it this way:

    ./all run +vid_fullscreen 0

By default, `./all` uses the SDL build (called `xonotic-sdl.exe` in releases). You can use the WGL build (`xonotic.exe`) like this:

    ./all run wgl

You will always need to use `./all` to launch the game. Do not forget that you need to be in the `xonotic` directory when you use the `./all` command. That means you have to type

    cd xonotic

when you start a MinGW Shell before updating, compiling, or running Xonotic.

Keeping up to date
------------------

To keep up to date, all you need to do is repeat some of the steps above. More precisely, here is what you will usually type in a new MinGW Shell to update Xonotic to the latest git revision:

    cd xonotic
    ./all update
    ./all compile

You can optionally use this as the third line if the compilation does not work:

    ./all compile -c

This will remove the partially compiled files from the previous compiles. It has been known to resolve some errors before, but it can take a little longer to recompile everything.

Getting help
------------

You can always ask for help in the [Xonotic forums](http://forums.xonotic.org), under the Help and Support section.
