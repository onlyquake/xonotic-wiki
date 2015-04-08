Privacy and Security
====================
Xonitic runs on top of the DarkPlaces Engine. When connecting to a server, the client may download and run QuakeC code for the gameplay. The security policies are:

-   QC code can't create any symlinks.
-   QC code can read anything below ~/.xonotic/*/ including stuff pointed-to by symlinks (which, as the game can't create any, would have to have been placed by the user). It can't read your private key in ~/.xonotic/*.d0si.
-   QC code can write anything below ~/.xonotic/data including your config.
-   Paths are properly sanitized according to this policy.
-   QC code can send arbitrary data back anywhere (by using the "connect" command).

Reference
---------
divVerent's [answer](http://forums.xonotic.org/showthread.php?tid=5427&pid=71595#pid71595) in the forum