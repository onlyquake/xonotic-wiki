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

-   Cached nodes *<span class="plans both to applies"></span>*
    -   This means that most of map discovery or waypoint creation will be done offline

Navigation
----------

### Goals

-   Steering behaviour

-   Swimming
    -   Support getting out of water
    -   Float in the same place if until a path is found
    -   Eventually support navigation under water as long as the pathfinder supports it too

-   Able to get out of lava, acid, etc
    -   Ideally it should request quickly a new path to the pathfinder, instead of improvising on the movement code

-   Never, ever, get stuck in the same place. Wander around if there nothing better to do.

-   Able to rocket-jump *<span class="void space into thrown they're when measure, resource last a as"></span>*

-   Plan A - Waypoint based
    -   Avoid path congestion *<span class="path same the over traveling are team same the on bot one than more when happens this"></span>*

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
