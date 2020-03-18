DarkPlaces Wiki
===============

Modeling for DP
===============

Quick notes from LordHavoc on model support (please improve this page!).

EDIT 2020-03-19 - exporting from blender might need specific (old) versions: https://forums.xonotic.org/showthread.php?tid=8269&pid=85677#pid85677

Supported model formats
-----------------------

**mdl** - vertex animated model with skin texture inside it, can contain multiple skins, can contain self-animating framegroups, low quality animation

**md2** - vertex animated model with a single external texture reference, very low quality animation

**md3** - vertex animated model with multiple texture references (multiple meshes), limited coordinate space

**zym** - skeletal animated model with multiple texture references (multiple meshes), no smooth skinning (each vertex is linked only to one joint), high quality animation.

**dpm** - skeletal animated model with multiple texture references (multiple meshes), smooth skinning supported, high quality animation.

**iqm** - skeletal animated model with multiple texture references (multiple meshes), smooth skinning supported, high quality animation, smallest files. More information: http://sauerbraten.org/iqm/

**psk** - skeletal animated model with multiple texture references (multiple meshes), smooth skinning supported, high quality animation. This format is commonly associated with UnrealEngine, in DarkPlaces it can only load one .psa file of the same name as the .psk file, so multiple animation files are not possible (however multiple animations can exist in one .psa file).

**obj** - non-animated static model, large files, easy to export.

Framegroups
-----------

All of these formats can use a .framegroups file (for example models/something/blah.dpm.framegroups) which contains lines such as:

    1 20 30 1 // idle1
    21 15 30 0 // jump

These lines contain: `firstframe numframes framerate loopflag`

Typically each line begins with a firstframe that is the previous firstframe + numframes, but this is not necessarily so, for example animations can be duplicated or played at different rates, the main use of this is to accommodate weapon firing anims where you can alternate between two firing animations (which may use the same frames) so that the network interpolation sees this as a new animation event.
The loopflag indicates if this animation should repeat, if it is 0 then it will stop on the last frame and stay there (death animations, jump animations, etc).

Formats which do not need a .framegroups file to get automated playback of animations (I.E. an animation sequence being set by quakec as a single .frame assignment): **mdl** (requires special configuration of frames in modeling program), **zym**, **iqm**.

Advanced animation topics
-------------------------

If your mod is not using CSQC for animation, it is recommended that you make sure there are multiple variants of any one-shot animations in a model if they may be intended to restart under any circumstances (for example firing a weapon again before the firing animation finishes), and that the code should be cycling through the variants to achieve this (otherwise the networking sees the code is still using the same animation and thinks it should let it finish as normal), however use of CSQC is recommended for more flexibility.

Animation blending between multiple variants of one anim is possible (in QuakeC this is done in CSQC using .frame, .frame2, .frame3, .frame4, .lerpfrac, .lerpfrac3, .lerpfrac4), as well as animation start time control (in QuakeC this is done in CSQC using .frame1time, .frame2time, .frame3time, .frame4time).

Full skeletal control is possible (in QuakeC this is done in CSQC using skel_create and friends, see FTE_CSQC_SKELETONOBJECTS documentation), including applying different animations to different parts of a model, eye tracking and other features.

At this time there is no skeletal rigging system for ragdolls (nor any ragdoll implementation that LordHavoc is aware of), but ragdolls are theoretically possible.
