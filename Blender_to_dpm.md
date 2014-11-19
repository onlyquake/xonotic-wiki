Blender to dpm, a mini tutorial
===============================

Pre-required tools and reading
------------------------------

-   Go here - http://developer.valvesoftware.com/wiki/Blender#Installation and download the export script.
-   Rig / Animate as outlined here - http://developer.valvesoftware.com/wiki/Animation_in_Blender.
-   Only works with Blender 248a -- 249b (2.50 is a no go).

Blender work flow
-----------------

-   Select your mesh and armature, export as smd. select Static Mesh. You only need to re-export this smd if the mesh or the rig change.
-   Now export as Animation Sequence. Preferably you have one track (and smd file) per animation. name it so you know what it is (modelname_attack1.smd for example).
-   You could possibly use the “Animation Sequence ( ALL )” or “All…” options, but I haven’t tried so i cant say if it works.

dpmodel work flow
-----------------

-   dpmodel needs and a text file telling it how to bake the mesh and animation(s) into a dpm. This text file should look something like:

    ```
    # save the model as model.dpm
    model model
    # move the model this much before saving
    origin 0 0 0
    # rotate the model 90 degrees around vertical
    rotate 90
    # scale the model by this amount, 0.5 would be half size and 2.0 would be double size
    scale 1
    # load the mesh file, this is stored into the dpm as frame 0
    scene model.smd
    # Each following (if any) smd's are animations
    scene model_action1.smd fps 30
    scene model_action2.smd fps 30
    ```

-   Place all smd’s and the text file in the same place, execute `dpmodel whatever_you_named_that_text_file`. If all goes well you should now have a working dpm (and .framegroups file if its animated)

Caveats:
--------

-   Your mesh needs to have a material assigned to it. The name of the material is what dp will look for to use as texture/shader on the model/mesh/es.
-   Blender exports what you got selected. make sure you have the relevant (and only the relevant) objects selected.
-   If export script fail with a encoding error, open it in a text editor and remove the whole top comment block (lines starting with \#). There’s an illegal character in there according to pyton. I haven’t bothered to check closer witch one it could be.

