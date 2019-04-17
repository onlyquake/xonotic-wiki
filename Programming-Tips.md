### Debug prints

You can show text anywhere on the map using `debug_text_3d(world_coords, message);` from `common/debug.qh`.

### Multiple clients + clean config

If you need 2 players for debugging, you can launch another client locally:
 - use -sessionid (e.g. `./all run -sessionid testing`) to keep your config
 - use -userdir (e.g. `./all run -userdir ~/.xonotic-testing +name tester +cl_allow_uid2name 0`) to get a clean config (`+` sets cvars to avoid annoying popups)

### Testing with bots

You can prevent bots from firing (`bot_nofire 1`) or stop them completely (`bot_cmd * pause`). With `sv_cheats 1` (takes effect next match), you can drag them around (default V or drag object in menu).

Note that `sv_cheats 1` prevents bots from spawning in the campaign (should you decide to put it in your `autoexec.cfg` and later wonder why the campaign is broken).
