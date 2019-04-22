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
