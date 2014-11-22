DarkPlaces Wiki
===============

Client-Side QuakeC
==================

What is Client-Side QuakeC (CSQC) ?
-----------------------------------

CSQC is a QuakeC virtual machine that will run your compiled QuakeC code only on the client offering special handling for doing all kinds of stuff such as simulating trivial effects to gameplay like:  

-   brass ejections
-   muzzleflashes
-   gibs
-   rendering a HUD / images and text with ease
-   simulating movement (for projectiles, players, or any object)
-   poll for input such as mouse movements or key strokes for things like menus, inventory, chat boxes, etc
-   various other effects without relying on the normal sever side only QuakeC code (Quake only had the equivalent of server side qc available for modders)

CSQC like SVQC (just known as QuakeC for classic Quake mods) is compiled into a .dat. The default naming convention is csprogs.dat, whereas SVQC was compiled to a progs.dat

CSQC shares many builtins with SVQC however has of course it's own unique ones (for example printing text or rendering your viewport).

CSQC is compiled with the same compiler you'd use typically for your normal QuakeC (such as fteqcc or frikqcc).
You simply have it compile from a different .src file have it name the output csprogs.dat for the engine to read it (default naming scheme for .dat can be changed however this is the default).

But can't normal QuakeC do stuff like muzzleflashes and some of the stuff you mention?
--------------------------------------------------------------------------------------

Yes! And a lot of mods out there that didn't have the oppurtunity to use CSQC did in fact to varying degrees of success implement things such as muzzle flashes, printing stuff on the HUD, and simulating their own movement or chase cameras.
However these implementation were limited to very strict builtins. For example:

-   Printing stuff on the HUD of the player could only be done via forcibly spamming the print functions to clients and tediously size them to fit the screens format with not much control.
    This info had to be continually forced down to each player from the server to have it print and offered no control on position, fading of objects, modifying fonts, pictures, or any snazzy stuff people want to do with their HUDS
-   Muzzle Flashes and Brass ejections could be spawned in the world surely and since they're using the classic Quake entities would reliably be sent to everyone in online games,
    however the unnecessary bandwidth and potential choppiness of updates for these entities (such as smoothly fading away objects or updating their origin lagging behind the player) makes this system in many cases either far too bandwidth inefficient or simply incapable of keeping up with the demands of visuals people want to make.

With CSQC you're harnessing the concept of the client/server architecture.
Depending on your personal choices you can either rely heavily still on server side stuff for entities (like vanilla QuakeC mods did entirely),
or decided to share some entities so you can update their visuals locally such as for player models, projectiles, and other things to have faster updates on entities and more rendering options such as rendering players names above their heads or seeing multiple animations played on a model.
Or you can rely heavily on the power of CSQC and have it simulate entire concepts of entities such as firing a weapon and having it know what weapon you're holding and choose a brass ejection to spawn without even having to touch the vanilla QuakeC!
Don't fret though, this may all be over your head right now, but just be aware you have a breadth of knowledge to grasp to use CSQC to it's greatest potential and it's extremely powerful and convenient once you get the hang of it which hopefully this can help you with!

So lets recap, what does CSQC offer me in less words?
-----------------------------------------------------

-   superior control to print fonts, images, and models onto the player's screen
-   save bandwidth for online games simulating objects trivial to the gameplay but important for visuals
-   share only data that you want to share with clients from server
-   do all kinds of multi-animation models, multiple projectiles, and other things that'd usually choke if forced down from server locally with ease

So shortest short hand imaginable: Save bandwidth, more control to QuakeC scripters, its just that simple!

_(There was a 2nd page linked here, that has been lost)_

