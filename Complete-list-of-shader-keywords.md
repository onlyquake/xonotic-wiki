Complete list of shader keywords
================================

Note: You can append a `:q3map` suffix to a shader name to make q3map2 use the shader but the engine ignore it.

Note: This list does not contain all possible shader keywords, but just those that q3map2 uses for anything. More keywords are likely to be supported by your engine. Check the documentation or the source code of your engine on this.

Inside shader stages
--------------------

-   **`map` texture:** loads a texture and displays it repeating
-   **`clampMap` texture:** loads a texture and displays it non-repeating
-   **`animMap` fps texture texture...:** loads an animation and displays it repeating
-   **`clampAnimMap` fps texture texture...:** loads an animation and displays it non-repeating
-   **`mapComp` texture:** ?
-   **`mapNoComp` texture:**?

In the shader preamble:
-----------------------

-   **`cull none`, `cull disable`, `cull twosided`:** treat the surface as two sided for lighting
-   **`damageShader` shadername:** sets the given shader as damage shader (for SoF2 mods)
-   **`fogparms` ...:** marks the brush as a fog volume; otherwise handled by the engine
-   **`implicitBlend`:** ?
-   **`implicitMap`:**?
-   **`implicitMask`:** ?
-   **`light` shadername:** sets the given shader as flare shader
-   **`polygonoffset`:** enable polygon offset
-   **`q3map_backShader` shadername:** sets the given shader as shader for back faces
-   **`q3map_backsplash` percent distance:** configures light backsplash (self-surfacelight)
-   **`q3map_baseShader` shadername:** inherit parameters from a shader
-   **`q3map_bounce` F, `q3map_bounceScale` F:** scales the intensity of radiosity
-   **`q3map_clipmodel`:**?
-   **`q3map_cloneShader` shadername:** ?
-   **`q3map_colorGen`:** FIXME later
-   **`q3map_deprecateShader` shadername:**?
-   **`q3map_flare` shadername, `q3map_flareShader` shadername:** sets the given shader as flare shader
-   **`q3map_floodLight` r g b dist intensity power:** overrides the global floodlight parameters
-   **`q3map_fogDir` ( x y z ):** sets the direction a fog shader fades from transparent to opaque
-   **`q3map_foliage` path scale density odds invertalpha:** ?
-   **`q3map_forceMeta`:** forces brush faces and/or triangle models to go through the metasurface pipeline
-   **`q3map_forceSunlight`:**?
-   **`q3map_fur` layers offset fade:** ?
-   **`q3map_globaltexture`:**?
-   **`q3map_indexed`:** ?
-   **`q3map_invert`:** inverts the direction from which the face is visible
-   **`q3map_lightRGB` r g b:** overrides the light color of the texture
-   **`q3map_lightStyle` N:** sets the light style (SoF2, JK2)
-   **`q3map_lightSubdivide` N:** subdivision interval for `q3map_surfacelight`
-   **`q3map_lightmapAxis` axis:** sets the lightmap axis to one of `x`, `y`, `z` (useful for terrain)
-   **`q3map_lightmapBrightness` F, `q3map_lightmapGamma` F:** overrides lightmap brightness
-   **`q3map_lightmapFilterRadius` self other:**?
-   **`q3map_lightmapMergable`:** allows merging the lightmap with other surfaces on another plane
-   **`q3map_lightmapSampleOffset` F:** multiplies samplesize by a factor
-   **`q3map_lightmapSampleSize` N:** overrides samplesize
-   **`q3map_lightmapSize` N:** overrides the lightmap size (forces an external lightmap for this surface)
-   **`q3map_material` materialname:** ?
-   **`q3map_noFast`:** disable `-fast` style lighting for this surface
-   **`q3map_noVertexLight`:** turns off vertex lighting for this surface
-   **`q3map_noVertexShadows`:**?
-   **`q3map_noclip`:** do not clip the surface by the BSP tree
-   **`q3map_nofog`:** ?
-   **`q3map_nonplanar`:** marks the surface as nonplanar for meta surface merging
-   **`q3map_notjunc`:** do not do t-junction elimination
-   **`q3map_offset` F:**?
-   **`q3map_onlyVertexLighting`:** same as using `surfaceparm pointlight`
-   **`q3map_patchShadows`:** force shadowing from patches using this shader
-   **`q3map_remapShader` shadername:** ?
-   **`q3map_shadeAngle` F:** sets the shading angle for nonplanar surfaces
-   **`q3map_skyLight` value iterations:** sets the amount of sky light from this surface
-   **`q3map_splotchfix`:**?
-   **`q3map_styleMarker2`:** ?
-   **`q3map_styleMarker`:**?
-   **`q3map_sunext` r g b intensity degrees elevation deviance samples:** sets an unsharp sun for the map
-   **`q3map_sun` r g b intensity degrees elevation, `sun` r g b intensity degrees elevation:** sets a sharp sun for the map
-   **`q3map_surfacelight` F:** sets the amount of surface light from this surface
-   **`q3map_surfacemodel` path density minscale maxscale minangle maxangle oriented:** randomly place models on the surface
-   **`q3map_tcGen ivector` ( sx sy sz ) ( tx ty tz ):** same as `q3map_tcGen vector` but with inverted values
-   **`q3map_tcGen vector` ( sx sy sz ) ( tx ty tz ):** overrides texcoords based on world coordinates (for terrain)
-   **`q3map_tcMod rotate` a:** rotates the texture
-   **`q3map_tcMod scale` s t:** multiplies texcoords by factors
-   **`q3map_tcMod translate` s t:** translates texcoords by a vector
-   **`q3map_terrain`:** ?
-   **`q3map_textureSize` width height:** overrides the texture size for texcoords
-   **`q3map_vertexScale` F:** scales vertex lighting amount by a factor
-   **`q3map_vertexShadows`:**?
-   **`qer_editorImage` texture:** sets the texture to show for radiant
-   **`qer_lightImage` texture:** sets the image to take the light color from
-   **`qer_normalImage` texture:** sets the normal map for bump mapping
-   **`skyparms` outerimage cloudheight innerimage:** loads a skybox
-   **`surfaceparm` alphashadow:** use the alpha channel of the shader image as shadow mask
-   **`surfaceparm` areaportal:** ?
-   **`surfaceparm` botclip:**?
-   **`surfaceparm` clusterportal:** ?
-   **`surfaceparm` detail:** ignore this surface for vis
-   **`surfaceparm` donotenter:**?
-   **`surfaceparm` fog:** ???
-   **`surfaceparm` hint:** use this surface as a hint to generate BSP splits
-   **`surfaceparm` lava:** Stef hates this brush
-   **`surfaceparm` lightfilter:** use the color channel of the shader image as shadow mask
-   **`surfaceparm` monsterclip:** monsters can’t go through this brush, but shots can
-   **`surfaceparm` nodraw:** do not generate draw surfaces
-   **`surfaceparm` nodrop:** items can’t be dropped on this brush
-   **`surfaceparm` nolightmap, `surfaceparm` pointlight:** do not lightmap this surface
-   **`surfaceparm` nomarks:** this surface is stain free
-   **`surfaceparm` nonsolid:** do not make this surface solid
-   **`surfaceparm` origin:** the center of this brush shall be the origin of this brush model
-   **`surfaceparm` playerclip:** players can’t go through this brush, but shots can
-   **`surfaceparm` sky:** this surface shows the skybox
-   **`surfaceparm` slime:** this brush contains more poisonous stuff than dihydrogene monoxide
-   **`surfaceparm` structural:** use this surface for vis
-   **`surfaceparm` trans:** cast no shadows
-   **`surfaceparm` trigger:** this is a trigger brush (translucent and solid)
-   **`surfaceparm` water:** this brush contains dihydrogene monoxide
-   **`tessSize` F, `q3map_tessSize` F:** subdivides the polygons to ensure no parts are larger than the given size

