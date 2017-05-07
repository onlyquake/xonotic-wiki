# Part 1: Hello world

In this tutorial we are going to create a Xonotic mutator that will print text when the player spawns.

## Step 1: Getting source code

First, you will need to get the [source code of Xonotic](Repository_Access). Once you've cloned the repository and built the game successfully, we can start adding our code.

Xonotic is built on top of DarkPlaces engine which in turn was forked from the Quake 1 engine. The game code is written in QuakeC. If you have experience with C or C++, it will be no problem to adapt to QuakeC. All QuakeC code is located in `xonotic/data/xonotic-data.pk3dir/qcsrc/` directory.

Here is the outline of some subdirectories:

* `client` - this directory contains client-side code.
* `common` - this directory contains the code that is shared between client and server.
* `dpdefs` - this directory contains declarations that are used by the engine - a glue between the engine and the game.
* `lib` - this directory contains "libraries" - pieces of reusable code that are not specific to Xonotic.
* `menu` - this directory contains client-side menu code.
* `server` - this directory contains server-side code.
* `tools` - this directory contains some useful shell scripts.

## Step 2: Creating a separate git branch

Xonotic uses git as its version control system. It is recommended to make your changes on a separate branch. There are few advantages of doing so. First, your code will not interfere with a main branch and you can quickly switch between vanilla Xonotic and your modded Xonotic. Second, if there is a breaking change in the master branch, it won't break your code until you will request manual merge of your code. Finally, this is the only way for your code to be officially added to the game.

Since we will only be modding the QuakeC part of the game, we only need to create our branch of `xonotic-data.pk3dir` repository. You should name your branch `<Your name>/<your feature>`.

    xonotic$ cd data/xonotic-data.pk3dir
    xonotic/data/xonotic-data.pk3dir$ git checkout -b Lyberta/HelloWorld

## Step 3: Adding your code

Regular mutators are located in `common/mutators/mutator` directory, let's create a new directory called `helloworld`. Now, the prefixes of files determine whether the code is included in different QuakeC virtual machines. Files that start with `cl_` are only compiled into client-side code and files that start with `sv_` are only compiled into server-side code. Our mutator will be fully server-side so let's create a file called `sv_helloworld.qc`.

Now we need to register our mutator, open `sv_helloworld.qc` and add the following text:

    REGISTER_MUTATOR(helloworld, cvar("g_helloworld"));

`helloworld` is the name of our mutator and `g_helloworld` is the console variable that will enable our mutator. Now we need to make our code execute when player spawns. To do that, Xonotic defines hooks that can be used by mutators. Server-side hooks are defined in `qcsrc/server/mutators/events.qh`. If we open this file and search for `PlayerSpawn`, we will find this:

    #define EV_PlayerSpawn(i, o) \
    	/** player spawning */ i(entity, MUTATOR_ARGV_0_entity) \
        /** spot that was used, or NULL */ i(entity, MUTATOR_ARGV_1_entity) \
        /**/
    MUTATOR_HOOKABLE(PlayerSpawn, EV_PlayerSpawn);

This code defines our hook, we can use by writing the following code in `sv_helloworld.qc`:

    MUTATOR_HOOKFUNCTION(helloworld, PlayerSpawn)
    {
    }

Now we have created our hook but its body is empty, we need to write some code between curly braces. How to find which functions we need to call? Using grep. Grep is used to find text inside files and is essential in exploring Xonotic codebase. The syntax we need is `grep <text> -iRn`. Let's open the terminal in `qcsrc` directory and search for `PrintToChat`:

    xonotic/data/xonotic-data.pk3dir/qcsrc$ grep PrintToChat -iRn

We will get something like this:

    server/player.qh:18:void PrintToChat(entity player, string text);
    server/player.qh:25:void DebugPrintToChat(entity player, string text);
    server/player.qh:30:void PrintToChatAll(string text);
    server/player.qh:36:void DebugPrintToChatAll(string text);
    server/player.qh:42:void PrintToChatTeam(int teamnum, string text);
    server/player.qh:49:void DebugPrintToChatTeam(int teamnum, string text);

Good, we have found our function. Let's add it to our mutator:

    MUTATOR_HOOKFUNCTION(helloworld, PlayerSpawn)
    {
    	PrintToChatAll("Hello world!");
    }

## Step 4: Adding code to the build system

Alright, that should do it. Now we need to instruct the build system to build our code. We do this by running `genmod.sh` script from the `tools` directory inside `qcsrc` directory.

    xonotic/data/xonotic-data.pk3dir/qcsrc$ ./tools/genmod.sh

You can now see that there 2 new `_mod` files inside our `helloworld` directory and if you do `git diff`, you can see that other `_mod` files now contain our new mutator.

## Step 5: Building the code

Now we need to build the QuakeC code. It is done using the `all` script:

    xonotic$ ./all compile -qc -r

## Step 6: Adjusting config files

The last thing we need to do is to create our console variable `g_helloworld` in configuration file. The best file for it would be `defaultXonotic.cfg`. Mutator variables start around line 423:

    set g_helloworld 0

## Step 7: Testing

The best way to test code changes is to run a dedicated server. You need to put `g_helloworld 1` in your `server.cfg`.

Now, start your server, connect to it and spawn. You should see the "Hello world!" message in the chat.

## Step 8: Committing changes

Now, if everything works you can commit your mutator into the git repository:

    xonotic/data/xonotic-data.pk3dir$ git add .
    xonotic/data/xonotic-data.pk3dir$ git commit -m "Added HelloWorld mutator. Yay!"

Now you can switch between vanilla Xonotic and your modded version. Type:

    xonotic/data/xonotic-data.pk3dir$ git checkout master

to switch to vanilla Xonotic and type

    xonotic/data/xonotic-data.pk3dir$ git checkout Lyberta/HelloWorld

to switch to your modded version.