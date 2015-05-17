Demo Camera
===========

The demo camera allows you to customize camera position and angles during demo playback. It was designed mainly for video recording, not for spectating complete matches although maybe you can use it for this purpose depending on the map.

Note that depending on server configuration you might not see all players all the time in your demos, this is due to the anti-wallhack feature that works by not sending to you information about players you can’t see.

Currently most camera options can be configured only using the console or config files. For more information about advanced configuration you can see Chapter 2 and Chapter 4 of the great [Nexuiz In Depth](http://www.youtube.com/user/NexuizInDepth) series by Green Marine. Also probably you will want to associate some camera commands to keyboard keys or mouse buttons, see this link for more information.

Basic usage
-----------

### Enable camera

This camera is available only during demo playback, to enable it you have to set the following variable (cvar)

    camera_enable 1

Instantly you will be able to look anywhere and change the camera position using standar movement keys. Use 0 instead of 1 to disable it :)

### Camera angles

Like I said before you can control vertical and horizontal angles using the mouse. To rotate the view you need to use the commands `+roll_right` and `+roll_left`. Probably you will want to bind them to keyboard keys with something like:

    bind LEFTARROW "+roll_left"
    bind RIGHTARROW "+roll_right"

### Camera position

Using standard movement keys you can move to right/left and forward/backward, also by default you can move up/down just looking up/down and moving forward/backward.
For moving up/down you can use +moveup and +movedown.

    bind UPARROW "+moveup"
    bind DOWNARROW "+moveDOWN"

### Camera modes

The camera has two modes: chase and free. By default the camera starts in chase mode, chaning the position according to player movements. To switch to free mode, where you can put the camera anywhere on the map, use:

    camera_free 1

Advanced usage
--------------

For more advanced configuration variables look for the prefix `camera_` in the advanced settings menu: Settings-\>Misc-\>Advanced Settings...

