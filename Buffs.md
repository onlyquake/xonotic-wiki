Buffs
=====

**Buffs** is a mutator that adds various [powerup](Powerups)-like collectibles, the “Buffs”. Buffs are little bonuses that improve your status effects or give you a special power. A few buffs have a downside as well.

Usage
-----
To collect a buff, simply walk over it. You can only have one buff at a time. All buffs have a duration of 60 seconds.

You can drop a buff (thereby destroying it) by pressing the “drop key/flag” control (default F).

List of buffs
-------------

This is a list of all possible buffs:

| Name | Description |
|:-|:-|
| Ammo | Your ammo is infinite |
| Bash | Increased knockback force and immunity to knockback |
| Disability | Attacks to enemies deal slowness (decreased movement/attack speed) for a few seconds) |
| Flight | Crouch in mid-air to reverse gravity for you |
| Inferno | Players you damage will also receive burning damage for a few seconds |
| Invisible | You will be nearly invisible |
| Jump | Greatly increased jump height |
| Luck | Each attack has a chance of a “critical hits” with greatly increased damage |
| Magnet | You will automatically collect items near you |
| Medic | Your health will regenerate up to 150 HP, you heal nearby players and have a chance to survive fatal hits |
| Resistance | Greatly reduces damage taken |
| Speed | Increased speed of movement, attacks and health regeneration. Downside: You are a bit more vulnerable to attacks as well |
| Swapper | You can press the “drop weapon” key to switch places with a nearby enemy |
| Vampire | You receive the damage you deal as health (even above 200 HP) |
| Vengeance | If someone hurts you, some of the damage is mirrored back to them |

Disability, Jump, Flight and Swapper are disabled by default.

Enabling buffs
--------------

Buffs are enabled in the Mutators menu or with setting the [CVar](CVars) `g_buffs` to `1`. However, buffs will only spawn in maps that support it. For maps that lack support for buffs, you can also set the CVar `g_buffs_replace_powerups` to `1`. This will spawn buffs where [Powerups](Powerups) would normally spawn.