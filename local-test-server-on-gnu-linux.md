This tutorial explains how to setup a local test server that can be launched on the same machine as client.

# Official release

This section explains how to setup a server from the official release of Xonotic. It assumes that you have extracted it in `~/Games/Xonotic/Release`.

First you need to create a file called `~/.xonotic/data/server.cfg` with the following content:

```
sv_public 1
hostname "My Test server"
maxplayers 32
```

This config creates a vanilla deathmatch server that will be visible to other players on the server list.

Next, you will probably want to create a launcher for your server so you can launch it from your desktop. Create a file called `~/Desktop/Xonotic Server.desktop` with the following content:

```
[Desktop Entry]
Version=1.0
Type=Application
Terminal=true
Exec=/home/user/Games/Xonotic/Release/xonotic-linux64-dedicated -sessionid 1
Name=Xonotic Server
Icon=/home/user/Games/Xonotic/Release/misc/logos/icons_png/xonotic_32.png
Path=/home/user/Games/Xonotic/Release/
```

Now try double clicking on that launcher in your desktop and it should launch a dedicated server. Then you can launch client and connect to it.

# Git version

This section explains how to setup a server from the git repository of Xonotic. It assumes that you have cloned it in `~/Games/Xonotic/Git/xonotic`.

You can use `server.cfg` from the previous section.

Create a file called `~/Desktop/Xonotic Git Server.desktop` with the following content:

```
#!/usr/bin/env xdg-open

[Desktop Entry]
Version=1.0
Type=Application
Terminal=true
Exec=/home/user/Games/Xonotic/Git/xonotic/darkplaces/darkplaces-dedicated -xonotic -sessionid 1
Name=Xonotic Git Server
Icon=/home/user/Games/Xonotic/Git/xonotic/misc/logos/icons_png/xonotic_32.png
Path=/home/user/Stuff/Games/Xonotic/Git/xonotic/
```

Again, double click on this launcher to launch server. Have fun!