Mapping-entity-func button
==========================

What Radiant Says
-----------------

    When a button is touched by a player, it moves in the direction set by the "angle" key, triggers all its targets, stays pressed by an amount of time set by the "wait" key, then returns to it's original position where it can be operated again.
    -------- KEYS --------
    angle : determines the direction in which the button will move (up = -1, down = -2).
    target : all entities with a matching targetname will be triggered.
    target2 : all entities with a matching targetname will be triggered.
    target3 : all entities with a matching targetname will be triggered.
    target4 : all entities with a matching targetname will be triggered.
    target_random : instead of triggering ALL matched entities, trigger ONE of them by random
    speed : speed of button's displacement (default 40).
    platmovetype : movement type (1 = linear, 2 = cosine [default])
    wait : number of seconds button stays pressed (default 1, -1 = return immediately).
    lip : lip remaining at end of move (default 4 units).
    health : (default 0) if set to any non-zero value, the button must take damage (any amount) to activate.
    -------- SPAWNFLAGS --------
    NOSPLASH : if set, splash damage cannot activate the door, only direct damage can (requires health to be set)

What NetRadiant Means
---------------------

A button entity is exactly as it sounds …  
A button …  
You push it …  
It does stuff …  

How to use it
-------------

-   Make a brush, with it selected, right click on the overview pane. Then go to func, and click on func\_button. Then hit [n] to bring up the entity editor, and pick a direction. Up is up and down is down. For z-axis, 0 degrees is east on the 2d view, so 90 is north, 180 is west, 270 is south. **NOTE :: it defaults to z-axiz when the radio button shows up. If you want up first select something else, then select up**

-   Then we need to link it so something. To do that select the button first, then select the tartget, and hit [ctrl]+[k]. You should see a line linking to the button and the object.

In the Wild
-----------

Currently none of the default xonotic maps have a button in them. However, warefare, a popular duel map uses a button to trigger the elevator.

