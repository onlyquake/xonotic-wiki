This page explains basic server settings. During the start of the server, it searches for the `data/server.cfg` file and executes it. You need to create it inside your user directory (GNU/Linux default: `~/.xonotic/data/server.cfg`).

# Quick start
Xonotic comes with an example configuration in `/server/server.cfg`. You can copy it into your user directory and simply edit it.

# Hello world
A minimal configuration would be this:

```
sv_public 1
hostname "My Test server"
maxplayers 32
```

It creates a server named "My Test server" that can handle 32 players and is visible on the master server. It will run deathmatch with default settings.

# Basic settings
```
sv_motd "Hi, this is my epic server"
```
Specifies the "message of the day" which will be displayed to players when they connect or press the info button.

```
port 26000
```
Specifies the port which is used by the server. This can be very useful if you want to run more than 1 server on the same machine. In that case, ports for each server must be unique.

```
log_file "server.log"
```
If set, the server will log game events to a file. Beware that this file may become very large with time.

```
rcon_password "Correct horse battery staple"
```
Specifies a RCON (remote console) password that can be used to control your server remotely such as from the connected client. This can be very useful when you are playing on your server and want to quickly change some settings.