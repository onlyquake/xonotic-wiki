Xonotic on Linux uses system libraries. For Windows and macOS external dlls and dylibs are needed. Those reside in xonotic/misc/buildfiles

Because at the time of writing there is no automatism to build or update the games dependencies for those 2 platforms and the current dlls/dylibs are VERY outdated and thus also contain vulnerabilities, this page should document on where to obtain or how to build them, retaining API compatibility to darkplaces and also older OS platform versions like Windows XP.

# libcurl
libcurl is used for downloading *.pk3 files from servers

### Windows
Darkplaces loads libcurl-4.dll or libcurl-3.dll

Build instructions:
* clone https://gitlab.com/incognico/build-libcurl-windows
* run build.bat in a VS2019 Development Shell
* rename the built dlls (x64 & x86) to libcurl-4.dll

### macOS
Darkplaces loads libcurl.4.dylib or libcurl.3.dylib or libcurl.2.dylib

# libjpeg-turbo
libjpeg-turbo is needed to display jpeg images/textures

### Windows
Darkplaces loads libjpeg.dll

Obtainment instructions:
* download libjpeg-turbo-VERSION-vc.exe & libjpeg-turbo-VERSION-vc64.exe from https://sourceforge.net/projects/libjpeg-turbo/files/
* extract the *.exe files and use bin/jpeg62.dll
* rename the dlls (x64 & x86) to libjpeg.dll

### macOS
Darkplaces loads libjpeg.62.dylib

# libpng
libpng is needed to display png images/textures

### Windows
Darkplaces loads libpng16.dll or libpng16-16.dll or libpng15-15.dll or libpng15.dll or libpng14-14.dll or libpng14.dll" or libpng12.dll

### macOS
Darkplaces loads libpng16.16.dylib or libpng15.15.dylib or libpng14.14.dylib or libpng12.0.dylib

# libfreetype

# libogg

# libvorbis

# libvorbisfile

# libvorbisenc

# libtheora

# libstdc++-6 & libgcc_s_sjlj-1
libgcc_s_sjlj-1 is a dependency of libstdc++-6

# libd0_blind_id-0 & libd0_rijndael-0
See https://gitlab.com/xonotic/d0_blind_id

# libgmp
A dependency of libd0_blind_id-0