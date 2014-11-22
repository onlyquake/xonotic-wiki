.framegroups File
=================

This file is needed to make md3, dpm, or iqm models play some animations in Xonotic.

For modelers
------------

It is named `<modelname.extension>.framegroups`. So if you are editing Ignis, it would be called `ignis.iqm.framegroups`.

Inside the file, the playermodel’s animations are defined one per line.

Syntax:

    <start frame> <frame count> <fps> <loop/noloop> // animname

Ex.

    1 100 30 0 // dieone

Defines a 100 frame death animation that start at frame 1, plays at 30 frames per second and does not loop.

Animations must be in this order (these are the values for animname):

1. `dieone`
1. `dietwo`
1. `draw` \*
1. `duck`
1. `duckwalk` \*
1. `duckjump`
1. `duckidle` \*
1. `idle` \*
1. `jump`
1. `painone`
1. `paintwo`
1. `shoot` \*
1. `taunt` \*
1. `run` \*
1. `runbackwards` \*
1. `strafeleft` \*
1. `straferight` \*
1. `deadone`
1. `deadtwo`
1. `forwardright` \*
1. `forwardleft` \*
1. `backright` \*
1. `backleft` \*
1. `melee`

Lines marked with a \* need to loop (last number on the line should be `1`).

If you make 1 looping animation and place model on map as misc\_gamemodel it will be animated.

For coders
----------

To play such a self-playing animation you just use `self.frame=1` to play 1st animation, `self.frame=2` to play 2nd animation, etc.
If the animation does not loop, it will just stop at the last frame and stay there until you run another animation.

