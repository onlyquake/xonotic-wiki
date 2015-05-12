Capturing video clips
=====================

Capturing video clips in Xonotic is easy, and does not need any external tools such as screen capturing software. You can choose to capture with either the (lossy) Ogg Theora codec or alternatively to an uncompressed avi file. Beware that capturing while playing is a bad idea, as this will result in very choppy video. Always record a demo of what you are going to capture before rendering it to a video file. Enabling auto recording of demos is a good idea, which can be done via the menu (Media -> Demos -> [X] Auto record demos). Playing them back can be done from the same menu.

cl\_capturevideo
----------------

To capture a demo to a video clip you first start playing the demo and toggle the `cl_capturevideo` cvar. When it’s on (1), the engine will start capturing screen frames and save them as either ogg or avi. The engine will slow down the demo enough to be able to capture all frames, which it can’t do if you are recording while playing. Toggling the cvar to 0 will stop recording.

To work around the problem of a visible console in the beginning and end of a recording, you will have to bind `cl_capturevideo` to a key as follows:

    bind x "toggle cl_capturevideo"

where x can be any key (any letter or number (0-9), pgup, pgdn, alt etc.)
Note that the ‘toggle’ command simply toggles the value of `cl_capturevideo`. This means that recording starts the first time you hit the key and stops when you hit it again.

To switch between Ogg Theora and avi, use one of the following commands:

    // enable encoding to ogg theora
    cl_capturevideo_ogg 1

    // use uncompressed avi instead (beware of huge files!)
    cl_capturevideo_ogg 0

Other useful cvars:
-------------------

    // increase the framerate of the captured clip (eg. to 60)
    cl_capturevideo_fps 60

    // quality setting for ogg theora (video if recording to ogg, eg. 32 (default))
    cl_capturevideo_ogg_theora_quality 32

    // quality setting for ogg vorbis (audio if recording to ogg, eg. 3 (default))
    cl_capturevideo_ogg_vorbis_quality 3

Fast forwarding
---------------

To fast forward, play a demo and type eg. “slowmo 50” into the console to fast forward 50 times faster. Set slowmo back to 1 when you want to start recording to return to normal speed. As of yet there’s unfortunately no way to rewind other than restarting the demo, which kind of sucks (!). Hope that’ll be fixed in the future…

Using the demo camera
=====================

The demo camera can be enabled with

    camera_enable 1

It will by default follow the player and let you move the camera around. When the camera is disabled (default), the player's 1st person view is shown.

Camera modes
------------

### Chase mode (default)

* Can be enabled with: `camera_free 0`
* Allows you to chase the player, and by default rotate and move the camera freely
* You can smooth out the camera path with: `camera_chase_smoothly`
* You can have the camera aim at the player with: `camera_look_player`

### Free fly mode

* Can be enabled with: `camera_free 1`
* Allows you to move and rotate the camera freely, and does not follow the player
* You can have the camera aim at the player with: `camera_look_player`

Changing speeds
---------------

* Change the treshold for ignoring small mouse movements: `camera_mouse_treshold`
* Change the camera rotation AND camera movement attenuation (why are these both in one cvar?): `camera_speed_attenuation`
* Change the camera movement speed in chase mode: `camera_speed_chase`, and free mode: `camera_speed_free`
* Change camera roll speed: `camera_speed_roll`

The camera can be moved with the same keys as you move with in the game, as well as `+moveup`, `+movedown`, `+roll_left` and `+roll_right`. These keys can be bound to a key as follows (eg):

    bind x +moveup

To reset the camera, use:

    toggle camera_reset

(to mand1nga: why is this a cvar, not a command?)

You can get a list of all camera cvars and their descriptions by typing `camera_` into the console and then hitting tab. You’ll also see the current value as well as the default value inside brackets, so don’t be shy to fiddle around with them :)

Advanced capturing
==================

There are a couple of tricks which you can do to eg. change shooting angle of the camera and hide HUD elements.

Changing shooting angles
------------------------

To change the angles of the camera you’ll have to create many video clips which you later have to merge in a video editor, but luckily you don’t need to restart the demo for each angle. Instead you could use some simple scripting to “pause” the demo exactly at the moment you stop recording a clip. (and vice-versa)
The console commands to accomplish this look something like this:

    bind x "slowmo 0;cl_capturevideo 0"
    bind y "cl_capturevideo 1;slowmo 1"

This’ll make the x key stop recording as well as pause the demo, giving you time to set up the next shooting angle and settings for the camera. The y key will start recording and immediately unpause.
Don’t forget you can put all commands and cvars into an autoexec.cfg file (which you might have to create!) in your data/ directory. Then they will be set at each startup of Xonotic, you can simply copy & paste them from here and don’t need to type them in manually each time.

Hiding HUD elements
-------------------

* `r_letterbox –1` hides most HUD elements, including the kill messages.
* If you instead only want to hide the HUD, use `viewsize 120` (100 is default)
* To hide the weapon, use `r_drawviewmodel 0`
* To hide the crosshair, use `crosshair 0`
* To hide waypointsprites, use `cl_hidewaypoints 1`

