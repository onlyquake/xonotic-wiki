# Nades

Come in a variety of types. The offhand hook bind or drop weapon bind throws the grenade. Hold the throw key E to throw the nade. (*NOTE: If you have a Grappling Hook weapon with you, you will have to press the G key once to throw it and then press it again when you want to throw the nade. Due to development reasons, the Grappling Hook only can be used with the E key as the main key, so it was developed to avoid errors in the game.*) Press F8 to switch nade types.

# Nade types

## Normal

<img src="uploads/7e75ed16f04358a1297c0cd1363a5e03/normal.jpg" alt="normalnade" width="450"/>

<img src="uploads/f087361a52e91df6459df22e3926f412/normalboom.jpg" alt="normalboom" width="450"/>

Frag grenade. Explodes.

## Napalm

<img src="uploads/eab7d20707a37db964faeca5b624648a/napalm.jpg" alt="napalm" width="450"/>

<img src="uploads/07e424e85718e7f40cf524183384b0e6/napalmboom.jpg" alt="napalmboom" width="450"/>

Shoots several napalm globs in a circle around the nade. Touching these will ignite players and likely kill them.

## Nitro

<img src="uploads/d5c18cbaed37fc98b28a3fc2d8b3f8ed/nitro.jpg" alt="nitro" width="450"/>

<img src="uploads/4790da4757c57d879be55493c95b6857/nitroboom.jpg" alt="nitroboom" width="450"/>

Freezes enemies in a large radius. Lethal.

## Translocate 

<img src="uploads/ee94f06409a122191a74d70e1e2250bd/translocate.jpg" alt="translocate" width="450"/>

<img src="uploads/1487c855c09637affb13c6cfeaaae994/translocateboom.jpg" alt="translocateboom" width="450"/>

Teleports the player to where the nade "explodes".

## Spawn

<img src="uploads/77f2c9768bec14f7b5c5cfd68452886f/spawnnade.jpg" alt="spawnnade" width="450"/>

Creates a spawn point that can be respawned on three times. It's useful when you need to go back in the point where you want to start after died, instead starting in the main points.

## Healing

<img src="uploads/22b3273ceedc7cbf526f7b7e8a719828/healing.jpg" alt="healing" width="450"/>

<img src="uploads/606e3175f20a9274b9c651f5b8fea151/healingboom.jpg" alt="healingboom" width="450"/>

Regenerates health in a large radius around the nade.

## Entrap

<img src="uploads/15add5938094995589a7d569e9195f24/entrap.jpg" alt="entrap" width="450"/>

<img src="uploads/e846c4dac00937a4bcef89c5fe961291/entrapboom.jpg" alt="entrapboom" width="450"/>

Slows movement within a large radius for 12 seconds. Makes the balls' gravity fall faster when they are inside the orb. In the orb, you will see that the electro balls fall quicker inside and rockets / bullets are slowing down.

## Veil

<img src="uploads/9ad5f03fe196de135e03f281cdd4cc62/veil.jpg" alt="veil" width="450"/>

<img src="uploads/88071dccb47d650aacd31c719eadb6b6/veilboom.jpg" alt="veilboom" width="450"/>

It creates an orb which makes invisible to the players whose are on the side of the one who has thrown(in TDM, CTF, team gamemodes) during a time.

# Pokenade 

<img src="uploads/3a0322703abb471d604d3b65b778bd53/monsternade.jpg" alt="monsternade" width="450"/>

<img src="uploads/f453f36f7b04dd48c0747fc9075f4895/monsternadeboom.jpg" alt="monsternadeboom" width="450"/>

Spawns a monster. Four monsters can be alive at one time. Options include:

## Zombie

Medium speed melee attacker. Can be ridden for movement speed higher than running (but not as fast as strafe jumping).

## Spider

High speed melee attacker. Drops 25 health on death.

## Wyvern

Flying monster.

## Shambler

Large, slow melee attacker. Drops 100 health on death.

## Random

Spawns all of the above and a marine at random.

**More info about monsters are in [this link](Monsters).**

## Notes for developers

**Nades source codes are in this [directory](https://gitlab.com/xonotic/xonotic-data.pk3dir/-/tree/master/qcsrc/common/mutators/mutator/nades).**

If you are creating a server for yourself, to play with the nades, you need to activate the nades and it is recommended to set those variables (you can toggle in the console while writing `g_nades` and pressing TAB to display info of these cvars):

`g_nades 1 // activate nades in the game`

`set g_nades_nade_damage 150 // normal nade explosion damage`

`set g_nades_bonus 1 // adding number of extra nades when it's obtained after time bonus`

`set g_nades_bonus_client_select 1 // allow client side selection of bonus nade type`

`set g_nades_bonus_max 3 // maximum number of bonus grenades`

`set g_nades_bonus_type 3 // type of the bonus grenade. 1:normal 2:napalm 3:ice 4:translocate 5:spawn 6:heal 7:pokenade 8:entrap`

`set g_nades_bonus_score_time 5 // time when someone is scoring, makes adding fast one nade extra more`

`set g_nades_heal_foe -5 // when someone is not ally of the healing orb will take damage during a certain time if this is inside the orb`

`set g_nades_nade_lifetime 3.5`

`set g_nades_nade_maxforce 2000`

`set g_nades_nade_minforce 400`

`set g_nades_nade_newton_style 0 // 0 is absolute, 1 is relative (takes into account player speed), 2 is something in between`

`set g_nades_napalm_ball_damage 110 // napalm explosion damage`

`set g_nades_napalm_ball_lifetime 4 // napalm burning time after exploded`

`set g_nades_napalm_burntime 3 // napalm burn time when someone is burning with those flames`

`set g_nades_entrap_time 15 // entrap orb time`

`set g_nades_nade_refire 10`

`set g_nades_veil_radius 720 // veil orb radius size`

`set g_nades_veil_time 6 // veil orb time`

`set g_nades_ice_freeze_time 2 // How long the ice field will last`

`set g_nades_ice_health 1 // How much health the player will have after being unfrozen`

`set g_nades_ice_teamcheck 0 // Don't freeze teammates`

`set g_nades_ice_explode 1 // Whether the ice nade should explode again once the ice field dissipated`

`set g_nades_spawn_count 1 // number of times player will spawn at their spawn nade explosion location`

`set g_nades_spread 0.04 // random spread offset of throw direction`


After setting all this, it can be necessary to restart the server, use `restart` command to apply the changes. Instead doing this manually, you can put those variables in a *.cfg* file. Save the variables inside *nades.cfg* empty file and save it in *xonotic/data* folder. In the game, when you are playing in your own server, execute in the console: `exec nades.cfg` and restart if necessary.