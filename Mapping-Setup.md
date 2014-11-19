h1. Mapping-Setup

h2. How to get your system all set up to start mapping ^^

h3. Step 1 -- Obtain mapping support

If you didn't already, download this ... http://dl.xonotic.org/xonotic-0.6.0-mappingsupport.zip

h3. Step 2 -- Extract zip

Extract the .zip archive using your favorite archiving tool 

h3. Step 3 -- Find the magic folders

Locate your .xonotic folder, note that this is NOT the install location. This is the place xonotic saves your config. 

* on linux this should be in ~/.xonotic 
* on windows (7) its in \users\user\saved games\xonotic 
* on mac ... its in ~/libraries/appdata ?? maybe ??

h3. Step 4 -- Understand the magic folders

if/when you find both of these folders, you will see that both of them contain a data folder. Game wise these data folders are treated the same, however, it is best to save your work in the .xonotic folder so that you don't accidentally mess up your xonotic install, or so that your work doesn't get lost in an update.

h3. Step 5 -- Moving stuff

remember that zip we extracted? There should be 2 folders in it.

* data (yes ... another data folder)
* mapping

First open up the data folder and find the .pk3 file. (may look similar to xonotic-maps-mapping.pk3)Then take the pk3 and copy it to xonotic/data Note, .pk3 is really a renamed .zip. DONT extract it. 

editors note :: is this step required ... im not sure --> Now take the mapping folder and move it to the root of .xonotic (dont put it in any of the data folders)

h3. Step 6 -- Get net-radaint working

* WINDOWS, you are ready to go just double click on radiant.exe
* LINUX users may have to compile theirs, don't worry, netradaint is rather easy to compile. If you need help ask on the forums, or irc
* MAC ... um ... its possible ... but complicated ... someone who knows how should edit this... and you will probably need OSX 10.5 or greater



h3. Step 7 -- Setting up netradiant

When you first start up radiant it may ask where the install location is. Simply, point it to the install location. Then net radaint should start,\ and the lower right pane should have lists of texture packs. If there are no texture packs, then refer back to step 5.


<< [[mapping-Introduction]] 1 [[mapping-NetRadiant]] >>
 

... [[Creating_Maps]] ...
