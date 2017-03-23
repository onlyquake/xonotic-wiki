Relics mutator:
===============

The Relics mutator spawns several relics around the map, as items that players can pick up and hold. Each player can carry one relic at a time, and drops it when they die or press the “drop relic” button. If not picked up after some time, a relic will respawn in another location. Each relic grants a special ability to the player carrying it. Currently, there are 16 relics in Xonotic.

*NOTE: This mutator is not committed to master yet. To test it, see the branch mirceakitsune/mutator\_relics in GIT.*  

*TODO: Test the mutator intensively and fix any possible remaining issues.*  
~~*TODO 2: Add sounds and particle effects when a relic causes an action.*~~ DONE  
*TODO 3: Remove Runematch, as this mutator will replace it.*  
*TODO 4: Teach bots to go for relics, as low priority items.*  
*TODO 5: Show the relic you are carrying on the HUD.*  

Relic types:
============

**1 - Resistance:** The Resistance relic protects the player carrying it, by making him take less damage. Does not work while you have the Shield powerup.

**2 - Regeneration:** This relic slowly regenerates the carrier’s health. It’s not available when normal health regeneration is enabled, and therefore will not spawn by default.

**3 - Vampire:** The carrier of this relic is healed based on the damage he deals to his opponent. This relic will not spawn when the vampire mutator is enabled.

**4 - Ammo:** Slowly grants ammo of all types to the owner. Except fuel when the fuel\_regen item is owned.

**5 - Damage:** The weapons of those who have this relic do more damage. Does not work while you have the Strength powerup.

**6 - Splash Damage:** When the holder shoots someone, the damage is transmitted to those around the victim, harming them as well.  
*TODO: Make this relic not affect team mates.*

**7 - Firing Speed:** The player’s weapons fire faster.

**8 - Disability:** A player shot by the owner of this relic is cursed for several seconds. Curses include: Slower movement, lower jump height, slower firing rate.  
~~*TODO: Add effects to the players cursed by this relic, such as particles and sounds.*~~ DONE

**9 - Team Boost:** Players carrying this relic boost team mates that get close to them. The boost also lasts for a few seconds after they leave the carrier’s radius. This relic will only spawn in team games.  
~~*TODO: Add effects to the players boosted by this relic, such as particles and sounds.*~~ DONE

**10 - Speed:** Owners of this relic can run faster.

**11 - Jump:** Helps the player jump higher.

**12 - Flight:** Players fly around when they pick up this relic (just like observers)

**13 - Invisibility:** The player becomes transparent, making him harder to see and hit. This relic will not spawn when the cloaked mutator is enabled.

**14 - Radioactive:** Those who get too close to the holder of this relic will take damage.  
*TODO: Make this relic not affect team mates.*

**15 - Resurrection:** If you die while holding this relic, you will be revived with your health to default spawn value. The relic then respawns in a different location. Does not work for suicides.

**16 - Vengeance:** When the carrier dies, he causes a big explosion that harms anyone who is close. The relic then respawns in a different location. Does not work for suicides.  
*TODO: Fix explosion particles, which are not showing for some reason.*

