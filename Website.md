Website
=======

An integrated wordpress and mybb system.

Wordpress
---------

### Plugins & Features

-   http://www.tevine.com/projects/voteitup/

-   http://wordpress.org/extend/plugins/tdo-mini-forms/ — look into this

-   Gallery with public and user upload

-   Map Repository

-   User Surveys/Polls

MyBB
----

### Plugins & Features

Goals
-----

-   Create a theme for Wordpress and MyBB to share

Needed
------

### Art

-   Splash image for the login / waiting screen on the forum
-   Website design

SSO (Single Sign On)
--------------------

(psychcf) After talking with z, here’s what we know we want to do:
- Have a centralized authentication system using LDAP
  * Write a plugin for mybb to auth against it
  * Find a plugin for wordpress to auth against it
  * The reasoning behind this would be that it would be easier to add other web apps to it later, and even have the dev site and git server auth against the ldap server.
- Later down the road we want to do an in-game community sort of thing
  * There would be achievements and statistics, server listings, possibly a friend/clan management thing, etc.
  * This would be accessible through the game through an exposed RPC service of some sort
    + For achievements, we need to come up with some way of preventing people from cheating by just calling the RPC functions from some script
  * We could use django or some other framework to do this pretty quickly
  * In-game chat between players/clan members could be done by running a jabber server on the hosting side, then writing some sort of client for it in the game, although this would be more complicated.

Forum structure
---------------

### General

Post anything about anything here

### Xonotic - News & Announcements

Comment on the news and view past news

### Xonotic - Help & Troubleshooting

### Xonotic - Bug Report

### Xonotic - Editing

Post anything to do with editing Xonotic here.  
Whether its problems you’ve had, questions, or if you just want to show off your work.

### Xonotic - Contests

Mapping, modding contests, FOTM, and more.

### Xonotic - Gameplay

Discuss Xonotic gameplay here.

### Xonotic - Configuration Tips

Tips on how to tweak Xonotic for the best performance, gameplay, etc

### Xonotic - Development

Developer discussion of experimental fixes, changes, and improvements.

### Xonotic - Map Releases

(Locked section, with sticky thread which points people to https://gitlab.com/xonotic/xonotic/wikis/home “How to report bugs”)

### Xonotic - Map Reviews

Community reviews of maps (both official and user-made).  
*Comment: This is likely to be confused with the Map Releases section. Do we want to keep this section? (this section is the least active on AT forum)*

### Xonotic - Server Administration

### Xonotic - Competition

-   Clan Discussion
-   Clan League
-   1v1 Matches
-   2v2 Matches
-   CTF Matches
-   Tournaments

