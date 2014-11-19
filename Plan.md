Organization
============

{{\>toc}}

-   3-6 leaders at the top
    -   board or committee of community members who act as liaisons between developers, players, leaders and other communities to help make sure the most important information is getting to the leaders
-   “big” decisions (like whole new gameplay balance) should be approved by ALL leaders, who stand personally for the community
-   nobody will be able AT ALL to sell/relicense the project :P

> <div0> as for organization, I suggest:
> <div0> - three “leaders” who should come from different backgrounds
> <div0> - otherwise, freedom should reign among the community
> <div0> - “big” decisions (like whole new gameplay balance) should be approved by ALL leaders, who stand personally for the community
> <div0> - small stuff can be decided by the community directly (e.g. by just performing a change and committing)
> <div0> - nobody will be able AT ALL to sell/relicense the project :P
> <div0> but regarding game relevant decisions, you [dokujisan] probably will represent the competitive side, which is good, as that NEEDS to be represented
> <div0> and with interest groups, I mean “from the players”
> <div0> why do you play Nexuiz?
> <Dokujisan> it’s my replacement for martial arts heh
> <Dokujisan> I used to train in martial arts a lot. I don’t as much and nexuiz sorta took that spot.
> <div0> I mostly play for fun, and therefore like development of new stuff and experimenting… others play competitively, which of course prefers sticking to the roots
> <div0> (and requires stability in the “core game”)
> <div0> also, as a free project, leadership should not be exerted by force :P
> <div0> if someone wants a feature, and the leaders are against it, one should think about a way to get it in in a varied but better fashion
> <div0> code wise, I’d go so far - if the code is harmless (e.g. if it can be turned off), and mostly bug free, it can go in - even if I don’t like what it brings
> <div0> art wise it’s a bit more difficult, as there can be many opinions what is good and what is not
> <div0> there, I’d only like to avoid bad taste (like, pr0n, or TOO strong displays of violence - after all, the game is meant to be PLAYed, and is not a virtual torture chamber)
> <div0> of course, the competitive players ALSO do not want overly strong violence, as it blocks the view :P

Code Clean-up
=============

> <div0> but basically, the goal should NOT be stripping the game to “what I like”
> <div0> and also NOT reimplementing it
> <div0> but JUST reorganizing the code
> <div0> not silently removing stuff
> <div0> what NEEDS cleanup, is teamplay.qc, player death handling, player spawn handling, player think
> <div0> anyway, as for rerwrite… shpuld be no goal for next release

Documentation
=============

Can we start using http://www.methods.co.nz/asciidoc/ for documentation?

Maps
====

-   aggressor,
-   aggressor\_ctf (with fixes and testing) — possible expand? it’s currently only good for \~2v2-3v3
-   courtfun? (shameless plug from me, SavageX). Reuses some content for desertfactory.
-   dance? (with some fixes)
-   desertfactory
-   eggandbacon (makeover)
-   egyptronex? (with some fixes?) (maybe make hydronexb4 prettier?)
-   final\_rage
-   gasolinepowered (makeover in progress)
-   greatwall\_whatever?
-   Hotgrounds (needs some modelled cave-love)
-   killall\_organic (with gameplay fixes or some parts totally redone)
-   lavaflag? (makeover)
-   reslimed (replace textures, fix movement to not get stuck on things)
-   runningman (makeover)
-   silvercity\_reloaded (fix FPS?)
-   Stonecastle?
-   stormkeep2
-   strength (gameplay adjustments and a makeover)
-   treasure\_island? (with gameplay fixes)
-   Vociferous? (I’d happily finish the map asap)
-   Fortress resurrection? (needs finishing of lighting up)
-   cbctf1? (already under WIP)

Website
=======

We’re going to be incorporating features from all of the community sites into a proper “core” site.

Using WordPress MU as the main site, We can use MyBB as a forum system and bridge it to WordPress. Alternatively we can look into use BuddyPress and dropping a forum system.

-   News
-   Tournament system (likely need to be homegrown)
-   Clan management (likely need to be homegrown, maybe integrate with MU or BuddyPress somehow)
-   Proper WIKI (instead of OUNS) — is the dev wiki good enough or do we want a user based one as well?
-   Pic hosting like pics.nexuizninja.com — can be integrated into WordPress with nextgen gallery + nextgen public upload, I think we can fork this plugin to do more, i.e. video gallery, and more as well. Will need to dedicate resources to this
-   Realtime server list (should be easy to make a plugin for)
-   Mumble interface (will need to talk to dokujisan about details on this but should be easy enough to make a plugin for)
-   cvar/cmd list search
-   keyboard binds

Chat
====

An official Mumble server
Possibly using a different network other than Quakenet

> <Dokujisan> for my other project I’m involved with, Getty was showing me a way to have \#nexuiz on multiple networks and have them all connect to each other through a bot
> <Dokujisan> so we would have our own IRC network
> <Dokujisan> and \#battlecube channels on quakenet and other networks and they would all echo to/from our network
> <Dokujisan> there would be a bot that echos what is typed
> <Dokujisan> between the various networks

Gameplay Balance
================

> <FruitieX> div0: I would also vote for sv\_maxspeed 320 and sv\_maxairspeed 320
> <FruitieX> so to sum it all up: current physicsNoQWBunny.cfg + sv\_airaccel\_sideways\_friction ~~1 + sv\_maxspeed 320 + sv\_maxairspeed 320
> <FruitieX> tZork: that is a slightly different physics config that div0 has been working on
> <FruitieX> Dokujisan: more physics stuff to note that’s really fun: sv\_doublejump 1, sv\_jump\_speedcap\_max 1, sv\_jumpspeedcap\_max\_disable\_on\_ramps 1
> h1. Player Models
> http://www.alientrap.org/forum/viewtopic.php?f=2&t=6051
> http://www.alientrap.org/forum/viewtopic.php?f=2&t=5997
> http://alientrap.org/forum/viewtopic.php?p=69763\#p69763
> bq. <tZork> Dokujisan: Oblivion, Morphed, DibTop and me all knows a bit abt assorted sobjects arround it.
> <tZork> i managed to export animated smd’s from blender yesterday
> <tZork> and turn to dpm
> <tZork> Dokujisan: yes the artist toolchain of darkpalces is bad
> <Dokujisan> tZork: perhaps we need to generate some documentation on “what we know” about player model technical details
> <Spaceman> I second that idea
> <tZork> but with the blender smd thing working, its way more likely ppl can do open models.
> h1. Sounds
> http://www.nullgaming.com/stuff/tenshihan-nexuiz.v6.6.pk3.zip
> h1. Training and Teaching
> There will be two types of training servers
> ~~ Dojo: with a special Dojo map that walks players through the various basics and intermediate details of the game
> - Bootcamp: a special training server with a trainer where player can get direct individual or group instruction on intermediate to advanced skills

Before, when we did bootcamp, we had an IRC server with available trainers idling and a webchat interface for players to request a trainer.
div0 suggested that we can build this interaction into the game and the server screen can have allow players to “sign up” for a trainer on a bootcamp server

The Dojo servers would also be on the server choosing screen in an obvious place.

New Menu Skin
=============

http://www.alientrap.org/forum/viewtopic.php?f=2&t=5998

with some refining and get these sources files to ~~z~~ to remix for the website design

Style Direction
===============

> \<}-z-{\> regarding artwork, I think we should gather a list of wants/needs/likes/dislikes
> \<}-z-{\> to give other artists direction when they are looking to contribute

> <Oblivion> i woudl like to put forward a suggestion of basing nexuiz’ art on treating it as if it was a galactic sport.
> think Rollerball. With enough emphasis given on balance (no hard to see or hard to hit models) and bright colors
> (that can be adjusted per clan), possibly adding another color mask in addition to the shirt/pants divide?
> <Oblivion> for things like stripes or markings. so that even in team based games where colors are mandated
> (to be blue/red), the players will still have an option of being identifiable as distinct from his teammates
> <Oblivion> that way you will know who is who within the team
> <Oblivion> you can for example have two players with the same player model both on blue team, but you can tell
> one from the other because the first has a green diagonal stripe while the other has yellow, etc.
> <Oblivion> nothing that would confuse opposing teams of course
> <Oblivion> giving players a degree of control over how they look like in a standardized way can encourage clan building
> <Oblivion> also a bit more cyberpunk direction rather than aliens (which was never implemented properly). that
> means humans and bots, but all humanoid and of the same sizes. and a bit less serious. (i’m actually planning a
> player model with armor that deliberately looks like bunny ears)

> <Morphed_> i think that perfect style for nexuiz is this http://hirez.http.internapcdn.net/hirez/images/photos/downloads/GAWallpaper\_1440X1080.jpg

Forum discussion here: http://forums.xonotic.org/showthread.php?tid=81

Bullet Points
=============

1. structure for the “management” so there are like 3-6 leaders and not just one leader making “big” decisions for the game
2. some sort of committee setup underneath the leadership to make “most” decisions for the game
3. use of a central user auth system that protects privacy but also allows for extra features like stats
4. we’re picking a new set of maps to be included with the game….with some fixes and makeovers
5. new player models
7. the Xenotic website will include all of the features that should have been in the nexuiz.com website…. like all of the nexuizninjaz.com features
8. we will work on gameplay balance again, but this time with proper testing and feedback loop
9. there will be emphasis on organizing projects and recruiting people for work on these projects
10. we haven’t picked a final name yet, we’re going to take some time with this
11. there will be an effort for some clean-up of the game code
12. more frequent releases

Server resources
================

-   ~~z~~ VPS in Washington DC for test builds, and test server
-   ~~z~~ california shared hosting for development site
-   pavlvs VPS for wordpress MU / website / other services below
-   dokujisan/-z- can provide offical game servers (vps/dedicated) — can we get an EU for this too?
-   dokujisan/-z- shared hosting for release mirrors, other files, backups, etc
-   merlijn can add more servers if needed, FruitieX can admin the “Pro” servers he might be hosting (ex-nexrun)
-   git repository can be hosted by icculus
-   Aussienexers offer up all of their servers to whatever we need for that region
-   Samual offers his VPS as another possible server if needed

