Impulse map
===========

Information taken from
-   server/cl\_impulse.qc
-   server/cheats.qc
-   OUNS wiki cached by [Google](http://webcache.googleusercontent.com/search?q=cache:V24C1sh8RQMJ:ouns.nexuizninjaz.com/tech:impulse+nexuiz+impulse+list&cd=1&hl=en&ct=clnk&gl=uk&client=opera&source=www.google.co.uk)

Note
-   Impulse 30 appears to be used twice

***

    Number: Effect [alias]
    0: Reserved (no input)
    1: Weapon group 1 (Laser and @!#'n Tuba) [1]
    2: Weapon group 2 (Shotgun) [2]
    3: Weapon group 3 (Machine Gun) [3]
    4: Weapon group 4 (Mortar and Mine Layer) [4]
    5: Weapon group 5 (Electro) [5]
    6: Weapon group 6 (HLAC and Crylink) [6]
    7: Weapon group 7 (Nex, MinstaNex and Rifle) [7]
    8: Weapon group 8 (Hagar and T.A.G. Seeker) [8]
    9: Weapon group 9 (Rocket Launcher and Fireball) [9]
    10: Next weapon according to linear list (1, 2, 3, 4 etc) [_weapnext_2]
    11: Most recently used weapon (last selected weapon) [weaplast]
    12: Previous weapon according to linear list (23, 22, 21, 20 etc) [_weapprev_2]
    13: Best weapon according to priority list [weapbest]
    14: Weapon group 0 (Port-O-Launch and Hook) [0]
    15: Next weapon according to priority list [_weapnext_1]
    16: Previous weapon according to priority list [_weapprev_1]
    17: Throw weapon [dropweapon]
    18: Next weapon according to sbar_hudselector 1 list [_weapnext_0]
    19: Previous weapon according to sbar_hudselector 1 list [_weapprev_0]
    20: Reload if possible [reload]
    30: CHIMPULSE_SPEEDRUN_INIT (found in cheats.qc)
    30: Personal waypoint at your location [g_waypointsprite_personal]
    31: Personal waypoint at crosshair location [g_waypointsprite_personal_p]
    32: Personal waypoint at last death location [g_waypointsprite_personal_d]
    33: 'Help Me' above you [g_waypointsprite_team_helpme]
    34: 'Here' at your location [g_waypointsprite_team_here]
    35: 'Here' at crosshair [g_waypointsprite_team_here_p]
    36: 'Here' at last death location [g_waypointsprite_team_here_d]
    37: 'Danger' at your location [g_waypointsprite_team_danger]
    38: 'Danger' at crosshair [g_waypointsprite_team_danger_p]
    39: 'Danger' at last death location [g_waypointsprite_team_danger_d]
    47: Clear personal waypoints [g_waypointsprite_clear_personal]
    48: Clear all waypoints [g_waypointsprite_clear]

    99: Grants all weapons, 999 ammo, health, and armor (needs sv_cheats 1)
    100: Tetris (needs Tetris to compiled in)
    103: spawn a bot waypoint [g_waypointeditor_spawn]
    104: remove a bot waypoint [g_waypointeditor_remove]
    105: relink objects and spawned bot waypoints [g_waypointeditor_relinkall]
    106: save spawned bot waypoints to .xonotic/data/data/maps.mapname.waypoints [g_waypointeditor_saveall]
    107: show any bot waypoints that cannot be reached (blue) and walked (red) to, and any player spawn points without any near bot waypoint [g_waypointeditor_unreachable]
    140: Moving clone (needs sv_cheats 1)
    141: CTF speedrun, teleports you to the location you last set a g_waypointsprite_personal, resets the flag, health, ammo, gives you all weapons on the map (needs sv_cheats 1)
    142: Static clone (needs sv_cheats 1)
    143: Emergency teleport (needs sv_cheats 1)
    148: Trigger explosion (needs sv_cheats 1)
    200: prev cl_weaponpriority0 "explosives weapons"
    210: best cl_weaponpriority0 "explosives weapons"
    220: next cl_weaponpriority0 "explosives weapons"
    201: prev cl_weaponpriority1 "energy weapons"
    211: best cl_weaponpriority1 "energy weapons"
    221: next cl_weaponpriority1 "energy weapons"
    202: prev cl_weaponpriority2 "hitscan exact weapons"
    212: best cl_weaponpriority2 "hitscan exact weapons"
    222: next cl_weaponpriority2 "hitscan exact weapons"
    203: prev cl_weaponpriority3 "hitscan all weapons"
    213: best cl_weaponpriority3 "hitscan all weapons"
    223: next cl_weaponpriority3 "hitscan all weapons"
    204: prev cl_weaponpriority4 "spam weapons"
    214: best cl_weaponpriority4 "spam weapons"
    224: next cl_weaponpriority4 "spam weapons"
    205: prev cl_weaponpriority5 "weapons for moving"
    215: best cl_weaponpriority5 "weapons for moving"
    225: next cl_weaponpriority5 "weapons for moving"
    206: prev cl_weaponpriority6
    216: best cl_weaponpriority6
    226: next cl_weaponpriority6
    207: prev cl_weaponpriority7
    217: best cl_weaponpriority7
    227: next cl_weaponpriority7
    208: prev cl_weaponpriority8
    218: best cl_weaponpriority8
    228: next cl_weaponpriority8
    209: prev cl_weaponpriority9
    219: best cl_weaponpriority9
    229: next cl_weaponpriority9
    230: Laser
    231: Shotgun
    232: Machine Gun
    233: Mortar
    234: Mine Layer
    235: Electro
    236: Crylink
    237: Nex
    238: Hagar
    239: Rocket Launcher
    240: Port-O-Launch
    241: Minsta Nex
    242: Grappling Hook
    243: Heavy Laser Assault Cannon
    244: @!#'n Tuba
    245: Rifle
    246: Fireball
    247: T.A.G. Seeker
    248: Reserved for a future weapon
    249: Reserved for a future weapon
    250: Reserved for a future weapon
    251: Reserved for a future weapon
    252: Reserved for a future weapon
    253: Reserved for a future weapon

