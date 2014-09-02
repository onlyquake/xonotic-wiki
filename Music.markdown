Music
=====

{{\>toc}}

Requirements
------------

-   Vorbis OGG -q4 or above (-q7 or above preferred), or a format good enough for being able to be converted to that (e.g. FLAC, WAV)
-   GPL v2 compatible *\_
    \* About 3 to 10 minutes
    \* Preferably with matching ending and beginning*(so the track loops smoothly)\_

Music Style
-----------

### Overview

While we don’t want to tie us to a specific genre, the music must match the visuals of the game. As it is being discussed on [this thread](http://forums.xonotic.org/showthread.php?tid=81) seems that we are about to use a futuristic ambient for the game, so its more than likely that the kind of music that we want will fit within the Electronic genre.

### Track Duration

Currently most contributions come in the format of a regular CD track, that is 3, 4 or 5 minutes long. This is currently an issue because the duration of most matches is about 15-20 minutes, that means that one listens to the very same track many times in row, which is kind of boring. For this reason we would like to have longer tracks, as long as this is possible for artists. However tracks longer than 10 or 15 minutes are not advisable as that will increase dramatically the size of the release package. Note that this is a file size size constraint, not a duration one, tracks that are more easily compressed can have a longer duration.

### Matching start and ending

In spite of having longer tracks its more than likely that a track gets played at two or more times during a match, for this is important that the end and beginning of the track can be matched without disruptions, giving a sense of continuity.

For this the ideal way is to find a start and end sample index, so that that region is perfectly (clickless) loopable. These can be set as LOOP\_START and LOOP\_END tags in the Vorbis file, and the engine will seek back to LOOP\_START when reaching LOOP\_END.

### Complexity

As this game is extremely fast we don’t want to have overly complex tracks at the point of being distracting or that one can’t even understand while playing (e.g. a mad breakbeat tune)

### Variations

Furthermore this game is based a lot on listening, as a way to know if a shot hit or not, or if there is someone nearby picking up items, etc. For this reason we want to avoid abrupt variations in the volume of tracks and/or the abuse of very high pitched sounds.

### Suggested Genres

Electronica, Drum and Bass, House, Jungle, 8 bit, Fake bit, Techno, Hybrid, Ambient, Experimental

### Moods

-   Wanted
    -   Intense, Trippy, Energetic, Cerebral, Hypnotic, Playful, Ominous, Ambitious, Fast
-   Unwanted
    -   Dramatic, Complex, Clinical, Visceral

### Reference tracks

Following tracks could be taken as a reference of the style that we want

[Forgotten Tides](http://www.jamendo.com/en/track/145959)
[Foregone Destruction](http://www.youtube.com/watch?v=yNrI6N2jQCk&feature=related)
[Skyward Fire](http://www.youtube.com/watch?v=2bFUNKg0mzg&feature=related)
[Botpack 9](http://www.youtube.com/watch?v=6gwdsQDwAb8&feature=related)
[Stairs](http://blkrbt.googlepages.com/stairs.ogg)
[Rabble Rouser](http://www.youtube.com/watch?v=ki71pm8yDKI&hd=1)

Links
-----

-   Licensing
    -   Our [Legal][] wiki page
    -   http://wiki.creativecommons.org/GarageBand
-   Tools
    -   OpenMPT http://www.lpchip.com/modplug
    -   LMMS http://www.lmms.sourceforge.net
    -   Ardour http://www.ardour.org
    -   Rosegarden http://www.rosegardenmusic.com/
    -   http://linux-sound.org/
-   Sound banks
    -   [The Free Sound Project](http://www.freesound.org/tagsViewSingle.php?id=99)
    -   http://ccmixter.org/
    -   http://freepats.zenvoid.org/olpc-sounds/
        -   http://lopho.org/xonotic/olpc\_sound\_samples\_v2.torrent

How-To’s
--------

**How to add a sound track to Xonotic?**

-   Copy the track file to the *data/sound/cdtracks* folder
-   Add the name of the track (without the extension) at the end of the cvar *g\_cdtracks\_remaplist*, on the file *defaultXonotic.cfg*. Count all tracks and remember the position of the added one, this information will be used on the following step.
-   Open the file <name of map>.mapinfo (*on data/xonotic-maps.pk3dir/maps*) and add a line with the text “cd loop x”. This x should be the position of the track within the cvar *g\_cdtracks\_remaplist*.

**How to add a sound track to a non official map?**

-   Copy the track to the folder *sound/cdtracks/* (inside the pk3 file)
-   Open the file *<name of map>.mapinfo* and add a line with the text “cd loop <track filename>”

