## CVars (see xonotic.org/tools/cacs for more up-to-date information)

* `sv_eventlog`: master switch
* `sv_eventlog_files`: print frags, scores and captures for separate files each match
* `sv_eventlog_console`: print frags, scores and captures to serverconsole during the match
* `sv_logscores_bots`: choose whether bot are included in stats or not
* `sv_eventlog_files_counter`: number of matches logged until now
* `sv_eventlog_files_nameprefix`: file name prefix to be used 
* `sv_eventlog_files_namesuffix`: file name extension to be used
* `sv_eventlog_files_timestamps`: prefix log lines in the files with time events
* `sv_eventlog_ipv6_delimiter`: change : in IPv6 addresses to _

## Log format
```
:logversion:3
:gamestart:<gametype>_<mapname>:<matchid>
:gameinfo:mutators:LIST:mutator1:mutator2:...
```
(note that mutators are listed by their cvar name with g_ removed, unless such a cvar is 1 by default - then the mutator is listed with a no_ prefix if the cvar is 0)
```
:gameinfo:end
:join:<ID>:<slot>:<ip>:<nickname>
:join:<ID>:<slot>:bot:<nickname>
:name:<ID>:<nickname>
:part:<ID>
:team:<ID>:<team>:<jointype>
:chat:<ID>:<message>
:chat_spec:<ID>:<message>
:kill:frag:<ID of killer>:<ID of victim>:type=<death type>:items=<itemstring of killer>:victimitems=<itemstring of victim>
:kill:tk:<ID of killer>:<ID of victim>:type=<death type>:items=<itemstring of killer>:victimitems=<itemstring of victim>
:kill:suicide:<ID>:<ID>:type=<death type>:items=<itemstring>
:kill:accident:<ID>:<ID>:type=<death type>:items=<itemstring>
:ctf:steal:<flagcolor>:<ID of attacker>
:ctf:dropped:<flagcolor>:<ID of dropper>
:ctf:pickup:<flagcolor>:<ID of attacker>
:ctf:capture:<flagcolor>:<ID of attacker>
:ctf:return:<flagcolor>:<ID of defender>
:ctf:returned:<flagcolor>
:dom:taken:<previouscolor>:<ID of player>
:keyhunt:capture:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:carrierfrag:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:collect:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:destroyed:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:destroyed_holdingkey:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:dropkey:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:losekey:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:push:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:keyhunt:pushed:<ID of player>:<points for player>:<ID of key owner>:<points for key owner>:<name of key>
:scores:<gametype>_<mapname>:<map runtime>
:labels:player:<head1><flags>,<head2><flags>,...
:player:see-labels:<score1>,<score2>,...:<playtime>:<team>:<ID>:<nickname>
:player:see-labels:<score1>,<score2>,...:<playtime>:spectator:<ID>:<nickname>
:labels:teamscores:<head1><flags>,<head2><flags>,...
:teamscores:see-labels:<score1>,<score2>,...:<team>
:end
:restart
:gameover
:vote:suggested:<mapname>:<playerid>
:vote:keeptwo:<mapname>:<mapvotes>:<mapname>:<mapvotes>:::<mapname>:<mapvotes>:...:didn't vote:<notvoters>
:vote:finished:<mapname>:<mapvotes>:::<mapname>:<mapvotes>:<mapname>:<mapvotes>:...:didn't vote:<notvoters>
:vote:suggestion_accepted:<mapname>
:vote:vcall:<ID of player>:<vote command display string>
:vote:vyes:<yescount>:<nocount>:<abstaincount>:<notvoters>:<mincount>
:vote:vno:<yescount>:<nocount>:<abstaincount>:<notvoters>:<mincount>
:vote:vtimeout:<yescount>:<nocount>:<abstaincount>:<notvoters>:<mincount>
:vote:vstop:<ID of stopper>
:vote:vlogin:<ID of player>
:vote:vdo:<ID of player>:<do command display string>
:time:<YYYY-MM-DD HH:MM:SS>
:recordset:<ID of player>:<time in seconds>
```
Note that only the :join and :player lines ever contain player names. The :time event only appears in the log files if sv_eventlog_files_timestamps is 1; there is no way to log these time stamps to the console (for console timestamps, set timestamps to 1).

### Team colors
* 1 = No Team (Domination)
* 5 = Red Team
* 14 = Blue Team
* 13 = Yellow Team
* 10 = Pink Team

### Join types
* 1 = connect
* 2 = auto
* 3 = manual
* 4 = spectating
* 6 = adminmove

### Label flags
* !! = primary sorting key
* <!! = primary sorting key, lower is better
* ! = secondary sorting key
* <! = secondary sorting key, lower is better
* < = lower is better

### Item string
`<weaponid><flags>` or `<weaponid><flags>|<buffs>`

where flags can contain:
* F = player carries the flag
* S = player has strength
* I = player has the shield
* T = player is typing (console, menu or chat)
   
and weapon IDs are:
* 1 = Blaster
* 2 = Shotgun
* 3 = Machine Gun
* 4 = Mortar
* 5 = Electro
* 6 = Crylink
* 7 = Vortex
* 8 = Hagar
* 9 = Rocket Launcher
* 10 = Port-O-Launch
* 11 = Vaporizer
* 12 = Grappling Hook
* 13 = Heavy Laser Assault Cannon
* 14 = T.A.G. Seeker

Weapon IDs are below 10000.

### Death type
either a weapon ID ORed with weapon death flags, or one of the notifications in common/deathtypes.qh in the form of a string.

weapon death flags are:
* 256 = secondary fire
* 512 = splash damage
* 1024 = bounced projectile
* 2048 = head shot (Vaporizer only)
* 4096 = unused flag

There will be a log analyzer parsing this file format soon.