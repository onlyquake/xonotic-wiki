DarkPlaces Wiki
===============

Material creation for DP
========================

Quick notes by LordHavoc (in need of cleanup and completion!):

All texture files are optional except for diffuse, a q3 shader allows additional options to be set but is not required for common materials.

Replacing Content
-----------------

Formats supported: tga (recommended), png (loads very slowly), jpg (loads slowly), pcx, wal, lmp

Usually you want to put replacement content in either `id1/` or another directory such as `pretty/` inside your quake directory, in DarkPlaces you can run multiple `-game` options at once (such as `-game ctf -game pretty -game dpmod` to have texture overrides from pretty, maps from ctf, and gameplay from dpmod) or multiple gamedirs specified with the gamedir console command (`gamedir ctf pretty dpmod`).

All texture layers are optional except diffuse (the others are NOT loaded without it)

**Replacing skins:**  
progs/player.mdl\_0.tga - diffuse  
progs/player.mdl\_0\_**norm**.tga - normalmap (can have alpha channel with bumpmap height for offsetmapping/reliefmapping)  
progs/player.mdl\_0\_**bump**.tga - bumpmap (not loaded if normalmap is present)  
progs/player.mdl\_0\_**glow**.tga - glow map (use `_luma` if tenebrae compatibility is a concern)  
progs/player.mdl\_0\_**luma**.tga - alternate tenebrae-compatible name for glow map (use one or the other)  
progs/player.mdl\_0\_**pants**.tga - pants image, greyscale and does not cover the same pixels as the diffuse texture (this is additive blended ('Screen' mode in photoshop) ontop of the diffuse texture with a color tint according to your pants color)  
progs/player.mdl\_0\_**shirt**.tga - shirt image, same type as pants  

**Replacing textures in specific maps:**  
textures/**e1m1**/ecop1\_6.tga  
textures/**e1m1**/ecop1\_6\_norm.tga  
textures/**e1m1**/ecop1\_6\_bump.tga  
textures/**e1m1**/ecop1\_6\_glow.tga  
textures/**e1m1**/ecop1\_6\_luma.tga  
textures/**e1m1**/ecop1\_6\_pants.tga - pants and shirt layers are possible on bmodel entities with quakec modifications to set their .colormap field  
textures/**e1m1**/ecop1\_6\_shirt.tga  

**Replacing textures in all maps:**  
textures/quake.tga  
textures/quake\_**norm**.tga  
textures/quake\_**bump**.tga  
textures/quake\_**glow**.tga  
textures/quake\_**luma**.tga  
textures/quake\_**pants**.tga  
textures/quake\_**shirt**.tga  

**Replacing hud and menu pictures:**
gfx/conchars.tga  

Diffuse Color + Alpha (Opacity)
-------------------------------

`textures/texturepackname/texturename.tga`  

Generally should have ambient occlusion baked into the color (in other words, the grooves are dark), but no shading.

NormalMap + Relief Height
-------------------------

`textures/texturepackname/texturename_norm.tga`  

The normalmap is OpenGL-style with green pointing up (often normalmap tools call this "inverted"), matching Doom3/Quake4/etc behavior, but contrary to several other games.  

The height channel is black for deep areas and white for being flush with the surface, the height is used only when offsetmapping (`r_glsl_offsetmapping`) or reliefmapping (`r_glsl_offsetmapping_reliefmapping` also on) are active.  

For best results the height channel should be fairly smooth, no fine bumps, just the overall shape of the material.  

Specular Color + Specular Exponent
----------------------------------

`textures/texturepackname/texturename_gloss.tga`  

The specular (gloss) color is full color and basically indicates how bright the specular reflection should when a light illuminates this surface, it should be black where you want the surface to look dull and bright where you want a shiny appearance.

For best results, color the gloss according to the material involved, for example plastic or car paint has a white specular color, copper has an orange specular color, gold has a yellow specular color, steel has a very slight blue tint to its otherwise white specular color, aluminum also has a very slight tint.

Generally the specular color should have ambient occlusion baked into the color (just like the diffuse does).

The alpha channel of this texture will multiply the specular exponent (`r_shadow_glossexponent`), white alpha will be sharp highlights, dark alpha produces very broad highlights very bright highlights, in general sharp highlights indicate metal or hard plastic materials, aluminum has a different specular hardness than steel, etc.

Glow color
----------

`textures/texturepackname/texturename_glow.tga`  

This is the luminous glow of the material, pretty much you want this to be black with color only where a light emitting part of the surface exists (for example a series of red dots for red LED lights).

Be sure not to have any glow color in the diffuse texture as it will not add up properly.

Alpha is unused at this time.

Reflection mask for cubemap environment mapping
-----------------------------------------------

`texturename_reflect.tga` - mask for the reflection, looks similar to gloss texture, basically this is where things will be shiny and what color of reflection (use orange for copper, yellow for gold, a slight blue tinted white color for steel, etc)

In shader: `dpreflectcube map/mapname/reflect1`

You can produce such a texture with this console command: `envmap map/mapname/reflect1 512`

Which will produce files such as:  
`map/mapname/reflect1px.tga map/mapname/reflect1py.tga map/mapname/reflect1pz.tga map/mapname/reflect1nx.tga map/mapname/reflect1ny.tga map/mapname/reflect1nz.tga`  

`map/mapname/reflect1ft.tga map/mapname/reflect1rt.tga map/mapname/reflect1bk.tga map/mapname/reflect1lf.tga map/mapname/reflect1up.tga map/mapname/reflect1dn.tga`  

The first 6 are a cubemap, the last 6 are a skybox, keep one or the other set of files, you don't need both.

Material description (.shader) file
-----------------------------------

In gamedir/scripts the engine will load all files with the extension .shader using a Quake3-compatible shader loader, however not all features will be utilized (for example it only supports one layer shaders, additional layers may be used to activate special behaviors - such as lightmapping - but will not be directly rendered).

The syntax of the Quake3-compatible .shader files is best explained by examples, so there are several here to look at.

Many additional features can be added to any shader with expected results, such as `tcmod scroll 1 0` (makes a texture scroll in one direction), `deformvertexes autosprite` (makes a surface consisting of quads render as billboards facing the view), `deformvertexes autosprite2` (makes a surface consisting of rectangular quads - not square - rotate around their long axis to face the view, useful for flame trail sprites and torch flames among other things)...

Lightmapped material
--------------------

    textures/texturepackname/texturename
    {
        {
            map $lightmap
            rgbGen identity
            tcGen lightmap
        }
        {
            map textures/texturepackname/texturename
            rgbGen identity
            blendFunc GL_DST_COLOR GL_ZERO
        }
    }

Transparent additive-blend unlit material
-----------------------------------------

    textures/texturepackname/texturename
    {
        surfaceparm noimpact
        surfaceparm nolightmap
        surfaceparm nomarks
        surfaceparm nonsolid
        surfaceparm nodlight
        surfaceparm trans
        {
            map textures/texturepackname/texturename
            blendfunc add
            rgbgen identity
        }
    }

Note: you can omit some of the surfaceparms (keep trans!) when making a model material rather than a map material.

Model material
--------------

    textures/texturepackname/texturename
    {
        {
            map textures/texturepackname/texturename
            rgbgen lightingDiffuse
        }
    }

Model material that does not cast shadows
-----------------------------------------

    textures/texturepackname/texturename
    {
        dpnoshadow
        {
            map textures/texturepackname/texturename
            rgbgen lightingDiffuse
        }
    }

Invisible shadow-casting model material
---------------------------------------

    textures/common/shadowmesh
    {
        dpshadow
    }

Lightmapped material with reflection cubemap and dpmeshcollisions
-----------------------------------------------------------------

    textures/texturepackname/texturename
    {
        dpreflectcube textures/texturepackname/reflect1
        dpmeshcollisions
        {
            map $lightmap
            rgbGen identity
            tcGen lightmap
        }
        {
            map textures/texturepackname/texturename
            rgbGen identity
            blendFunc GL_DST_COLOR GL_ZERO
        }
    }

DP Shader Commands
------------------

    dp_reflect distort r g b a

Makes surfaces of this shader reflective with `r_water`. The reflection is alpha blended on the texture with the given alpha, and modulated by the given color. distort is used in conjunction with the normalmap to simulate a nonplanar water surface.  

    dp_refract distort r g b

Makes surfaces of this shader refractive with `r_water`. The refraction replaces the transparency of the texture. distort is used in conjunction with the normalmap to simulate a nonplanar water surface.  

    dp_water <reflectmin> <reflectmax> <refractdistort> <reflectdistort> <refractr> <refractg><refractb>
     <reflectr> <reflectg> <reflectb> <alpha>

This combines the effects of dp_reflect and dp_refract to simulate a water surface. However, the refraction and the reflection are mixed using a Fresnel equation that makes the amount of reflection slide from reflectmin when looking parallel to the water to reflectmax when looking directly into the water. The result of this reflection/refraction mix is then layered BELOW the texture of the shader, so basically, it "fills up" the alpha values of the water. The alpha value is a multiplicator for the alpha value on the texture (set this to a small value like 0.1) to emphasize the reflection and make the water transparent; but if `r_water` is 0, alpha isn't used, so the water can be very visible then too.

    tcmod page <width> <height> <delay>

The texture is shifted by 1/<width> every <delay> seconds, and by 1/<height> every <delay>\*<width> seconds. It is some sort of animmap replacement that keeps all animation frames in a single texture.

To use it, make a texture with the frames aligned in a grid like this:

    1   2   3   4
    5   6   7   8

then align it in Radiant so only one of the animation frames can be seen on the surface, and specify "tcmod page 4 2 0.1". DP will then display the frames in order and the cycle will repeat every 0.8 seconds.
