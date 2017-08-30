You can use `addvote` command to add custom vote commands to your server. For example, suppose you want your players to be able to vote whether they want bots or not. This can be achieved using the following code:

```
alias bots "minplayers 4"
addvote bots

alias nobots "minplayers 0"
addvote nobots
```

Now players will be able to type `vcall bots` or `vcall nobots` which will start a vote to have those commands issued.

Here's example that allows voting common server types assuming your `server.cfg` doesn't force them:

```
alias vanilla "exec defaultXonotic.cfg; exec server.cfg; endmatch"
addvote vanilla

alias instagib "exec defaultXonotic.cfg; exec server.cfg; g_instagib 1; g_grappling_hook 1; endmatch"
addvote instagib

alias overkill "exec defaultOverkill.cfg; exec server.cfg; endmatch"
addvote overkill
```