Darkplaces Parameters
=====================

-safe parameter disables the usage of like every goody a graphic card offers to speed up things

Other options you might want to try are (-safe should be like you use all/most of them at once, but i did not check for this list being complete):
-noanisotropy disables GL\_EXT\_texture\_filter\_anisotropic (allows higher quality texturing)
-nocombine disables GL\_ARB\_texture\_env\_combine or GL\_EXT\_texture\_env\_combine (required for bumpmapping and faster map rendering)
-nocubemap disables GL\_ARB\_texture\_cube\_map (required for bumpmapping)
-nocva disables GL\_EXT\_compiled\_vertex\_array (renders faster)
-nodot3 disables GL\_ARB\_texture\_env\_dot3 (required for bumpmapping)
-nodrawrangeelements disables GL\_EXT\_draw\_range\_elements (renders faster)
-noedgeclamp disables GL\_EXT\_texture\_edge\_clamp or GL\_SGIS\_texture\_edge\_clamp (recommended, some cards do not support the other texture clamp method)
-nofragmentshader disables GL\_ARB\_fragment\_shader (allows pixel shader effects, can improve per pixel lighting performance and capabilities)
-nomtex disables GL\_ARB\_multitexture (required for faster map rendering)
-noseparatestencil disables use of OpenGL2.0 glStencilOpSeparate and GL\_ATI\_separate\_stencil extensions (which accelerate shadow rendering)
-noshaderobjects disables GL\_ARB\_shader\_objects (required for vertex shader and fragment shader)
-noshadinglanguage100 disables GL\_ARB\_shading\_language\_100 (required for vertex shader and fragment shader)
-nostenciltwoside disables GL\_EXT\_stencil\_two\_side (which accelerate shadow rendering)
-notexture3d disables GL\_EXT\_texture3D (required for spherical lights, otherwise they render as a column)
-novertexshader disables GL\_ARB\_vertex\_shader (allows vertex shader effects)

