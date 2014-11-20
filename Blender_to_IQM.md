Blender to IQM
==============

Blender when exporting to IQM
-----------------------------

### Needed/Example files

* Bounding Box for Stand and Crouch: http://dev.xonotic.org/attachments/download/33/bbox_crouch_stand.zip
* Erebus example blend: http://dev.xonotic.org/attachments/download/291/erebus.blend
* Erebus example framegroups: http://dev.xonotic.org/attachments/download/292/erebus.iqm.framegroups
* Link to exporter: http://sauerbraten.org/iqm/

### Before You Start

* use the bbox.blend in order to see the size that your model should be. Iqm exporter scale function untested.
* use the duck_bbox.blend in order to see the size that your model should be when crouching.
* for more information on bbox size refer to div0’s model specs [Player_Model_Spec](Player_Model_Spec)
* naming conventions for textures and model go as follow assuming the example is the umbra model: modelname: umbra.iqm, framegroups: umbra.iqm.framegroups, textures: umbra.tga or (jpg), umbra_norm.tga, umbra_gloss.tga, (need to add more)

### Exporting

1. Select both mesh and armature in object mode.
2. Go to scripts \> export \> inter-quake-model.
3. Now make sure bounding boxes and meshes are both highlighted in the script window.
4. Export to a file path of your choosing, /path/to/umbra.iqm. Put the names of all the animations in the animations box, using commas for multiple anims. Then hit the export button and hopefully it will work without any errors.
5. Your model will need a .framegroups file to be used in Xonotic, look at the example file at the beginning of this article or check the [Framegroups](Framegroups) section of this wiki.

### Notes

As of 01/06/2012, Xonotic uses these animations:

    dieone,dietwo,draw,duck,duckwalk,duckjump,duckidle,idle,jump,painone,paintwo,shoot,taunt,run,runbackwards,strafeleft,straferight,deadone,deadtwo,forwardright,forwardleft,backright,backleft,melee,duckwalkbackwards,duckstrafeleft,duckstraferight,duckforwardright,duckwalkforwardleft,duckbackwardright,duckbackwardleft
