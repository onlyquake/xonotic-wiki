Console Variables (CVars)
=========================

Introduction
------------
Console Variables (CVars) are internal variables that control almost all aspects of the game. You can enable mutators, change damage of weapons, enable special game rules, tweak your HUD, and do many other things.

How to use
----------
Here you will find all Console Variables for changing even the most minute aspect of Darkplaces. To access the console to modify these variables, simply press the `~` key on your keyboard. This is the default bind for this action.  

You may also get to it through this menu sequence: `Main Menu -> Options -> Go To Console` or possibly using `Shift + Escape`.

You can also access a list of CVars in the game's menus: `Main Menu -> Options -> Misc. -> Advanced Settings …`. This lists all cvars, some of them have a description. Use the filter to find a particular cvar name. You must use the asterisk (“*”) to search for any sequence of characters. Example: To find all cvars with “keyhunt” in their name, type in “*keyhunt*”.

List of CVars (Darkplaces)
--------------------------

    _cl_color is "179" ["0"] internal storage cvar for current player colors (changed by color command)
    _cl_name is "Error" ["player"] internal storage cvar for current player name (changed by name command)
    _cl_playermodel is "" [""] internal storage cvar for current player model in Nexuiz (changed by playermodel command)
    _cl_playerskin is "" [""] internal storage cvar for current player skin in Nexuiz (changed by playerskin command)
    _cl_rate is "20000" ["20000"] internal storage cvar for current rate (changed by rate command)
    _snd_mixahead is "0.15" ["0.15"] how much sound to mix ahead of time
    ambient_fade is "100" ["100"] rate of volume fading when moving from one environment to another
    ambient_level is "0.3" ["0.3"] volume of environment noises (water and wind)
    bgmvolume is "1" ["1"] volume of background music (such as CD music or replacement files such as sound/cdtracks/track002.ogg)
    cdaudio is "1" ["1"] CD playing mode (0 = never access CD drive, 1 = play CD tracks if no replacement available, 2 = play fake tracks if no CD track available, 3 = play only real CD tracks, 4 = play real CD tracks even instead of named fake tracks)
    cdaudioinitialized is "1" ["1"] indicates if CD Audio system is active
    chase_active is "0" ["0"] enables chase cam
    chase_back is "48" ["48"] chase cam distance from the player
    chase_overhead is "0" ["0"] chase cam looks straight down if this is not zero
    chase_pitchangle is "55" ["55"] chase cam pitch angle
    chase_up is "24" ["24"] chase cam distance from the player
    cl_anglespeedkey is "1.5" ["1.5"] how much +speed multiplies keyboard turning speed
    cl_autodemo is "0" ["0"] records every game played, using the date/time and map name to name the demo file
    cl_autodemo_nameformat is "autodemos/%Y-%m-%d_%H-%M" ["autodemos/%Y-%m-%d_%H-%M"] The format of the cl_autodemo filename, followed by the map name (the date is encoded using strftime escapes)
    cl_backspeed is "400" ["400"] backward movement speed
    cl_beams_instantaimhack is "0" ["0"] makes your lightning gun aiming update instantly
    cl_beams_lightatend is "1" ["0"] make a light at the end of the beam
    cl_beams_polygons is "1" ["1"] use beam polygons instead of models
    cl_beams_quakepositionhack is "1" ["1"] makes your lightning gun appear to fire from your waist (as in Quake and QuakeWorld)
    cl_bob is "0.02" ["0.02"] view bobbing amount
    cl_bobcycle is "0.6" ["0.6"] view bobbing speed
    cl_bobmodel is "1" ["1"] enables gun bobbing
    cl_bobmodel_side is "0.15" ["0.15"] gun bobbing sideways sway amount
    cl_bobmodel_speed is "7" ["7"] gun bobbing speed
    cl_bobmodel_up is "0.06" ["0.06"] gun bobbing upward movement amount
    cl_bobup is "0.5" ["0.5"] view bobbing adjustment that makes the up or down swing of the bob last longer
    cl_capturevideo is "0" ["0"] enables saving of video to a .avi file using uncompressed I420 colorspace and PCM audio, note that scr_screenshot_gammaboost affects the brightness of the output)
    cl_capturevideo_fps is "30" ["30"] how many frames per second to save (29.97 for NTSC, 30 for typical PC video, 15 can be useful)
    cl_capturevideo_framestep is "1" ["1"] when set to n >= 1, render n frames to capture one (useful for motion blur like effects)
    cl_capturevideo_height is "0" ["0"] scales all frames to this resolution before saving the video
    cl_capturevideo_nameformat is "dpvideo" ["dpvideo"] prefix for saved videos (the date is encoded using strftime escapes)
    cl_capturevideo_number is "1" ["1"] number to append to video filename, incremented each time a capture begins
    cl_capturevideo_ogg is "1" ["1"] save captured video data as Ogg/Vorbis/Theora streams
    cl_capturevideo_ogg_theora_bitrate is "-1" ["-1"] video bitrate (45 to 2000 kbps), or -1 to use quality only; higher is better
    cl_capturevideo_ogg_theora_keyframe_auto_threshold is "80" ["80"] threshold for key frame decision (0 to 100)
    cl_capturevideo_ogg_theora_keyframe_bitrate_multiplier is "1.5" ["1.5"] how much more bit rate to use for keyframes, specified as a factor of at least 1
    cl_capturevideo_ogg_theora_keyframe_maxinterval is "64" ["64"] maximum keyframe interval (1 to 1000)
    cl_capturevideo_ogg_theora_keyframe_mininterval is "8" ["8"] minimum keyframe interval (1 to 1000)
    cl_capturevideo_ogg_theora_noise_sensitivity is "1" ["1"] video noise sensitivity (0 to 6); lower is better
    cl_capturevideo_ogg_theora_quality is "32" ["32"] video quality factor (0 to 63), or -1 to use bitrate only; higher is better
    cl_capturevideo_ogg_vorbis_quality is "3" ["3"] audio quality (-1 to 10); higher is better
    cl_capturevideo_printfps is "1" ["1"] prints the frames per second captured in capturevideo (is only written to the log file, not to the console, as that would be visible on the video)
    cl_capturevideo_realtime is "0" ["0"] causes video saving to operate in realtime (mostly useful while playing, not while capturing demos), this can produce a much lower quality video due to poor sound/video sync and will abort saving if your machine stalls for over a minute
    cl_capturevideo_width is "0" ["0"] scales all frames to this resolution before saving the video
    cl_curl_enabled is "1" ["1"] whether client's download support is enabled
    cl_curl_maxdownloads is "1" ["1"] maximum number of concurrent HTTP/FTP downloads
    cl_curl_maxspeed is "300" ["300"] maximum download speed (KiB/s)
    cl_deathfade is "0" ["0"] fade screen to dark red when dead, value represents how fast the fade is (higher is faster)
    cl_deathnoviewmodel is "1" ["1"] hides gun model when dead
    cl_deathscoreboard is "1" ["1"] shows scoreboard (+showscores) while dead
    cl_decals is "1" ["1"] enables decals (bullet holes, blood, etc)
    cl_decals_bias is "0.125" ["0.125"] distance to bias decals from surface to prevent depth fighting
    cl_decals_fadetime is "1" ["1"] how long decals take to fade away
    cl_decals_max is "4096" ["4096"] maximum number of decals allowed to exist in the world at once
    cl_decals_models is "0" ["0"] enables decals on animated models (if newsystem is also 1)
    cl_decals_newsystem is "0" ["0"] enables new advanced decal system
    cl_decals_newsystem_intensitymultiplier is "2" ["2"] boosts intensity of decals (because the distance fade can make them hard to see otherwise)
    cl_decals_time is "20" ["20"] how long before decals start to fade away
    cl_decals_visculling is "1" ["1"] perform a very cheap check if each decal is visible before drawing
    cl_demo_mousegrab is "0" ["0"] Allows reading the mouse input while playing demos. Useful for camera mods developed in csqc. (0: never, 1: always)
    cl_dlights_decaybrightness is "1" ["1"] reduces brightness of light flashes over time
    cl_dlights_decayradius is "1" ["1"] reduces size of light flashes over time
    cl_explosions_alpha_end is "0" ["0"] end alpha of an explosion shell (just before it disappears)
    cl_explosions_alpha_start is "1.5" ["1.5"] starting alpha of an explosion shell
    cl_explosions_lifetime is "0.5" ["0.5"] how long an explosion shell lasts
    cl_explosions_size_end is "128" ["128"] ending alpha of an explosion shell (just before it disappears)
    cl_explosions_size_start is "16" ["16"] starting size of an explosion shell
    cl_forwardspeed is "400" ["400"] forward movement speed
    cl_gameplayfix_soundsmovewithentities is "1" ["1"] causes sounds made by lifts, players, projectiles, and any other entities, to move with the entity, so for example a rocket noise follows the rocket rather than staying at the starting position
    cl_iplog_name is "darkplaces_iplog.txt" ["darkplaces_iplog.txt"] name of iplog file containing player addresses for iplog_list command and automatic ip logging when parsing status command
    cl_itembobheight is "0" ["0"] how much items bob up and down (try 8)
    cl_itembobspeed is "0.5" ["0.5"] how frequently items bob up and down
    cl_joinbeforedownloadsfinish is "1" ["1"] if non-zero the game will begin after the map is loaded before other downloads finish
    cl_lerpanim_maxdelta_framegroups is "0.1" ["0.1"] maximum frame delta for smoothing between framegroups (when 0, one network frame)
    cl_lerpanim_maxdelta_server is "0.1" ["0.1"] maximum frame delta for smoothing between server-controlled animation frames (when 0, one network frame)
    cl_maxfps is "0" ["0"] maximum fps cap, 0 = unlimited, if game is running faster than this it will wait before running another frame (useful to make cpu time available to other programs)
    cl_maxfps_alwayssleep is "1" ["1"] gives up some processing time to other applications each frame, value in milliseconds, disabled if cl_maxfps is 0
    cl_maxidlefps is "20" ["20"] maximum fps cap when the game is not the active window (makes cpu time available to other programs
    cl_minfps is "40" ["40"] minimum fps target - while the rendering performance is below this, it will drift toward lower quality
    cl_minfps_fade is "0.2" ["0.2"] how fast the quality adapts to varying framerate
    cl_minfps_qualitymax is "1" ["1"] highest allowed drawdistance multiplier
    cl_minfps_qualitymin is "0.25" ["0.25"] lowest allowed drawdistance multiplier
    cl_minfps_qualitypower is "4" ["4"] raises quality value to a power of itself, higher values make quality drop more sharply in relation to framerate
    cl_minfps_qualityscale is "0.5" ["0.5"] multiplier for quality
    cl_movecliptokeyboard is "0" ["0"] if set to 1, any move is clipped to the nine keyboard states; if set to 2, only the direction is clipped, not the amount
    cl_movement is "0" ["0"] enables clientside prediction of your player movement
    cl_movement_accelerate is "10" ["10"] how fast you accelerate (should match sv_accelerate)
    cl_movement_airaccel_qw is "1" ["1"] ratio of QW-style air control as opposed to simple acceleration (reduces speed gain when zigzagging) (should match sv_airaccel_qw); when < 0, the speed is clamped against the maximum allowed forward speed after the move
    cl_movement_airaccel_sideways_friction is "0" ["0"] anti-sideways movement stabilization (should match sv_airaccel_sideways_friction); when < 0, only so much friction is applied that braking (by accelerating backwards) cannot be stronger
    cl_movement_airaccelerate is "-1" ["-1"] how fast you accelerate while in the air (should match sv_airaccelerate), if less than 0 the cl_movement_accelerate variable is used instead
    cl_movement_edgefriction is "1" ["1"] how much to slow down when you may be about to fall off a ledge (should match edgefriction)
    cl_movement_friction is "4" ["4"] how fast you slow down (should match sv_friction)
    cl_movement_jumpvelocity is "270" ["270"] how fast you move upward when you begin a jump (should match the quakec code)
    cl_movement_maxairspeed is "30" ["30"] how fast you can move while in the air (should match sv_maxairspeed)
    cl_movement_maxspeed is "320" ["320"] how fast you can move (should match sv_maxspeed)
    cl_movement_minping is "0" ["0"] whether to use prediction when ping is lower than this value in milliseconds
    cl_movement_nettimeout is "0.3" ["0.3"] stops predicting moves when server is lagging badly (avoids major performance problems), timeout in seconds
    cl_movement_stepheight is "18" ["18"] how tall a step you can step in one instant (should match sv_stepheight)
    cl_movement_stopspeed is "100" ["100"] speed below which you will be slowed rapidly to a stop rather than sliding endlessly (should match sv_stopspeed)
    cl_movement_track_canjump is "1" ["1"] track if the player released the jump key between two jumps to decide if he is able to jump or not; when off, this causes some "sliding" slightly above the floor when the jump key is held too long; if the mod allows repeated jumping by holding space all the time, this has to be set to zero too
    cl_movement_wallfriction is "1" ["1"] how fast you slow down while sliding along a wall (should match sv_wallfriction)
    cl_movement_wateraccelerate is "-1" ["-1"] how fast you accelerate while in water (should match sv_wateraccelerate), if less than 0 the cl_movement_accelerate variable is used instead
    cl_movement_waterfriction is "-1" ["-1"] how fast you slow down (should match sv_waterfriction), if less than 0 the cl_movement_friction variable is used instead
    cl_movespeedkey is "2.0" ["2.0"] how much +speed multiplies keyboard movement speed
    cl_netfps is "72" ["72"] how many input packets to send to server each second
    cl_netimmediatebuttons is "1" ["1"] sends extra packets whenever your buttons change or an impulse is used (basically: whenever you click fire or change weapon)
    cl_netlocalping is "0" ["0"] lags local loopback connection by this much ping time (useful to play more fairly on your own server with people with higher pings)
    cl_netpacketloss_receive is "0" ["0"] drops this percentage of incoming packets, useful for testing network protocol robustness (jerky movement, effects failing to start, sounds failing to play, etc)
    cl_netpacketloss_send is "0" ["0"] drops this percentage of outgoing packets, useful for testing network protocol robustness (jerky movement, prediction errors, etc)
    cl_netrepeatinput is "1" ["1"] how many packets in a row can be lost without movement issues when using cl_movement (technically how many input messages to repeat in each packet that have not yet been acknowledged by the server), only affects DP7 and later servers (Quake uses 0, QuakeWorld uses 2, and just for comparison Quake3 uses 1)
    cl_nettimesyncboundmode is "6" ["6"] method of restricting client time to valid values, 0 = no correction, 1 = tight bounding (jerky with packet loss), 2 = loose bounding (corrects it if out of bounds), 3 = leniant bounding (ignores temporary errors due to varying framerate), 4 = slow adjustment method from Quake3, 5 = slighttly nicer version of Quake3 method, 6 = bounding + Quake3
    cl_nettimesyncboundtolerance is "0.25" ["0.25"] how much error is tolerated by bounding check, as a fraction of frametime, 0.25 = up to 25% margin of error tolerated, 1 = use only new time, 0 = use only old time (same effect as setting cl_nettimesyncfactor to 1)
    cl_nettimesyncfactor is "0" ["0"] rate at which client time adapts to match server time, 1 = instantly, 0.125 = slowly, 0 = not at all (bounding still applies)
    cl_nodelta is "0" ["0"] disables delta compression of non-player entities in QW network protocol
    cl_nolerp is "0" ["0"] network update smoothing
    cl_noplayershadow is "0" ["0"] hide player shadow
    cl_particles is "1" ["1"] enables particle effects
    cl_particles_alpha is "1" ["1"] multiplies opacity of particles
    cl_particles_blood is "1" ["1"] enables blood effects
    cl_particles_blood_alpha is "1" ["1"] opacity of blood, does not affect decals
    cl_particles_blood_bloodhack is "1" ["1"] make certain quake particle() calls create blood effects instead
    cl_particles_blood_decal_alpha is "1" ["1"] opacity of blood decal
    cl_particles_blood_decal_scalemax is "2" ["2"] maximal random scale of decal
    cl_particles_blood_decal_scalemin is "1.5" ["1.5"] minimal random scale of decal
    cl_particles_bubbles is "1" ["1"] enables bubbles (used by multiple effects)
    cl_particles_bulletimpacts is "1" ["1"] enables bulletimpact effects
    cl_particles_collisions is "1" ["1"] allow costly collision detection on particles (sparks that bounce, particles not going through walls, blood hitting surfaces, etc)
    cl_particles_explosions_shell is "1" ["0"] enables polygonal shell from explosions
    cl_particles_explosions_sparks is "1" ["1"] enables sparks from explosions
    cl_particles_quake is "1" ["0"] makes particle effects look mostly like the ones in Quake
    cl_particles_quality is "1" ["1"] multiplies number of particles
    cl_particles_rain is "1" ["1"] enables rain effects
    cl_particles_size is "1" ["1"] multiplies particle size
    cl_particles_smoke is "1" ["1"] enables smoke (used by multiple effects)
    cl_particles_smoke_alpha is "0.5" ["0.5"] smoke brightness
    cl_particles_smoke_alphafade is "0.55" ["0.55"] brightness fade per second
    cl_particles_snow is "1" ["1"] enables snow effects
    cl_particles_sparks is "1" ["1"] enables sparks (used by multiple effects)
    cl_particles_visculling is "0" ["0"] perform a costly check if each particle is visible before drawing
    cl_pitchspeed is "150" ["150"] keyboard pitch turning speed
    cl_port is "0" ["0"] forces client to use chosen port number if not 0
    cl_prydoncursor is "0" ["0"] enables a mouse pointer which is able to click on entities in the world, useful for point and click mods, see PRYDON_CLIENTCURSOR extension in dpextensions.qc
    cl_prydoncursor_notrace is "0" ["0"] disables traceline used in prydon cursor reporting to the game, saving some cpu time
    cl_readpicture_force is "0" ["0"] when enabled, the low quality pictures read by ReadPicture() are preferred over the high quality pictures on the file system
    cl_rollangle is "2.0" ["2.0"] how much to tilt the view when strafing
    cl_rollspeed is "200" ["200"] how much strafing is necessary to tilt the view
    cl_serverextension_download is "2" ["0"] indicates whether the server supports the download command
    cl_shownet is "0" ["0"] 1 = print packet size, 2 = print packet message list
    cl_sidespeed is "350" ["350"] strafe movement speed
    cl_sound_hknighthit is "hknight/hit.wav" ["hknight/hit.wav"] sound to play during TE_KNIGHTSPIKE (empty cvar disables sound)
    cl_sound_r_exp3 is "weapons/r_exp3.wav" ["weapons/r_exp3.wav"] sound to play during TE_EXPLOSION and related effects (empty cvar disables sound)
    cl_sound_ric1 is "weapons/ric1.wav" ["weapons/ric1.wav"] sound to play with 5% chance during TE_SPIKE/TE_SUPERSPIKE (empty cvar disables sound)
    cl_sound_ric2 is "weapons/ric2.wav" ["weapons/ric2.wav"] sound to play with 5% chance during TE_SPIKE/TE_SUPERSPIKE (empty cvar disables sound)
    cl_sound_ric3 is "weapons/ric3.wav" ["weapons/ric3.wav"] sound to play with 10% chance during TE_SPIKE/TE_SUPERSPIKE (empty cvar disables sound)
    cl_sound_ric_gunshot is "0" ["0"] specifies if and when the related cl_sound_ric and cl_sound_tink sounds apply to TE_GUNSHOT/TE_GUNSHOTQUAD, 0 = no sound, 1 = TE_GUNSHOT, 2 = TE_GUNSHOTQUAD, 3 = TE_GUNSHOT and TE_GUNSHOTQUAD
    cl_sound_tink1 is "weapons/tink1.wav" ["weapons/tink1.wav"] sound to play with 80% chance during TE_SPIKE/TE_SUPERSPIKE (empty cvar disables sound)
    cl_sound_wizardhit is "wizard/hit.wav" ["wizard/hit.wav"] sound to play during TE_WIZSPIKE (empty cvar disables sound)
    cl_stainmaps is "0" ["0"] stains lightmaps, much faster than decals but blurred
    cl_stainmaps_clearonload is "1" ["1"] clear stainmaps on map restart
    cl_stairsmoothspeed is "160" ["160"] how fast your view moves upward/downward when running up/down stairs
    cl_upspeed is "400" ["400"] vertical movement speed (while swimming or flying)
    cl_viewmodel_scale is "1" ["1"] changes size of gun model, lower values prevent poking into walls but cause strange artifacts on lighting and especially r_stereo/vid_stereobuffer options where the size of the gun becomes visible
    cl_yawspeed is "140" ["140"] keyboard yaw turning speed
    cmdline is "C:\Quake\darkplaces.exe " ["C:\Quake\darkplaces.exe "] contains commandline the engine was launched with
    collision_debug_tracelineasbox is "0" ["0"] workaround for any bugs in Collision_TraceLineBrushFloat by using Collision_TraceBrushBrushFloat
    collision_endnudge is "0" ["0"] how much to bias collision trace end
    collision_endposnudge is "0" ["0"] workaround to fix trace_endpos sometimes being returned where it would be inside solid by making that collision hit (recommended: values like 1)
    collision_enternudge is "0" ["0"] how much to bias collision entry fraction
    collision_impactnudge is "0.03125" ["0.03125"] how much to back off from the impact
    collision_leavenudge is "0" ["0"] how much to bias collision exit fraction
    collision_prefernudgedfraction is "1" ["1"] whether to sort collision events by nudged fraction (1) or real fraction (0)
    collision_startnudge is "0" ["0"] how much to bias collision trace start
    con_chat is "0" ["0"] how many chat lines to show in a dedicated chat area
    con_chatpos is "0" ["0"] where to put chat (negative: lines from bottom of screen, positive: lines below notify, 0: at top)
    con_chatsize is "8" ["8"] chat text size in virtual 2D pixels (if con_chat is enabled)
    con_chatsound is "1" ["1"] enables chat sound to play on message
    con_chattime is "30" ["30"] how long chat lines last, in seconds
    con_chatwidth is "1.0" ["1.0"] relative chat window width
    con_closeontoggleconsole is "1" ["1"] allows toggleconsole binds to close the console as well
    con_completion_exec is "*.cfg" ["*.cfg"] completion pattern for the exec command
    con_completion_playdemo is "*.dem" ["*.dem"] completion pattern for the playdemo command
    con_completion_timedemo is "*.dem" ["*.dem"] completion pattern for the timedemo command
    con_nickcompletion is "1" ["1"] tab-complete nicks in console and message input
    con_nickcompletion_flags is "11" ["11"] Bitfield: 0: add nothing after completion. 1: add the last color after completion. 2: add a quote when starting a quote instead of the color. 4: will replace 1, will force color, even after a quote. 8: ignore non-alphanumerics. 16: ignore spaces. 
    con_notify is "4" ["4"] how many notify lines to show
    con_notifyalign is "" [""] how to align notify lines: 0 = left, 0.5 = center, 1 = right, empty string = game default)
    con_notifysize is "8" ["8"] notify text size in virtual 2D pixels
    con_notifytime is "3" ["3"] how long notify lines last, in seconds
    con_textsize is "8" ["8"] console text size in virtual 2D pixels
    coop is "0" ["0"] coop mode, 0 = no coop, 1 = coop mode, multiple players playing through the singleplayer game (coop mode also shuts off deathmatch)
    crosshair is "0" ["0"] selects crosshair to use (0 is none)
    crosshair_color_alpha is "1" ["1"] how opaque the crosshair should be
    crosshair_color_blue is "0" ["0"] customizable crosshair color
    crosshair_color_green is "0" ["0"] customizable crosshair color
    crosshair_color_red is "1" ["1"] customizable crosshair color
    crosshair_size is "1" ["1"] adjusts size of the crosshair on the screen
    csqc_progcrc is "-1" ["-1"] CRC of csprogs.dat file to load (-1 is none), only used during level changes and then reset to -1
    csqc_progname is "csprogs.dat" ["csprogs.dat"] name of csprogs.dat file to load
    csqc_progsize is "-1" ["-1"] file size of csprogs.dat file to load (-1 is none), only used during level changes and then reset to -1
    cutscene is "1" ["1"] enables cutscenes in nehahra, can be used by other mods
    deathmatch is "0" ["0"] deathmatch mode, values depend on mod but typically 0 = no deathmatch, 1 = normal deathmatch with respawning weapons, 2 = weapons stay (players can only pick up new weapons)
    demo_nehahra is "0" ["0"] reads all quake demos as nehahra movie protocol
    developer is "0" ["0"] prints debugging messages and information (recommended for all developers and level designers)
    developer_entityparsing is "0" ["0"] prints detailed network entities information each time a packet is received
    developer_extra is "0" ["0"] prints additional debugging messages, often very verbose!
    developer_font is "0" ["0"] prints debug messages about fonts
    developer_insane is "0" ["0"] prints huge streams of information about internal workings, entire contents of files being read/written, etc.  Not recommended!
    developer_loadfile is "0" ["0"] prints name and size of every file loaded via the FS_LoadFile function (which is almost everything)
    developer_loading is "0" ["0"] prints information about files as they are loaded or unloaded successfully
    developer_memory is "0" ["0"] prints debugging information about memory allocations
    developer_memorydebug is "0" ["0"] enables memory corruption checks (very slow)
    developer_networkentities is "0" ["0"] prints received entities, value is 0-4 (higher for more info)
    developer_networking is "0" ["0"] prints all received and sent packets (recommended only for debugging)
    developer_texturelogging is "0" ["0"] produces a textures.log file containing names of skins and map textures the engine tried to load
    edgefriction is "1" ["1"] how much you slow down when nearing a ledge you might fall off, multiplier of sv_friction (Quake used 2, QuakeWorld used 1 due to a bug in physics code)
    forceqmenu is "0" ["0"] enables the quake menu instead of the quakec menu.dat (if present)
    fov is "90" ["90"] field of vision, 1-170 degrees, default 90, some players use 110-130
    fraglimit is "0" ["0"] ends level if this many frags is reached by any player
    freelook is "1" ["1"] mouse controls pitch instead of forward/back
    fs_empty_files_in_pack_mark_deletions is "0" ["0"] if enabled, empty files in a pak/pk3 count as not existing but cancel the search in further packs, effectively allowing patch pak/pk3 files to 'delete' files
    fs_gamedir is "" [""] the list of currently selected gamedirs (use the 'gamedir' command to change this)
    gamecfg is "0" ["0"] unused cvar in quake, can be used by mods
    gameversion is "0" ["0"] version of game data (mod-specific) to be sent to querying clients
    gameversion_max is "-1" ["-1"] maximum version of game data (mod-specific), when client and server gameversion mismatch in the server browser the server is shown as incompatible; if -1, gameversion is used alone
    gameversion_min is "-1" ["-1"] minimum version of game data (mod-specific), when client and server gameversion mismatch in the server browser the server is shown as incompatible; if -1, gameversion is used alone
    gl_combine is "1" ["1"] indicates whether the OpenGL 1.3 rendering path is active
    gl_dither is "1" ["1"] enables OpenGL dithering (16bit looks bad with this off)
    gl_ext_separatestencil is "1" ["1"] make use of OpenGL 2.0 glStencilOpSeparate or GL_ATI_separate_stencil extension
    gl_ext_stenciltwoside is "1" ["1"] make use of GL_EXT_stenciltwoside extension (NVIDIA only)
    gl_finish is "0" ["0"] make the cpu wait for the graphics processor at the end of each rendered frame (can help with strange input or video lag problems on some machines)
    gl_flashblend is "1" ["0"] render bright coronas for dynamic lights instead of actual lighting, fast but ugly
    gl_info_driver is "opengl32.dll" [""] name of driver library (opengl32.dll, libGL.so.1, or whatever).
    gl_info_extensions is " 1.1  GL_ARB_depth_texture  GL_ARB_draw_buffers  GL_ARB_fragment_shader  GL_ARB_multitexture  GL_ARB_occlusion_query  GL_ARB_shader_objects  GL_ARB_shading_language_100  GL_ARB_shadow  GL_ARB_texture_compression  GL_ARB_texture_cube_map  GL_ARB_texture_env_combine  GL_ARB_texture_non_power_of_two  GL_ARB_texture_rectangle  GL_ARB_vertex_buffer_object  GL_ARB_vertex_shader  2.0  GL_EXT_blend_minmax  GL_EXT_blend_subtract  1.2  GL_EXT_framebuffer_object  GL_EXT_stencil_two_side  GL_EXT_texture3D  GL_EXT_texture_compression_s3tc  GL_EXT_texture_edge_clamp  GL_EXT_texture_filter_anisotropic " [""] indicates extension list found by engine, space separated.
    gl_info_platform is "WGL" [""] indicates GL platform: WGL, GLX, or AGL.
    gl_info_renderer is "GeForce 7950 GT/PCI/SSE2/3DNOW!" [""] indicates graphics chip model and other information
    gl_info_vendor is "NVIDIA Corporation" [""] indicates brand of graphics chip
    gl_info_version is "2.1.2" [""] indicates version of current renderer. begins with 1.0.0, 1.1.0, 1.2.0, 1.3.1 etc.
    gl_lightmaps is "0" ["0"] draws only lightmaps, no texture (for level designers)
    gl_max_lightmapsize is "1024" ["1024"] maximum allowed texture size for lightmap textures, use larger values to improve rendering speed, as long as there is enough video memory available (setting it too high for the hardware will cause very bad performance)
    gl_max_size is "2048" ["2048"] maximum allowed texture size, can be used to reduce video memory usage, limited by hardware capabilities (typically 2048, 4096, or 8192)
    gl_mesh_drawrangeelements is "1" ["1"] use glDrawRangeElements function if available instead of glDrawElements (for performance comparisons or bug testing)
    gl_mesh_prefer_short_elements is "1" ["1"] use GL_UNSIGNED_SHORT element arrays instead of GL_UNSIGNED_INT
    gl_mesh_testarrayelement is "0" ["0"] use glBegin(GL_TRIANGLES);glArrayElement();glEnd(); primitives instead of glDrawElements (useful to test for driver bugs with glDrawElements)
    gl_mesh_testmanualfeeding is "0" ["0"] use glBegin(GL_TRIANGLES);glTexCoord2f();glVertex3f();glEnd(); primitives instead of glDrawElements (useful to test for driver bugs with glDrawElements)
    gl_nopartialtextureupdates is "1" ["1"] use alternate path for dynamic lightmap updates that avoids a possibly slow code path in the driver
    gl_paranoid is "0" ["0"] enables OpenGL error checking and other tests
    gl_picmip is "0" ["0"] reduces resolution of textures by powers of 2, for example 1 will halve width/height, reducing texture memory usage by 75%
    gl_polyblend is "1" ["1"] tints view while underwater, hurt, etc
    gl_printcheckerror is "0" ["0"] prints all OpenGL error checks, useful to identify location of driver crashes
    gl_texture_anisotropy is "16" ["1"] anisotropic filtering quality (if supported by hardware), 1 sample (no anisotropy) and 8 sample (8 tap anisotropy) are recommended values
    gl_texturecompression is "0" ["0"] whether to compress textures, a value of 0 disables compression (even if the individual cvars are 1), 1 enables fast (low quality) compression at startup, 2 enables slow (high quality) compression at startup
    gl_texturecompression_2d is "0" ["0"] whether to compress 2d (hud/menu) textures other than the font
    gl_texturecompression_color is "1" ["1"] whether to compress colormap (diffuse) textures
    gl_texturecompression_gloss is "1" ["1"] whether to compress glossmap (specular) textures
    gl_texturecompression_glow is "1" ["1"] whether to compress glowmap (luma) textures
    gl_texturecompression_lightcubemaps is "1" ["1"] whether to compress light cubemaps (spotlights and other light projection images)
    gl_texturecompression_normal is "0" ["0"] whether to compress normalmap (normalmap) textures
    gl_texturecompression_q3bspdeluxemaps is "0" ["0"] whether to compress deluxemaps in q3bsp format levels (only levels compiled with q3map2 -deluxe have these)
    gl_texturecompression_q3bsplightmaps is "0" ["0"] whether to compress lightmaps in q3bsp format levels
    gl_texturecompression_reflectmask is "1" ["1"] whether to compress reflection cubemap masks (mask of which areas of the texture should reflect the generic shiny cubemap)
    gl_texturecompression_sky is "0" ["0"] whether to compress sky textures
    gl_vbo is "3" ["3"] make use of GL_ARB_vertex_buffer_object extension to store static geometry in video memory for faster rendering, 0 disables VBO allocation or use, 1 enables VBOs for vertex and triangle data, 2 only for vertex data, 3 for vertex data and triangle data of simple meshes (ones with only one surface)
    halflifebsp is "0" ["0"] indicates the current map is hlbsp format (useful to know because of different bounding box sizes)
    host_framerate is "0" ["0"] locks frame timing to this value in seconds, 0.05 is 20fps for example, note that this can easily run too fast, use cl_maxfps if you want to limit your framerate instead, or sys_ticrate to limit server speed
    host_speeds is "0" ["0"] reports how much time is used in server/graphics/sound
    hostname is "UNNAMED" ["UNNAMED"] server message to show in server browser
    in_pitch_max is "90" ["90"] how far upward you can aim (quake used 80
    in_pitch_min is "-90" ["-90"] how far downward you can aim (quake used -70
    joyadvanced is "0" ["0"] use more than 2 axis joysticks (configuring this is very technical)
    joyadvaxisr is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyadvaxisu is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyadvaxisv is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyadvaxisx is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyadvaxisy is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyadvaxisz is "0" ["0"] axis mapping for joyadvanced 1 mode
    joyforwardsensitivity is "-1.0" ["-1.0"] how fast the joystick moves forward
    joyforwardthreshold is "0.15" ["0.15"] minimum joystick movement necessary to move forward
    joyname is "joystick" ["joystick"] name of joystick to use (informational only, used only by joyadvanced 1 mode)
    joypitchsensitivity is "1.0" ["1.0"] how fast the joystick looks up/down
    joypitchthreshold is "0.15" ["0.15"] minimum joystick movement necessary to look up/down
    joysidesensitivity is "-1.0" ["-1.0"] how fast the joystick moves sideways (strafing)
    joysidethreshold is "0.15" ["0.15"] minimum joystick movement necessary to move sideways (strafing)
    joystick is "0" ["0"] enables joysticks
    joywwhack1 is "0.0" ["0.0"] special hack for wingman warrior
    joywwhack2 is "0.0" ["0.0"] special hack for wingman warrior
    joyyawsensitivity is "-1.0" ["-1.0"] how fast the joystick turns left/right
    joyyawthreshold is "0.15" ["0.15"] minimum joystick movement necessary to turn left/right
    locs_enable is "1" ["1"] enables replacement of certain % codes in chat messages: %l (location), %d (last death location), %h (health), %a (armor), %x (rockets), %c (cells), %r (rocket launcher status), %p (powerup status), %w (weapon status), %t (current time in level)
    locs_show is "0" ["0"] shows defined locations for editing purposes
    log_dest_udp is "" [""] UDP address to log messages to (in QW rcon compatible format); multiple destinations can be separated by spaces; DO NOT SPECIFY DNS NAMES HERE
    log_file is "" [""] filename to log messages to
    lookspring is "0" ["0"] returns pitch to level with the floor when no longer holding a pitch key
    lookstrafe is "0" ["0"] move instead of turning
    m_accelerate is "1" ["1"] mouse acceleration factor (try 2)
    m_accelerate_filter is "0.1" ["0.1"] mouse acceleration factor filtering
    m_accelerate_maxspeed is "10000" ["10000"] above this speed, full acceleration is done
    m_accelerate_minspeed is "5000" ["5000"] below this speed, no acceleration is done
    m_filter is "0" ["0"] smoothes mouse movement, less responsive but smoother aiming
    m_forward is "1" ["1"] mouse forward speed multiplier
    m_pitch is "0.022" ["0.022"] mouse pitch speed multiplier
    m_side is "0.8" ["0.8"] mouse side speed multiplier
    m_yaw is "0.022" ["0.022"] mouse yaw speed multiplier
    menu_options_colorcontrol_correctionvalue is "0.5" ["0.5"] intensity value that matches up to white/black dither pattern, should be 0.5 for linear color
    mod_alias_supporttagscale is "1" ["1"] support scaling factors in bone/tag attachment matrices as supported by MD3
    mod_collision_bih is "1" ["1"] enables use of generated Bounding Interval Hierarchy tree instead of compiled bsp tree in collision code
    mod_generatelightmaps_borderpixels is "2" ["2"] extra space around polygons to prevent sampling artifacts
    mod_generatelightmaps_gridradius is "64" ["64"] sampling area around each lightgrid cell center
    mod_generatelightmaps_gridsamples is "64" ["64"] number of shadow tests done per lightgrid cell
    mod_generatelightmaps_lightmapradius is "16" ["16"] sampling area around each lightmap pixel
    mod_generatelightmaps_lightmapsamples is "16" ["16"] number of shadow tests done per lightmap pixel
    mod_generatelightmaps_texturesize is "1024" ["1024"] size of lightmap textures
    mod_generatelightmaps_unitspersample is "8" ["8"] lightmap resolution
    mod_generatelightmaps_vertexradius is "16" ["16"] sampling area around each vertex
    mod_generatelightmaps_vertexsamples is "16" ["16"] number of shadow tests done per vertex
    mod_q1bsp_polygoncollisions is "0" ["0"] disables use of precomputed cliphulls and instead collides with polygons (uses Bounding Interval Hierarchy optimizations)
    mod_q3bsp_curves_collisions is "1" ["1"] enables collisions with curves (SLOW)
    mod_q3bsp_curves_collisions_stride is "16" ["16"] collisions against curves: optimize performance by doing a combined collision check for this triangle amount first (-1 avoids any box tests)
    mod_q3bsp_curves_stride is "16" ["16"] particle effect collisions against curves: optimize performance by doing a combined collision check for this triangle amount first (-1 avoids any box tests)
    mod_q3bsp_debugtracebrush is "0" ["0"] selects different tracebrush bsp recursion algorithms (for debugging purposes only)
    mod_q3bsp_lightmapmergepower is "4" ["4"] merges the quake3 128x128 lightmap textures into larger lightmap group textures to speed up rendering, 1 = 256x256, 2 = 512x512, 3 = 1024x1024, 4 = 2048x2048, 5 = 4096x4096, ...
    mod_q3bsp_nolightmaps is "0" ["0"] do not load lightmaps in Q3BSP maps (to save video RAM, but be warned: it looks ugly)
    mod_q3bsp_optimizedtraceline is "1" ["1"] whether to use optimized traceline code for line traces (as opposed to tracebox code)
    mod_q3bsp_tracelineofsight_brushes is "0" ["0"] enables culling of entities behind detail brushes, curves, etc
    mod_q3shader_default_offsetmapping is "1" ["1"] use offsetmapping by default on all surfaces
    mod_recalculatenodeboxes is "1" ["1"] enables use of generated node bounding boxes based on BSP tree portal reconstruction, rather than the node boxes supplied by the map compiler
    music_playlist_current0 is "0" ["0"] current track index to play in list
    music_playlist_current1 is "0" ["0"] current track index to play in list
    music_playlist_current2 is "0" ["0"] current track index to play in list
    music_playlist_current3 is "0" ["0"] current track index to play in list
    music_playlist_current4 is "0" ["0"] current track index to play in list
    music_playlist_current5 is "0" ["0"] current track index to play in list
    music_playlist_current6 is "0" ["0"] current track index to play in list
    music_playlist_current7 is "0" ["0"] current track index to play in list
    music_playlist_current8 is "0" ["0"] current track index to play in list
    music_playlist_current9 is "0" ["0"] current track index to play in list
    music_playlist_index is "-1" ["-1"] selects which of the music_playlist_ variables is the active one, -1 disables playlists
    music_playlist_list0 is "" [""] list of tracks to play
    music_playlist_list1 is "" [""] list of tracks to play
    music_playlist_list2 is "" [""] list of tracks to play
    music_playlist_list3 is "" [""] list of tracks to play
    music_playlist_list4 is "" [""] list of tracks to play
    music_playlist_list5 is "" [""] list of tracks to play
    music_playlist_list6 is "" [""] list of tracks to play
    music_playlist_list7 is "" [""] list of tracks to play
    music_playlist_list8 is "" [""] list of tracks to play
    music_playlist_list9 is "" [""] list of tracks to play
    music_playlist_random0 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random1 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random2 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random3 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random4 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random5 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random6 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random7 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random8 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_random9 is "0" ["0"] enables random play order if 1, 0 is sequential play
    music_playlist_sampleposition0 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition1 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition2 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition3 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition4 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition5 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition6 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition7 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition8 is "-1" ["-1"] resume position for track, -1 restarts every time
    music_playlist_sampleposition9 is "-1" ["-1"] resume position for track, -1 restarts every time
    net_address is "" [""] network address to open ipv4 ports on (if empty, use default interfaces)
    net_address_ipv6 is "" [""] network address to open ipv6 ports on (if empty, use default interfaces)
    net_connectfloodblockingtimeout is "5" ["5"] when a connection packet is received, it will block all future connect packets from that IP address for this many seconds (cuts down on connect floods)
    net_connecttimeout is "15" ["15"] after requesting a connection, the client must reply within this many seconds or be dropped (cuts down on connect floods). Must be above 10 seconds.
    net_messagetimeout is "300" ["300"] drops players who have not sent any packets for this many seconds
    net_slist_favorites is "" [""] contains a list of IP addresses and ports to always query explicitly
    net_slist_maxtries is "3" ["3"] how many times to ask the same server for information (more times gives better ping reports but takes longer)
    net_slist_pause is "0" ["0"] when set to 1, the server list won't update until it is set back to 0
    net_slist_queriesperframe is "4" ["4"] maximum number of server information requests to send each rendered frame (guards against low framerates causing problems)
    net_slist_queriespersecond is "20" ["20"] how many server information requests to send per second
    net_slist_timeout is "4" ["4"] how long to listen for a server information response before giving up
    noaim is "1" ["1"] QW option to disable vertical autoaim
    noexit is "0" ["0"] kills anyone attempting to use an exit
    nomonsters is "0" ["0"] unused cvar in quake, can be used by mods
    nosound is "0" ["0"] disables sound
    pausable is "1" ["1"] allow players to pause or not
    port is "26000" ["26000"] server port for players to connect to
    pr_checkextension is "1" ["1"] indicates to QuakeC that the standard quakec extensions system is available (if 0, quakec should not attempt to use extensions)
    prvm_backtraceforwarnings is "0" ["0"] print a backtrace for warnings too
    prvm_errordump is "0" ["0"] write a savegame on crash to crash-server.dmp
    prvm_language is "" [""] when set, loads progs.dat.LANGUAGENAME.po for string translations; when set to dump, progs.dat.dump.po is written from the strings in the progs
    prvm_leaktest is "0" ["0"] try to detect memory leaks in strings or entities
    prvm_leaktest_ignore_classnames is "" [""] classnames of entities to NOT leak check because they are found by find(world, classname, ...) but are actually spawned by QC code (NOT map entities)
    prvm_reuseedicts_neverinsameframe is "1" ["1"] never allows re-use of freed entity slots during same frame
    prvm_reuseedicts_startuptime is "2" ["2"] allows immediate re-use of freed entity slots during start of new level (value in seconds)
    prvm_statementprofiling is "0" ["0"] counts how many times each QuakeC statement has been executed, these counts are displayed in prvm_printfunction output (if enabled)
    prvm_traceqc is "0" ["0"] prints every QuakeC statement as it is executed (only for really thorough debugging!)
    qport is "31514" ["31514"] identification key for playing on qw servers (allows you to maintain a connection to a quakeworld server even if your port changes)
    r_ambient is "0" ["0"] brightens map, value is 0-128
    r_batchmode is "1" ["1"] selects method of rendering multiple surfaces with one driver call (values are 0, 1, 2, etc...)
    r_bloom is "1" ["0"] enables bloom effect (makes bright pixels affect neighboring pixels)
    r_bloom_blur is "4" ["4"] how large the glow is
    r_bloom_brighten is "2" ["2"] how bright the glow is, after subtract/power
    r_bloom_colorexponent is "1" ["1"] how exagerated the glow is
    r_bloom_colorscale is "1" ["1"] how bright the glow is
    r_bloom_colorsubtract is "0.125" ["0.125"] reduces bloom colors by a certain amount
    r_bloom_resolution is "320" ["320"] what resolution to perform the bloom effect at (independent of screen resolution)
    r_colormap_palette is "gfx/colormap_palette.lmp" ["gfx/colormap_palette.lmp"] name of a palette lmp file to override the shirt/pants colors of player models. It consists of 16 shirt colors, 16 scoreboard shirt colors, 16 pants colors and 16 scoreboard pants colors
    r_coronas is "1" ["1"] brightness of corona flare effects around certain lights, 0 disables corona effects
    r_coronas_occlusionquery is "1" ["1"] use GL_ARB_occlusion_query extension if supported (fades coronas according to visibility)
    r_coronas_occlusionsizescale is "0.1" ["0.1"] size of light source for corona occlusion checksm the proportion of hidden pixels controls corona intensity
    r_cullentities_trace is "1" ["1"] probabistically cull invisible entities
    r_cullentities_trace_delay is "1" ["1"] number of seconds until the entity gets actually culled
    r_cullentities_trace_enlarge is "0" ["0"] box enlargement for entity culling
    r_cullentities_trace_samples is "2" ["2"] number of samples to test for entity culling (in addition to center sample)
    r_cullentities_trace_tempentitysamples is "-1" ["-1"] number of samples to test for entity culling of temp entities (including all CSQC entities), -1 disables trace culling on these entities to prevent flicker (pvs still applies)
    r_damageblur is "0" ["0"] motionblur based on damage
    r_depthfirst is "0" ["0"] renders a depth-only version of the scene before normal rendering begins to eliminate overdraw, values: 0 = off, 1 = world depth, 2 = world and model depth
    r_drawdecals is "1" ["1"] enables drawing of decals
    r_drawdecals_drawdistance is "500" ["500"] decals further than drawdistance*size will not be drawn
    r_draweffects is "1" ["1"] renders temporary sprite effects
    r_drawentities is "1" ["1"] draw entities (doors, players, projectiles, etc)
    r_drawexplosions is "1" ["1"] enables rendering of explosion shells (see also cl_particles_explosions_shell)
    r_drawexteriormodel is "1" ["1"] draw your player model (e.g. in chase cam, reflections)
    r_drawfog is "1" ["1"] allows one to disable fog rendering
    r_drawparticles is "1" ["1"] enables drawing of particles
    r_drawparticles_drawdistance is "2000" ["2000"] particles further than drawdistance*size will not be drawn
    r_drawportals is "0" ["0"] shows portals (separating polygons) in world interior in quake1 maps
    r_drawviewmodel is "1" ["1"] draw your weapon model
    r_dynamic is "1" ["1"] enables dynamic lights (rocket glow and such)
    r_editlights is "0" ["0"] enables .rtlights file editing mode
    r_editlights_cursordistance is "1024" ["1024"] maximum distance of cursor from eye
    r_editlights_cursorgrid is "4" ["4"] snaps cursor to this grid size
    r_editlights_cursorpushback is "0" ["0"] how far to pull the cursor back toward the eye
    r_editlights_cursorpushoff is "4" ["4"] how far to push the cursor off the impacted surface
    r_editlights_quakelightsizescale is "1" ["1"] changes size of light entities loaded from a map
    r_equalize_entities_by is "0.7" ["0.7"] light equalizing: exponent of dynamics compression (0 = no compression, 1 = full compression)
    r_equalize_entities_fullbright is "0" ["0"] render fullbright entities by equalizing their lightness, not by not rendering light
    r_equalize_entities_minambient is "0.5" ["0.5"] light equalizing: ensure at least this ambient/diffuse ratio
    r_equalize_entities_to is "0.8" ["0.8"] light equalizing: target light level
    r_explosionclip is "1" ["1"] enables collision detection for explosion shell (so that it flattens against walls and floors)
    r_farclip_base is "65536" ["65536"] farclip (furthest visible distance) for rendering when r_useinfinitefarclip is 0
    r_farclip_world is "2" ["2"] adds map size to farclip multiplied by this value
    r_fixtrans_auto is "0" ["0"] automatically fixtrans textures (when set to 2, it also saves the fixed versions to a fixtrans directory)
    r_fog_exp2 is "0" ["0"] uses GL_EXP2 fog (as in Nehahra) rather than realistic GL_EXP fog
    r_font_antialias is "1" ["1"] 0 = monochrome, 1 = grey
    r_font_disable_freetype is "1" ["1"] disable freetype support for fonts entirely
    r_font_hinting is "3" ["3"] 0 = no hinting, 1 = light autohinting, 2 = full autohinting, 3 = full hinting
    r_font_kerning is "1" ["1"] Use kerning if available
    r_font_postprocess_blur is "0" ["0"] font blur amount
    r_font_postprocess_outline is "0" ["0"] font outline amount
    r_font_postprocess_shadow_x is "0" ["0"] font shadow X shift amount, applied during outlining
    r_font_postprocess_shadow_y is "0" ["0"] font shadow Y shift amount, applied during outlining
    r_font_postprocess_shadow_z is "0" ["0"] font shadow Z shift amount, applied during blurring
    r_font_size_snapping is "1" ["1"] stick to good looking font sizes whenever possible - bad when the mod doesn't support it!
    r_font_use_alpha_textures is "0" ["0"] use alpha-textures for font rendering, this should safe memory
    r_framedatasize is "1" ["1"] size of renderer data cache used during one frame (for skeletal animation caching, light processing, etc)
    r_fullbright is "0" ["0"] makes map very bright and renders faster
    r_fullbrights is "1" ["1"] enables glowing pixels in quake textures (changes need r_restart to take effect)
    r_glsl is "1" ["1"] indicates whether the OpenGL 2.0 rendering path is active
    r_glsl_deluxemapping is "1" ["1"] use per pixel lighting on deluxemap-compiled q3bsp maps (or a value of 2 forces deluxemap shading even without deluxemaps)
    r_glsl_offsetmapping is "0" ["0"] offset mapping effect (also known as parallax mapping or virtual displacement mapping)
    r_glsl_offsetmapping_reliefmapping is "0" ["0"] relief mapping effect (higher quality)
    r_glsl_offsetmapping_scale is "0.04" ["0.04"] how deep the offset mapping effect is
    r_glsl_postprocess is "0" ["0"] use a GLSL postprocessing shader
    r_glsl_postprocess_uservec1 is "0 0 0 0" ["0 0 0 0"] a 4-component vector to pass as uservec1 to the postprocessing shader (only useful if default.glsl has been customized)
    r_glsl_postprocess_uservec2 is "0 0 0 0" ["0 0 0 0"] a 4-component vector to pass as uservec2 to the postprocessing shader (only useful if default.glsl has been customized)
    r_glsl_postprocess_uservec3 is "0 0 0 0" ["0 0 0 0"] a 4-component vector to pass as uservec3 to the postprocessing shader (only useful if default.glsl has been customized)
    r_glsl_postprocess_uservec4 is "0 0 0 0" ["0 0 0 0"] a 4-component vector to pass as uservec4 to the postprocessing shader (only useful if default.glsl has been customized)
    r_glsl_saturation is "1" ["1"] saturation multiplier (only working in glsl!)
    r_hdr is "1" ["0"] enables High Dynamic Range bloom effect (higher quality version of r_bloom)
    r_hdr_glowintensity is "1" ["1"] how bright light emitting textures should appear
    r_hdr_range is "4" ["4"] how much dynamic range to render bloom with (equivilant to multiplying r_bloom_brighten by this value and dividing r_bloom_colorscale by this value)
    r_hdr_scenebrightness is "1" ["1"] global rendering brightness
    r_labelsprites_roundtopixels is "1" ["1"] try to make label sprites sharper by rounding their size to 0.5x or 1x and by rounding their position to whole pixels if possible
    r_labelsprites_scale is "1" ["1"] global scale to apply to label sprites before conversion to HUD coordinates
    r_lerpimages is "1" ["1"] bilinear filters images when scaling them up to power of 2 size (mode 1), looks better than glquake (mode 0)
    r_lerplightstyles is "0" ["0"] enable animation smoothing on flickering lights
    r_lerpmodels is "1" ["1"] enables animation smoothing on models
    r_lerpsprites is "0" ["0"] enables animation smoothing on sprites
    r_letterbox is "0" ["0"] reduces vertical height of view to simulate a letterboxed movie effect (can be used by mods for cutscenes)
    r_lightningbeam_color_blue is "1" ["1"] color of the lightning beam effect
    r_lightningbeam_color_green is "1" ["1"] color of the lightning beam effect
    r_lightningbeam_color_red is "1" ["1"] color of the lightning beam effect
    r_lightningbeam_qmbtexture is "0" ["0"] load the qmb textures/particles/lightning.pcx texture instead of generating one, can look better
    r_lightningbeam_repeatdistance is "128" ["128"] how far to stretch the texture along the lightning beam effect
    r_lightningbeam_scroll is "5" ["5"] speed of texture scrolling on the lightning beam effect
    r_lightningbeam_thickness is "4" ["4"] thickness of the lightning beam effect
    r_lockpvs is "0" ["0"] disables pvs switching, allows you to walk around and inspect what is visible from a given location in the map (anything not visible from your current location will not be drawn)
    r_lockvisibility is "0" ["0"] disables visibility updates, allows you to walk around and inspect what is visible from a given viewpoint in the map (anything offscreen at the moment this is enabled will not be drawn)
    r_mipskins is "0" ["0"] mipmaps model skins so they render faster in the distance and do not display noise artifacts, can cause discoloration of skins if they contain undesirable border colors
    r_mipsprites is "1" ["1"] mipmaps sprites so they render faster in the distance and do not display noise artifacts
    r_motionblur is "0" ["0"] motionblur value scale - 0.5 recommended
    r_motionblur_bmin is "0.5" ["0.5"] velocity at which there is no blur yet (may be negative to always have some blur)
    r_motionblur_maxblur is "0.88" ["0.88"] cap for motionblur alpha value
    r_motionblur_randomize is "0.1" ["0.1"] randomizing coefficient to workaround ghosting
    r_motionblur_vcoeff is "0.05" ["0.05"] sliding average reaction time for velocity
    r_motionblur_vmax is "600" ["600"] maximum influence from velocity
    r_motionblur_vmin is "300" ["300"] minimum influence from velocity
    r_nearclip is "1" ["1"] distance from camera of nearclip plane
    r_nosurftextures is "0" ["0"] pretends there was no texture lump found in the q1bsp/hlbsp loading (useful for debugging this rare case)
    r_novis is "0" ["0"] draws whole level, see also sv_cullentities_pvs 0
    r_overheadsprites_perspective is "0.15" ["0.15"] fake perspective effect for SPR_OVERHEAD sprites
    r_overheadsprites_pushback is "16" ["16"] how far to pull the SPR_OVERHEAD sprites toward the eye (used to avoid intersections with 3D models)
    r_picmipsprites is "1" ["1"] make gl_picmip affect sprites too (saves some graphics memory in sprite heavy games)
    r_picmipworld is "1" ["1"] whether gl_picmip shall apply to world textures too
    r_polygonoffset_decals_factor is "0" ["0"] biases depth values of decals to prevent z-fighting artifacts
    r_polygonoffset_decals_offset is "-14" ["-14"] biases depth values of decals to prevent z-fighting artifacts
    r_polygonoffset_submodel_factor is "0" ["0"] biases depth values of world submodels such as doors, to prevent z-fighting artifacts in Quake maps
    r_polygonoffset_submodel_offset is "14" ["14"] biases depth values of world submodels such as doors, to prevent z-fighting artifacts in Quake maps
    r_q1bsp_skymasking is "1" ["1"] allows sky polygons in quake1 maps to obscure other geometry
    r_q3bsp_renderskydepth is "0" ["0"] draws sky depth masking in q3 maps (as in q1 maps), this means for example that sky polygons can hide other things
    r_render is "1" ["1"] enables rendering 3D views (you want this on!)
    r_renderview is "1" ["1"] enables rendering 3D views (you want this on!)
    r_shadow_bumpscale_basetexture is "0" ["0"] generate fake bumpmaps from diffuse textures at this bumpyness, try 4 to match tenebrae, higher values increase depth, requires r_restart to take effect
    r_shadow_bumpscale_bumpmap is "4" ["4"] what magnitude to interpret _bump.tga textures as, higher values increase depth, requires r_restart to take effect
    r_shadow_debuglight is "-1" ["-1"] renders only one light, for level design purposes or debugging
    r_shadow_deferred is "0" ["0"] uses image-based lighting instead of geometry-based lighting, the method used renders a depth image and a normalmap image, renders lights into separate diffuse and specular images, and then combines this into the normal rendering, requires r_shadow_shadowmapping
    r_shadow_deferred_8bitrange is "2" ["2"] dynamic range of image-based lighting when using 32bit color (does not apply to fp)
    r_shadow_frontsidecasting is "1" ["1"] whether to cast shadows from illuminated triangles (front side of model) or unlit triangles (back side of model)
    r_shadow_gloss is "1" ["1"] 0 disables gloss (specularity) rendering, 1 uses gloss if textures are found, 2 forces a flat metallic specular effect on everything without textures (similar to tenebrae)
    r_shadow_gloss2exponent is "32" ["32"] same as r_shadow_glossexponent but for forced gloss (gloss 2) surfaces
    r_shadow_gloss2intensity is "0.125" ["0.125"] how bright the forced flat gloss should look if r_shadow_gloss is 2
    r_shadow_glossexact is "0" ["0"] use exact reflection math for gloss (slightly slower, but should look a tad better)
    r_shadow_glossexponent is "32" ["32"] how 'sharp' the gloss should appear (specular power)
    r_shadow_glossintensity is "1" ["1"] how bright textured glossmaps should look if r_shadow_gloss is 1 or 2
    r_shadow_lightattenuationdividebias is "1" ["1"] changes attenuation texture generation
    r_shadow_lightattenuationlinearscale is "2" ["2"] changes attenuation texture generation
    r_shadow_lightintensityscale is "1" ["1"] renders all world lights brighter or darker
    r_shadow_lightradiusscale is "1" ["1"] renders all world lights larger or smaller
    r_shadow_polygonfactor is "0" ["0"] how much to enlarge shadow volume polygons when rendering (should be 0!)
    r_shadow_polygonoffset is "1" ["1"] how much to push shadow volumes into the distance when rendering, to reduce chances of zfighting artifacts (should not be less than 0)
    r_shadow_projectdistance is "0" ["0"] how far to cast shadows
    r_shadow_realtime_dlight is "1" ["1"] enables rendering of dynamic lights such as explosions and rocket light
    r_shadow_realtime_dlight_portalculling is "0" ["0"] enables portal optimization on dynamic lights (slow!)
    r_shadow_realtime_dlight_shadows is "1" ["1"] enables rendering of shadows from dynamic lights
    r_shadow_realtime_dlight_svbspculling is "0" ["0"] enables svbsp optimization on dynamic lights (very slow!)
    r_shadow_realtime_world is "0" ["0"] enables rendering of full world lighting (whether loaded from the map, or a .rtlights file, or a .ent file, or a .lights file produced by hlight)
    r_shadow_realtime_world_compile is "1" ["1"] enables compilation of world lights for higher performance rendering
    r_shadow_realtime_world_compileportalculling is "0" ["0"] enables portal-based culling optimization during compilation (overrides compilesvbsp)
    r_shadow_realtime_world_compileshadow is "1" ["1"] enables compilation of shadows from world lights for higher performance rendering
    r_shadow_realtime_world_compilesvbsp is "1" ["1"] enables svbsp optimization during compilation (slower than compileportalculling but more exact)
    r_shadow_realtime_world_lightmaps is "0" ["0"] brightness to render lightmaps when using full world lighting, try 0.5 for a tenebrae-like appearance
    r_shadow_realtime_world_shadows is "1" ["1"] enables rendering of shadows from world lights
    r_shadow_scissor is "1" ["1"] use scissor optimization of light rendering (restricts rendering to the portion of the screen affected by the light)
    r_shadow_shadowmapping is "0" ["0"] enables use of shadowmapping (depth texture sampling) instead of stencil shadow volumes, requires gl_fbo 1
    r_shadow_shadowmapping_bias is "0.03" ["0.03"] shadowmap bias parameter (this is multiplied by nearclip * 1024 / lodsize)
    r_shadow_shadowmapping_bordersize is "4" ["4"] shadowmap size bias for filtering
    r_shadow_shadowmapping_depthbits is "24" ["24"] requested minimum shadowmap texture depth bits
    r_shadow_shadowmapping_filterquality is "-1" ["-1"] shadowmap filter modes: -1 = auto-select, 0 = no filtering, 1 = bilinear, 2 = bilinear 2x2 blur (fast), 3 = 3x3 blur (moderate), 4 = 4x4 blur (slow)
    r_shadow_shadowmapping_maxsize is "512" ["512"] shadowmap size limit
    r_shadow_shadowmapping_minsize is "32" ["32"] shadowmap size limit
    r_shadow_shadowmapping_nearclip is "1" ["1"] shadowmap nearclip in world units
    r_shadow_shadowmapping_polygonfactor is "2" ["2"] slope-dependent shadowmapping bias
    r_shadow_shadowmapping_polygonoffset is "0" ["0"] constant shadowmapping bias
    r_shadow_shadowmapping_precision is "1" ["1"] makes shadowmaps have a maximum resolution of this number of pixels per light source radius unit such that, for example, at precision 0.5 a light with radius 200 will have a maximum resolution of 100 pixels
    r_shadow_shadowmapping_texturetype is "-1" ["-1"] shadowmap texture types: -1 = auto-select, 0 = 2D, 1 = rectangle, 2 = cubemap
    r_shadow_shadowmapping_vsdct is "1" ["1"] enables use of virtual shadow depth cube texture
    r_shadow_texture3d is "1" ["1"] use 3D voxel textures for spherical attenuation rather than cylindrical (does not affect OpenGL 2.0 render path)
    r_shadow_usenormalmap is "1" ["1"] enables use of directional shading on lights
    r_shadows is "0" ["0"] casts fake stencil shadows from models onto the world (rtlights are unaffected by this); when set to 2, always cast the shadows in the direction set by r_shadows_throwdirection, otherwise use the model lighting.
    r_shadows_castfrombmodels is "0" ["0"] do cast shadows from bmodels
    r_shadows_darken is "0.5" ["0.5"] how much shadowed areas will be darkened
    r_shadows_drawafterrtlighting is "0" ["0"] draw fake shadows AFTER realtime lightning is drawn. May be useful for simulating fast sunlight on large outdoor maps with only one noshadow rtlight. The price is less realistic appearance of dynamic light shadows.
    r_shadows_focus is "0 0 0" ["0 0 0"] offset the shadowed area focus
    r_shadows_shadowmapscale is "1" ["1"] increases shadowmap quality (multiply global shadowmap precision) for fake shadows. Needs shadowmapping ON.
    r_shadows_throwdirection is "0 0 -1" ["0 0 -1"] override throwing direction for r_shadows 2
    r_shadows_throwdistance is "500" ["500"] how far to cast shadows from models
    r_showbboxes is "0" ["0"] shows bounding boxes of server entities, value controls opacity scaling (1 = 10%,  10 = 100%)
    r_showcollisionbrushes is "0" ["0"] draws collision brushes in quake3 maps (mode 1), mode 2 disables rendering of world (trippy!)
    r_showcollisionbrushes_polygonfactor is "-1" ["-1"] expands outward the brush polygons a little bit, used to make collision brushes appear infront of walls
    r_showcollisionbrushes_polygonoffset is "0" ["0"] nudges brush polygon depth in hardware depth units, used to make collision brushes appear infront of walls
    r_showdisabledepthtest is "0" ["0"] disables depth testing on r_show* cvars, allowing you to see what hidden geometry the graphics card is processing
    r_showlighting is "0" ["0"] shows areas lit by lights, useful for finding out why some areas of a map render slowly (bright orange = lots of passes = slow), a value of 2 disables depth testing which can be interesting but not very useful
    r_shownormals is "0" ["0"] shows per-vertex surface normals and tangent vectors for bumpmapped lighting
    r_showshadowvolumes is "0" ["0"] shows areas shadowed by lights, useful for finding out why some areas of a map render slowly (bright blue = lots of passes = slow), a value of 2 disables depth testing which can be interesting but not very useful
    r_showsurfaces is "0" ["0"] 1 shows surfaces as different colors, or a value of 2 shows triangle draw order (for analyzing whether meshes are optimized for vertex cache)
    r_showtris is "0" ["0"] shows triangle outlines, value controls brightness (can be above 1)
    r_skeletal_debugbone is "-1" ["-1"] development cvar for testing skeletal model code
    r_skeletal_debugbonecomponent is "3" ["3"] development cvar for testing skeletal model code
    r_skeletal_debugbonevalue is "100" ["100"] development cvar for testing skeletal model code
    r_skeletal_debugtranslatex is "1" ["1"] development cvar for testing skeletal model code
    r_skeletal_debugtranslatey is "1" ["1"] development cvar for testing skeletal model code
    r_skeletal_debugtranslatez is "1" ["1"] development cvar for testing skeletal model code
    r_sky is "1" ["1"] enables sky rendering (black otherwise)
    r_skyscroll1 is "1" ["1"] speed at which upper clouds layer scrolls in quake sky
    r_skyscroll2 is "2" ["2"] speed at which lower clouds layer scrolls in quake sky
    r_smoothnormals_areaweighting is "1" ["1"] uses significantly faster (and supposedly higher quality) area-weighted vertex normals and tangent vectors rather than summing normalized triangle normals and tangents
    r_speeds is "0" ["0"] displays rendering statistics and per-subsystem timings
    r_stereo_angle is "0" ["0"] separation angle of eyes (makes the views look different directions, as an example, 90 gives a 90 degree separation where the views are 45 degrees left and 45 degrees right)
    r_stereo_redblue is "0" ["0"] red/blue anaglyph stereo glasses (note: most of these glasses are actually red/cyan, try that one too)
    r_stereo_redcyan is "0" ["0"] red/cyan anaglyph stereo glasses, the kind given away at drive-in movies like Creature From The Black Lagoon In 3D
    r_stereo_redgreen is "0" ["0"] red/green anaglyph stereo glasses (for those who don't mind yellow)
    r_stereo_separation is "4" ["4"] separation distance of eyes in the world (negative values are only useful for cross-eyed viewing)
    r_stereo_sidebyside is "0" ["0"] side by side views for those who can't afford glasses but can afford eye strain (note: use a negative r_stereo_separation if you want cross-eyed viewing)
    r_subdivisions_collision_maxtess is "1024" ["1024"] maximum number of subdivisions (prevents curves beyond a certain detail level, limits smoothing)
    r_subdivisions_collision_maxvertices is "4225" ["4225"] maximum vertices allowed per subdivided curve
    r_subdivisions_collision_mintess is "0" ["0"] minimum number of subdivisions (values above 0 will smooth curves that don't need it)
    r_subdivisions_collision_tolerance is "15" ["15"] maximum error tolerance on curve subdivision for collision purposes (usually a larger error tolerance than for rendering)
    r_subdivisions_maxtess is "1024" ["1024"] maximum number of subdivisions (prevents curves beyond a certain detail level, limits smoothing)
    r_subdivisions_maxvertices is "65536" ["65536"] maximum vertices allowed per subdivided curve
    r_subdivisions_mintess is "0" ["0"] minimum number of subdivisions (values above 0 will smooth curves that don't need it)
    r_subdivisions_tolerance is "4" ["4"] maximum error tolerance on curve subdivision for rendering purposes (in other words, the curves will be given as many polygons as necessary to represent curves at this quality)
    r_test is "0" ["0"] internal development use only, leave it alone (usually does nothing anyway)
    r_textbrightness is "0" ["0"] additional brightness for text color codes (0 keeps colors as is, 1 makes them all white)
    r_textcontrast is "1" ["1"] additional contrast for text color codes (1 keeps colors as is, 0 makes them all black)
    r_textshadow is "0" ["0"] draws a shadow on all text to improve readability (note: value controls offset, 1 = 1 pixel, 1.5 = 1.5 pixels, etc)
    r_texture_convertsRGB_2d is "0" ["0"] load textures as sRGB and convert to linear for proper shading
    r_texture_convertsRGB_cubemap is "0" ["0"] load textures as sRGB and convert to linear for proper shading
    r_texture_convertsRGB_particles is "0" ["0"] load textures as sRGB and convert to linear for proper shading
    r_texture_convertsRGB_skin is "0" ["0"] load textures as sRGB and convert to linear for proper shading
    r_texture_convertsRGB_skybox is "0" ["0"] load textures as sRGB and convert to linear for proper shading
    r_texture_dds_load is "0" ["0"] load compressed dds/filename.dds texture instead of filename.tga, if the file exists (requires driver support)
    r_texture_dds_save is "0" ["0"] save compressed dds/filename.dds texture when filename.tga is loaded, so that it can be loaded instead next time
    r_textureunits is "4" ["32"] number of texture units to use in GL 1.1 and GL 1.3 rendering paths
    r_track_sprites is "1" ["1"] track SPR_LABEL* sprites by putting them as indicator at the screen border to rotate to
    r_track_sprites_flags is "1" ["1"] 1: Rotate sprites accodringly, 2: Make it a continuous rotation
    r_track_sprites_scaleh is "1" ["1"] height scaling of tracked sprites
    r_track_sprites_scalew is "1" ["1"] width scaling of tracked sprites
    r_transparentdepthmasking is "0" ["0"] enables depth writes on transparent meshes whose materially is normally opaque, this prevents seeing the inside of a transparent mesh
    r_useinfinitefarclip is "1" ["1"] enables use of a special kind of projection matrix that has an extremely large farclip
    r_useportalculling is "1" ["1"] improve framerate with r_novis 1 by using portal culling - still not as good as compiled visibility data in the map, but it helps (a value of 2 forces use of this even with vis data, which improves framerates in maps without too much complexity, but hurts in extremely complex maps, which is why 2 is not the default mode)
    r_water is "0" ["0"] whether to use reflections and refraction on water surfaces (note: r_wateralpha must be set below 1)
    r_water_clippingplanebias is "1" ["1"] a rather technical setting which avoids black pixels around water edges
    r_water_reflectdistort is "0.01" ["0.01"] how much water reflections shimmer
    r_water_refractdistort is "0.01" ["0.01"] how much water refractions shimmer
    r_water_resolutionmultiplier is "0.5" ["0.5"] multiplier for screen resolution when rendering refracted/reflected scenes, 1 is full quality, lower values are faster
    r_wateralpha is ".2" ["1"] opacity of water polygons
    r_waterscroll is "1" ["1"] makes water scroll around, value controls how much
    r_waterwarp is "1" ["1"] warp view while underwater
    rcon_address is "" [""] server address to send rcon commands to (when not connected to a server)
    rcon_password is "********" [""] password to authenticate rcon commands; NOTE: changing rcon_secure clears rcon_password, so set rcon_secure always before rcon_password; may be set to a string of the form user1:pass1 user2:pass2 user3:pass3 to allow multiple user accounts - the client then has to specify ONE of these combinations
    rcon_restricted_commands is "" [""] allowed commands for rcon when the restricted mode password was used
    rcon_restricted_password is "********" [""] password to authenticate rcon commands in restricted mode; may be set to a string of the form user1:pass1 user2:pass2 user3:pass3 to allow multiple user accounts - the client then has to specify ONE of these combinations
    rcon_secure is "0" ["0"] force secure rcon authentication (1 = time based, 2 = challenge based); NOTE: changing rcon_secure clears rcon_password, so set rcon_secure always before rcon_password
    rcon_secure_challengetimeout is "5" ["5"] challenge-based secure rcon: time out requests if no challenge came within this time interval
    rcon_secure_maxdiff is "5" ["5"] maximum time difference between rcon request and server system clock (to protect against replay attack)
    registered is "1" ["1"] indicates if this is running registered quake (whether gfx/pop.lmp was found)
    samelevel is "0" ["0"] repeats same level if level ends (due to timelimit or someone hitting an exit)
    saved1 is "0" ["0"] unused cvar in quake that is saved to config.cfg on exit, can be used by mods
    saved2 is "0" ["0"] unused cvar in quake that is saved to config.cfg on exit, can be used by mods
    saved3 is "0" ["0"] unused cvar in quake that is saved to config.cfg on exit, can be used by mods
    saved4 is "0" ["0"] unused cvar in quake that is saved to config.cfg on exit, can be used by mods
    savedgamecfg is "0" ["0"] unused cvar in quake that is saved to config.cfg on exit, can be used by mods
    sbar_alpha_bg is "0.4" ["0.4"] opacity value of the statusbar background image
    sbar_alpha_fg is "1" ["1"] opacity value of the statusbar weapon/item icons and numbers
    sbar_gametime is "1" ["1"] shows an overlay for the time left in the current match/level (or current game time if there is no timelimit set)
    sbar_hudselector is "0" ["0"] selects which of the builtin hud layouts to use (meaning is somewhat dependent on gamemode, so nexuiz has a very different set of hud layouts than quake for example)
    sbar_info_pos is "0" ["0"] pixel position of the info strings (such as showfps), from the bottom
    sbar_miniscoreboard_size is "-1" ["-1"] sets the size of the mini deathmatch overlay in items, or disables it when set to 0, or sets it to a sane default when set to -1
    sbar_scorerank is "1" ["1"] shows an overlay for your score (or team score) and rank in the scoreboard
    scr_centertime is "2" ["2"] how long centerprint messages show
    scr_conalpha is "1" ["1"] opacity of console background
    scr_conbrightness is "1" ["1"] brightness of console background (0 = black, 1 = image)
    scr_conforcewhiledisconnected is "1" ["1"] forces fullscreen console while disconnected
    scr_loadingscreen_background is "0" ["0"] show the last visible background during loading screen (costs one screenful of video memory)
    scr_loadingscreen_count is "1" ["1"] number of loading screen files to use randomly (named loading.tga, loading2.tga, loading3.tga, ...)
    scr_menuforcewhiledisconnected is "0" ["0"] forces menu while disconnected
    scr_printspeed is "0" ["0"] speed of intermission printing (episode end texts), a value of 0 disables the slow printing
    scr_refresh is "1" ["1"] allows you to completely shut off rendering for benchmarking purposes
    scr_screenshot_gammaboost is "1" ["1"] gamma correction on saved screenshots and videos, 1.0 saves unmodified images
    scr_screenshot_hwgamma is "1" ["1"] apply the video gamma ramp to saved screenshots and videos
    scr_screenshot_jpeg is "1" ["1"] save jpeg instead of targa
    scr_screenshot_jpeg_quality is "0.9" ["0.9"] image quality of saved jpeg
    scr_screenshot_name is "dp" ["dp"] prefix name for saved screenshots (changes based on -game commandline, as well as which game mode is running; the date is encoded using strftime escapes)
    scr_screenshot_name_in_mapdir is "0" ["0"] if set to 1, screenshots are placed in a subdirectory named like the map they are from
    scr_screenshot_png is "0" ["0"] save png instead of targa
    scr_stipple is "0" ["0"] interlacing-like stippling of the display
    scr_zoomwindow is "0" ["0"] displays a zoomed in overlay window
    scr_zoomwindow_fov is "20" ["20"] fov of zoom window
    scr_zoomwindow_viewsizex is "20" ["20"] horizontal viewsize of zoom window
    scr_zoomwindow_viewsizey is "20" ["20"] vertical viewsize of zoom window
    scratch1 is "0" ["0"] unused cvar in quake, can be used by mods
    scratch2 is "0" ["0"] unused cvar in quake, can be used by mods
    scratch3 is "0" ["0"] unused cvar in quake, can be used by mods
    scratch4 is "0" ["0"] unused cvar in quake, can be used by mods
    sensitivity is "3" ["3"] mouse speed multiplier
    showblur is "0" ["0"] shows the current alpha level of motionblur
    showbrand is "0" ["0"] shows gfx/brand.tga in a corner of the screen (different values select different positions, including centered)
    showdate is "0" ["0"] shows current date (useful on screenshots)
    showdate_format is "%Y-%m-%d" ["%Y-%m-%d"] format string for date
    showfps is "0" ["0"] shows your rendered fps (frames per second)
    shownetgraph is "0" ["0"] shows a graph of packet sizes and other information, 0 = off, 1 = show client netgraph, 2 = show client and server netgraphs (when hosting a server)
    showpause is "1" ["1"] show pause icon when game is paused
    showram is "1" ["1"] show ram icon if low on surface cache memory (not used)
    showsound is "0" ["0"] shows number of active sound sources, sound latency, and other statistics
    showspeed is "0" ["0"] shows your current speed (qu per second); number selects unit: 1 = qu/s, 2 = m/s, 3 = km/h, 4 = mph, 5 = knots
    showtime is "0" ["0"] shows current time of day (useful on screenshots)
    showtime_format is "%H:%M:%S" ["%H:%M:%S"] format string for time of day
    showtopspeed is "0" ["0"] shows your top speed (kept on screen for max 3 seconds); value -1 takes over the unit from showspeed, otherwise it's an unit number just like in showspeed
    showturtle is "0" ["0"] show turtle icon when framerate is too low
    skill is "1" ["1"] difficulty level of game, affects monster layouts in levels, 0 = easy, 1 = normal, 2 = hard, 3 = nightmare (same layout as hard but monsters fire twice)
    skin is "" [""] QW player skin name (example: base)
    slowmo is "1.0" ["1.0"] controls game speed, 0.5 is half speed, 2 is double speed
    snd_channellayout is "1" ["0"] channel layout. Can be 0 (auto - snd_restart needed), 1 (standard layout), or 2 (ALSA layout)
    snd_channels is "2" ["2"] number of channels for the sound ouput (2 for stereo; up to 8 supported for 3D sound)
    snd_csqcchannel0volume is "1" ["1"] volume multiplier of the auto-allocate entity channel of the world entity
    snd_csqcchannel1volume is "1" ["1"] volume multiplier of the 1st entity channel of the world entity
    snd_csqcchannel2volume is "1" ["1"] volume multiplier of the 2nd entity channel of the world entity
    snd_csqcchannel3volume is "1" ["1"] volume multiplier of the 3rd entity channel of the world entity
    snd_csqcchannel4volume is "1" ["1"] volume multiplier of the 4th entity channel of the world entity
    snd_csqcchannel5volume is "1" ["1"] volume multiplier of the 5th entity channel of the world entity
    snd_csqcchannel6volume is "1" ["1"] volume multiplier of the 6th entity channel of the world entity
    snd_csqcchannel7volume is "1" ["1"] volume multiplier of the 7th entity channel of the world entity
    snd_entchannel0volume is "1" ["1"] volume multiplier of the auto-allocate entity channel of regular entities
    snd_entchannel1volume is "1" ["1"] volume multiplier of the 1st entity channel of regular entities
    snd_entchannel2volume is "1" ["1"] volume multiplier of the 2nd entity channel of regular entities
    snd_entchannel3volume is "1" ["1"] volume multiplier of the 3rd entity channel of regular entities
    snd_entchannel4volume is "1" ["1"] volume multiplier of the 4th entity channel of regular entities
    snd_entchannel5volume is "1" ["1"] volume multiplier of the 5th entity channel of regular entities
    snd_entchannel6volume is "1" ["1"] volume multiplier of the 6th entity channel of regular entities
    snd_entchannel7volume is "1" ["1"] volume multiplier of the 7th entity channel of regular entities
    snd_initialized is "1" ["1"] indicates the sound subsystem is active
    snd_mutewhenidle is "1" ["1"] whether to disable sound output when game window is inactive
    snd_noextraupdate is "0" ["0"] disables extra sound mixer calls that are meant to reduce the chance of sound breakup at very low framerates
    snd_playerchannel0volume is "1" ["1"] volume multiplier of the auto-allocate entity channel of player entities
    snd_playerchannel1volume is "1" ["1"] volume multiplier of the 1st entity channel of player entities
    snd_playerchannel2volume is "1" ["1"] volume multiplier of the 2nd entity channel of player entities
    snd_playerchannel3volume is "1" ["1"] volume multiplier of the 3rd entity channel of player entities
    snd_playerchannel4volume is "1" ["1"] volume multiplier of the 4th entity channel of player entities
    snd_playerchannel5volume is "1" ["1"] volume multiplier of the 5th entity channel of player entities
    snd_playerchannel6volume is "1" ["1"] volume multiplier of the 6th entity channel of player entities
    snd_playerchannel7volume is "1" ["1"] volume multiplier of the 7th entity channel of player entities
    snd_precache is "1" ["1"] loads sounds before they are used
    snd_show is "0" ["0"] shows some statistics about sound mixing
    snd_soundradius is "2000" ["2000"] radius of weapon sounds and other standard sound effects (monster idle noises are half this radius and flickering light noises are one third of this radius)
    snd_spatialization_control is "0" ["0"] enable spatialization control (headphone friendly mode)
    snd_spatialization_max is "0.95" ["0.95"] maximum spatialization of sounds
    snd_spatialization_max_radius is "100" ["100"] use maximum spatialization below this radius
    snd_spatialization_min is "0.70" ["0.70"] minimum spatializazion of sounds
    snd_spatialization_min_radius is "10000" ["10000"] use minimum spatialization above to this radius
    snd_spatialization_occlusion is "1" ["1"] enable occlusion testing on spatialized sounds, which simply quiets sounds that are blocked by the world
    snd_spatialization_power is "0" ["0"] exponent of the spatialization falloff curve (0: logarithmic)
    snd_speed is "48000" ["48000"] sound output frequency, in hertz
    snd_staticvolume is "1" ["1"] volume of ambient sound effects (such as swampy sounds at the start of e1m2)
    snd_streaming is "1" ["1"] enables keeping compressed ogg sound files compressed, decompressing them only as needed, otherwise they will be decompressed completely at load (may use a lot of memory)
    snd_swapstereo is "0" ["0"] swaps left/right speakers for old ISA soundblaster cards
    snd_wav_partitionsize is "1024" ["1024"] controls sound delay in samples, values too low will cause crackling, too high will cause delayed sounds
    snd_width is "2" ["2"] sound output precision, in bytes (1 and 2 supported)
    snd_worldchannel0volume is "1" ["1"] volume multiplier of the auto-allocate entity channel of the world entity
    snd_worldchannel1volume is "1" ["1"] volume multiplier of the 1st entity channel of the world entity
    snd_worldchannel2volume is "1" ["1"] volume multiplier of the 2nd entity channel of the world entity
    snd_worldchannel3volume is "1" ["1"] volume multiplier of the 3rd entity channel of the world entity
    snd_worldchannel4volume is "1" ["1"] volume multiplier of the 4th entity channel of the world entity
    snd_worldchannel5volume is "1" ["1"] volume multiplier of the 5th entity channel of the world entity
    snd_worldchannel6volume is "1" ["1"] volume multiplier of the 6th entity channel of the world entity
    snd_worldchannel7volume is "1" ["1"] volume multiplier of the 7th entity channel of the world entity
    sv_accelerate is "10" ["10"] rate at which a player accelerates to sv_maxspeed
    sv_adminnick is "" [""] nick name to use for admin messages instead of host name
    sv_aim is "2" ["2"] maximum cosine angle for quake's vertical autoaim, a value above 1 completely disables the autoaim, quake used 0.93
    sv_airaccel_qw is "1" ["1"] ratio of QW-style air control as opposed to simple acceleration; when < 0, the speed is clamped against the maximum allowed forward speed after the move
    sv_airaccel_sideways_friction is "" [""] anti-sideways movement stabilization (reduces speed gain when zigzagging); when < 0, only so much friction is applied that braking (by accelerating backwards) cannot be stronger
    sv_airaccelerate is "-1" ["-1"] rate at which a player accelerates to sv_maxairspeed while in the air, if less than 0 the sv_accelerate variable is used instead
    sv_aircontrol is "0" ["0"] CPMA-style air control
    sv_airstopaccelerate is "0" ["0"] when set, replacement for sv_airaccelerate when moving backwards
    sv_airstrafeaccelerate is "0" ["0"] when set, replacement for sv_airaccelerate when just strafing
    sv_allowdownloads is "1" ["1"] whether to allow clients to download files from the server (does not affect http downloads)
    sv_allowdownloads_archive is "0" ["0"] whether to allow downloads of archives (pak/pk3)
    sv_allowdownloads_config is "0" ["0"] whether to allow downloads of config files (cfg)
    sv_allowdownloads_dlcache is "0" ["0"] whether to allow downloads of dlcache files (dlcache/)
    sv_allowdownloads_inarchive is "0" ["0"] whether to allow downloads from archives (pak/pk3)
    sv_areagrid_mingridsize is "128" ["128"] minimum areagrid cell size, smaller values work better for lots of small objects, higher values for large objects
    sv_autodemo_perclient is "0" ["0"] set to 1 to enable autorecorded per-client demos (they'll start to record at the beginning of a match); set it to 2 to also record client->server packets (for debugging)
    sv_autodemo_perclient_nameformat is "sv_autodemos/%Y-%m-%d_%H-%M" ["sv_autodemos/%Y-%m-%d_%H-%M"] The format of the sv_autodemo_perclient filename, followed by the map name, the client number and the IP address + port number, separated by underscores (the date is encoded using strftime escapes)
    sv_cheats is "0" ["0"] enables cheat commands in any game, and cheat impulses in dpmod
    sv_checkforpacketsduringsleep is "0" ["0"] uses select() function to wait between frames which can be interrupted by packets being received, instead of Sleep()/usleep()/SDL_Sleep() functions which do not check for packets
    sv_clmovement_enable is "1" ["1"] whether to allow clients to use cl_movement prediction, which can cause choppy movement on the server which may annoy other players
    sv_clmovement_inputtimeout is "0.2" ["0.2"] when a client does not send input for this many seconds, force them to move anyway (unlike QuakeWorld)
    sv_clmovement_minping is "0" ["0"] if client ping is below this time in milliseconds, then their ability to use cl_movement prediction is disabled for a while (as they don't need it)
    sv_clmovement_minping_disabletime is "1000" ["1000"] when client falls below minping, disable their prediction for this many milliseconds (should be at least 1000 or else their prediction may turn on/off frequently)
    sv_cullentities_nevercullbmodels is "0" ["0"] if enabled the clients are always notified of moving doors and lifts and other submodels of world (warning: eats a lot of network bandwidth on some levels!)
    sv_cullentities_pvs is "1" ["1"] fast but loose culling of hidden entities
    sv_cullentities_stats is "0" ["0"] displays stats on network entities culled by various methods for each client
    sv_cullentities_trace is "0" ["0"] somewhat slow but very tight culling of hidden entities, minimizes network traffic and makes wallhack cheats useless
    sv_cullentities_trace_delay is "1" ["1"] number of seconds until the entity gets actually culled
    sv_cullentities_trace_delay_players is "0.2" ["0.2"] number of seconds until the entity gets actually culled if it is a player entity
    sv_cullentities_trace_enlarge is "0" ["0"] box enlargement for entity culling
    sv_cullentities_trace_entityocclusion is "0" ["0"] also check if doors and other bsp models are in the way
    sv_cullentities_trace_prediction is "1" ["1"] also trace from the predicted player position
    sv_cullentities_trace_prediction_time is "0.2" ["0.2"] how many seconds of prediction to use
    sv_cullentities_trace_samples is "2" ["2"] number of samples to test for entity culling
    sv_cullentities_trace_samples_extra is "2" ["2"] number of samples to test for entity culling when the entity affects its surroundings by e.g. dlight
    sv_cullentities_trace_samples_players is "8" ["8"] number of samples to test for entity culling when the entity is a player entity
    sv_curl_defaulturl is "" [""] default autodownload source URL
    sv_curl_maxspeed is "0" ["0"] maximum download speed for clients downloading from sv_curl_defaulturl (KiB/s)
    sv_curl_serverpackages is "" [""] list of required files for the clients, separated by spaces
    sv_debugmove is "0" ["0"] disables collision detection optimizations for debugging purposes
    sv_echobprint is "1" ["1"] prints gamecode bprint() calls to server console
    sv_entpatch is "1" ["1"] enables loading of .ent files to override entities in the bsp (for example Threewave CTF server pack contains .ent patch files enabling play of CTF on id1 maps)
    sv_fixedframeratesingleplayer is "1" ["1"] allows you to use server-style timing system in singleplayer (don't run faster than sys_ticrate)
    sv_freezenonclients is "0" ["0"] freezes time, except for players, allowing you to walk around and take screenshots of explosions
    sv_friction is "4" ["4"] how fast you slow down
    sv_gameplayfix_blowupfallenzombies is "1" ["1"] causes findradius to detect SOLID_NOT entities such as zombies and corpses on the floor, allowing splash damage to apply to them
    sv_gameplayfix_consistentplayerprethink is "1" ["1"] improves fairness in multiplayer by running all PlayerPreThink functions (which fire weapons) before performing physics, then runing all PlayerPostThink functions
    sv_gameplayfix_delayprojectiles is "1" ["1"] causes entities to not move on the same frame they are spawned, meaning that projectiles wait until the next frame to perform their first move, giving proper interpolation and rocket trails, but making weapons harder to use at low framerates
    sv_gameplayfix_downtracesupportsongroundflag is "1" ["1"] prevents very short moves from clearing onground (which may make the player stick to the floor at high netfps)
    sv_gameplayfix_droptofloorstartsolid is "1" ["1"] prevents items and monsters that start in a solid area from falling out of the level (makes droptofloor treat trace_startsolid as an acceptable outcome)
    sv_gameplayfix_droptofloorstartsolid_nudgetocorrect is "1" ["1"] tries to nudge stuck items and monsters out of walls before droptofloor is performed
    sv_gameplayfix_easierwaterjump is "1" ["1"] changes water jumping to make it easier to get out of water (exactly like in QuakeWorld)
    sv_gameplayfix_findradiusdistancetobox is "1" ["1"] causes findradius to check the distance to the corner of a box rather than the center of the box, makes findradius detect bmodels such as very large doors that would otherwise be unaffected by splash damage
    sv_gameplayfix_gravityunaffectedbyticrate is "0" ["0"] fix some ticrate issues in physics.
    sv_gameplayfix_grenadebouncedownslopes is "1" ["1"] prevents MOVETYPE_BOUNCE (grenades) from getting stuck when fired down a downward sloping surface
    sv_gameplayfix_multiplethinksperframe is "1" ["1"] allows entities to think more often than the server framerate, primarily useful for very high fire rate weapons
    sv_gameplayfix_noairborncorpse is "1" ["1"] causes entities (corpses, items, etc) sitting ontop of moving entities (players) to fall when the moving entity (player) is no longer supporting them
    sv_gameplayfix_noairborncorpse_allowsuspendeditems is "1" ["1"] causes entities sitting ontop of objects that are instantaneously remove to float in midair (special hack to allow a common level design trick for floating items)
    sv_gameplayfix_nudgeoutofsolid is "1" ["1"] attempts to fix physics errors (where an object ended up in solid for some reason)
    sv_gameplayfix_nudgeoutofsolid_bias is "0" ["0"] over-correction on nudgeoutofsolid logic, to prevent constant contact
    sv_gameplayfix_q2airaccelerate is "0" ["0"] Quake2-style air acceleration
    sv_gameplayfix_setmodelrealbox is "1" ["1"] fixes a bug in Quake that made setmodel always set the entity box to ('-16 -16 -16', '16 16 16') rather than properly checking the model box, breaks some poorly coded mods
    sv_gameplayfix_slidemoveprojectiles is "1" ["1"] allows MOVETYPE_FLY/FLYMISSILE/TOSS/BOUNCE/BOUNCEMISSILE entities to finish their move in a frame even if they hit something, fixes 'gravity accumulation' bug for grenades on steep slopes
    sv_gameplayfix_stepdown is "0" ["0"] attempts to step down stairs, not just up them (prevents the familiar thud..thud..thud.. when running down stairs and slopes)
    sv_gameplayfix_stepmultipletimes is "1" ["1"] applies step-up onto a ledge more than once in a single frame, when running quickly up stairs
    sv_gameplayfix_stepwhilejumping is "1" ["1"] applies step-up onto a ledge even while airborn, useful if you would otherwise just-miss the floor when running across small areas with gaps (for instance running across the moving platforms in dm2, or jumping to the megahealth and red armor in dm2 rather than using the bridge)
    sv_gameplayfix_swiminbmodels is "1" ["1"] causes pointcontents (used to determine if you are in a liquid) to check bmodel entities as well as the world model, so you can swim around in (possibly moving) water bmodel entities
    sv_gameplayfix_upwardvelocityclearsongroundflag is "1" ["1"] prevents monsters, items, and most other objects from being stuck to the floor when pushed around by damage, and other situations in mods
    sv_gravity is "800" ["800"] how fast you fall (512 = roughly earth gravity)
    sv_heartbeatperiod is "120" ["120"] how often to send heartbeat in seconds (only used if sv_public is 1)
    sv_idealpitchscale is "0.8" ["0.8"] how much to look up/down slopes and stairs when not using freelook
    sv_jumpstep is "0" ["0"] whether you can step up while jumping (sv_gameplayfix_stepwhilejumping must also be 1)
    sv_jumpvelocity is "270" ["270"] cvar that can be used by QuakeC code for jump velocity
    sv_master1 is "" [""] user-chosen master server 1
    sv_master2 is "" [""] user-chosen master server 2
    sv_master3 is "" [""] user-chosen master server 3
    sv_master4 is "" [""] user-chosen master server 4
    sv_masterextra1 is "69.59.212.88" ["69.59.212.88"] ghdigital.com - default master server 1 (admin: LordHavoc)
    sv_masterextra2 is "64.22.107.125" ["64.22.107.125"] dpmaster.deathmask.net - default master server 2 (admin: Willis)
    sv_masterextra3 is "92.62.40.73" ["92.62.40.73"] dpmaster.tchr.no - default master server 3 (admin: tChr)
    sv_maxairspeed is "30" ["30"] maximum speed a player can accelerate to when airborn (note that it is possible to completely stop by moving the opposite direction)
    sv_maxairstrafespeed is "0" ["0"] when set, replacement for sv_maxairspeed when just strafing
    sv_maxrate is "1000000" ["1000000"] upper limit on client rate cvar, should reflect your network connection quality
    sv_maxspeed is "320" ["320"] maximum speed a player can accelerate to when on ground (can be exceeded by tricks)
    sv_maxvelocity is "2000" ["2000"] universal speed limit on all entities
    sv_nostep is "0" ["0"] prevents MOVETYPE_STEP entities (monsters) from moving
    sv_onlycsqcnetworking is "0" ["0"] disables legacy entity networking code for higher performance (except on clients, which can still be legacy)
    sv_playerphysicsqc is "1" ["1"] enables QuakeC function to override player physics
    sv_progs is "progs.dat" ["progs.dat"] selects which quakec progs.dat file to run
    sv_protocolname is "DP7" ["DP7"] selects network protocol to host for (values include QUAKE, QUAKEDP, NEHAHRAMOVIE, DP1 and up)
    sv_public is "0" ["0"] 1: advertises this server on the master server (so that players can find it in the server browser); 0: allow direct queries only; -1: do not respond to direct queries; -2: do not allow anyone to connect
    sv_random_seed is "" [""] random seed; when set, on every map start this random seed is used to initialize the random number generator. Don't touch it unless for benchmarking or debugging
    sv_ratelimitlocalplayer is "0" ["0"] whether to apply rate limiting to the local player in a listen server (only useful for testing)
    sv_sound_land is "demon/dland2.wav" ["demon/dland2.wav"] sound to play when MOVETYPE_STEP entity hits the ground at high speed (empty cvar disables the sound)
    sv_sound_watersplash is "misc/h2ohit1.wav" ["misc/h2ohit1.wav"] sound to play when MOVETYPE_FLY/TOSS/BOUNCE/STEP entity enters or leaves water (empty cvar disables the sound)
    sv_status_privacy is "0" ["0"] do not show IP addresses in 'status' replies to clients
    sv_status_show_qcstatus is "0" ["0"] show the 'qcstatus' field in status replies, not the 'frags' field. Turn this on if your mod uses this field, and the 'frags' field on the other hand has no meaningful value.
    sv_stepheight is "18" ["18"] how high you can step up (TW_SV_STEPCONTROL extension)
    sv_stopspeed is "100" ["100"] how fast you come to a complete stop
    sv_wallfriction is "1" ["1"] how much you slow down when sliding along a wall
    sv_warsowbunny_accel is "0.1585" ["0.1585"] how fast you accelerate until after reaching sv_maxspeed (it gets harder as you near sv_warsowbunny_topspeed)
    sv_warsowbunny_airforwardaccel is "1.00001" ["1.00001"] how fast you accelerate until you reach sv_maxspeed
    sv_warsowbunny_backtosideratio is "0.8" ["0.8"] lower values make it easier to change direction without losing speed; the drawback is "understeering" in sharp turns
    sv_warsowbunny_topspeed is "925" ["925"] soft speed limit (can get faster with rjs and on ramps)
    sv_warsowbunny_turnaccel is "0" ["0"] max sharpness of turns (also master switch for the sv_warsowbunny_* mode; set this to 9 to enable)
    sv_wateraccelerate is "-1" ["-1"] rate at which a player accelerates to sv_maxspeed while in the air, if less than 0 the sv_accelerate variable is used instead
    sv_waterfriction is "-1" ["-1"] how fast you slow down, if less than 0 the sv_friction variable is used instead
    sv_writepicture_quality is "10" ["10"] WritePicture quality offset (higher means better quality, but slower)
    sys_colortranslation is "0" ["0"] terminal console color translation (supported values: 0 = strip color codes, 1 = translate to ANSI codes, 2 = no translation)
    sys_debugsleep is "0" ["0"] write requested and attained sleep times to standard output, to be used with gnuplot
    sys_specialcharactertranslation is "1" ["1"] terminal console conchars to ASCII translation (set to 0 if your conchars.tga is for an 8bit character set or if you want raw output)
    sys_ticrate is "0.0138889" ["0.0138889"] how long a server frame is in seconds, 0.05 is 20fps server rate, 0.1 is 10fps (can not be set higher than 0.1), 0 runs as many server frames as possible (makes games against bots a little smoother, overwhelms network players), 0.0138889 matches QuakeWorld physics
    sys_usenoclockbutbenchmark is "0" ["0"] don't use ANY real timing, and simulate a clock (for benchmarking); the game then runs as fast as possible. Run a QC mod with bots that does some stuff, then does a quit at the end, to benchmark a server. NEVER do this on a public server.
    sys_usequeryperformancecounter is "0" ["0"] use windows QueryPerformanceCounter timer (which has issues on multicore/multiprocessor machines and processors which are designed to conserve power) for timing rather than timeGetTime function (which has issues on some motherboards)
    team is "none" ["none"] QW team (4 character limit, example: blue)
    teamplay is "0" ["0"] teamplay mode, values depend on mod but typically 0 = no teams, 1 = no team damage no self damage, 2 = team damage and self damage, some mods support 3 = no team damage but can damage self
    temp1 is "0" ["0"] general cvar for mods to use, in stock id1 this selects which death animation to use on players (0 = random death, other values select specific death scenes)
    timedemo_screenshotframelist is "" [""] when performing a timedemo, take screenshots of each frame in this space-separated list - example: 1 201 401
    timeformat is "[%Y-%m-%d %H:%M:%S] " ["[%Y-%m-%d %H:%M:%S] "] time format to use on timestamped console messages
    timelimit is "0" ["0"] ends level at this time (in minutes)
    timestamps is "0" ["0"] prints timestamps on console messages
    utf8_enable is "0" ["0"] Enable UTF-8 support. For compatibility, this is disabled by default in most games.
    v_brightness is "0" ["0"] brightness of black, useful for monitors that are too dark
    v_centermove is "0.15" ["0.15"] how long before the view begins to center itself (if freelook/+mlook/+jlook/+klook are off)
    v_centerspeed is "500" ["500"] how fast the view centers itself
    v_color_black_b is "0" ["0"] desired color of black
    v_color_black_g is "0" ["0"] desired color of black
    v_color_black_r is "0" ["0"] desired color of black
    v_color_enable is "0" ["0"] enables black-grey-white color correction curve controls
    v_color_grey_b is "0.5" ["0.5"] desired color of grey
    v_color_grey_g is "0.5" ["0.5"] desired color of grey
    v_color_grey_r is "0.5" ["0.5"] desired color of grey
    v_color_white_b is "1" ["1"] desired color of white
    v_color_white_g is "1" ["1"] desired color of white
    v_color_white_r is "1" ["1"] desired color of white
    v_contrast is "1" ["1"] brightness of white (values above 1 give a brighter image with increased color saturation, unlike v_gamma)
    v_contrastboost is "1" ["1"] by how much to multiply the contrast in dark areas (1 is no change)
    v_deathtilt is "1" ["1"] whether to use sideways view when dead
    v_deathtiltangle is "80" ["80"] what roll angle to use when tilting the view while dead
    v_flipped is "0" ["0"] mirror the screen (poor man's left handed mode)
    v_gamma is "1.500000" ["1"] inverse gamma correction value, a brightness effect that does not affect white or black, and tends to make the image grey and dull
    v_glslgamma is "0" ["0"] enables use of GLSL to apply gamma correction ramps if available (note: overrides v_hwgamma)
    v_hwgamma is "1" ["1"] enables use of hardware gamma correction ramps if available (note: does not work very well on Windows2000 and above), values are 0 = off, 1 = attempt to use hardware gamma, 2 = use hardware gamma whether it works or not
    v_idlescale is "0" ["0"] how much of the quake 'drunken view' effect to use
    v_ipitch_cycle is "1" ["1"] v_idlescale pitch speed
    v_ipitch_level is "0.3" ["0.3"] v_idlescale pitch amount
    v_iroll_cycle is "0.5" ["0.5"] v_idlescale roll speed
    v_iroll_level is "0.1" ["0.1"] v_idlescale roll amount
    v_iyaw_cycle is "2" ["2"] v_idlescale yaw speed
    v_iyaw_level is "0.3" ["0.3"] v_idlescale yaw amount
    v_kickpitch is "0.6" ["0.6"] how much a view kick from damage pitches your view
    v_kickroll is "0.6" ["0.6"] how much a view kick from damage rolls your view
    v_kicktime is "0.5" ["0.5"] how long a view kick from damage lasts
    v_psycho is "0" ["0"] easter egg (does not work on Windows2000 or above)
    vid_bitsperpixel is "32" ["32"] how many bits per pixel to render at (32 or 16, 32 is recommended)
    vid_conheight is "480" ["480"] virtual height of 2D graphics system
    vid_conwidth is "640" ["640"] virtual width of 2D graphics system
    vid_forcerefreshrate is "0" ["0"] try to set the given vid_refreshrate even if Windows doesn't list it as valid video mode
    vid_fullscreen is "0" ["1"] use fullscreen (1) or windowed (0)
    vid_gl13 is "1" ["1"] enables faster rendering using OpenGL 1.3 features (such as GL_ARB_texture_env_combine extension)
    vid_gl20 is "1" ["1"] enables faster rendering using OpenGL 2.0 features (such as GL_ARB_fragment_shader extension)
    vid_grabkeyboard is "0" ["0"] whether to grab the keyboard when mouse is active (prevents use of volume control keys, music player keys, etc on some keyboards)
    vid_hardwaregammasupported is "0" ["1"] indicates whether hardware gamma is supported (updated by attempts to set hardware gamma ramps)
    vid_height is "768" ["480"] resolution
    vid_minheight is "0" ["0"] minimum vid_height that is acceptable (to be set in default.cfg in mods)
    vid_minwidth is "0" ["0"] minimum vid_width that is acceptable (to be set in default.cfg in mods)
    vid_mouse is "1" ["1"] whether to use the mouse in windowed mode (fullscreen always does)
    vid_pixelheight is "1" ["1"] adjusts vertical field of vision to account for non-square pixels (1280x1024 on a CRT monitor for example)
    vid_refreshrate is "60" ["60"] refresh rate to use, in hz (higher values flicker less, if supported by your monitor)
    vid_resizable is "0" ["0"] 0: window not resizable, 1: resizable, 2: window can be resized but the framebuffer isn't adjusted
    vid_samples is "1" ["1"] how many anti-aliasing samples per pixel to request from the graphics driver (4 is recommended, 1 is faster)
    vid_stereobuffer is "0" ["0"] enables 'quad-buffered' stereo rendering for stereo shutterglasses, HMD (head mounted display) devices, or polarized stereo LCDs, if supported by your drivers
    vid_stick_mouse is "0" ["0"] have the mouse stuck in the center of the screen
    vid_userefreshrate is "0" ["0"] set this to 1 to make vid_refreshrate used, or to 0 to let the engine choose a sane default
    vid_vsync is "0" ["0"] sync to vertical blank, prevents 'tearing' (seeing part of one frame and part of another on the screen at the same time), automatically disabled when doing timedemo benchmarks
    vid_width is "1024" ["640"] resolution
    viewsize is "120" ["100"] how large the view should be, 110 disables inventory bar, 120 disables status bar
    volume is "0.7" ["0.7"] volume of sound effects

