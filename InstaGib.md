InstaGib
========

Overview
--------

InstaGib is a mutator that replaces all weaponry with the [Vaporizer](Weapons#vaporizer). It is a powerful hitscan weapon that will immediately kill the target player in one shot (unless they got an extra life).

InstaGib is a popular mutator that mixes well with almost all game modes and may be included in many Xonotic servers. When participating in an InstaGib match, one must have particularly good aim and conserve shots whenever possible. Because if you run out of ammo for 10 seconds, you will suicide.

Rules
-----

* Vaporizer:
    * Everyone spawns with the Vaporizer with 10 cells
    * The Vaporizer consumes 1 cell per shot
    * If you don't have ammo for 10 seconds, you suicide and might lose a point (depends on game mode)
    * The secondary fire of the Vaporizer doesn't deal damage
* Extra Lives
    * Extra lives act like armor: If a player is shot while having one or more extra lives, they will survive the shot but suffer a strong pushback
    * The number of your extra lives is shown in the HUD as armor
* Items and powerup replacements:
    * Strength [powerup](Powerups) is replaced by Invisibility
    * Shield powerup is replaced by Speed
    * [Mega Health](Items) is replaced by Extra Life
* If you took damage from the enviroment (e.g. lava), this will reduce the countdown timer when you run out of ammo. You can restore your health back to 100 by collecting ammo

Collectibles and powerups
-------------------------
* Vaporizer (dropped weapon): +5 cells
* Cells item: +5 cells
* Invisibility: Makes you (nearly) invisible for 30 seconds
* Speed: Greatly increases your movement speed for 30 seconds
* Extra Life: Grants you one or more extra lives (amount depends on settings)

Hints
---------------
* Cells ammunition may be difficult to find on some maps, but can be picked up readily from a downed player.

CVar
----

InstaGib is enabled with the [CVar](CVars) `g_instagib`.