You can use `addvote` command to add custom vote commands to your server. For example, suppose you want your players to be able to vote whether they want bots or not. This can be achieved using the following code:

```
alias bots "minplayers 4"
addvote bots

alias nobots "minplayers 0"
addvote nobots
```

Now players will be able to type `vcall bots` or `vcall nobots` which will start a vote to have those commands issued.

You can prefix the contents of an alias with `settemp` to make it be valid only for the current game. For example `alias nobots "settemp minplayers 0"`.

You can create documentation for your votes by creating a cvars with `sv_vote_command_help_%VOTE_NAME%` pattern, for example:

```
set sv_vote_command_help_bots "\nUsage:^3 vcall bots\n^7  Adds some bots to the server."
```

Here's example that allows voting common server types assuming your `server.cfg` doesn't force them (you get infinite recursion if it does):

```
alias vanilla "exec ruleset-xonotic.cfg; exec server.cfg; endmatch"
addvote vanilla
set sv_vote_command_help_vanilla "\nUsage:^3 vcall vanilla\n^7  Resets the server to vanilla ruleset."

alias instagib "exec ruleset-xonotic.cfg; exec server.cfg; g_instagib 1; g_grappling_hook 1; endmatch"
addvote instagib
set sv_vote_command_help_instagib "\nUsage:^3 vcall instagib\n^7  Sets the server to instagib ruleset."

alias overkill "exec ruleset-overkill.cfg; exec server.cfg; endmatch"
addvote overkill
set sv_vote_command_help_overkill "\nUsage:^3 vcall overkill\n^7  Sets the game to overkill ruleset."
```
