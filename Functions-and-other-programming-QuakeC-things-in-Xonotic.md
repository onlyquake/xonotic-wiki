**Note:** The article is written as developer notes to ease developer tasks and save QuakeC function terms here.

# CSQC, MENUQC, SVQC and GAMEQC blocks

Menu and HUD code are actually separated as they run in 2 distinct programs: ***csprogs.dat*** and ***menu.dat***

Server program is ***progs.dat***

- Code inside a **`#ifdef CSQC`** block is part of the client code and will be compiled to **csprogs.dat**

- Code inside a **`#ifdef MENUQC`** block is part of the menu code and will be compiled to **menu.dat**

- Code inside a **`#ifdef SVQC`** block is part of the menu code and will be compiled to **progs.dat**

- Also, code inside a **`#ifdef GAMEQC`** block is part of both client (not menu) and server code.

Example: `g_balance_grapplehook_speed_fly` is clearly a server cvar (**g_*** cvars are server cvars), so you CAN'T declare it within a `#ifdef CSQC` block. This cvar should be declared inside a **`#ifdef SVQC`**.

Other example: `cl_chatsound` is clearly a client cvar (**cl_*** cvars are client cvars), only can be declared in a **`#ifdef CSQC`** block.


<br />

# MUTATOR functions (from: [`qcsrc/client/mutators/events.qh`](https://timepath.github.io/scratchspace/d8/d0e/client_2mutators_2events_8qh_source.html), [`qcsrc/common/mutators/events.qh`](https://timepath.github.io/scratchspace/d4/d95/common_2mutators_2events_8qh_source.html), [`qcsrc/server/mutators/events.qh`](https://timepath.github.io/scratchspace/d6/ddd/server_2mutators_2events_8qh_source.html))

### How to use MUTATOR functions:

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

- **COMMON:** [`qcsrc/common/mutators/events.qh`](https://timepath.github.io/scratchspace/d4/d95/common_2mutators_2events_8qh.html)

- **CLIENT:** [`qcsrc/client/mutators/events.qh`](https://timepath.github.io/scratchspace/d8/d0e/client_2mutators_2events_8qh.html)

- **SERVER:** [`qcsrc/server/mutators/events.qh`](https://timepath.github.io/scratchspace/d6/ddd/server_2mutators_2events_8qh.html)


<br />
<br />

# WEAPON functions

## A bit of introduction

You'll need understand that weapons can be interacted with **autocvars** variables (example: `float autocvar_g_balance_someweapon_speed;`) and each weapon with .qh file where cvars are declared without the need to declare using `autocvar_blabla...`. *Think*, *touch*, *explode* and those types of functions can be declared within an *attack* function and *whatever* it is called. Note that there are also METHODs that are necessary for the weapon to work.

- **Think** function makes the weapon shot react on what to do.
- **Touch** function makes the weapon shot react against some element where touch (like player, monster, vehicle, ...).
- **Explode** function makes the weapon explosion react.
- **Attack/Whatever** function is where the weapon attack executes, keep in mind that it has the other functions attached to be executed.

You can look the example of this weapon code:
- [**devastator.qh**](https://timepath.github.io/scratchspace/d9/dfa/devastator_8qh_source.html)
- [**devastator.qc**](https://timepath.github.io/scratchspace/d9/d5d/devastator_8qc_source.html)

<br />

## List of WEAPON functions

This is a created list of functions to modify/create weapons. There are incomplete explanations for each function.

There are contents taken from [`qcsrc/common/weapons/all.qh`](https://timepath.github.io/scratchspace/d0/ddd/weapons_2all_8qh_source.html)

**WARNING:** The contents may content wonky code, and the interactions can change and not do the same what happens here.

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

- [**Weapon selection functions**](https://timepath.github.io/scratchspace/d8/d6b/selection_8qh.html)
(located in `qcsrc/server/weapons/selection.qh`)

- [**Weapon decrease ammo, speed factor, rate factor, reload functions**](https://timepath.github.io/scratchspace/d5/de0/weaponsystem_8qc.html)
(located in `qcsrc/server/weapons/weaponsystem.qh`)

<br />
<br />

# HUD, Menu and Draw functions

You can look the draw functions where HUD is being drawn: 
- [**Draw functions and macros (`qcsrc/client/draw.qh`)**](https://timepath.github.io/scratchspace/d5/d8d/client_2draw_8qh_source.html)

More info inside the code where you can draw/print HUD and menu: 
- [**Globals, constants, fonts, prints, error cmds, vector stuff, conversion functions and all drawing/printing HUDs/menus/characters related (`qcsrc/dpdefs/upstream/menudefs.qc`)**](https://timepath.github.io/scratchspace/d8/de2/menudefs_8qc_source.html)

<br />

AND... STILL more things in process