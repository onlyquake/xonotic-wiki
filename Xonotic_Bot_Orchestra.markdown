Xonotic Bot Orchestra
=====================

This page explains how to create your very own Bot Orchestra performance.

In case you want to watch existing Bot Orchestra performances, visit http://www.youtube.com/user/XonoticBotOrchestra

Note: stuff in *italics* is up to you and may/will need changing from my examples here.

Mapping a Bot Orchestra Stage
-----------------------------

To do a bot orchestra performance, a “stage” map for the orchestra is required. It needs the following entities, if you use the default midi2cfg-ng.conf:

-   a target\_position called tVocals for the vocalist
-   a target\_position called tPercussion which is where the bots will aim. It’s a good idea to have a noimpact surface behind it so shots don’t make a noise on their impact.
-   32 target\_position entities called tUba1 to tUba32 for where bots with tubas/accordeons should walk to start their performance
-   32 target position entities called tChr1 to tChr32 for where percussion bots should walk to start their performance. They will then aim at tPercussion. These targets must not be on a nosteps or metalsteps surface!
-   3 target\_position entities called tMetalSteps1 to tMetalSteps3 for bots to jump on for metal step sounds
-   4 target\_position entities called tNoSteps1 to tNoSteps4 for jetpack bots so they don’t make an unwanted landing sound
-   info\_player\_deathmatch spawnpoints with “restriction” “1” for where bots are to spawn
-   info\_player\_deathmatch spawnpoints with “restriction” “2” for where humans are to spawn
-   you probably want to make it so the tUba bots can’t leave their area using various means; see the opera map for a quite safe approach involving a “shootable” trigger, but you could also make a pit you can fall into but not get out, or a teleport, or similar tricks to keep them enclosed.
-   also you may want to look at opera’s mapinfo settings: it sets *independent\_players 1 and bot\_navigation\_ignoreplayers 1 to help bot navigation. If you can get it to work without these hacks, it’d be better though.
    In the following example, we will use the map*opera\_ by Morphed for the orchestra. You can find it in the branch *divVerent/opera-by-morphed*.

Creating a bot script
---------------------

To create a bot script, first you need to prepare a MIDI file, for which you need to take care of:

-   percussion must be on track 10 only; percussion was mapped manually by me in midi2cfg-ng.conf by “similar sound”; you may want to read that file for reference so you can assign percussion instruments the way you want
-   program change event for Accordeon, Harmonica and Tango Accordeon uses the `!#%'n Accordeons
    * anything else uses the `!\#%’n Tuba

Then, you run in misc/tools/ of Xonotic:

perl midi2cfg-ng.pl midi2cfg-ng.conf *MIDIFILE.mid* *transpose* \> *\~/.xonotic/data/x.cfg*

(you also can use any other .cfg name here, but it must be in the same directory as config.cfg and I prefer x.cfg because the unmodified tuba-play.cfg uses it)

In case not all notes could be played, information is printed to help you choose the *transpose* parameter. You should try 0 at first.

Vocals
------

In order to play vocals, you need to put an additional file *MIDIFILE.mid.vocals* next to your MIDI file. An example vocals file:

scale 0.5
18240 sound/ikamusume-op/01-shinryaku.ogg
65142 sound/ikamusume-op/02-kirakira.ogg
72868 sound/ikamusume-op/03-kagayaku.ogg
80594 sound/ikamusume-op/04-minna-de.ogg
87629 sound/ikamusume-op/05-hajimemashou.ogg
91392 sound/ikamusume-op/05-hajimemashou.ogg
95831 sound/ikamusume-op/06-horahora.ogg
103465 sound/ikamusume-op/07-wagamama.ogg
111191 sound/ikamusume-op/08-ochitari.ogg
118426 sound/ikamusume-op/09-ikan-deshou.ogg
122312 sound/ikamusume-op/09-ikan-deshou.ogg
126505 sound/ikamusume-op/10-honto.ogg
134216 sound/ikamusume-op/11-yasashii.ogg
142034 sound/ikamusume-op/12-motteru.ogg
149253 sound/ikamusume-op/13-anata.ogg
157440 sound/ikamusume-op/14-hitoribocchi.ogg
164936 sound/ikamusume-op/15-umi-no.ogg
172800 sound/ikamusume-op/16-ichigen.ogg
176548 sound/ikamusume-op/17-kigen-mo.ogg
180311 sound/ikamusume-op/18-shiawase.ogg
184228 sound/ikamusume-op/19-mamorimasu.ogg
191770 sound/ikamusume-op/20.ogg
195840 sound/ikamusume-op/21-iikanji.ogg
203520 sound/ikamusume-op/22-iikanji.ogg
211200 sound/ikamusume-op/23-higashi.ogg
218880 sound/ikamusume-op/24-otakara.ogg
226560 sound/ikamusume-op/25-iikanji.ogg
234240 sound/ikamusume-op/26-iikanji.ogg
241920 sound/ikamusume-op/27-tanjouseki.ogg
249600 sound/ikamusume-op/28-konomama.ogg
257111 sound/ikamusume-op/29-shinryaku.ogg
264791 sound/ikamusume-op/30-keikaku.ogg
272548 sound/ikamusume-op/31-shinryaku.ogg

The numbers are measured in MIDI ticks, but are multiplied by the scale. I made this file by first using audio files inside Rosegarden and positioning them right, and then getting the numbers out of the compressed XML Rosegarden writes as its own file format. Another idea to get these numbers may be the event list editor in your MIDI app.

Performing
----------

To perform, copy the files tuba-play.cfg, tuba-record.cfg and tuba-settings.cfg to your Xonotic config directory (\~/.xonotic/data/ on Linux) and edit them to your taste. Then:

./all run *exec tuba-play.cfg*map *opera*

The performance will soon begin, and your task is to move the camera appropriately for a good recording!

Recording
---------

To make a video, you first run a performance as above, and then find out the file name of the .dem file in your Xonotic demo directory (\~/.xonotic/data/demos/ on Linux). Then you do:

./all run *exec input-demoseeking.cfg*exec tuba-record.cfg ~~demo *demos/demofilename.dem*
You can use the keys m,.~~ for seeking, where , and . go backwards and forwards by a small step, and m and - seek by a large step. Press x to start/stop video capture.

Enjoy!
