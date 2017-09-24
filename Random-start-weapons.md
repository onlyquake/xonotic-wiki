You can specify weapons which will be randomly given to player during spawn. The code will try to make sure that these weapons are not duplicates. If a player receives a weapon but has no ammo for it, they will be given some ammo.

## Server settings
```
g_random_start_weapons_count 0
```
Number of random start weapons that will be given to the player.

```
g_random_start_weapons "machinegun mortar electro crylink vortex hagar devastator"
```
Names of potential random start weapons.

```
g_random_start_shells 15
```
How many shells will be given with a shell-based weapon.

```
g_random_start_bullets 80
```
How many bullets will be given with a bullet-based weapon.

```
g_random_start_rockets 40
```
How many rockets will be given with a rocket-based weapon.

```
g_random_start_cells 30
```
How many cells will be given with a cell-based weapon.

```
g_random_start_plasma 30
```
How much plasma will be given with a plasma-based weapon.