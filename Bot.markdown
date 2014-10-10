Bot
===

General behaviour
-----------------

### Goals

Pathfinding
-----------

### Goals

-   Plan A - Grid based

-   Plan B - Waypoints based
    -   Cached waypoint links

-   A\* based

-   Cached nodes *\_
    **\* This means that most of map discovery or waypoint creation will be done offline
    h2. Navigation
    h3. Goals
    ** Steering behaviour
    \* Swimming
    **\* Support getting out of water
    **\* Float in the same place if until a path is found
    **\* Eventually support navigation under water as long as the pathfinder supports it too
    ** Able to get out of lava, acid, etc
    **\* Ideally it should request quickly a new path to the pathfinder, instead of improvising on the movement code
    ** Never, ever, get stuck in the same place. Wander around if there nothing better to do.
    \* Able to rocket-jump*(as a last resource measure, when they're thrown into space void)\_

-   Plan A - Waypoint based
    -   Avoid path congestion \_(this happens when more than one bot on the same team are traveling over the same path)\_

-   Filter insanely quick movements (aka shaking)

Talking
-------

### Goals

Aiming
------

### Goals

Coding guidelines
-----------------

Links
-----
