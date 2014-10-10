HowTo: WarpZones
================

Create a brush, resize it and move it to where you want the first warpzone. You must leave some space in the wall behind the warp surface so that there would be space for about two player bounding boxes, and you must resize the warpzone brush to cover all of this space!

When done with all that, select the warpzone brush, right click and select trigger\_warpzone. Select the brush again, press T, find the common/trigger texture and use it on all surfaces. Unselect the brush by hitting ESC, select your warp surface in the 3d view by pressing CTRL+SHIFT+Left mouse button. Then use the common/warpzone texture on this one surface only!

Now clone the warpzone by selecting it, then hitting CTRL+C and CTRL+V. Move the second warpzone to where you want it, but don’t resize! (only move/rotate). Same story here about the space behind the warp surface.

Now unselect everything with ESC, select both warpzones and hit CTRL+K to connect them. Now there should be a line between them indicating they are connected, there’s your warpzone! :).
