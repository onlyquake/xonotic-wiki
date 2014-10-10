Lighting
========

In netradiant, there are two kinds of lights, real time lights (which must be added in-game) and radiosity-based lights (which are added in radiant). This article will deal with both.

Real time lights (rtlights)
---------------------------

Real time lights are added and modified using the following console commands, accessible in-game using r\_editlights\_help.

|Command|Function|
|-------|--------|
|=.Settings|
|r\_editlights|enable/disable editing mode|
|r\_editlights\_cursordistance|maximum distance of cursor from eye|
|r\_editlights\_cursorpushback|push back cursor this far from surface|
|r\_editlights\_cursorpushoff|push cursor off surface this far|
|r\_editlights\_cursorgrid|snap cursor to grid of this size|
|r\_editlights\_quakelightsizescale|imported quake light entity size scaling|
|=.Commands|
|r\_editlights\_help|this help|
|r\_editlights\_clear|remove all lights|
|r\_editlights\_reload|reload .rtlights, .lights file, or entities|
|r\_editlights\_save|save to .rtlights file|
|r\_editlights\_spawn|create a light with default settings|
|r\_editlights\_edit command|edit selected light - more documentation below|
|r\_editlights\_remove|remove selected light|
|r\_editlights\_toggleshadow|toggles on/off selected light's shadow property|
|r\_editlights\_importlightentitiesfrommap|reload light entities|
|r\_editlights\_importlightsfile|reload .light file (produced by hlight)|
|=.Edit commands (given as arguments to r\_editlights\_edit|
|origin x y z|set light location|
|originx x|set x component of light location|
|originy y|set y component of light location|
|originz z|set z component of light location|
|move x y z|adjust light location|
|movex x|adjust x component of light location|
|movey y|adjust y component of light location|
|movez z|adjust z component of light location|
|angles x y z|set light angles|
|anglesx x|set x component of light angles|
|anglesy y|set y component of light angles|
|anglesz z|set z component of light angles|
|color r g b|set color of light (can be brighter than 1 1 1)|
|radius radius|set radius (size) of light|
|colorscale grey|multiply color of light (1 does nothing)|
|colorscale r g b|multiply color of light (1 1 1 does nothing)|
|radiusscale scale|multiply radius (size) of light (1 does nothing)|
|sizescale scale|multiply radius (size) of light (1 does nothing)|
|style style|set lightstyle of light (flickering patterns, switches, etc)|
|cubemap basename|set filter cubemap of light (not yet supported)|
|shadows 1/0|turn on/off shadows|
|corona n|set corona intensity|
|coronasize n|set corona size (0-1)|
|ambient n|set ambient intensity (0-1)|
|diffuse n|set diffuse intensity (0-1)|
|specular n|set specular intensity (0-1)|
|normalmode 1/0|turn on/off rendering of this light in rtworld 0 mode|
|realtimemode 1/0|turn on/off rendering of this light in rtworld 1 mode|
|<nothing>|print light properties to console|

The most important commands to remember are r\_editlights, r\_editlights\_edit (color, realtimemode and radius arguments), and of course, r\_editlights\_save. You will not see your light and its effects in real time if you do not execute r\_editlights\_realtimemode 1 while having selected the light.

It is important to note that rtlights can put a serious drain on computers due to the way they work, and they should be used sparingly (don't make an rtlight on every radiosity light, generally). However, they can easily be disabled from the client-side if a user's machine cannot handle them.

Radiosity lights
----------------
