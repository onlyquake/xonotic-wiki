Darkplaces Parameters
=====================

~~safe parameter disables the usage of like every goody a graphic card offers to speed up things
Other options you might want to try are :
~~noanisotropy disables GL\_EXT\_texture\_filter\_anisotropic (allows higher quality texturing)
~~nocombine disables GL\_ARB\_texture\_env\_combine or GL\_EXT\_texture\_env\_combine
~~nocubemap disables GL\_ARB\_texture\_cube\_map (required for bumpmapping)
~~nocva disables GL\_EXT\_compiled\_vertex\_array
~~nodot3 disables GL\_ARB\_texture\_env\_dot3 (required for bumpmapping)
~~nodrawrangeelements disables GL\_EXT\_draw\_range\_elements
~~noedgeclamp disables GL\_EXT\_texture\_edge\_clamp or GL\_SGIS\_texture\_edge\_clamp (recommended, some cards do not support the other texture clamp method)
~~nofragmentshader disables GL\_ARB\_fragment\_shader
~~nomtex disables GL\_ARB\_multitexture (required for faster map rendering)
~~noseparatestencil disables use of OpenGL2.0 glStencilOpSeparate and GL\_ATI\_separate\_stencil extensions
~~noshaderobjects disables GL\_ARB\_shader\_objects (required for vertex shader and fragment shader)
~~noshadinglanguage100 disables GL\_ARB\_shading\_language\_100
~~nostenciltwoside disables GL\_EXT\_stencil\_two\_side (which accelerate shadow rendering)
~~notexture3d disables GL\_EXT\_texture3D
~~novertexshader disables GL\_ARB\_vertex\_shader (allows vertex shader effects)
