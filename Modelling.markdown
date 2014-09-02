Modeling
\> h2. Blender when exporting to iqm
\> \> h3. Needed/Example files
\> \> \> \* //Will be added
\> \> h3. Before You Start
\> \> \> \* use the bbox.blend in order to see the size that your model should be. Iqm exporter scale function untested.
\> \> \> \* use the duck\_bbox.blend in order to see the size that your model should be when crouching.
\> \> \> \* for more information on bbox size refer to div0’s model specs [Player\_Model\_Spec](Player\_Model\_Spec)
\> \> \> \* naming conventions for textures and model go as follow assuming the example is the umbra model: modelname: umbra.iqm, framegroups: umbra.iqm.framegroups, textures: umbra.tga or (jpg), umbra\_norm.tga, umbra\_gloss.tga, (need to add more)
\> \> h3. Before exporting
\> \> \> \* you must assign material to your model. Select your model in object mode. Press F5. Look for the MA box and type the name of your model for example umbra.
\> \> \> \* as of right now you cannot use relative paths with the exporter so we will export to iqe, rename the material path, and compile iqe to iqm.
\> \> h3. Exporting
\> \> \> \# Select both mesh and armature in object mode. 
\> \> \> \# Go to scripts \> export \> inter-quake-model. 
\> \> \> \# Now make sure bounding boxes and meshes are both highlighted in the script window. 
\> \> \> \# First we will export the mesh. Leave the animation box empty. Export to a file path of your choosing, /path/to/mesh.iqe. Then hit the export button and hopefully it will work without any errors. 
\> \> \> \# Next we repeat the same steps for each animation but this time we put the animation name in the animation box: Animations: jump. In the file output box put the same file path as mesh.iqe and change it to jump.iqe: /path/to/jump.iqe.
\> \> \> \# You must open the iqe files in text editor and find the line which says Material. Make sure you lead it to the correct path for your textures, for example textures/umbra.tga.
\> \> \> Once you are done with this, it is time to compile iqe to iqm.
\> \> h3. Compile iqe to iqm
\> \> \> \# Create a .bat file with any text editor.
\> \> \> \# Place the .bat file in the folder with the .iqes you exported.
\> \> \> \# Place the iqm.exe into the folder as well.
\> \> \> \# In the .bat file add the following: iqm.exe umbra.iqm mesh.iqe jump.iqe run.iqe (and the rest of the anims). Add the line; pause to the bttom of the file.
\> \> \> \# Now run the .bat file using wine or windows to finally get your iqm.
=========================================================================================================================================================================================================================================================
