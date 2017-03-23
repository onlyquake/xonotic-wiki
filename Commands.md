DarkPlaces Wiki
===============

Console Commands
================

!!**documentation needed**!! how to use console commands through console and alias commands

    +attack : begin firing
    +back : move backward
    +button10 : activate button10 (behavior depends on mod)
    +button11 : activate button11 (behavior depends on mod)
    +button12 : activate button12 (behavior depends on mod)
    +button13 : activate button13 (behavior depends on mod)
    +button14 : activate button14 (behavior depends on mod)
    +button15 : activate button15 (behavior depends on mod)
    +button16 : activate button16 (behavior depends on mod)
    +button3 : activate button3 (behavior depends on mod)
    +button4 : activate button4 (behavior depends on mod)
    +button5 : activate button5 (behavior depends on mod)
    +button6 : activate button6 (behavior depends on mod)
    +button7 : activate button7 (behavior depends on mod)
    +button8 : activate button8 (behavior depends on mod)
    +button9 : activate button9 (behavior depends on mod)
    +forward : move forward
    +jump : jump
    +klook : activate keyboard looking mode, do not recenter view
    +left : turn left
    +lookdown : look downward
    +lookup : look upward
    +mlook : activate mouse looking mode, do not recenter view
    +movedown : swim downward
    +moveleft : strafe left
    +moveright : strafe right
    +moveup : swim upward
    +right : turn right
    +showscores : show scoreboard
    +speed : activate run mode (faster movement and turning)
    +strafe : activate strafing mode (move instead of turn)
    +use : use something (may be used by some mods)
    -attack : stop firing
    -back : stop moving backward
    -button10 : deactivate button10
    -button11 : deactivate button11
    -button12 : deactivate button12
    -button13 : deactivate button13
    -button14 : deactivate button14
    -button15 : deactivate button15
    -button16 : deactivate button16
    -button3 : deactivate button3
    -button4 : deactivate button4
    -button5 : deactivate button5
    -button6 : deactivate button6
    -button7 : deactivate button7
    -button8 : deactivate button8
    -button9 : deactivate button9
    -forward : stop moving forward
    -jump : end jump (so you can jump again)
    -klook : deactivate keyboard looking mode
    -left : stop turning left
    -lookdown : stop looking downward
    -lookup : stop looking upward
    -mlook : deactivate mouse looking mode
    -movedown : stop swimming downward
    -moveleft : stop strafing left
    -moveright : stop strafing right
    -moveup : stop swimming upward
    -right : stop turning right
    -showscores : hide scoreboard
    -speed : deactivate run mode
    -strafe : deactivate strafing mode
    -use : stop using something
    alias : create a script function (parameters are passed in as $X (being X a number), $* for all parameters, $X- for all parameters starting from $X). Without arguments show the list of all alias
    apropos : lists all console variables/commands/aliases containing the specified string in the name or description
    begin : signon 3 (client asks server to start sending entities, and will go to signon 4 (playing) when the first entity update is received)
    bestweapon : send an impulse number to server to select the first usable weapon out of several (example: 8 7 6 5 4 3 2 1)
    bf : briefly flashes a bright color tint on view (used when items are picked up); optionally takes R G B [A [alphafade]] arguments to specify how the flash looks
    bind : binds a command to the specified key in bindmap 0
    bindlist : bindlist: displays bound keys for bindmap 0 bindmaps
    bottomcolor : QW command to set bottom color without changing top color
    cd : execute a CD drive command (cd on/off/reset/remap/close/play/loop/stop/pause/resume/eject/info) - use cd by itself for usage
    centerview : gradually recenter view (stop looking up/down)
    changelevel : change to another level, bringing along all connected clients
    changing : sent by qw servers to tell client to wait for level change
    cl_areastats : prints statistics on entity culling during collision traces
    cl_begindownloads : used internally by darkplaces client while connecting (causes loading of models and sounds or triggers downloads for missing ones)
    cl_cmd : calls the client QC function GameCommand with the supplied string as argument
    cl_downloadbegin : (networking) informs client of download file information, client replies with sv_startsoundload to begin the transfer
    cl_downloadfinished : signals that a download has finished and provides the client with file size and crc to check its integrity
    cl_modelindexlist : list information on all models in the client modelindex
    cl_particles_reloadeffects : reloads effectinfo.txt and maps/levelname_effectinfo.txt (where levelname is the current map)
    cl_soundindexlist : list all sounds in the client soundindex
    clear : clear console history
    cmd : send a console commandline to the server (used by some mods)
    cmdlist : lists all console commands beginning with the specified prefix or matching the specified wildcard pattern
    color : change your player shirt and pants colors
    commandmode : input a console command
    condump : output console history to a file (see also log_file)
    connect : connect to a server by IP address or hostname
    cprint : print something at the screen center
    curl : download data from an URL and add to search path
    cvar_lockdefaults : stores the current values of all cvars into their default values, only used once during startup after parsing default.cfg
    cvar_resettodefaults_all : sets all cvars to their locked default values
    cvar_resettodefaults_nosaveonly : sets all non-saved cvars to their locked default values (variables that will not be saved to config.cfg)
    cvar_resettodefaults_saveonly : sets all saved cvars to their locked default values (variables that will be saved to config.cfg)
    cvarlist : lists all console variables beginning with the specified prefix or matching the specified wildcard pattern
    defer : execute a command in the future
    demos : restart looping demos defined by the last startdemos command
    dir : list files in searchpath matching an * filename pattern, one per line
    disconnect : disconnect from server (or disconnect all clients if running a server)
    download : downloads a specified file from the server
    echo : print a message to the console (useful in scripts)
    entities : print information on network entities known to client
    envmap : render a cubemap (skybox) of the current scene
    exec : execute a script file
    fixtrans : change alpha-zero pixels in an image file to sensible values, and write out a new TGA (warning: SLOW)
    fly : fly mode (flight)
    fog : set global fog parameters (density red green blue [alpha [mindist [maxdist [top [fadedepth]]]]])
    fog_heighttexture : set global fog parameters (density red green blue alpha mindist maxdist top depth textures/mapname/fogheight.tga)
    force_centerview : recenters view (stops looking up/down)
    fs_rescan : rescans filesystem for new pack archives and any other changes
    fullinfo : allows client to modify their userinfo
    fullserverinfo : internal use only, sent by server to client to update client's local copy of serverinfo string
    gamedir : changes active gamedir list (can take multiple arguments), not including base directory (example usage: gamedir ctf)
    gecko_create : Create a gecko browser instance
    gecko_destroy : Destroy a gecko browser instance
    gecko_injecttext : Injects text into a browser
    gecko_movecursor : Move the cursor to a certain position
    gecko_navigate : Navigate a gecko browser to a URI
    give : alter inventory
    gl_texturemode : set texture filtering mode (GL_NEAREST, GL_LINEAR, GL_LINEAR_MIPMAP_LINEAR, etc); an additional argument 'force' forces the texture mode even in cases where it may not be appropriate
    gl_vbostats : prints a list of all buffer objects (vertex data and triangle elements) and total video memory used by them
    god : god mode (invulnerability)
    heartbeat : send a heartbeat to the master server (updates your server information)
    help : open the help menu
    impulse : send an impulse number to server (select weapon, use item, etc)
    in_bind : binds a command to the specified key in the selected bindmap
    in_bindlist : bindlist: displays bound keys for all bindmaps, or the given bindmap
    in_bindmap : selects active foreground and background (used only if a key is not bound in the foreground) bindmaps for typing
    in_unbind : removes command on the specified key in the selected bindmap
    infobar : display a text in the infobar (usage: infobar expiretime string)
    iplog_list : lists names of players whose IP address begins with the supplied text (example: iplog_list 123.456.789)
    joyadvancedupdate : applies current joyadv* cvar settings to the joystick driver
    kick : kick a player off the server by number or name
    kill : die instantly
    load : load a saved game file
    loadconfig : reset everything and reload configs
    loadfont : loadfont function tganame loads a font; example: loadfont console gfx/veramono; loadfont without arguments lists the available functions
    loadsky : load a skybox by basename (for example loadsky mtnsun_ loads mtnsun_ft.tga and so on)
    locs_add : add a point or box location (usage: x y z[ x y z] "name", if two sets of xyz are supplied it is a box, otherwise point)
    locs_clear : remove all loc points/boxes
    locs_reload : reload .loc file for this map
    locs_removenearest : remove the nearest point or box (note: you need to be very near a box to remove it)
    locs_save : save .loc file for this map containing currently defined points and boxes
    ls : list files in searchpath matching an * filename pattern, multiple per line
    map : kick everyone off the server and start a new level
    maps : list information about available maps
    maxplayers : sets limit on how many players (or bots) may be connected to the server at once
    memlist : prints memory pool information (or if used as memlist 5 lists individual allocations of 5K or larger, 0 lists all allocations)
    memstats : prints memory system statistics
    menu_cmd : calls the menu QC function GameCommand with the supplied string as argument
    menu_credits : open the credits menu
    menu_keys : open the key binding menu
    menu_load : open the loadgame menu
    menu_main : open the main menu
    menu_mods : open the mods browser menu
    menu_multiplayer : open the multiplayer menu
    menu_options : open the options menu
    menu_options_colorcontrol : open the color control menu
    menu_options_effects : open the effects options menu
    menu_options_graphics : open the graphics options menu
    menu_quit : open the quit menu
    menu_reset : open the reset to defaults menu
    menu_restart : restart menu system (reloads menu.dat)
    menu_save : open the savegame menu
    menu_setup : open the player setup menu
    menu_singleplayer : open the singleplayer menu
    menu_transfusion_episode : open the transfusion episode select menu
    menu_transfusion_skill : open the transfusion skill select menu
    menu_video : open the video options menu
    messagemode : input a chat message to say to everyone
    messagemode2 : input a chat message to say to only your team
    mod_generatelightmaps : rebuilds lighting on current worldmodel
    modeldecompile : exports a model in several formats for editing purposes
    modellist : prints a list of loaded models
    modelprecache : load a model
    name : change your player name
    net_refresh : query dp master servers and refresh all server information
    net_slist : query dp master servers and print all server information
    net_slistqw : query qw master servers and print all server information
    net_stats : print network statistics
    nextul : sends next fragment of current upload buffer (screenshot for example)
    noclip : noclip mode (flight without collisions, move through walls)
    notarget : notarget mode (monsters do not see you)
    packet : send a packet to the specified address:port containing a text string
    path : print searchpath (game directories and archives)
    pause : pause the game (if the server allows pausing)
    pausedemo : pause demo playback (can also safely pause demo recording if using QUAKE, QUAKEDP or NEHAHRAMOVIE protocol, useful for making movies)
    ping : print ping times of all players on the server
    pingplreport : command sent by server containing client ping and packet loss values for scoreboard, triggered by pings command from client (not used by QW servers)
    pings : command sent by clients to request updated ping and packetloss of players on scoreboard (originally from QW, but also used on NQ servers)
    play : play a sound at your current location (not heard by anyone else)
    play2 : play a sound globally throughout the level (not heard by anyone else)
    playdemo : watch a demo file
    playermodel : change your player model
    playerskin : change your player skin number
    playvideo : play a .dpv video file
    playvol : play a sound at the specified volume level at your current location (not heard by anyone else)
    pointfile : display point file produced by qbsp when a leak was detected in the map (a line leading through the leak hole, to an entity inside the level)
    pqrcon : sends a command to a proquake server console (if your rcon_password matches the server's rcon_password), or to the address specified by rcon_address when not connected (again rcon_password must match the server's)
    prespawn : signon 1 (client acknowledges that server information has been received)
    prvm_callprofile : prints execution statistics about the most time consuming QuakeC calls from the engine in the selected VM (server, client, menu)
    prvm_childprofile : prints execution statistics about the most used QuakeC functions in the selected VM (server, client, menu), sorted by time taken in function with child calls
    prvm_edict : print all data about an entity number in the selected VM (server, client, menu)
    prvm_edictcount : prints number of active entities in the selected VM (server, client, menu)
    prvm_edictget : retrieves the value of a specified property of a specified entity in the selected VM (server, client menu) into a cvar or to the console
    prvm_edicts : prints all data about all entities in the selected VM (server, client, menu)
    prvm_edictset : changes value of a specified property of a specified entity in the selected VM (server, client, menu)
    prvm_fields : prints usage statistics on properties (how many entities have non-zero values) in the selected VM (server, client, menu)
    prvm_global : prints value of a specified global variable in the selected VM (server, client, menu)
    prvm_globalget : retrieves the value of a specified global variable in the selected VM (server, client menu) into a cvar or to the console
    prvm_globals : prints all global variables in the selected VM (server, client, menu)
    prvm_globalset : sets value of a specified global variable in the selected VM (server, client, menu)
    prvm_printfunction : prints a disassembly (QuakeC instructions) of the specified function in the selected VM (server, client, menu)
    prvm_profile : prints execution statistics about the most used QuakeC functions in the selected VM (server, client, menu)
    quit : quit the game
    r_editlights_clear : removes all world lights (let there be darkness!)
    r_editlights_copyinfo : store a copy of all properties (except origin) of the selected light
    r_editlights_edit : changes a property on the selected light
    r_editlights_editall : changes a property on ALL lights at once (tip: use radiusscale and colorscale to alter these properties)
    r_editlights_help : prints documentation on console commands and variables in rtlight editing system
    r_editlights_importlightentitiesfrommap : load lights from .ent file or map entities (ignoring .rtlights or .lights file)
    r_editlights_importlightsfile : load lights from .lights file (ignoring .rtlights or .ent files and map entities)
    r_editlights_pasteinfo : apply the stored properties onto the selected light (making it exactly identical except for origin)
    r_editlights_reload : reloads rtlights file (or imports from .lights file or .ent file or the map itself)
    r_editlights_remove : remove selected light
    r_editlights_save : save .rtlights file for current level
    r_editlights_spawn : creates a light with default properties (let there be light!)
    r_editlights_togglecorona : toggle on/off the corona option on the selected light
    r_editlights_toggleshadow : toggle on/off the shadow option on the selected light
    r_glsl_dumpshader : dumps the engine internal default.glsl shader into glsl/default.glsl
    r_glsl_restart : unloads GLSL shaders, they will then be reloaded as needed
    r_listmaptextures : list all textures used by the current map
    r_replacemaptexture : override a map texture for testing purposes
    r_restart : restarts renderer
    r_texturestats : print information about all loaded textures and some statistics
    rate : change your network connection speed
    rcon : sends a command to the server console (if your rcon_password matches the server's rcon_password), or to the address specified by rcon_address when not connected (again rcon_password must match the server's); note: if rcon_secure is set, client and server clocks must be synced e.g. via NTP
    reconnect : reconnect to the last server you were on, or resets a quakeworld connection (do not use if currently playing on a netquake server)
    record : record a demo
    register_bestweapon : (for QC usage only) change weapon parameters to be used by bestweapon; stuffcmd this in ClientConnect
    restart : restart current level
    save : save the game to a file
    saveconfig : save settings to config.cfg (or a specified filename) immediately (also automatic when quitting)
    say : send a chat message to everyone on the server
    say_team : send a chat message to your team on the server
    screenshot : takes a screenshot of the next rendered frame
    sendcvar : sends the value of a cvar to the server as a sentcvar command, for use by QuakeC
    set : create or change the value of a console variable
    seta : create or change the value of a console variable that will be saved to config.cfg
    setinfo : modifies your userinfo
    sizedown : decrease view size (decreases viewsize cvar)
    sizeup : increase view size (increases viewsize cvar)
    skins : downloads missing qw skins from server
    snd_restart : restart sound system
    snd_unloadallsounds : unload all sound files
    soundinfo : print sound system information (such as channels and speed)
    soundlist : list loaded sounds
    spawn : signon 2 (client has sent player information, and is asking server to send scoreboard rankings)
    srcon : sends a command to the server console (if your rcon_password matches the server's rcon_password), or to the address specified by rcon_address when not connected (again rcon_password must match the server's); this always works as if rcon_secure is set; note: client and server clocks must be synced e.g. via NTP
    startdemos : start playing back the selected demos sequentially (used at end of startup script)
    status : print server status information
    stop : stop recording or playing a demo
    stopdemo : stop playing or recording demo (like stop command) and return to looping demos
    stopdownload : terminates a download
    stopsound : silence
    stopul : aborts current upload (screenshot for example)
    stopvideo : stop playing a .dpv video file
    stuffcmds : execute commandline parameters (must be present in quake.rc script)
    sv_areastats : prints statistics on entity culling during collision traces
    sv_cmd : calls the server QC function GameCommand with the supplied string as argument
    sv_saveentfile : save map entities to .ent file (to allow external editing)
    sv_startdownload : begins sending a file to the client (network protocol use only)
    tell : send a chat message to only one person on the server
    timedemo : play back a demo as fast as possible and save statistics to benchmark.log
    timerefresh : turn quickly and print rendering statistcs
    toggle : toggles a console variable's values (use for more info)
    toggleconsole : opens or closes the console
    togglemenu : opens or closes menu
    topcolor : QW command to set top color without changing bottom color
    unalias : remove an alias
    unbind : removes a command on the specified key in bindmap 0
    unbindall : removes all commands from all keys in all bindmaps (leaving only shift-escape and escape)
    user : prints additional information about a player number or name on the scoreboard
    users : prints additional information about all players on the scoreboard
    v_cshift : sets tint color of view
    version : print engine version
    vid_restart : restarts video system (closes and reopens the window, restarts renderer)
    viewframe : change animation frame of viewthing entity in current level
    viewmodel : change model of viewthing entity in current level
    viewnext : change to next animation frame of viewthing entity in current level
    viewprev : change to previous animation frame of viewthing entity in current level
    wait : make script execution wait for next rendered frame
    which : accepts a file name as argument and reports where the file is taken from

