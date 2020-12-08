**Note:** The article is written as developer notes to ease developer tasks and save QuakeC function terms here. Some references are taken from `events.qh`.


# MUTATOR functions (from: `qcsrc/server/mutators/events.qh`)

### Introduction

How to use MUTATOR functions:

**Attention:** to use a hook, first register your mutator using `REGISTER_MUTATOR`, then create your function using `MUTATOR_HOOKFUNCTION`.


- **`REGISTER_MUTATOR`**

Registers a new `MUTATOR_HOOKFUNCTION`.
```c
REGISTER_MUTATOR(new_mutator_name, some_variable);
```


- **`MUTATOR_HOOKFUNCTION`**

Creates a function and calls `new_mutator_name` (from `REGISTER_MUTATOR`) and one of `#define MUTATOR()` (from `qcsrc/server/mutators/events.qh` main hooks).

Example:
```c
MUTATOR_HOOKFUNCTION(new_mutator_name_or_events.qh_main_hook, PlayerSpawn)
{
    // whatever does
}
```

- **`MUTATOR_CALLHOOK`**

Calls some `MUTATOR_HOOKFUNCTION`.
```c
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hook);
```

There are different versions and depends how many variables need to be called in a `MUTATOR_HOOKFUNCTION`:

1 `MUTATOR_HOOKFUNCTION` and 1 variable:

```c
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hook, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and 2 variables:

```c
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hook, some_variable, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and 3 variables:

```c
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hook, some_variable, some_variable, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and multiple variables:

```c
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hook, some_variable, some_variable, some_variable, some_variable, ...);
```

<br />
<br />


## List of MUTATOR functions

**Warning:** 

- **`MakePlayerObserver`**

Called when a player becomes observer, after shared setup.
```c
#define EV_MakePlayerObserver(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(MakePlayerObserver, EV_MakePlayerObserver)
```

- **`PutClientInServer`**

Called when client spawns in server. (Not sure described)
```c
#define EV_PutClientInServer(i, o) \
	/** client wanting to spawn */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(PutClientInServer, EV_PutClientInServer);
```

- **`ForbidSpawn`**

Returns true to prevent a spectator/observer to spawn as player.
```c
 #define EV_ForbidSpawn(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(ForbidSpawn, EV_ForbidSpawn);
```

- **`AutoJoinOnConnection`**

Returns true if client should be put as player on connection.
```c
#define EV_AutoJoinOnConnection(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(AutoJoinOnConnection, EV_AutoJoinOnConnection);
```

- **`ForbidRandomStartWeapons`**

Called when player spawns to determine whether to give them random start weapons. Return true to forbid giving them.
```c
#define EV_ForbidRandomStartWeapons(i, o) \
	/** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(ForbidRandomStartWeapons, EV_ForbidRandomStartWeapons);
```

- **`PlayerSpawn`**

Called when a player spawns as player, after shared setup, before his weapon is chosen (so items may be changed in here)

```c
#define EV_PlayerSpawn(i, o) \
    /** player spawning */ i(entity, MUTATOR_ARGV_0_entity) \
    /** spot that was used, or NULL */ i(entity, MUTATOR_ARGV_1_entity) \
    /**/
MUTATOR_HOOKABLE(PlayerSpawn, EV_PlayerSpawn);
```

- **`PlayerWeaponSelect`**

Called after a player's weapon is chosen so it can be overriden here.
```c
#define EV_PlayerWeaponSelect(i, o) \
	/** player spawning */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(PlayerWeaponSelect, EV_PlayerWeaponSelect);
```

- **`reset_map_global`**

Called in reset_map.
```c
#define EV_reset_map_global(i, o) \
    /**/
MUTATOR_HOOKABLE(reset_map_global, EV_reset_map_global);
```

- **`reset_map_players`**

Called in reset_map.
```c
#define EV_reset_map_players(i, o) \
    /**/
MUTATOR_HOOKABLE(reset_map_players, EV_reset_map_players);
```

- **`ForbidPlayerScore_Clear`**

Returns 1 if clearing player score shall not be allowed.
```c
#define EV_ForbidPlayerScore_Clear(i, o) \
    /**/
MUTATOR_HOOKABLE(ForbidPlayerScore_Clear, EV_ForbidPlayerScore_Clear);
```

- **`ClientDisconnect`**

Called when a player disconnects.
```c
#define EV_ClientDisconnect(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(ClientDisconnect, EV_ClientDisconnect);
```

- **`PlayerDies`**

Called when a player dies to e.g. remove stuff he was carrying.
```c
#define EV_PlayerDies(i, o) \
	/** inflictor  		*/ i(entity, MUTATOR_ARGV_0_entity) \
    /** attacker    	*/ i(entity, MUTATOR_ARGV_1_entity) \
    /** target    		*/ i(entity, MUTATOR_ARGV_2_entity) \
    /** deathtype     	*/ i(float,  MUTATOR_ARGV_3_float) \
    /** damage         */ i(float,  MUTATOR_ARGV_4_float) \
    /** damage  		*/ o(float,  MUTATOR_ARGV_4_float) \
    /**/
MUTATOR_HOOKABLE(PlayerDies, EV_PlayerDies);
```

- **`PlayerDied`**

Called after a player died.
```c
#define EV_PlayerDied(i, o) \
    /** player    		*/ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(PlayerDied, EV_PlayerDied);
```

- **`ClientObituary`**

Called when showing an obituary for the player. Returns true to show nothing (workarounds may be needed).
```c
#define EV_ClientObituary(i, o) \
    /** inflictor       */ i(entity, MUTATOR_ARGV_0_entity) \
    /** attacker        */ i(entity, MUTATOR_ARGV_1_entity) \
    /** target          */ i(entity, MUTATOR_ARGV_2_entity) \
    /** deathtype       */ i(float,  MUTATOR_ARGV_3_float) \
    /** wep entity      */ i(entity, MUTATOR_ARGV_4_entity) \
    /** anonymous killer*/ o(bool,   MUTATOR_ARGV_5_bool) \
    /**/
MUTATOR_HOOKABLE(ClientObituary, EV_ClientObituary);
```

- **`FragCenterMessage`**

Allows overriding the frag centerprint messages.
```c
#define EV_FragCenterMessage(i, o) \
    /** attacker       */ i(entity, MUTATOR_ARGV_0_entity) \
    /** target         */ i(entity, MUTATOR_ARGV_1_entity) \
    /** deathtype      */ i(float, MUTATOR_ARGV_2_float) \
    /** attacker kcount*/ i(int,  MUTATOR_ARGV_3_int) \
    /** targ killcount */ i(int,  MUTATOR_ARGV_4_int) \
    /**/
MUTATOR_HOOKABLE(FragCenterMessage, EV_FragCenterMessage);
```

- **`PlayHitsound`**

Called when a player dies to e.g. remove stuff he was carrying.
```c
#define EV_PlayHitsound(i, o) \
    /** victim */ i(entity, MUTATOR_ARGV_0_entity) \
    /** attacker */ i(entity, MUTATOR_ARGV_1_entity) \
    /**/
MUTATOR_HOOKABLE(PlayHitsound, EV_PlayHitsound);
```

- **`ItemModel`**

Called when an item model is about to be set, allows custom paths etc.
```c
#define EV_ItemModel(i, o) \
    /** model       */ i(string, MUTATOR_ARGV_0_string) \
    /** output      */ i(string, MUTATOR_ARGV_1_string) \
    /**/               o(string, MUTATOR_ARGV_1_string) \
    /**/
MUTATOR_HOOKABLE(ItemModel, EV_ItemModel);
```

- **`ItemSound`**

Called when an item sound is about to be played, allows custom paths etc.
```c
#define EV_ItemSound(i, o) \
    /** sound       */ i(string, MUTATOR_ARGV_0_string) \
    /** output      */ i(string, MUTATOR_ARGV_1_string) \
    /**/               o(string, MUTATOR_ARGV_1_string) \
    /**/
MUTATOR_HOOKABLE(ItemSound, EV_ItemSound);
```

- **`GiveFragsForKill`**

Called when someone was fragged by "self", and is expected to change frag_score to adjust scoring for the kill.
```c
#define EV_GiveFragsForKill(i, o) \
    /** attacker   */ i(entity, MUTATOR_ARGV_0_entity) \
    /** target     */ i(entity, MUTATOR_ARGV_1_entity) \
    /** frag score */ i(float, MUTATOR_ARGV_2_float) \
    /**            */ o(float, MUTATOR_ARGV_2_float) \
    /** deathtype  */ i(float, MUTATOR_ARGV_3_float) \
    /** wep entity */ i(entity, MUTATOR_ARGV_4_entity) \
    /**/
MUTATOR_HOOKABLE(GiveFragsForKill, EV_GiveFragsForKill);
```

- **`MatchEnd`**

Called when the match ends.
```c
MUTATOR_HOOKABLE(MatchEnd, EV_NO_ARGS);
```

- **`TeamBalance_CheckAllowedTeams`**

Allows adjusting allowed teams. Return true to use the bitmask value and set non-empty string to use team entity name. Both behaviors can be active at the same time and will stack allowed teams.
```c
#define EV_TeamBalance_CheckAllowedTeams(i, o) \
    /** mask of teams      */ i(float, MUTATOR_ARGV_0_float) \
    /**/                      o(float, MUTATOR_ARGV_0_float) \
    /** team entity name   */ i(string, MUTATOR_ARGV_1_string) \
    /**/                      o(string, MUTATOR_ARGV_1_string) \
    /** player checked     */ i(entity, MUTATOR_ARGV_2_entity) \
    /**/
MUTATOR_HOOKABLE(TeamBalance_CheckAllowedTeams, EV_TeamBalance_CheckAllowedTeams);
```

- **`TeamBalance_GetTeamCounts`**

Returns true to manually override team counts.
```c
MUTATOR_HOOKABLE(TeamBalance_GetTeamCounts, EV_NO_ARGS);
```

- **`TeamBalance_GetTeamCount`**

Allows overriding of team counts.
```c
#define EV_TeamBalance_GetTeamCount(i, o) \
    /** team index to count             */ i(float, MUTATOR_ARGV_0_float) \
    /** player to ignore                */ i(entity, MUTATOR_ARGV_1_entity) \
    /** number of players in a team     */ o(float, MUTATOR_ARGV_2_float) \
    /** number of bots in a team        */ o(float, MUTATOR_ARGV_3_float) \
    /**/
MUTATOR_HOOKABLE(TeamBalance_GetTeamCount, EV_TeamBalance_GetTeamCount);
```

- **`TeamBalance_FindBestTeams`**

Allows overriding the teams that will make the game most balanced if the player joins any of them.
```c
#define EV_TeamBalance_FindBestTeams(i, o) \
    /** player checked   */ i(entity, MUTATOR_ARGV_0_entity) \
    /** bitmask of teams */ o(float, MUTATOR_ARGV_1_float) \
    /**/
MUTATOR_HOOKABLE(TeamBalance_FindBestTeams, EV_TeamBalance_FindBestTeams);
```

- **`TeamBalance_GetPlayerForTeamSwitch`**

Called during autobalance. Returns true to override the player that will be switched.
```c
#define EV_TeamBalance_GetPlayerForTeamSwitch(i, o) \
    /** source team index      */ i(int, MUTATOR_ARGV_0_int) \
    /** destination team index */ i(int, MUTATOR_ARGV_1_int) \
    /** is looking for bot     */ i(bool, MUTATOR_ARGV_2_bool) \
    /** player to switch       */ o(entity, MUTATOR_ARGV_3_entity) \
    /**/
MUTATOR_HOOKABLE(TeamBalance_GetPlayerForTeamSwitch, EV_TeamBalance_GetPlayerForTeamSwitch);
```

- **`SpectateCopy`**

Copies variables for spectating "spectatee" to "this".
```c
#define EV_SpectateCopy(i, o) \
    /** spectatee   */ i(entity, MUTATOR_ARGV_0_entity) \
    /** client      */ i(entity, MUTATOR_ARGV_1_entity) \
    /**/
MUTATOR_HOOKABLE(SpectateCopy, EV_SpectateCopy);
```

- **`FormatMessage`**

Called when formatting a chat message to replace fancy functions.
```c
#define EV_FormatMessage(i, o) \
    /** player        */ i(entity, MUTATOR_ARGV_0_entity) \
    /** escape        */ i(string, MUTATOR_ARGV_1_string) \
    /** replacement   */ i(string, MUTATOR_ARGV_2_string) \
    /**/                 o(string, MUTATOR_ARGV_2_string) \
    /** message       */ i(string, MUTATOR_ARGV_3_string) \
    /**/
MUTATOR_HOOKABLE(FormatMessage, EV_FormatMessage);
```

- **`PreFormatMessage`**

Called before any formatting is applied, handy for tweaking the message before scripts get ahold of it.
```c
#define EV_PreFormatMessage(i, o) \
    /** player        */ i(entity, MUTATOR_ARGV_0_entity) \
    /** message       */ i(string, MUTATOR_ARGV_1_string) \
    /**/                 o(string, MUTATOR_ARGV_1_string) \
    /**/
MUTATOR_HOOKABLE(PreFormatMessage, EV_PreFormatMessage);
```

- **`ForbidThrowCurrentWeapon`**

Returns true if throwing the current weapon shall not be allowed.
```c
#define EV_ForbidThrowCurrentWeapon(i, o) \
    /** player        */ i(entity, MUTATOR_ARGV_0_entity) \
    /** weapon entity */ i(entity, MUTATOR_ARGV_1_entity) \
    /**/
MUTATOR_HOOKABLE(ForbidThrowCurrentWeapon, EV_ForbidThrowCurrentWeapon);
```

- **`ForbidDropCurrentWeapon`**

Returns true if dropping the current weapon shall not be allowed at any time including death */
```c
#define EV_ForbidDropCurrentWeapon(i, o) \
    /** player */        i(entity, MUTATOR_ARGV_0_entity) \
    /** weapon id */     i(int, MUTATOR_ARGV_1_int) \
    /**/
MUTATOR_HOOKABLE(ForbidDropCurrentWeapon, EV_ForbidDropCurrentWeapon);
```

- **`SetDefaultAlpha`**

Sets alpha value by default. (Not sure described)
```c
MUTATOR_HOOKABLE(SetDefaultAlpha, EV_NO_ARGS);
```






<br />
<br />


- **`Damage_Calculate`**

Called to adjust damage and force values which are applied to the player, used for e.g. strength damage/force multiplier, I'm not sure if I should change this around slightly (Naming of the entities, and also how they're done in g_damage).

```c
#define EV_Damage_Calculate(i, o) \
    /** inflictor  		*/ i(entity, MUTATOR_ARGV_0_entity) \
    /** attacker    	*/ i(entity, MUTATOR_ARGV_1_entity) \
    /** target    		*/ i(entity, MUTATOR_ARGV_2_entity) \
    /** deathtype     	*/ i(float,  MUTATOR_ARGV_3_float) \
    /** damage          */ i(float,  MUTATOR_ARGV_4_float) \
    /** damage  		*/ o(float,  MUTATOR_ARGV_4_float) \
    /** mirrordamage    */ i(float,  MUTATOR_ARGV_5_float) \
    /** mirrordamage 	*/ o(float,  MUTATOR_ARGV_5_float) \
    /** force           */ i(vector, MUTATOR_ARGV_6_vector) \
    /** force           */ o(vector, MUTATOR_ARGV_6_vector) \
    /** weapon entity 	*/ i(entity, MUTATOR_ARGV_7_entity) \
    /**/
MUTATOR_HOOKABLE(Damage_Calculate, EV_Damage_Calculate);
```
<br />
<br />

AND.... STILL in process