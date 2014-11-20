In-game announcement script by MirceaKitsune
============================================

I made an announcement script that can be used on pubic servers, for notifying players in-game.

To use, copy the script below in your autoexec.cfg. If you don't already have one, create a file called autoexec.cfg in your Nexuiz data folder and put the script in it. Type "news" in the console (\~ button) to echo the message while playing.

Please read the comment lines, especially the one about spamming! Feel free to share and modify the script to spread the information. Here it is:

    // Nexuiz name changing announcement. To use, write "news" (without "") in the console while playing on a public server, or bind it to a custom keybind in the menu.
    // DO NOT UNDER ANY CIRCUMSTANCES SPAM THIS!!! Never post it more often than 20 minutes on the same server! The purpose of this announcement is to inform players, not to annoy them. Thanks.
    alias news_1 "say ^1Important! ^2Although the news has reached many players, Nexuiz is being renamed and continuing as a new project called Xonotic."
    alias news_2 "say ^2Players must eventually switch to the new branch as Nexuiz is being discontinued. For more information visit xonotic.org or dev.xonotic.org/projects/xonotic/wiki. Thank you."
    alias news_enable "alias news \"echo ^1Remember, don't spam this! Only post it again 20-30 minutes from now (unless you switch servers);news_1;defer 8 news_2;news_disable\""
    alias news_disable "alias news \"echo ^1News announcer: Please wait at least 3 minutes between posts to avoid accidental spam.\";defer 180 news_enable"
    news_enable
