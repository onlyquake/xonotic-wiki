Voices and sounds
=================

Each player model should have a .sounds file, named with the syntax `<name of model><format of mode>_0.sounds`. So for Ignis, the sound file would be `ignis.iqm_0.sounds`. This file will give a voice to the player model, allowing it to make noises and so on.

There are 32 lines in a .sounds file, which looks something like this:

    //TAG: insurrectionist
    //affirmative sound/player/carni-lycan/player/affirmative 0
    attack sound/player/insurrectionist/coms/attack 0
    //attacking sound/player/carni-lycan/player/attacking 0
    attackinfive sound/player/insurrectionist/coms/attackinfive 0
    coverme sound/player/insurrectionist/coms/coverme 0
    defend sound/player/insurrectionist/coms/defend 0
    //defending sound/player/carni-lycan/player/defending 0
    //droppedflag sound/player/carni-lycan/player/droppedflag 0
    //flagcarriertakingdamage sound/player/soldier/player/flagcarriertakingdamage 0
    freelance sound/player/insurrectionist/coms/freelance 2
    //getflag sound/player/soldier/player/getflag 0
    incoming sound/player/insurrectionist/coms/incoming 0
    meet sound/player/insurrectionist/coms/meet 0
    needhelp sound/player/insurrectionist/coms/needhelp 2
    //negative sound/player/carni-lycan/player/negative 0
    //onmyway sound/player/carni-lycan/player/onmyway 0
    //roaming sound/player/carni-lycan/player/roaming 0
    //seenenemy sound/player/carni-lycan/player/seenenemy 0
    seenflag sound/player/insurrectionist/coms/seenflag 0
    taunt sound/player/insurrectionist/coms/taunt 4
    teamshoot sound/player/insurrectionist/coms/teamshoot 3
    death sound/player/insurrectionist/player/death 3
    drown sound/player/insurrectionist/player/drown 0
    fall sound/player/insurrectionist/player/fall 0
    falling sound/player/insurrectionist/player/falling 0
    gasp sound/player/insurrectionist/player/gasp 0
    jump sound/player/insurrectionist/player/jump 0
    pain25 sound/player/insurrectionist/player/pain25 0
    pain50 sound/player/insurrectionist/player/pain50 0
    pain75 sound/player/insurrectionist/player/pain75 0
    pain100 sound/player/insurrectionist/player/pain100 0

The first line is not read by the game, it is simply for humans to tell which voice pack is being used in this file. There are, at the time of writing, 9 voice packs (carni-lycan, fricka, insurrectionist, marine, pyria-skadi, reptilian, soldier, specop, and torus).

For every line after that, the format is the same:

    <sound name> <sound path> <variations of sound>

Sound name is the name of the sound, as can be seen in the example .sounds file above. Sound path is the path to the sound file, relative to xonotic root. The last argument is the number of variations of the sound. For instance, insurrectionist has 3 teamshoot sound files, named `teamshoot1.ogg`, `teamshoot2.ogg`, and `teamshoot3.ogg`. This is why the last number in line 22 is a 3. However, insurrectionist has only one attack sound, `attack.ogg`, so the last number in line 3 is 0.

The `//` you see in certain lines means that the voice pack used in the file does not have those sounds. They are sort of like a comment - the game throws an error while parsing them, but it does not affect anything else.

Entries up to line 23 are voice entries, meaning that in a perfect world a player can evoke them using `cmd voice <name of voice>`, but few of them are supported in game code. Line 23 and onward are voices the player makes automatically, when falling, taking damage, fragging, and so on.

Unfortunately, these 9 voice packs only have a few sounds in common, as voice packs frequently lack certain voices. The easiest way to fix this problem would be to include new voice packs in xonotic, but this may not happen due to a lack of people with voices and microphones.

