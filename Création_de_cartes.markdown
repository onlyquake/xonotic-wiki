Création de cartes
==================

Introduction
------------

Créer des cartes nécéssite [Netradiant](Netradiant), un gtkradiant, un logiciel de fabrication de cartes qui génère des fichiers .bsp compilés en q3map2. Il aide à obtenir une [carte bien empaquetée](carte bien empaquetée) tout en lisant cet article.

Utiliser Netradiant
-------------------

NetRadiant est un fork de l’éditeur de jeu Quake basé populaire, GtkRadiant, si vous avez connaissance de ce logiciel ou un autre dérivé de celui-ci, ce sera plus facile.
Pour plus d’informations et plus en profondeur les détails, reportez-vous à la page [Netradiant](Netradiant).

### Compilation de la source

NetRadiant est inclus avec le git checkout de la [référentiel](Accès référentiel). Sur un système Linux/UNIX, la technique de base pour la construction est de changer votre dossier **./xonotic/netradiant** et d’utiliser ‘make’ pour le compiler. Résolvez toutes les dépendances. Le fichier binaire se trouve dans **./xonotic/netradiant/install**, ‘radiant.x86’.

*Indications pour compiler sur windows \_
h3. Constructions
http://www.icculus.org/netradiant/files/
h2. Forfaits Carte
Les cartes sont emballé comme un fichier .zip avec une extension .pk3. Ils peuvent être ouvert avec n’importe quel programme qui ouvre des fichiers zip. Le pk3 est chargé lorsque vous démarrez le jeu, ]. Le moteur, ] lit les fichiers pk3 comme un système normal de fichiers. Vous pouvez ainsi créer un package pk3 avec tous les fichiers que le moteur peut normalement lire.
h3. Arts appliqués aux paquets
h4. Conventions de nom
<mapname> doit être uniquement alphanumérique, minuscules avec des tirets, des nombres et soulignements, .pk3 — de préférence ils sont suffixés avec une version et de révision. Suite à cette convention donnera de meilleurs résultats à partir de scripts qui utilisent ce format pour aider à distribuer votre carte.
h4. Fichiers requis
maps/<mapname>.bsp - Ceci est votre fichier de carte compilé
maps/<mapname>.map - Ceci est un jeu open-source, aider les autres à apprendre. Ce fichier est requis pour être dans le match.
maps/<mapname>.mapinfo - Ce fichier a la méta-information, le suivi mondial de la musique, mode de jeu et les paramètres de jeu
maps/<mapname>.tga|png|jpg - Ce fichier est une capture d’écran de votre carte. Si vous n’incluez pas cela, vous carte ne possède pas de photo dans le menu ou l’écran de vote pour les serveurs et pleurer les anges.
maps/<mapname>.waypoints - Ceci est nécessaire pour être ajouté au jeu, c’est pour les bots
maps/gfx/<mapname>*mini.tga|png|jpg - Ceci est nécessaire pour être ajouté au jeu, c’est un radar de la carte. Ceux-ci peuvent être générés avec la commande “\<”.

#### Facultatif / Fichiers suggérée

Ce n’est pas une liste exhaustive, souvenez-vous, vous pouvez inclure presque n’importe quel fichier qui se charge avec une carte. (Liste des besoins des fichiers)

#### Fichiers que vous devriez jamais inclure

csprogs.dat
progs.dat
effectsinfo.txt

En incluant l’un des fichiers ci-dessus, vous pourriez provoquer des résultats indésirables. Essayez d’utiliser le sens commun sur la façon dont vous ajoutez dimension à votre carte, si vous avez des questions, demandez de l’aide.

Exemples
--------

maps/tutorial-world-v1\_r2.bsp
maps/tutorial-world-v1\_r2.map
maps/tutorial-world-v1\_r2.mapinfo
maps/tutorial-world-v1\_r2.png
maps/tutorial-world-v1\_r2.waypoints
maps/gfx/tutorial-world-v1\_r2\_mini.png
maps/models/tutorial-world/crate.md3
maps/models/tutorial-world/jumppad.md3
scripts/tutorial-world/map-tutorial-world.shader
maps/sound/cdtracks/tutorial-world/main-room.ogg
maps/sound/tutorial-world/jumppad.ogg
maps/sound/tutorial-world/wind.ogg
maps/textures/tutorial-world/base\_1.tga
maps/textures/tutorial-world/floor\_1.tga
maps/textures/tutorial-world/floor\_2.tga
maps/textures/tutorial-world/floor\_1.tga
maps/textures/tutorial-world/wall\_1.tga
maps/textures/tutorial-world/wall\_2.tga

*ajoutez une carte bien emballée*

Tests de cartes
---------------

Vous pouvez compiler votre carte localement ou sur le serveur de construction. Le serveur de construction (nécessite un [référentiel d’accès](référentiel d’accès)) nécessite un fichier <nomdecarte>.nomdoptions. Pour vérifier, et plus d’info, demandez dans \#xonotic.editing sur irc.quakenet.org

Cartes sur les serveurs
-----------------------

Trouver un serveur admin pour ajouter votre carte. (Cette section doit être travaillée)

Dépôts de carte
---------------

***Les cartes doivent être correctement emballés pour être inclus dans un référentiel***

Un référentiel carte officielle est en cours de planification, s’il vous plaît, revenez plus tard ou trouvez de l’aide sur IRC.

Aide
----

\#xonotic.editing on irc.quakenet.org
http://forums.xonotic.org

[English](Creating Maps)
