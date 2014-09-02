Old Creating Maps
=================

**![]() this page has been replaced … I left this hear for archival purposes … and if my page ins’t good enough for you
— hutty —**

Introduction
------------

Creating maps requires the [[Netradiant]], a gtkradiant based mapping program that generates .bsp files compiled by q3map2. It helps to have a [[well packaged map]] while reading through this article.

Using Netradiant
----------------

NetRadiant is a fork of the popular Quake-based game editor, GtkRadiant, if you have familiarity with that software or another derivative of it, this For more information and more in-depth specifics, refer to the [[Netradiant]] page.

### Compiling from Source

NetRadiant is included with the git checkout from the [Repository Access](repository). On a Linux/UNIX system, the basic technique for building is to change to your **./xonotic/netradiant** directory and use ‘make’ to compile it. Resolve any dependencies. The binary file is located in **./xonotic/netradiant/install**, ‘radiant.x86’.

*directions to compile on windows \_
h3. Builds
http://www.icculus.org/netradiant/files/
h2. Map Packages
Maps are packaged as a .zip file with a .pk3 extension. They can be opened with any program that opens zip files. The pk3 gets loaded when you start the game, ]. The engine, ] reads pk3 files as it would a normal files system. You can thus create a pk3 package with any files that the engine can normally read.
h3. Package Design
h4. Naming Conventions
<mapname> should be alpha-numeric, lowercase with dashes, periods and underscores only,.pk3 — preferably they are suffixed with a version and revision. Following this convention will yield better results from scripts that use this format to help distribute your map.
h4. Required Files
maps/<mapname>.bsp - This is your compiled map file
maps/<mapname>.map - This is an open-source game, help others learn. This file is required to be in the game.
maps/<mapname>.mapinfo - This file has the meta information, global music track, gametype and game settings
maps/<mapname>.tga|png|jpg - This file is a screenshot of your map. If you don’t include this, you map doesn’t have a picture in the menu or the voting screen for servers and angels cry.
maps/<mapname>.waypoints - This is required to be added to the game, it’s for bot
maps/gfx/<mapname>*mini.tga|png|jpg - This is required to be added to the game, it’s a radar of the map. These can be generated with the command “\<”.

#### Optional/Suggested Files

This is not an exhaustive list, remember, you can include almost any file that loads with a map. (needs list of files)

#### Files You Should Never Include

csprogs.dat
progs.dat
effectsinfo.txt

By including any of the files above, you could cause undesired results. Try and use common sense about how you’re adding dimension to your map, if you have questions, ask for help.

Examples
--------

maps/tutorial-world-v1\_r2.bsp
maps/tutorial-world-v1\_r2.map
maps/tutorial-world-v1\_r2.mapinfo
maps/tutorial-world-v1\_r2.png
maps/tutorial-world-v1\_r2.waypoints
maps/gfx/tutorial-world-v1\_r2\_mini.png
maps/models/tutorial-world/crate.md3
maps/models/tutorial-world/jumppad.md3
scripts/tutorial-world/map-tutorial-world.shader
maps/sound/cdtracks/tutorial-world/main-room.ogg
maps/sound/tutorial-world/jumppad.ogg
maps/sound/tutorial-world/wind.ogg
maps/textures/tutorial-world/base\_1.tga
maps/textures/tutorial-world/floor\_1.tga
maps/textures/tutorial-world/floor\_2.tga
maps/textures/tutorial-world/floor\_1.tga
maps/textures/tutorial-world/wall\_1.tga
maps/textures/tutorial-world/wall\_2.tga

*add a well packaged map*

Testing Maps
------------

You can compile your map locally or on the build server. The build server (requires [[Repository Access]]) requires a <mapname>.mapoptions file. For more info check ask in \#xonotic.editing on irc.quakenet.org

Maps on Servers
---------------

Find a server admin to add your map. (this section needs work)

Map Repositories
----------------

***Maps must be properly packaged to be included in a repository***

An official map repository is in the planning stages, please check back later or find help on IRC.

Help
----

\#xonotic.editing on irc.quakenet.org
http://forums.xonotic.org

[Création de cartes](Français)

\<\< [[Creating\_Maps]]
