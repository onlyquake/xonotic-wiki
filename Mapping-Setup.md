Mapping - Setup
===============

How to get your system all set up to start mapping
--------------------------------------------------

### Step 1: Obtain mapping support

If you didn’t already, download the [mapping support zip](http://dl.xonotic.org/xonotic-0.8.2-mappingsupport.zip)

### Step 2: Extract zip

Extract the zip archive using your favorite archiving tool

### Step 3: Get NetRadiant working

-   **Windows**: The mapping support zip contains a compiled version of NetRadiant in the `mapping` folder
-   **Linux**: Linux users need to compile NetRadiant themselves (see [NetRadiant Repo](https://gitlab.com/xonotic/netradiant)) or can download a compiled version [here](http://ingar.intranifty.net/gtkradiant/index.html)
-   **Mac**: Current versions of MacOS/OSX don't seem to work because of gtkglext, compiled versions from [here](http://ingar.intranifty.net/gtkradiant/index.html) might work

### Step 4: Locate the folder for userdata

Locate your userdata folder, note that this is **NOT** the install location. This is the place xonotic saves your userdata.

-   **Windows**: `C:\users\user\saved games\xonotic\data`
-   **Linux**: `~/.xonotic/data`
-   **Mac**: `~/Library/Application Support/xonotic/data`

This folder has a similar layout as the game folder. Game wise these data folders are treated similarly, however, it is best to save your work in the userdata folder so that you don’t accidentally mess up your Xonotic install, or so that your work doesn’t get lost in an update.

### Step 5: Moving the mapping support pk3

The mapping support zip contains a file called `xonotic-<timestamp>-maps-mapping.pk3`. Move this file to the userdata folder (see step 4), **NOT** `data/data`.
This folder should also contain your `config.cfg`.

### Step 6: Setting up NetRadiant

When you first start up radiant it may ask where the install location is. Simply, point it to the install location. Then NetRadaint should start,and the lower right pane should have lists of texture packs. If there are no texture packs, then refer back to step 5.

\<\< [Introduction](mapping-Introduction) 1 [NetRadiant](mapping-NetRadiant) \>\>

… [Creating_Maps](Creating-Maps) …

