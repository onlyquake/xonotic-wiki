h1. Repository Access

{{>toc}}

Xonotic uses several Git repositories. There's a helper script in the main repository to aid in checking out all relevant repositories and help you with building and running Xonotic.
The repository also contains several branches next to the stable "master" branch. So if you're interested in the progress of a certain feature, or want to help or create a new one, you can checkout the appropriate branch.
For information on how to obtain write access, skip down to the "[[Repository Access#Contributing-and-getting-write-access|Getting write access]]" section.

For more information about Git we have a [[Git]] page on the wiki [[Git|here]].

h2. Setting up the development environment

The first thing you must do in order to begin development is set up your system to be able to download and compile the Xonotic game data.

h3. Linux

Linux already has an adequate base for development, all we really need to do here is install the dependencies for the download/compilation process and then we can move right along to cloning the data.

Ubuntu Dependencies (independent package x11-proto-devel dependencies fill the rest of the Debian package dependencies):
<pre>
sudo apt-get install build-essential xserver-xorg-dev x11proto-xf86dri-dev x11proto-xf86dga-dev x11proto-xf86vidmode-dev libxxf86dga-dev libxcb-xf86dri0-dev libxpm-dev libxxf86vm-dev libsdl1.2-dev libsdl-image1.2-dev libclalsadrv-dev libasound2-dev libxext-dev libsdl1.2debian libjpeg-turbo8-dev git-core unzip wget
</pre>
Note: If using i386 architecture, you can replace libdsl1.2debian by ibsdl1.2debian:i386 in the list above. On Debian, use libjpeg8-dev if libjpeg-turbo8-dev isn't available in the package repositories. To be able to download maps from game servers when using Xonotic for online gaming, you will also need curl installed on your system.

For Fedora and other RPM based distro's, compiling dependencies are as follows:
<pre>
x11-proto-devel, libalsa2-static-devel libjpeg62-devel libjpeg62-static-devel libSDL-devel
</pre>

h3. Windows

By default, Windows has no real environment to handle the necessary scripting and compiling tools for building Xonotic... So, what we have to do is install something called "msysgit":https://code.google.com/p/msysgit/downloads/list to allow us to have a similar environment as on Linux. In this case, we want the download which is entirely self contained (including build-essentials and other corely required dependencies), which at the time of writing this is called "msysGit-fullinstall-1.8.0-preview20121022.exe." Simply follow the instructions on screen at this point. NOTE: Unless you know what you're doing, install with default settings/directories.

Once you have completed the installation, you should be able to launch the msysgit shell by simply finding "msys.bat"- by default, it is located at: C:\msysgit\msysgit\msys.bat, and you can use this shell to continue on with the guide and clone and compile the Xonotic repositories. It is recommended that you make a shortcut to msysgit (simply right click the shell and hit "Create Shortcut") for easier access on your desktop or in your start menu.

h3. Mac OSX

You must first install XCode which comes on your installation DVD or can be downloaded from the Apple website. This package provides tools like Git and GCC, which are needed for successful checkout and compilation of Xonotic. Some versions of XCode come with Git and others don't - if you don't have Git after installing XCode get it here: http://code.google.com/p/git-osx-installer/

After your development environment is all set up, you can continue on to cloning the git repository and compiling Xonotic.

h2. Cloning the repository and compiling

Making sure that your environment is set up properly, you can do the following to begin downloading and compilation (execute the first line only to download):

<pre>
git clone git://git.xonotic.org/xonotic/xonotic.git
cd xonotic
./all update -l best
</pre>

Take care do do these steps as normal user on Linux (not as a superuser), otherwise you'll have to take care about the file permissions later on.

The git:// protocol uses port 9418, which may be a problem if you're behind a strict firewall. You may instead use the clone url <code>http://git.xonotic.org/xonotic/xonotic.git</code> (however, using the git protocol directly is preferred for performance reasons).

After that, you have a working checkout of the repository. The game can be compiled and run with the following commands:
<pre>
./all compile
./all run
</pre>

The run line can be followed by one of "glx" (Linux native), "sdl" (input/sound managed by SDL), agl (OSX native), wgl (Windows native), or dedicated (for server hosting) to choose which executable to run or compile... Seen as follows:
<pre>
./all compile dedicated
./all run wgl
./all run sdl
</pre>

The run command can also be followed by standard DarkPlaces commandline arguments:
<pre>
./all run +vid_fullscreen 0
</pre>

To update your Git clone, you can repeat the commands above without the first "git clone" line- And don't forget to compile after you update- Like this:
<pre>
cd xonotic
./all update
./all compile
</pre>

h2. Contributing and getting write access

A condition for write (push) access is that you agree that any code or data you push will be licensed under the General Public License, version 2, with or without the "or any later version" clause. In case the directory the changes apply to contains a LICENSE or COPYING file indicating another license, then your pushed code has to be dual licensed appropriately. Subdirectories currently having a dual license:
* data/qcsrc/warpzonelib - dual licensed as "GPLv2 or later" or MIT license.
In case the code you pushed was not written by you, it is your responsibility to ensure proper licensing.

To apply for write access, make an issue of type "Support" in the category "Repository" and attach your public SSH key to it. (Windows users: see the Windows section below for more on SSH keys)

h3. Windows/Linux/OS X

Get a checkout (see above), and do:

<pre>
./all keygen
</pre>

and follow the instructions that are shown.

After that, you can write to the repository using the usual git commands (commit, push).

Alternatively, you can use the helper script "all".
It supports the following commands:

<pre>
./all update
</pre>

This command updates all the Xonotic repositories.

<pre>
./all branch
</pre>

Lists the branches you are currently on, in the respective repositories.

<pre>
./all branches
</pre>

Lists all the branches known for all the respective repositories.

<pre>
./all compile
</pre>

Compiles the game, assuming that you have the required libs installed.

<pre>
./all checkout BRANCH
</pre>

Switch to that branch in all repositories where its available.

<pre>
./all commit
</pre>

This command commits and pushes your local changes.

<pre>
./all run xonotic
</pre>

Starts the Xonotic client

<pre>
./all run dedicated xonotic
</pre>

Starts a Xonotic dedicated server

h2. General contributor guidelines

# Before creating your local branch and committing to it, make sure you've configured your user settings such as your name which will display in the logs (in TortoiseGit: Settings -> Git - > Config).
# Try naming your branch myname/mychange for each patch. For instance, if your name is Alex and the change you are committing is a menu fix, use something like alex/menufix.

h2. Further git information

About tracking remote branches:
http://www.gitready.com/beginner/2009/03/09/remote-tracking-branches.html

This wiki's [[Git]] page.

A tutorial for SVN users:
http://git-scm.org/course/svn.html
