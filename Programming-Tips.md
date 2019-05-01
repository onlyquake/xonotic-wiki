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
