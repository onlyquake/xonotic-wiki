Skyboxes (with blender)
=======================

In this tutorial we will make a very simple skybox for Xonotic
--------------------------------------------------------------

### Requirements

-   Xonotic (and a mapping setup (I use netradiant))
-   Blender (I will be using version 2.62, older versions may work)
-   gimp (I will be using 2.6, older versions may work)
-   a text editor (I'll be using kate)

### Intro

This is what we will make...

![](start-shot.jpg)

Its actually not that hard to do, so lets get started

### Step 1 - open blender

Lets get started.
The first thing you will need is blender, so open it up and delete the default cube, camera, and light.
![](blender-open.jpg)

### Step 2 - Make the ground

We are going to make the ground using a large plane. So hit [shift] + [a] to bring up the add menu, and add a plane.
![](blender-add-plane.jpg)

![](blender-plane.jpg)

After adding the plane hit [s] and scale it up quite a bit.

![](blender-plane-scaled.jpg)

Then with the plane selected hit [tab] to enter edit mode. After that find the subdivide button on the left and subdivide your plane, also move up the number of divisions to get smaller squares. (you may have to subdivide twice)

![](blender-plane-sub.jpg)

Enable proportional editing, It is in the lower left by default

![](blender-pedit.jpg)

Set the proportional editing mode to random

![](blender-redit.jpg)

Now you can move one face, and the nearby faces will follow suit. Note that you can adjust the radius of effect by using your mouse's scroll wheel.

![](blender-redit2.jpg)

Go crazy with the editing. I found that having the larger hills on outside, and a flatter area in the middle worked out best.

![](blender-hills1.jpg)

After you are done making some hills, we are going to smooth them out. To easily do this, we simply add a subdivision surface modifier. So, first click on the modifiers tab (the little wrench). Then click the "add modifier" drop down box. And finally hit Subdivision Surface.

![](blender-subsurf.jpg)

Adjust the subsurf values so the hills become nice and smooth (poly count does not matter here), then press the smooth shading button on the left.

![](blender-smooth.jpg)

Now we need to add the sun and sky. To do this simple go to the add menu [shift][a] and add a "sun" light

![](blender-addlight)

Then turn on the sky option in the light settings

![](blender-sky.jpg)

Finally adjust the camera (add one if you dont have one already), and render a shot.

![](blender-render1.jpg)

... still working on it ... sorry ...
