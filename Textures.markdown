Textures in Xonotic
===================

{{\>toc}}

There are 2 material/texture systems in Xonotic that can work together.

System one
----------

This system is based off of the texture name, with the suffix denoting what the texture describes.

|Texture name|Filename|Description|
|------------|--------|-----------|
|Diffuse|texturename.tga|This is the texture as it will look to an observer without lighting or any other effects.|
|Normal|texturename\_norm.tga|Xonotic uses OpenGL style tangent space normal map (Inverted Y/green channel). You can put height map in normal maps alpha channel and it will be used when offset or relief mapping is on. This will give your texture a 3d look.|
|/2.Alpha channel|texturename\_norm.tga|If the TGA image is 32bits, the alpha channel will be loaded from the image.|
|texturename\_alpha.jpg|**note ONLY works with jpg at the moment** (What does this mean? Why is there a tga entry for this then?)|
|Bump map|texturename\_bump.tga|Bump maps are like normal maps in that they allow a texture to be 3d. However, normal maps have higher priorities and so will overwrite bump maps. It is a better idea to use a normal map instead of a bump map, since the roughness of a bump map is limited by a cvar.|
|Specular|texturename\_gloss.tga|This map will make your texture more or less shiny. There may be colors in this map.|
|Fullbright|texturename\_glow.tga|Areas textured with this map will always glow and shadows will not affect them.|
|Team color/custom|texturename\_pants.tga|Areas textured with this map will show the user’s custom or team color. Make it grayscale and leave same area 100% black in diffuse texture.|
|Shirt|texturename\_shirt.tga|Like the above, but a secondary color. **Does this still exist?**|

System two
----------

Second material system is simplified Quake 3™ shader system.
The main difference is that you can use only 1 pass, with a few exceptions:
\* Lightmap pass is allowed
\* Blend shaders are allowed (blending two diffuse textures + lightmap). Same syntax as in quake3.
