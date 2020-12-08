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

You can look the MUTATOR functions in:

**`qcsrc/common/mutators/events.qh`** :
https://timepath.github.io/scratchspace/d4/d95/common_2mutators_2events_8qh.html

**`qcsrc/server/mutators/events.qh`** :
https://timepath.github.io/scratchspace/d6/ddd/server_2mutators_2events_8qh.html


<br />
<br />

AND.... STILL in process