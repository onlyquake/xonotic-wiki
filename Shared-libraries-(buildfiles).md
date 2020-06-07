darkplaces/Xonotic on Linux uses system libraries. For Windows and macOS external dlls and dylibs are needed. Those reside in xonotic/misc/buildfiles

Because at the time of writing there is no automatism to build or update the games dependencies for those 2 platforms and the current dlls/dylibs are VERY outdated and thus also contain vulnerabilities, this page should document on where to obtain or how to build them, retaining API compatibility to darkplaces and also older OS platform versions like Windows XP.

For Windows, all libraries can/should be obtained from https://packages.msys2.org/ [1] with the exception of an official DLL release from the upstream being available (this is the case for jpeg-turbo and freetype) or if it has to be compiled on under Windows for some reason (eg. libcurl for Schannel (Windows crypto for HTTPS) support).

A handy tool to check dll deps on Windows is https://github.com/lucasg/Dependencies

# libcurl
libcurl is used for downloading *.pk3 files from servers

### Windows
Darkplaces loads `libcurl-4.dll` or `libcurl-3.dll`

Build instructions:
* clone https://gitlab.com/incognico/build-libcurl-windows
* run `build.bat` in a VS2019 Development Shell
* rename the built dlls (x64 & x86) to `libcurl-4.dll`

### macOS
Darkplaces loads `libcurl.4.dylib` or `libcurl.3.dylib` or `libcurl.2.dylib`

# libjpeg-turbo
libjpeg-turbo is needed to display jpeg images/textures

### Windows
Darkplaces loads `libjpeg.dll`

Obtainment instructions:
* download `libjpeg-turbo-VERSION-vc.exe` & `libjpeg-turbo-VERSION-vc64.exe` from https://sourceforge.net/projects/libjpeg-turbo/files/
* extract the *.exe files and use `bin/jpeg62.dll`
* rename the dlls (x64 & x86) to `libjpeg.dll`

### macOS
Darkplaces loads `libjpeg.62.dylib`

# libpng
libpng is needed to display png images/textures

### Windows
Darkplaces loads `libpng16.dll` or `libpng16-16.dll` or `libpng15-15.dll` or `libpng15.dll` or `libpng14-14.dll` or `libpng14.dll` or `libpng12.dll`

Obtainment instructions:
* download MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-libpng
* use dll from `bin` folder

### macOS
Darkplaces loads `libpng16.16.dylib` or `libpng15.15.dylib` or `libpng14.14.dylib` or `libpng12.0.dylib`

# zlib
zlib is required to read *.pk3 files. Also it is a dependency of libpng and probably some other libraries.

### Windows
Darkplaces loads: ifdef ZLIB_USES_WINAPI `zlibwapi.dll` or `zlib.dll` else `zlib1.dll`. We use `zlib1.dll`!

Obtainment instructions:
* download as MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-zlib
* use dll from `bin` folder

### macOS
Darkplaces loads `libz.dylib`

# libfreetype
Required for the Xolonium font

### Windows
Darkplaces loads: `libfreetype-6.dll` or `freetype6.dll`

Obtainment instructions:
* Download x86 and x64 dlls from: https://github.com/ubawurinna/freetype-windows-binaries

### macOS
Darkplaces loads: `libfreetype.6.dylib` or `libfreetype.dylib`

# libvorbis + libvorbisfile + libvorbisenc
libvorbis + libvorbisfile are used to play .ogg audio files while libvorbis + libvorbisenc is used for the audio in video capturing (cl_capturevideo)

### Windows
Darkplaces loads `libvorbis-0.dll` or `libvorbis.dll` or `vorbis.dll` and `libvorbisfile-3.dll` or `libvorbisfile.dll` or `vorbisfile.dll` and `libvorbisenc-2.dll` or `vorbisenc-2.dll` or `vorbisenc.dll`

Obtainment instructions:
* download MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-libvorbis
* use dll from `bin` folder

### macOS
Darkplaces loads `libvorbis.dylib` and `libvorbisfile.dylib`

# libtheora
libtheora is used for the video in cl_capturevideo
libtheoraenc/libtheoradec are not needed, they are the newer API; darkplaces uses the legacy pre 1.0 API (libtheora).

### Windows
Darkplaces loads `libtheora-0.dll` or `theora-0.dll` or `theora.dll`

Obtainment instructions:
* download MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-libtheora
* use dll from `bin` folder

### macOS
Darkplaces loads `libtheora.dylib`

# libogg
libogg is used for the container in cl_capturevideo

### Windows
Darkplaces loads `libogg-0.dll` or `libogg.dll` or `ogg.dll`

Obtainment instructions:
* download MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-libogg
* use dll from `bin` folder

### macOS
Darkplaces loads `libogg.dylib`

# libd0_blind_id-0 & libd0_rijndael-0
Internal project, see https://gitlab.com/xonotic/d0_blind_id

# libgmp
A dependency of libd0_blind_id-0

### Windows
libd0_blind_id-0 loads `libgmp-10.dll`

Obtainment instructions:
* download as MSYS2 Package [1] in x86 and x64 versions: https://packages.msys2.org/base/mingw-w64-gmp
* use dll from `bin` folder

# libode
Is not loaded under Windows and crashes the game if it is and a map is loaded up.
Also it is not statically linked and thus requires libstdc++-6.dll and libgcc_s_sjlj-1.dll.

# libavw
*Note:* Old and not used in Xonotic but also not disabled :) Adding this for the sake of completeness.

### Windows
Darkplaces loads: `libavw.dll`

Source code: https://github.com/paulvortex/DpLibAVW

### macOS
Darkplaces loads: `libavw.dylib`