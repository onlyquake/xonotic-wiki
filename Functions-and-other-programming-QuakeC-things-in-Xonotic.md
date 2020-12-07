# Functions and other programming QuakeC things in Xonotic

**Note:** The article is written as developer notes to ease developer tasks and save QuakeC function terms here. Some references are taken from `events.qh`.


# MUTATOR functions (from: `qcsrc/server/mutators/events.qh`)

### Introduction

How to use MUTATOR functions:

**Attention:** to use a hook, first register your mutator using `REGISTER_MUTATOR`, then create your function using `MUTATOR_HOOKFUNCTION`.


**`REGISTER_MUTATOR`**

Registers a new `MUTATOR_HOOKFUNCTION`.
```
REGISTER_MUTATOR(new_mutator_name, some_variable);
```


**`MUTATOR_HOOKFUNCTION`**

Creates a function and calls `new_mutator_name` (from `REGISTER_MUTATOR`) and one of `#define MUTATOR()` (from `qcsrc/server/mutators/events.qh` main hooks).

Example:

    MUTATOR_HOOKFUNCTION(helloworld, PlayerSpawn)
    {
    	// whatever does
    }


**`MUTATOR_CALLHOOK`**

Calls some `MUTATOR_HOOKFUNCTION`.
```
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hooks);
```

There are different versions and depends how many variables need to be called in a `MUTATOR_HOOKFUNCTION`:

1 `MUTATOR_HOOKFUNCTION` and 1 variable:

```
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hooks, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and 2 variables:

```
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hooks, some_variable, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and 3 variables:

```
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hooks, some_variable, some_variable, some_variable);
```

1 `MUTATOR_HOOKFUNCTION` and multiple variables:

```
MUTATOR_CALLHOOK(name_of_MUTATOR_HOOKFUNCTION_or_events.qh_main_hooks, some_variable, some_variable, some_variable, some_variable, ...);
```

<br />
<br />


## List of MUTATOR functions

**`MakePlayerObserver`**

Called when a player becomes observer, after shared setup.
```
#define EV_MakePlayerObserver(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(MakePlayerObserver, EV_MakePlayerObserver)
```

**`PutClientInServer`**

Called when client spawns in server. (Not sure described)
```
#define EV_PutClientInServer(i, o) \
	/** client wanting to spawn */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(PutClientInServer, EV_PutClientInServer);
```

**`ForbidSpawn`**

Returns true to prevent a spectator/observer to spawn as player.
```
 #define EV_ForbidSpawn(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(ForbidSpawn, EV_ForbidSpawn);
```

**`AutoJoinOnConnection`**

Returns true if client should be put as player on connection.
```
#define EV_AutoJoinOnConnection(i, o) \
    /** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(AutoJoinOnConnection, EV_AutoJoinOnConnection);
```

**`ForbidRandomStartWeapons`**

Called when player spawns to determine whether to give them random start weapons. Return true to forbid giving them.
```
#define EV_ForbidRandomStartWeapons(i, o) \
	/** player */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(ForbidRandomStartWeapons, EV_ForbidRandomStartWeapons);
```

**`PlayerSpawn`**

Called when a player spawns as player, after shared setup, before his weapon is chosen (so items may be changed in here)


    #define EV_PlayerSpawn(i, o) \
    	/** player spawning */ i(entity, MUTATOR_ARGV_0_entity) \
        /** spot that was used, or NULL */ i(entity, MUTATOR_ARGV_1_entity) \
        /**/
    MUTATOR_HOOKABLE(PlayerSpawn, EV_PlayerSpawn);


**`PlayerWeaponSelect`**

Called after a player's weapon is chosen so it can be overriden here.
```
#define EV_PlayerWeaponSelect(i, o) \
	/** player spawning */ i(entity, MUTATOR_ARGV_0_entity) \
    /**/
MUTATOR_HOOKABLE(PlayerWeaponSelect, EV_PlayerWeaponSelect);
```

**`reset_map_global`**

Called in reset_map.
```
#define EV_reset_map_global(i, o) \
    /**/
MUTATOR_HOOKABLE(reset_map_global, EV_reset_map_global);
```

**`reset_map_players`**

Called in reset_map.
```
#define EV_reset_map_players(i, o) \
    /**/
MUTATOR_HOOKABLE(reset_map_players, EV_reset_map_players);
```

<br />
<br />


**`Damage_Calculate`**

Called to adjust damage and force values which are applied to the player, used for e.g. strength damage/force multiplier, I'm not sure if I should change this around slightly (Naming of the entities, and also how they're done in g_damage).


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
        /** force 			*/ o(vector, MUTATOR_ARGV_6_vector) \
        /**/
    MUTATOR_HOOKABLE(Damage_Calculate, EV_Damage_Calculate);

<br />
<br />

AND.... STILL in process