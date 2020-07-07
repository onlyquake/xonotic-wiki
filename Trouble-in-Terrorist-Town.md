# Trouble in Terrorist Town (TTT)

## WARNING! This gamemode has been lost. There is no way to recover this only if the responsible author does. Possibly the author violated the GPL rule, specifically he broke "sharing" rule in an open source community (as he didn't share and contribute). The community would be glad to retrieve this gamemode resources.

## This gamemode appeared once in a server called "FSMP Teamplay", the server was shutdown in late 2019.

<img src="uploads/6cdb741c94684e2633821c7540269186/iconTTTgamemode.png" alt="iconTTTxonotic"/>

# Objective of the Game

The game mode is based on the fact that there is a small group of traitors and another of detectives, there is an explanation of the functions of each one.


## Traitors

The Traitors are the medium sized group in TTT (25% of the population or one Traitor for every four players.) Their group color is red, but this is not displayed to anyone other than Traitors, or when a Traitor has been confirmed to be dead.
The traitors must murder everyone undetected, they know who they are because only among themselves do they see a red "circle" that blinks around their companions' bodies. They must kill all innocents before time runs out.


## Detectives

The Detectives are the smallest group in TTT (12.5% of the population or one Detective for every eight players.) They are special Innocents given equipment. Their group color is blue.
Detectives have special methods to detect the traitor, for example, when they see a body, they must analyze the body, searching in it until it says a message in the middle "Unidentified", when seeing it, touch the E, if the body was recently killed, it will tell if he was Innocent or a Traitor.

They always appear as CT and everyone sees them as CTs, plus they flash a blue circle on their body that everyone sees (unlike traitors who only see each other CT and the flash is only seen by them).


## Innocent

The Innocent are the majority (62.5% of the game's population by default.) Their group color is green.
The task of the innocent is to detect traitors and defend detectives more than anything, they must kill the right person or anything special.


## About Karma points

It is worth clarifying that everyone can kill each other, but there is something called "**Karma**", which starts with an initial, and increases if they do things right (if traitors kill, or if traitors kill people), otherwise, the Karma will be discounted.

The Karma is used for the damage that weapons generate, the more Karma, the more damage your weapon will do.

If the Karma is lower, the player can be banned temporarily to avoid teamkills or any abuse with the end to keep the game in balance.


# Screenshots

The screenshots are from 23/08/2019.

<img src="uploads/7ba1f8aed1b8dc2f41cec2679b8928d0/iconTroubleinTerroristTown.jpg" alt="selectgamemodeTroubleinTerroristTownFSMPServer" width="400"/>

<img src="uploads/bb848a10f699a55df73e70d9ab6e1102/spectating.jpg" alt="TTTspectatingInterface" width="400"/>

<img src="uploads/fbdadc8a4d7a66b459475f12fcfb3944/traitor.jpg" alt="TTTtraitor" width="400"/>

<img src="uploads/5953f5fd352f33e8d915350f16fbbe3c/whenFinishedmakes_public_everyone_whotheyare.jpg" alt="TTTwhenmatchFinishedmakeseveryonesayingwhotheyare" width="400">

<img src="uploads/098c35c194b1a2e12857eade57a0ad03/karmaScore.jpg" alt="TTTkarmaScore" width="400"/>


# Rules

## Basic Rules

All basic rules apply to any role and or players.
​

- No Randomly Damaging Mate​

1. Randomly Damaging a teammate without sufficient evidence of them committing a kill on site as offence, This includes damages that have been done unintentionally.​

2. Killing any player that is away from their keyboard.​


- No Traitor Baiting

1. Performing traitorous acts as Innocent repeatedly.

2. Tricking other players into believing you're a Traitor.



## Role Rules

These rules only apply if you are apart of that role for example you can't break a detective rule if you're an innocent.​


<span style="color:green">**Innocents**</span>​

1. Do not commit any Traitorous acts.

2. Do not work with Traitors

3. Only kill when you have a valid reason to do so.

4. Obey valid detective orders at all times.

5. Do not harm the detectives in any way.

6. Do not use a Traitor defib at all.


<span style="color:red">**Traitors**</span>

1. Do not kill other Traitors.

2. Always try to alert other Traitors to your traps.

3. Do not sell out other Traitors.

4. Do not use a Cleaning defib at all.


<span style="color:blue">**Detectives**</span>

1. Do not give unreasonable orders.

2. Do not harm Innocents

3. Do not abuse your powers.

4. Do not work with Traitors.

5. Do not use the Traitor defib at All.

## Kill on Site Rules

A kill on site must come under valid for you to act on it. Any kill on site marked with the role letter and color (<span style="color:blue">D</span>, <span style="color:red">T</span> or <span style="color:green">I</span>) are only valid if given by that role. if you kill on site someone for an invalid reason then you may be warned for False kill on site.​

- Valid kill on site​

1. Self Defence.

2. Damage without a valid reason.​

3. Mass killing.​

4. Associating with Traitors.​

5. Hiding game sensitive items.​

6. Using traitor weaponry without being proven.​

7. Failing to Identify bodies after killing.​

8. Walking past multiple unidentified bodies.​

9. Not following Detectives orders. (<span style="color:blue">D</span>)​


- Invalid kill on site​

1. kill on site on a Skin.​

2. kill on site on a Weapon.​

3. kill on site on a Location.​

4. Not following Innocents orders.​

5. Suspicion.​

6. Aiming at players.​


## Notes for developers / mappers

Sorry, developers, the code will have to be recreated, it is hard to find it in order to recover it.

Inside the map (.pk3 file), in .mapinfo file, you write: `gametype ttt`

Optionally, you can write this too:

`settemp_for_type ttt g_buffs 0`

`settemp_for_type ttt g_new_toys 1`

`settemp_for_type ttt g_random_items 1`

`settemp_for_type ttt g_random_items_powerup_probability 0`

`settemp_for_type ttt g_random_items_weapon_crylink_probability 0`

`settemp_for_type ttt g_random_items_weapon_devastator_probability 0`

`settemp_for_type ttt g_random_items_weapon_electro_probability 0`

`settemp_for_type ttt g_random_items_weapon_hlac_probability 1`

`settemp_for_type ttt g_random_items_weapon_minelayer_probability 1`

`settemp_for_type ttt g_random_items_weapon_vortex_probability 0`

`settemp_for_type ttt g_random_items_weapon_rifle_probability 1`

`settemp_for_type ttt g_random_items_item_armor_mega_probability 0`

`settemp_for_type ttt g_random_items_item_health_mega_probability 0`

`settemp_for_type ttt g_pickup_respawntime_ammo 0`

`settemp_for_type ttt g_pickup_respawntime_weapon 0`

`settemp_for_type ttt g_chat_nospectators 2`


Moreover, you can enable this gamemode in the console using this command: 
`sv_cmd gametype ttt`
