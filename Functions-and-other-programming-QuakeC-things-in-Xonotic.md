**Note:** The article is written as developer notes to ease developer tasks and save QuakeC function terms here. Some references are taken from `events.qh`.


# MUTATOR functions (from: `qcsrc/client/mutators/events.qh`, `qcsrc/common/mutators/events.qh`, `qcsrc/server/mutators/events.qh`)

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
MUTATOR_HOOKFUNCTION(new_mutator_name, events.qh_main_hook)
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

You can look the MUTATOR functions in:

**COMMON**:

**`qcsrc/common/mutators/events.qh`** :
https://timepath.github.io/scratchspace/d4/d95/common_2mutators_2events_8qh.html


**CLIENT**:

**`qcsrc/client/mutators/events.qh`** :
https://timepath.github.io/scratchspace/d8/d0e/client_2mutators_2events_8qh.html


**SERVER**:

**`qcsrc/server/mutators/events.qh`** :
https://timepath.github.io/scratchspace/d6/ddd/server_2mutators_2events_8qh.html


<br />
<br />


## List of WEAPON functions

This is a created functions list to modify/create weapons. There are incomplete explanations for each function.

There are contents taken from `qcsrc/common/weapons/all.qh`.

**WARNING:** The contents may content wonky code, and the interactions can change and not do the same what happens here.

<br />
<br />

- [**W_SetupShot_Dir**](https://timepath.github.io/scratchspace/d4/d3f/tracing_8qh.html#aff0ea351757ee6caf83b25d12d18656c)

```c
W_SetupShot_Dir(
	ent,
 	wepent,
 	s_forward,
 	antilag,
 	recoil,
 	snd,
 	chan,
 	maxdamage,
 	deathtype 
)
```

- [**W_SetupProjVelocity_Explicit**](https://timepath.github.io/scratchspace/d7/d31/tracing_8qc.html#a55f8f2b1828413bfb123a5fcb61b9f8e)

```c
void W_SetupProjVelocity_Explicit(
    entity 	proj,
    vector 	dir,
    vector 	upDir,
    float 	pSpeed,
    float 	pUpSpeed,
    float 	pZSpeed,
    float 	spread,
    float 	forceAbsolute 
)
```

- [**W_MuzzleFlash**](https://timepath.github.io/scratchspace/d0/ddd/weapons_2all_8qh_source.html)(located in `qcsrc/common/weapons/all.qh` line 406)

In the moment when player shots the weapon, weapon flashes.
*Note:* write `#ifdef SVQC` at the start of using this function, and write with `#endif` after declared the function(only can do this if the code which needs execute can do this, although maybe you need more functions/things in the code inside this).

```c
void W_MuzzleFlash(Weapon thiswep, entity actor, .entity weaponentity, vector shotorg, vector shotdir);
```

- [**`Weapon selection functions`**](https://timepath.github.io/scratchspace/d8/d6b/selection_8qh.html)
(located in `qcsrc/server/weapons/selection.qh`)

- [**``Weapon decrease ammo, speed factor, rate factor, reload functions`**](https://timepath.github.io/scratchspace/d5/de0/weaponsystem_8qc.html)
(located in `qcsrc/server/weapons/weaponsystem.qh`)


AND.... STILL in process