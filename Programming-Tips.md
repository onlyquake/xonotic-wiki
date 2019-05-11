### Debug prints

Use `con_notify 4` together with `LOG_INFOF("my_var: %s", my_var);` (`%s` string, `%f` float, `%d` integer, `%v` vector) to see debug output without opening the console. Type `con_notify` and press `<TAB>` to see descriptions and more options (or use `apropos con_notify`).

You can draw text anywhere on the map using `debug_text_3d(world_coords, message);` from `common/debug.qh`.

### Multiple clients + clean config

If you need 2 players for debugging, you can launch another client locally:
 - use -sessionid (e.g. `./all run -sessionid testing`) to keep your config
 - use -userdir (e.g. `./all run -userdir ~/.xonotic-testing +name tester +cl_allow_uid2name 0`) to get a clean config (`+cl_allow_uid2name 0` to avoid an annoying popup). You can set whatever cvar on start with `+cvar_name value`.

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

### Tool to find C symbols, functions, declarations and definitions inside source code

For this purpose it's possible to use a text-based tool called [Cscope](https://en.wikipedia.org/wiki/Cscope) together with a GUI (it can be either an application or a plugin for a text editor).

#### Download / Installation

* Download and install cscope with `pacman -S cscope`  
Windows users must download the Windows version of cscope from https://code.google.com/archive/p/cscope-win32/downloads since the mingw version generates broken indices and put it into the main xonotic repo directory.

* Download and install a cscope GUI or a plugin for your text editor / IDE. For example for jEdit there is a plugin called [CscopeFinder](http://plugins.jedit.org/plugins/?CscopeFinder).

* Copy [cscope_createindex.sh](uploads/17c725e19be8f4935c30c2506e168405/cscope_createindex.sh) into the main xonotic repo directory.  

#### Usage

* Run `cscope_createindex.sh` to build cscope indices for both game (QC code) and Darkplaces (C code). This step must be repeated every time you do some code changes.  
The indices can now be used to browse code confortably with the cscope GUI of your choice.

### QC syntax highlighting:

* For jEdit: [qc.xml](https://gitlab.com/terencehill/qc-syntax-highlighting-for-jedit/blob/master/qc.xml)
* For Kate: [qc.xml](https://gist.github.com/DefaultUser/998f030ab41a9e8edf4a9f8e703c6350)