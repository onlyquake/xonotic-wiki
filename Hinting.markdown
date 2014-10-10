Hinting
=======

By default, the map is broken into 1024x1204x1024 cubes, called "leaves". These leaves are then only rendered if the user can see them directly. Using hint brushes allows you to break the map up into leafs of your own creation in addition to the ones the compiler generates.

Take the following image for example:

![](http://developer.valvesoftware.com/w/images/c/c8/Hint_example1.jpg)

This is a map view shown from the top down. As you can see, there are three sections to this map: the left room, the right room, and the top hallway. Now, let's say the player is in the left room. The player can't see into the right room, but can partially see into the hallway. However, since there are no hint brushes and the rooms are not completely separated by structure brushes, the whole area is rendered for the player because the hall and right room are in the same "leaf." This means an FPS drop due to the unneeded drawing.

To fix this, let's use a hint brush. Create a rectangular brush perpendicular to the wall, across the entrances of both rooms and set the texture facing the rooms to common/hint. Make sure that the side facing the corridor has the HINT SKIP texture.

![](http://developer.valvesoftware.com/w/images/7/70/Hint_example3.jpg)

Now we've put a hint brush across the entrances to the two rooms, shown here by a white line. Now, a player standing in the left room looking at the hallway will only render those two rooms, meaning that the fps will be higher, particularly if there is a lot of polygons in the two rooms.

By: PlasmaSheep
