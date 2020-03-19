Autobuilds are nightly builds of the latest code. They have the latest features, bugfixes and assets but they could be less stable than regular releases. 

If you "installed" Xonotic by downloading and unpacking the [zip](http://xonotic.org/download/), you can update a regular release to autobuild using the scripts located in `misc/tools/rsync-updater` (use `update-to-autobuild.bat` if you're one Windows, `update-to-autobuild.sh` on Linux and Mac).

It's best to **make a copy of the original Xonotic directory first** in case you wanna go back to using the release but you can also go back by using the `update-to-release` scripts. Releases and autobuilds should be able to coexist (they will share the same [config](https://www.xonotic.org/faq/#config) though).

Autobuilds (and [git builds](https://gitlab.com/xonotic/xonotic/-/wikis/Repository_Access)) are compatible with the same servers as the latest release. When you connect to a server, Xonotic downloads the gamelogic from it (and runs it sandboxed) so you always use the same version as the server. Autobuilds therefore only affect assets (models, sounds, ...) or gamelogic of local games.