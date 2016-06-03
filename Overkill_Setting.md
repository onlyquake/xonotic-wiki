[Overkill](Overkill_Tutorial) is a special mutator for Xonotic. See its [tutorial](overkill-tutorial) for details.

Overkill has been merged into the main game and will be available in 0.8 release!

Server owners looking to run the new overkill on their server will need to change a few things before running their updated server though;
The following options are required in server.cfg for overkill to run properly:

exec balance-overkill.cfg
g_overkill 1
g_spawn_near_teammate 1
g_spawn_near_teammate_ignore_spawnpoint 1
g_dodging 1
g_nades 1

Optionally, if you wish to use legacy ammo reloading, instead of the new ammo charging system, you may set the following cvar in server.cfg as well:
g_overkill_ammo_charge 0

Also, for wall dodging (extra push when dodging against walls), you may also add this to server.cfg:

sv_dodging_wall_dodging 1 

That's all there is to it! Happy overkilling!
