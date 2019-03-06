### Session Id

If you need 2 players for debugging, you can launch another client locally:
 - use -sessionid (e.g. `./all run -sessionid testing`) to keep your config
 - use -userdir (e.g. `./all run -userdir ~/.xonotic-testing +name tester +cl_allow_uid2name 0`) to get a clean config (`+` sets cvars to avoid annoying popups)

### Debug prints

You can show text anywhere on the map using `debug_text_3d(position, message);` from `common/debug.qh`.
