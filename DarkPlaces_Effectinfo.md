DarkPlaces Wiki
===============

Effectinfo Scripting Reference
==============================

EffectInfo is built-in scripting language to describe particle effects in DarkPlaces, it's pretty simple and contains basic scripting functions.

Each effect can have several emitters which is defined in `effectinfo.txt` or `maps/mapname_effectinfo.txt`

General syntax
--------------

    // emitter 1
    effect EFFECT_NAME
    parm value
    parm2 value
    ...

    // emitter 2
    effect EFFECT_NAME
    parm value
    parm2 value
    ...

    // emitter for another effect
    effect ANOTHER_EFFECT
    parm value
    parm2 value
    ...

Console variables
-----------------

`r_drawparticles`: toggle drawing of all particles 

`r_drawparticles_drawdistance`: set a maximal distance to draw particles at 

`cl_particles_size`: this will scale a size of all particles 

`cl_particles_quality`: multiplier of particles count spawned by emitters, better quality = more particles (1 - min, 4 - max. quality) 

`cl_particles_reloadeffects`: reloads effectinfo.txt while in the game; that eliminates a need to quit and restart DP to see updated effects 

Particle parameters
-------------------

    effect <name>

Defines a new emitter with effectname is belongs to, all parms after that will be applied to that emitter.  

    effect <name>

Defines a new emitter with effectname is belongs to, all parms after that will be applied to that emitter.

    count <count>

How many particles to spawn at this emitter, this setting is affected by cl_particles_quality cvar

    countabsolute <count>

Defines a count of particles spawned regardless of cl_particles_quality setting  
Total particles count = countabsolute + count * cl_particles_quality

    type <type>

Sets a generic particle type, affect appearance, blending, physics.  
List of particle types:

-   alphastatic : alpha-blended billboard
-   static : additive-blended billboard
-   spark : additive blended, stretched (based on velocity)
-   beam : a beam particle, drawn from origin to origin + velocity
-   rain : a rain particle, alpha-blended spart that will cause splash effect on impact
-   raindecal: oriented rain decal, additive-blended
-   snow: alpha blended, velocity jitters in realtime
-   bubble: alpha-blended
-   blood: inverse-modulated, leaves decal
-   smoke: alpha-blended billboard
-   decal: makes a decal on nearest surface
-   entityparticle: alpha-blended, this particle gets removed after being drawn (used on EF_BRIGHTFIELD)

</end list hack>

    blend <blendtype>

Generic blend is set by type, but with this parm it cound be changed after type is defined.  
List of blend types:

-   alpha : alpha blended
-   add: additive blended
-   invmod: inverse modulation (used on blood and blood decals)

</end list hack>

    orientation <orientationtype>

Same as for blend, generic orientation is set by type, could be altered by this parm.  
List of orientation types:

-   billboard : always turned to viewer
-   oriented : ignores viewwer, turned to velocity
-   beam : facing viewer on 2 axises, stretched from origin to origin + velocity
-   spark : facing viewer on 2 axises, stretched (based on velocity)

</end list hack>

    color <min_color> <max_color>

Sets a color for particles. On each particle spawn, it's color is linearly randomized betwen two given colors. Color should be defined as HEX 0xRRGGBB, like 0xFFFFFF is white, and 0xFF0000 is red.

    tex <min_index> <max_index>

Sets a index of particle from particlefont. Indexes are counted from left to right, from up to down, last index is 63, first is 0. Randomized linearly on each particle spawn.

    size <min_size> <max_size>

Size of particle in game units, typical value is 4, randomized.

    sizeincrease <rate>

This will make particle grow or diminish over time. <rate> is to how much utits to add or subtract per second. Note that while diminishing particle, engine will not check if particle will go to negative size, it will just invert it.

    alpha <min_alpha> <max_alpha> <fade_rate>

Opacity of particles, 256 is opaque, 0 is transparent. Randomized. Could be more that 256 (to simulate fade delay). Fade rate is how huch alpha to throw away per second, once particle gets alpha 0 (full transparence), it gets removed.

    time <min_time> <max_time>

Particle time-to-live in seconds, randomized.

    gravity <value>

Particle gravity modifier, 1 is full gravity, 0.5 is half etc., negative values are supported (particle go up).

    bounce <value>

Particle bounce-of-walls factor, 1 - bounce with full speed, 0.5 bounce with half speed. A value of -1 means particle will be removed on impact. Not that particle physics considered slow and spawning lots of bouncing particles is not recommended.

    airfriction <value>

Particle friction while moving in air, good option for smoke emitters. A value of 0 means no friction, negative values will do acceleration.

    liquidfriction <value>

Particle friction while moving in liquids.

    originoffset <x> <y> <z>

Offset particle spawning origin by this values. Coordspace are world, x - forward, y - right, z - up.

    velocityoffset <x> <y> <z>

Add this amount of constant velocity to particle on spawn.

    originjitter <x> <y> <z>

Like originoffset but each axis is jittered between -value/+value. Hence it is defining spherical shape of particle random spawning.

    velocityjitter <x> <y> <z>

Same as originjitter but for velocity.

    velocitymultiplier <x>

Multiply particle starting velocity (one that set by QC or engine, whatever calls effect) by this value. Useful with trails. Negative values are supported.

    underwater

Sets underwater flag for particles. Particles that are underwater will be removed in air. Useful for water bubbles.

    notunderwater

Sets notunderwater flag for particles. Particles that are notunderwater will be removed in liquid. Useful for fire particles.

    trailspacing <x>

This parm is only useful when effect is spawned as trail, defines a game units gap between effect invocations.

    stretchfactor <x>

A custom stretch factor that is used on sparks.

    rotate <startangle_min> <startangle_max> <spin_min> <spin_max>

Used to rotate particle, first 2 parms is start angle, other two are spin velocity.

Particles leaving decals
------------------------

Particles can leave decals once hit something. For this behavior a special set of parms should be used. This section is unfinished, futher explanation is required.  

    staincolor <min_color> <max_color>

A randomized color for decal particle.

    stainalpha <min_alpha> <max_alpha>

A randomized alpha.

    stainsize <min_size> <max_size>

A randomized size.

    staintex <min_index> <max_index>

A randomized index into particlefont.

    stainless

Disables decal spawning and returns all parms to it's default values.

Dynamic lights
--------------

Dynamic realtime lights could be placed in particle effects (useful for explosions) with this range of parms. These params apply just like standard ones.  

    lightradius <radius>

Radius of light in game units. Typical value is 200.

    lightradiusfade <rate>

Radius fade rate, how many units to add/subtract per second. Once light reaches radius of 0 it gets removed.

    lighttime <time>

If radius fading not set, this parm can be used to define light life time.

    lightcolor <red> <green> <blue>

A RGB-normalized light color, 1 1 1 is white, 0 0 1 is blue. Can exceed 1 (overbright light).

    lightshadow <value>

Cast shadows from light, value is 0 or 1.

    lightcubemapnum <value>

Sets a numbered cubefilter for light, cubemap texture is cubemaps/<value>

Engine effect names
-------------------

Heres a list of effect names used by engine.

    TE_GUNSHOT
    TE_GUNSHOTQUAD
    TE_SPIKE
    TE_SPIKEQUAD
    TE_SUPERSPIKE
    TE_SUPERSPIKEQUAD
    TE_WIZSPIKE
    TE_KNIGHTSPIKE
    TE_EXPLOSION
    TE_EXPLOSIONQUAD
    TE_TAREXPLOSION
    TE_TELEPORT
    TE_LAVASPLASH
    TE_SMALLFLASH
    TE_FLAMEJET
    EF_FLAME
    TE_BLOOD
    TE_SPARK
    TE_PLASMABURN
    TE_TEI_G3
    TE_TEI_SMOKE
    TE_TEI_BIGEXPLOSION
    TE_TEI_PLASMAHIT
    EF_STARDUST
    TR_ROCKET
    TR_GRENADE
    TR_BLOOD
    TR_WIZSPIKE
    TR_SLIGHTBLOOD
    TR_KNIGHTSPIKE
    TR_VORESPIKE
    TR_NEHAHRASMOKE
    TR_NEXUIZPLASMA
    TR_GLOWTRAIL
    SVC_PARTICLE

Using custom effects in QuakeC
------------------------------

There are 3 QuakeC functions that can are used to call custom effects. They are defined `in dpextensions.qc`.

```c
float(string effectname) particleeffectnum = #335;
void(entity ent, float effectnum, vector start, vector end) trailparticles = #336;
void(float effectnum, vector org, vector vel, float howmany) pointparticles = #337;
```

Effects can called by first obtaining the effectnum, then calling the appropriate particle function.

```c
local float effectnum;

effectnum = particleeffectnum("EFFECT_NAME");

pointparticles(effectnum, self.origin, '0 0 0', 10);
```
