DarkPlaces Wiki
===============

QuakeC Extensions
=================

QuakeC Extensions are a method for mod developers to detect the presence of particular engine features, as their mods may be run on a wide range of Quake engines.
Below is a list of all the extensions supported by Darkplaces.

**!!TODO!!** Organize into groups (ie. GFX, QuakeC, Server, Network) and start filling in description pages. use the checkextension page as a base.

-   [No extension yet](#lost-link)
-   [Left out Quake definitions](#lost-link)
-   [checkextension builtin](#lost-link)

Graphics Extensions
-------------------

    BX_WAL_SUPPORT

Indicates the engine supports .wal textures for filenames in the textures/ directory

    DP_EF_ADDITIVE

Additive blending when this object is rendered

    DP_EF_BLUE

Entity emits blue light (used for quad)

    DP_EF_DOUBLESIDED

Render entity as double sided (backfaces are visible, I.E. you see the 'interior' of the model, rather than just the front), can be occasionally useful on transparent stuff.

    DP_EF_FLAME

Entity is on fire

    DP_EF_FULLBRIGHT

Entity is always brightly lit

    DP_EF_NODEPTHTEST

Makes entity show up to client even through walls, useful with EF_ADDITIVE for special indicators like where team bases are in a map, so that people don't get lost

    DP_EF_NODRAW

Prevents server from sending entity to client (forced invisible, even if it would have been a light source or other such things)

    DP_EF_NOGUNBOB

Prevents gun bobbing on player.viewmodel

    DP_EF_NOSHADOW

Realtime lights will not cast shadows from this entity (but can still illuminate it)

    DP_EF_RED

Entity emits red light (used for invulnerability)

    DP_EF_RESTARTANIM_BIT

When toggled, the current animation is restarted. Useful for weapon animation.

    DP_EF_STARDUST

Entity emits bouncing sparkles in every direction

    DP_EF_TELEPORT_BIT

When toggled, interpolation of the entity is skipped for one frame. Useful for teleporting.



    DP_GFX_EXTERNALTEXTURES

loads external textures found in various directories (tenebrae compatible)

    DP_GFX_EXTERNALTEXTURES_PERMAPTEXTURES

Q1BSP and HLBSP map loading loads external textures found in textures/<mapname>/ as well as textures/.

    DP_GFX_FOG

Global fog for the map, can not be changed by QC

    DP_GFX_QUAKE3MODELTAGS

Allows entities to be visually attached to model tags (which follow animations perfectly)

    DP_GFX_SKINFILES

Alias models (mdl, md2, md3) can have .skin files to replace conventional texture naming

    DP_GFX_SKYBOX


    DP_TE_BLOOD
    DP_TE_BLOODSHOWER
    DP_TE_CUSTOMFLASH
    DP_TE_EXPLOSIONRGB
    DP_TE_FLAMEJET
    DP_TE_PARTICLECUBE
    DP_TE_PARTICLERAIN
    DP_TE_PARTICLESNOW
    DP_TE_PLASMABURN
    DP_TE_QUADEFFECTS1
    DP_TE_SMALLFLASH
    DP_TE_SPARK


    DP_QUAKE2_MODEL
    DP_QUAKE2_SPRITE
    DP_QUAKE3_MAP
    DP_QUAKE3_MODEL


    DP_HALFLIFE_MAP
    DP_HALFLIFE_MAP_CVAR
    DP_HALFLIFE_SPRITE


    DP_ENT_ALPHA
    DP_ENT_COLORMOD
    DP_ENT_CUSTOMCOLORMAP
    DP_ENT_EXTERIORMODELTOCLIENT
    DP_ENT_GLOW
    DP_ENT_GLOWMOD
    DP_ENT_LOWPRECISION
    DP_ENT_SCALE
    DP_ENT_VIEWMODEL


    TENEBRAE_GFX_DLIGHTS
    NXQ_GFX_LETTERBOX

QuakeC Extensions
-----------------

    DP_QC_ASINACOSATANATAN2TAN
    DP_QC_AUTOCVARS
    DP_QC_CHANGEPITCH
    DP_QC_COPYENTITY
    DP_QC_CVAR_DEFSTRING
    DP_QC_CVAR_DESCRIPTION
    DP_QC_CVAR_STRING
    DP_QC_CVAR_TYPE
    DP_QC_EDICT_NUM
    DP_QC_ENTITYDATA
    DP_QC_ENTITYSTRING
    DP_QC_ETOS
    DP_QC_EXTRESPONSEPACKET
    DP_QC_FINDCHAIN
    DP_QC_FINDCHAIN_TOFIELD
    DP_QC_FINDCHAINFLAGS
    DP_QC_FINDCHAINFLOAT
    DP_QC_FINDFLAGS
    DP_QC_FINDFLOAT
    DP_QC_FS_SEARCH
    DP_QC_GETLIGHT
    DP_QC_GETSURFACE
    DP_QC_GETSURFACEPOINTATTRIBUTE
    DP_QC_GETSURFACETRIANGLE
    DP_QC_GETTAGINFO
    DP_QC_GETTAGINFO_BONEPROPERTIES
    DP_QC_GETTIME
    DP_QC_GETTIME_CDTRACK
    DP_QC_LOG
    DP_QC_MINMAXBOUND
    DP_QC_NUM_FOR_EDICT
    DP_QC_RANDOMVEC
    DP_QC_SINCOSSQRTPOW
    DP_QC_SPRINTF
    DP_QC_STRFTIME
    DP_QC_STRINGCOLORFUNCTIONS
    DP_QC_STRING_CASE_FUNCTIONS
    DP_QC_TOKENIZEBYSEPARATOR
    DP_QC_TOKENIZE_CONSOLE
    DP_QC_TRACEBOX
    DP_QC_TRACETOSS
    DP_QC_TRACE_MOVETYPE_HITMODEL
    DP_QC_TRACE_MOVETYPE_WORLDONLY
    DP_QC_UNLIMITEDTEMPSTRINGS
    DP_QC_VECTOANGLES_WITH_ROLL
    DP_QC_VECTORVECTORS
    DP_QC_WHICHPACK
    DP_QC_URI_ESCAPE
    DP_QC_URI_GET

Unsorted
--------

    DP_BUTTONCHAT
    DP_BUTTONUSE
    DP_CL_LOADSKY
    DP_CON_SET
    DP_CON_SETA
    DP_CON_ALIASPARAMETERS
    DP_EXPANDCVAR
    DP_CON_STARTMAP


    DP_GECKO_SUPPORT


    DP_INPUTBUTTONS
    DP_LIGHTSTYLE_STATICVALUE
    DP_LITSPRITES
    DP_LITSUPPORT
    DP_MONSTERWALK
    DP_MOVETYPEBOUNCEMISSILE
    DP_NULL_MODEL
    DP_MOVETYPEFOLLOW

    DP_SKELETONOBJECTS
    DP_SV_SPAWNFUNC_PREFIX
    DP_REGISTERCVAR
    DP_SND_DIRECTIONLESSATTNNONE
    DP_SND_FAKETRACKS
    DP_SND_OGGVORBIS
    DP_SND_STEREOWAV
    DP_SOLIDCORPSE
    DP_SPRITE32
    DP_SV_BOTCLIENT
    DP_SV_BOUNCEFACTOR
    DP_SV_CLIENTCOLORS
    DP_SV_CLIENTNAME
    DP_SV_CUSTOMIZEENTITYFORCLIENT
    DP_SV_DRAWONLYTOCLIENT
    DP_SV_DROPCLIENT
    DP_SV_EFFECT
    DP_SV_ENTITYCONTENTSTRANSITION
    DP_SV_MOVETYPESTEP_LANDEVENT
    DP_SV_POINTSOUND
    DP_SV_ONENTITYNOSPAWNFUNCTION
    DP_SV_ONENTITYPREPOSTSPAWNFUNCTION
    DP_SV_MODELFLAGS_AS_EFFECTS
    DP_SV_NETADDRESS
    DP_SV_NODRAWTOCLIENT
    DP_SV_PING
    DP_SV_PING_PACKETLOSS
    DP_SV_POINTPARTICLES
    DP_SV_PUNCHVECTOR
    DP_SV_PLAYERPHYSICS
    DP_SV_PRINT
    DP_SV_PRECACHE_ANYTIME
    DP_SV_QCSTATUS
    DP_SV_ROTATINGBMODEL
    DP_SV_SETCOLOR
    DP_SV_SLOWMO
    DP_SV_WRITEPICTURE
    DP_SV_WRITEUNTERMINATEDSTRING
    DP_TE_STANDARDEFFECTBUILTINS
    DP_TRACE_HITCONTENTSMASK_SURFACEINFO
    DP_VIEWZOOM
    EXT_BITSHIFT
    FRIK_FILE
    FTE_CSQC_SKELETONOBJECTS
    KRIMZON_SV_PARSECLIENTCOMMAND
    NEH_CMD_PLAY2
    NEH_RESTOREGAME
    NEXUIZ_PLAYERMODEL
    PRYDON_CLIENTCURSOR
    TW_SV_STEPCONTROL
    FTE_QC_CHECKPVS
    FTE_STRINGS
    DP_CON_BESTWEAPON
    DP_QC_STRINGBUFFERS
    DP_QC_STRINGBUFFERS_CVARLIST
    DP_QC_STRREPLACE
    DP_QC_CRC16
    DP_SV_SHUTDOWN
    EXT_CSQC
    ZQ_PAUSE

    DP_PHYSICS
