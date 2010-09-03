h1. Normal Maps

Normal maps are critical to make your texture look less flat in game. Normal maps must be automatically generated from a heightmap. Here is how to make a normal map, from initial design to final _norm texture.

# Make a texture
The first step is to actually make a texture. In order to create a normal map, you just need the diffuse texture.
# Install necessary tools
You can use "this gimp plugin":http://code.google.com/p/gimp-normalmap/ for this. It is also available in ubuntu repos under the name gimp-normalmap.
# Create a heightmap
Now that you've got the necessary tools and materials, you must make a heightmap. A heightmap is a representation of a surface where black is lower than white (that is, white is on the same level as the texture and black is on a lower level). How long it takes you to do this will vary from texture to texture but there are a few key things to remember:
## Do not use black. Use #010101 with an alpha of 1.
## Do not have any transparent areas.
Your final result should look similar to "this":http://rm.endoftheinternet.org/img/uploaded/643cc7461e286dbb853e66a9cf3db4e0.png.
# Create a normal map
Now that you have your heightmap, open it in gimp and go to Filters->Map->Normalmap. Check "Invert Y", "Wrap", set "Height Source" to "Average RGB" and "Alpha Channel" to "Height". The rest are up to you (but do not check any more options). Experiment particularly with "Minimum Z" and "Scale", these will vary from texture to texture.


To be continued...
