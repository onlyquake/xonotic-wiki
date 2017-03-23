Darkplaces Parameters
=====================

`-safe` parameter disables the usage of like every goody a graphic card offers to speed up things  

Other options you might want to try are (-safe should be like you use all/most of them at once, but i did not check for this list being complete):

`-noanisotropy` disables `GL_EXT_texture_filter_anisotropic` (allows higher quality texturing)  
`-nocombine` disables `GL_ARB_texture_env_combine` or `GL_EXT_texture_env_combine` (required for bumpmapping and faster map rendering)  
`-nocubemap` disables `GL_ARB_texture_cube_map` (required for bumpmapping)  
`-nocva` disables `GL_EXT_compiled_vertex_array` (renders faster)  
`-nodot3` disables `GL_ARB_texture_env_dot3` (required for bumpmapping)  
`-nodrawrangeelements` disables `GL_EXT_draw_range_elements` (renders faster)  
`-noedgeclamp` disables `GL_EXT_texture_edge_clamp` or `GL_SGIS_texture_edge_clamp` (recommended, some cards do not support the other texture clamp method)  
`-nofragmentshader` disables `GL_ARB_fragment_shader` (allows pixel shader effects, can improve per pixel lighting performance and capabilities)  
`-nomtex` disables `GL_ARB_multitexture` (required for faster map rendering)  
`-noseparatestencil` disables use of OpenGL2.0 `glStencilOpSeparate` and `GL_ATI_separate_stencil` extensions (which accelerate shadow rendering)  
`-noshaderobjects` disables `GL_ARB_shader_objects` (required for vertex shader and fragment shader)  
`-noshadinglanguage100` disables `GL_ARB_shading_language_100` (required for vertex shader and fragment shader)  
`-nostenciltwoside` disables `GL_EXT_stencil_two_side` (which accelerate shadow rendering)  
`-notexture3d` disables `GL_EXT_texture3D` (required for spherical lights, otherwise they render as a column)  
`-novertexshader` disables `GL_ARB_vertex_shader` (allows vertex shader effects)  

