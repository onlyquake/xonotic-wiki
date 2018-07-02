## CVars (see xonotic.org/tools/cacs for more up-to-date information):

* `sv_logscores_console`: print scores to serverconsole after each match (set to 1 to enable)
* `sv_logscores_file`: print scores to a file after each match 
* `sv_logscores_filename`: filename of the output file if sv_logscores_file is enabled (the file will be stored in Xonotic/data/data or ~/.xonotic/data/data)
* `sv_logscores_bots`:choose whether bot are included in stats or not


## Commands

* `printstats`: print current scores to file/console (requires sv_logscores_console and/or sv_logscores_file to be enabled)


## Log format

example:
```   
:scores:dm_nexdm01:131
:player:1:7:129:1:GrooveMachine
:player:1:4:129:1:DanceWithMe
:player:10:1:130:3:Player
:end
```   
start of a new section:	`:scores:<gametype>_<mapname>:<map runtime>` (if the dump was triggered by "printstats", the line starts with :status:)

player entry: `:player:<frags>:<deaths>:<playtime>:<team>:<nickname>` (playername might contain ":", so be sure your parser doesn't split them, playtime is messured in seconds)

section end: `:end`

Team colors:
* Red Team	=  5
* Blue Team	= 14
* Yellow Team	= 13
* Pink Team	= 10

Other team numbers may appear in free for all games.

For an example parser (written in php, thanks to tChr) have a look at http://excalibur.nvg.ntnu.no/nexuiz/statsparser