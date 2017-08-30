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

# Gametype and maps
```
gametype dm
```
Specifies default gametype that will be played.

```
sv_vote_gametype 0
```
If set to 1, players will be able to vote for different gametypes.

```
sv_vote_gametype_options "dm tdm lms ctf ca ft ka kh dom ons as"
```
Specifies the list of gametypes that the player are allowed to vote for.

```
g_maplist_votable 6
```
Specifies the number of maps that will be offered for voting. Higher values will allow more choices.

```
g_maplist_votable_nodetail 1
```
If set to 0, the players will be able to see the number of votes for each map (or gametype if `sv_vote_gametype` is 1).

# Bots
```
minplayers 0
```
If set to more than 0, the server will try to make sure that the number of all active players matches the value set. For example, if `minplayers` is 4 and there is 1 person playing, the server will have 3 bots. Bots will leave or join when the number of players changes. When nobody is connected to the server, no bots will be playing.

```
skill 5
```
Sets the skill level of bots. Higher values mean harder bots. Possible values are 0 through 10.

# Warmup
```
g_warmup 0
```
If set to 1, the map will start in the warmup mode which is designed to let everyone join before the game begins. All players will need to become ready (by pressing `F4` by default) or vote `allready` in order for the game to begin.

```
g_warmup_limit 0
```
If set to more than 0, specifies the maximum time of the warmup state. Can be used to force the game to begin without player consensus or when players forgot about warmup being active.