### Faster compiling and reloading of QuakeC

You can use `QCCFLAGS_WERROR="" ZIP=: ./all compile` to let the build succeed even with warnings and to skip compressing the resulting csprogs.dat (client gamecode) into a pk3.

Server and menu code produce progs.dat and menu.dat respectively.

No need to restart Xonotic to load the new client and server code, just start a new map with `map XXX` (depending on how you launch Xonotic you may need to use `fs_rescan; map XXX`). You can restart the menu with `menu_restart`.

### Debug prints

Use `con_notify 4` together with `LOG_INFOF("my_var: %s", my_var);` (`%s` string, `%f` float, `%d` integer, `%v` vector) to see debug output without opening the console. Type `con_notify` and press `<TAB>` to see descriptions and more options (or use `apropos con_notify`).

You can draw text anywhere on the map using `debug_text_3d(world_coords, message);` from `common/debug.qh`.

### Multiple clients + clean config

If you need 2 players for debugging, you can launch another client locally:
- use -sessionid (e.g. `./all run -sessionid testing`) to keep your config
- use -userdir (e.g. `./all run -userdir ~/.xonotic-testing +name tester +cl_allow_uid2name 0`) to get a clean config (if you delete the dir before each use)
  - you can set any cvar or run any command on start with `+cvar_name value`
    - `+name tester` avoids the nick selection dialog
    - `+cl_allow_uid2name 0` avoids an annoying popup 

### Testing with bots

You can prevent bots from firing with `bot_nofire 1` or stop them completely with `bot_cmd * pause` (unstop them with `bot_cmd * continue`). With `sv_cheats 1` (takes effect next match), you can drag them around (default key V or 'drag object' in menu).

Note that `sv_cheats 1` prevents bots from spawning in the campaign (should you decide to put it in your `autoexec.cfg` and later wonder why the campaign is broken).

### Debugging

Useful commands to debug qc code:
```
prvm_breakpoint : marks a statement or function as breakpoint (when this is executed, a stack trace is printed); to actually halt and investigate state, combine this with a gdb breakpoint on PRVM_Breakpoint, or with prvm_breakpointdump; run with just progs name to clear breakpoint

prvm_edict    : print all data about an entity number in the selected VM (server, client, menu)
prvm_edictget : retrieves the value of a specified property of a specified entity in the selected VM (server, client menu) into a cvar or to the console
prvm_edicts   : prints all data about all entities in the selected VM (server, client, menu)
prvm_edictset : changes value of a specified property of a specified entity in the selected VM (server, client, menu)
prvm_edictwatchpoint : marks an entity field as watchpoint (when this is executed, a stack trace is printed); to actually halt and investigate state, combine this with a gdb breakpoint on PRVM_Breakpoint, or with prvm_breakpointdump; run with just progs name to clear watchpoint

prvm_global    : prints value of a specified global variable in the selected VM (server, client, menu)
prvm_globalget : retrieves the value of a specified global variable in the selected VM (server, client menu) into a cvar or to the console
prvm_globals   : prints all global variables in the selected VM (server, client, menu)
prvm_globalset : sets value of a specified global variable in the selected VM (server, client, menu)
prvm_globalwatchpoint : marks a global as watchpoint (when this is executed, a stack trace is printed); to actually halt and investigate state, combine this with a gdb breakpoint on PRVM_Breakpoint, or with prvm_breakpointdump; run with just progs name to clear watchpoint
```

Examples:  
Print to console origin of entity number 1: `prvm_edictget server 1 origin`  
Save to a cvar origin of entity number 1: `prvm_edictget server 1 origin my_cvar`  
Set a custom origin for entity number 1: `prvm_edictset server 1 origin "100 200 0"`

Setting view angles requires a particular trick, we also need to set fixangle to true in the same server frame:
`prvm_edictset server 1 fixangle 1; prvm_edictset server 1 angles "20 -90 0"`

Print to console vid_conheight client global: `prvm_edictget client vid_conheight`

"Break" on statement: `prvm_breakpoint server 12345`  
"Break" on function: `prvm_breakpoint server ClientConnect`  
Watch for global change: `prvm_globalwatchpoint server time`  
Watch for entity field change: `prvm_edictwatchpoint server 1 health`  

There can be only one of each kind. To clear, do:
```
prvm_breakpoint server
prvm_globalwatchpoint server
prvm_edictwatchpoint server
```

### Doxygen

Incomplete [Doxygen documentation](https://timepath.github.io/scratchspace/index.html) is generated as part of CI on [xonotic-data.pk3dir](https://gitlab.com/xonotic/xonotic-data.pk3dir) - you can search functions, "classes", globals, etc.

Note that it might be incomplete or incorrect because Doxygen doesn't understand all of QC's constructs and our code heavily uses macros. See the [CI file](https://gitlab.com/xonotic/xonotic-data.pk3dir/blob/master/.gitlab-ci.yml) for details what's missing.

### Tool to find C symbols, functions, declarations and definitions inside source code

For this purpose it's possible to use a text-based tool called [Cscope](https://en.wikipedia.org/wiki/Cscope) together with a GUI (it can be either an application or a plugin for a text editor).

##### Download / Installation

* Download and install cscope with `pacman -S cscope`  
Windows users must download the Windows version of cscope from https://code.google.com/archive/p/cscope-win32/downloads and put it into the main xonotic repo directory. The mingw version can't be used as it puts Unix paths into the generated indices, making them unusable.

* Download and install a cscope GUI or a plugin for your text editor / IDE.
  * For [jEdit](http://www.jedit.org) there is a plugin called [CscopeFinder](http://plugins.jedit.org/plugins/?CscopeFinder).
  * For [SublimeText](https://www.sublimetext.com) there is [SublimeCscope](https://github.com/jgust/SublimeCscope)
  * For [Atom](https://atom.io/) there is [atom-cscope](https://atom.io/packages/atom-cscope)

* If you don't use Atom, you also need to copy ~~[cscope_createindex.sh](uploads/17c725e19be8f4935c30c2506e168405/cscope_createindex.sh)(old version)~~ [cscope_createindex.sh](uploads/451835f6b1894145af06050915256048/cscope_createindex.sh) into the main xonotic repo directory.


##### Configuration

* Configure your plugin if needed:  
  * jEdit's CscopeFinder settings:  
  set cscope.out as cscope index filename.  

  * SublimeCscope user settings (with Windows executable as example):
	```
		"executable": "C:\\xonotic\\cscope.exe",
		"prompt_before_searching": false,
	```

  * atom-cscope settings:
  1. set the full path of cscope binary, e.g. C:\xonotic\cscope.exe (with Windows executable as example)  
  1. add .qc and .qh to source file extensions (".c .cc .cpp .h .hpp .qc .qh")
  1. you also need to create projects for darkplaces and xonotic/data/xonotic-data.pk3dir/qcsrc folders (toggle tree-view with `Ctrl + \`, right-click there and select "Add Project Folder")

* Run `cscope_createindex.sh` to build cscope indices for both game (QC code) and Darkplaces (C code). This step must be repeated every time you do some code changes.

* Some plugins assume that your index file is generated with compression turned on (SublimeCscope's case). In this case `cscope_createindex.sh` can be instructed to use compression by changing `compress=false` to `compress=true`.

* With Atom you can build cscope indices in the atom-cscope window (open with `Ctrl + Alt + o`) by clicking the flash icon.

##### Usage

* jEdit: select a word in the editor, right-click and select "Find this C symbol" or another "Find ..." entry (if you don't see these entries you should add them in the context menu settings).
* SublimeText: select a word in the editor, right-click and select "Look up symbol" or another "Look up ..." entry.
* Atom: open atom-cscope window (`Ctrl + Alt + o`) and type a symbol that you want to search.


### QC syntax highlighting:

* terencehill's version for jEdit: [qc.xml](https://gitlab.com/terencehill/qc-syntax-highlighting-for-jedit/blob/master/qc.xml)
* EACFreddy's version for Kate: [qc.xml](https://gist.github.com/DefaultUser/998f030ab41a9e8edf4a9f8e703c6350)