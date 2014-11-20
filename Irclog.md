Irclog
======


    **** BEGIN LOGGING AT Wed Mar 03 10:28:36 2010

    Mar 03 10:28:36 *   Now talking on #notnexuiz
    Mar 03 10:28:41  Hi
    Mar 03 10:28:44  hello
    Mar 03 10:28:52 <[-z-]> why hello
    Mar 03 10:28:55 *   [-z-] gives channel operator status to Dokujisan Taoki
    Mar 03 10:29:46 *   div0 (Fg8deKX0@rm.endoftheinternet.org) has joined #notnexuiz
    Mar 03 10:30:07 *   [-z-] gives channel operator status to div0
    Mar 03 10:30:11   Welcome to Noxious.
    Mar 03 10:31:07 <[-z-]> I've talked to div0 and Dokujisan in private about different aspects in moving forward with a fork away from Nexuiz and away from Alientrap
    Mar 03 10:32:07 <[-z-]> we've begin discussing project organization, server availabiltiy, repository, name, interested parties, possible repurcussions and where we go from here
    Mar 03 10:32:11   just not sure if it will be an actual fork
    Mar 03 10:32:20   or rather, whether AT will even continue with Nexuiz then
    Mar 03 10:32:38   to summarize a bit:
    Mar 03 10:32:56   - repository I can provide, on icculus.org. In fact, I already have a Nexuiz repo there.
    Mar 03 10:33:10  I'm always with this project no matter what new name it will have, team name, etc. What happened happened, i mainly care what is best for this project now
    Mar 03 10:33:13   - project organization: there should be not "one leader who speaks for everyone".
    Mar 03 10:33:27     to make things like what had happened to not happen again
    Mar 03 10:34:04   I suggest a scheme that ensures 3 "leaders", and big decisions have to be agreed upon by all three, and they also should be "somewhat responsible" for the rest of the community
    Mar 03 10:34:16   e.g. no persons who are so detached that they simply do not care for the community any more
    Mar 03 10:34:34  I told -z- that I think all good projects need some sort of leadership to be succesful. The 3-leader idea isn't bad.
    Mar 03 10:34:40 <[-z-]> and perhaps a board or committee under that
    Mar 03 10:34:45   in AT, LordHavoc maybe somewhat still can represent the community - Vermeulen certainly can't
    Mar 03 10:35:25   2 leaders aren't enough, as at times there would be only one leader available :P
    Mar 03 10:35:28 <[-z-]> also for project reorganization, I've begun talking about better package management and distribution
    Mar 03 10:35:33   I think the existence of a "dictator" should eb avoided
    Mar 03 10:35:44   hm... how?
    Mar 03 10:36:04 <[-z-]> how? the whole upload test package and alert servers thing I was talking about
    Mar 03 10:36:11  I can confess I am a tiny little bit upset at LordHavoc too, because he could have declined this whole thing and not ported the engine to xbox. But I still like him and am not upset on him or anything... just wish he would have thought more at first maybe
    Mar 03 10:36:21  erm ps3
    Mar 03 10:36:48   [-z-]: oh
    Mar 03 10:36:53   you don't mean packaging of the game :P
    Mar 03 10:37:01 <[-z-]> oh no no
    Mar 03 10:37:03   because, regarding that I think the old Nexuiz way was right
    Mar 03 10:37:11 <[-z-]> yeah, there is a good workflow there
    Mar 03 10:37:13   other than that I am working on a new build script that works more efficiently wiht git
    Mar 03 10:37:16 <[-z-]> I wouldn't want to modify that
    Mar 03 10:37:22   but that doesn't change the result
    Mar 03 10:37:32 <[-z-]> you know best about that area
    Mar 03 10:37:42   still, we ARE doing oddball packaging
    Mar 03 10:37:48 <[-z-]> I want to start getting this project more organized though
    Mar 03 10:37:51   so MAYBE we should make it more "standard" anyway
    Mar 03 10:37:56   but well
    Mar 03 10:37:59 <[-z-]> and built the website into the workflow
    Mar 03 10:38:02   it is oddball that we put all platforms in one download
    Mar 03 10:38:06   but it has its advantages too
    Mar 03 10:38:22 <[-z-]> I want to build everything into wordpress/mybb and get the build script putting out cvar / command lists for the tool I'll integrate into the site.
    Mar 03 10:38:32   I wouldn't want to touch that for now, but do some attempts at making platform specific versions too
    Mar 03 10:38:42   I e.g. have recently made an engine feature that allows attaching a pk3 to a executable
    Mar 03 10:38:49   so we could make a single selfcontained exe file for the game
    Mar 03 10:38:51   (a 900MB one...)
    Mar 03 10:39:32   for OS X, such a thing can already be accomplished because applications are just folders anyway
    Mar 03 10:39:33  I hope there aren't plans to distribute Nexuiz like that in the future.
    Mar 03 10:39:39   and Linux users don't care about that structure anyway :P
    Mar 03 10:39:53   Taoki: I don 't want to exclude it, but probably it won't happen
    Mar 03 10:40:01   except maybe for DSN :P
    Mar 03 10:40:22   I think the advantages of the multiplatform zip overweigh that
    Mar 03 10:40:27  I don't support that personally. The data being in a pk3 file is very important for flexibility and the like imo
    Mar 03 10:40:31 <[-z-]> I think it would be helpful in some cases where users prefer simplicity
    Mar 03 10:40:33   it stays just as flexible
    Mar 03 10:40:34 <[-z-]> but never a forced thing
    Mar 03 10:40:37   if you cat the pk3 to an executable
    Mar 03 10:40:44   you can rename the result to zip and work with it normally
    Mar 03 10:40:50   it is no less flexible than the pk3 way
    Mar 03 10:41:07   zip self extractors work that way too :P
    Mar 03 10:41:16  Hmm, I see
    Mar 03 10:41:20   still
    Mar 03 10:41:26   it means different downloads for different platforms
    Mar 03 10:41:32   which somewhat hides that the game is multiplatform
    Mar 03 10:41:48   and that is the part that I don't like about it
    Mar 03 10:42:03   for damn small nexuiz this is no issue htough :P
    Mar 03 10:42:11  I still like the way it is packed now myself. Don't think we should change that.
    Mar 03 10:42:15   right
    Mar 03 10:42:17   I like it too
    Mar 03 10:42:26   this is, again, more an idea for specialized "distributions" like DSN
    Mar 03 10:43:15   [16:38:43] <@[-z-]> I want to build everything into wordpress/mybb and get the build script putting
    Mar 03 10:43:17                       out cvar / command lists for the tool I'll integrate into the site.
    Mar 03 10:43:27   you want the buoild script accessible from a web interface... not sure if that is good
    Mar 03 10:43:49   another thing however that I would like, is more frequent public releases
    Mar 03 10:43:56   with git, we can easily separate into different branches
    Mar 03 10:44:03   and merge features into the main branch when they are done
    Mar 03 10:44:19  Yeah, same div0. New versions seem to be released once or twice an year
    Mar 03 10:44:27   so we should be able to make "weekly" test releases, and make actual minor releases every 3 months
    Mar 03 10:44:31  Maybe once every 3-4 months at most wouldn't be bad
    Mar 03 10:44:55   just like I did my work on Nexuiz/DP lately
    Mar 03 10:45:08   I e.g. finished the warpzones code before putting it into the main branch
    Mar 03 10:45:53   the problem is just, I cannot enforce such a policy on darkplaces
    Mar 03 10:46:04  div0: I have wanted a fork of nexuiz for a long while. The reasons were mainly because of missing elements of project management. We (I discussed this with a handful of others) couldn't do a fork before because we didn't have someone like you, a primary developer who knows the code very well. But if YOU are involved in a Nexuiz fork, that changes things. I would be onboard as long as we have an outline of management....and some i
    Mar 03 10:46:04  ntention of doing "official" community development, "official" marketing efforts, "official" testing procedures with a select group of volunteer testers, etc.
    Mar 03 10:46:07   for that I am maintaining a "stable branch", but unstabilities still happen once in a while in DP
    Mar 03 10:46:14   as I often simply cannot properlya judge if something is stable
    Mar 03 10:46:35   select group of testers... not sure :P
    Mar 03 10:46:44   I don't think testing should be limited
    Mar 03 10:46:52   everyone should be allowed, and even encouraged, to
    Mar 03 10:47:11   but, some select group for "heavier" testing is still a very good idea
    Mar 03 10:47:20   i.e. people who should feel responsible for actually testing it :P
    Mar 03 10:47:23  Not sure to whom I mentioned this, but for a while ago I've started making an own game from Nexuiz as well. Obviously, one that will be named differently and remain GPL too :P Probably a little game which is just like, a sort of story i wanted to make for myself
    Mar 03 10:47:30  well of course features can be experienced by all, but a select group would do some proper feedback and have better communication with the dev team
    Mar 03 10:47:39   right
    Mar 03 10:47:44   I just say... we shouldn't restrict
    Mar 03 10:47:49 <[-z-]> sorry went to make tea, let me catch up
    Mar 03 10:47:51   a testing team should not be exclusive
    Mar 03 10:47:58   but it should eb responsible for the testing
    Mar 03 10:48:07   anyone else still is free to test too :P
    Mar 03 10:48:16  anyone could give feedback....my point is that this type of subject should be discussed. The whole game balance issues that we went through (before and after LH rejoined the project) could have been handled better
    Mar 03 10:48:19  Yeah, SVn should always be public imo
    Mar 03 10:48:22 <[-z-]> div0: the cvar and command lists would be text files reformated as json and accessible through a web application
    Mar 03 10:48:35   Taoki: not just svn
    Mar 03 10:48:37   also binary builds
    Mar 03 10:48:42  sure
    Mar 03 10:48:44 <[-z-]> wordpress is an open format many developers know and love and it will be easy for us to scale
    Mar 03 10:48:50   my goal is weekly binary builds from the "stable" branch
    Mar 03 10:49:04   feature freeze would simply mean no feature branches get merged into main, only bugfixes would
    Mar 03 10:49:10   other devs can then still work on features :P
    Mar 03 10:49:27   they just won't appear in the release the freeze is for
    Mar 03 10:49:42 <[-z-]> This will help give us a stronger community because we can build user auth into other parts of the site, like a map repository.
    Mar 03 10:49:58   as for cvar list...
    Mar 03 10:50:05   don't know how to properly generate json from shell script
    Mar 03 10:50:12 <[-z-]> you don't have to
    Mar 03 10:50:12   but well, I do know how to make a full cvar list text file :P
    Mar 03 10:50:16 <[-z-]> yes
    Mar 03 10:50:18 <[-z-]> that's all I need
    Mar 03 10:50:20 <[-z-]> that's how it works
    Mar 03 10:50:22 <[-z-]> I have it in git
    Mar 03 10:50:24  I'm strongly in favor of a central user system
    Mar 03 10:50:27   once did that by actually running the engine, and doing cvarlist :P
    Mar 03 10:50:41 <[-z-]> Dokujisan: I don't think it's a completely central user system
    Mar 03 10:50:50 <[-z-]> and I'm open to creating a distributed network
    Mar 03 10:51:06   I don't think repository access and web user auth can be combined
    Mar 03 10:51:12 <[-z-]> div0: this is how it works http://github.com/z/ncacs
    Mar 03 10:51:17   but all the rest should be able to
    Mar 03 10:51:40 <[-z-]> so just a cronjob to generate the list and upload it to a web server
    Mar 03 10:51:42  Heh, I realize now i never thouht about any such changes, now that it is talked about. Nexuiz, for a free and opensource project, always seemed perfect to me. Never thought anything could or should be improved in how it's managed etc.
    Mar 03 10:51:46   only problem: this lacks cvars that are specific to some builds
    Mar 03 10:51:58   like renderer stuff
    Mar 03 10:52:01  Except that patches could be checked more often, been struggling with that for the last months
    Mar 03 10:52:04 <[-z-]> div0: well, we can further separate it
    Mar 03 10:52:05  div0: I'm working on another gaming project with Getty and we're planning something called a PlayerID which is to be a central user system that even other games other than ours could use
    Mar 03 10:52:14   Taoki: thing is
    Mar 03 10:52:24   working with such patches is quite tedious
    Mar 03 10:52:36   I say, when using git, more people should get commit access to branches
    Mar 03 10:52:43   and merging gets easier then too
    Mar 03 10:53:11  Yeah, i'm still not so familiar with git. It is more difficult to understand than SVN, ad least over Windows with Tortoise
    Mar 03 10:53:16   Dokujisan: you know I am against an enforced user system for the game
    Mar 03 10:53:20   I want to play anonymously
    Mar 03 10:53:26   even though that means proper banning cannot happen
    Mar 03 10:53:34   an optioanl registration for stats, why not
    Mar 03 10:53:37  div0: even if you register a name, isn't that still anonymous?
    Mar 03 10:53:50   not really, one can easily find out :P
    Mar 03 10:53:55 <[-z-]> well, I wasn't even thinking about stats but we can do that too... I was thinking more for content submissions
    Mar 03 10:54:04   I basically don't want to be trackable in game
    Mar 03 10:54:09  why not?
    Mar 03 10:54:10   I sometimes play with other nicks
    Mar 03 10:54:23   because e.g. employers are not supposed to know that I sometimes play 3 hours on a day
    Mar 03 10:54:32 <[-z-]> :-P
    Mar 03 10:54:32   they are prone to expect you to be there for the company all day
    Mar 03 10:54:41   the times of 8hr/day are over
    Mar 03 10:55:13   and no, I do not mean playing from work.
    Mar 03 10:55:16   not doing THAT :P
    Mar 03 10:55:17  what if each user account is allowed 3 hidden aliases tied to the account?
    Mar 03 10:55:21   no
    Mar 03 10:55:25  or some other variation
    Mar 03 10:55:28   why do you want to enforce accounts?
    Mar 03 10:55:40   even though _I_ know my email address won't eb abused
    Mar 03 10:55:44   how would anyone else be sure?
    Mar 03 10:55:58   (I would know because I'd have control over that system :P)
    Mar 03 10:56:10  the moderation features alone are worth the central user system
    Mar 03 10:56:14  but as far as trusting people
    Mar 03 10:56:28   banning is not worth tracking
    Mar 03 10:56:31  we could win people's faith because of being an open source project with open values
    Mar 03 10:56:34   how would hidden aliases even work?
    Mar 03 10:56:41   i mean, if you use it for banning
    Mar 03 10:56:45  div0: that can be discussed. I just thought of that off the top of my head
    Mar 03 10:57:06   other way round, for positive display of trust - sure
    Mar 03 10:57:13   people SHOULD be able to register others as friends
    Mar 03 10:57:25   and I can always opt to play as an "unknown" :P
    Mar 03 10:57:36   think of IRC nickname registration
    Mar 03 10:57:50   that is optional, although you sort of have to do it if you want to have some sort of status (e.g. op in a channel)
    Mar 03 10:58:07   I'd have no problem if this user auth system is tied to e.g. vote masterä
    Mar 03 10:58:09 <[-z-]> Hey, can we rewind for a second and brain storm names for this group and project so we can go forward with setting up resources to outline the project and discuss these things with a wiki / forum?
    Mar 03 10:58:13   or even required for being allowed to start a vote
    Mar 03 10:58:25  well your main concern is with tracking, like stats of tracking the times that you are online playing.... the aliases would be for avoiding that. You could use your alias names when you don't want to be tracked publicly.
    Mar 03 10:58:38   how would that even help?
    Mar 03 10:58:46   the server would probably know that I am the same person
    Mar 03 10:58:49   and just display other info
    Mar 03 10:59:12   I do not WANT the server to know, as I don't have good reasons to trust it
    Mar 03 10:59:42  yes the central server would be the only thing knowing the link between the user account and the alias
    Mar 03 10:59:47   thing is basically... in the open source community, many people are also friends of privacy :P
    Mar 03 10:59:51  I'm not sure why you wouldn't trust that
    Mar 03 11:00:03  well this is still supporting privacy, I think
    Mar 03 11:00:04   _I_ would because I would have access to that server, and know how it works
    Mar 03 11:00:08   how could anyone else be able to trust it?
    Mar 03 11:00:12 <[-z-]> wouldn't the solution here be for servers to opt into this centralized service?
    Mar 03 11:00:12   any "mere player"?
    Mar 03 11:00:38  don't mere players trust websites all the time anyway?
    Mar 03 11:00:43   not all
    Mar 03 11:00:45  with registering
    Mar 03 11:00:50   e.g. what about all the noscript users? :P
    Mar 03 11:00:58   or, you do know bugmenot.com? :P
    Mar 03 11:01:08  well I mean with your example of trusting someone with your email address
    Mar 03 11:01:15  that's one scenario
    Mar 03 11:01:16   there IS a large group who is on the side of privacy
    Mar 03 11:01:23   I am part of that
    Mar 03 11:01:34   I do not want others to be able to track me, when I don't positively allow them to
    Mar 03 11:01:41   in a forum it can't be avoided, so it's fine by me
    Mar 03 11:01:52   but in a game, it should be avoided
    Mar 03 11:02:02   still, you can give good incentives for registering in the game
    Mar 03 11:02:06   #just shouldn't enforce it
    Mar 03 11:02:15   even nick name coloring could depend on it :P
    Mar 03 11:02:17  do you want to be allowed to spam servers like nadz does?
    Mar 03 11:02:26   it can't be helped
    Mar 03 11:02:26 <[-z-]> just make it an opt in feature
    Mar 03 11:02:29   I want to ensure my privacy
    Mar 03 11:02:30 <[-z-]> by the server admin
    Mar 03 11:02:31  I'm wondering what level of freedom you are after
    Mar 03 11:02:45   basically:
    Mar 03 11:02:46 <[-z-]> 90% of the internet uses google, so they clearly don't give a shit about privacy :-P
    Mar 03 11:02:49  this is just a game here. The goal should always be about allowing players to....play the game
    Mar 03 11:02:57  and that is really what moderation is about...or should be about
    Mar 03 11:03:01 <[-z-]> plus, we can mask their ips from the server if they feel so inclined
    Mar 03 11:03:10   IPs are already masked :P
    Mar 03 11:03:12   that isn't the problem
    Mar 03 11:03:18 <[-z-]> yes but I mean with cool names
    Mar 03 11:03:23   well
    Mar 03 11:03:25 <[-z-]> or annoying depending on how you look at them :-P
    Mar 03 11:03:29   what about this:
    Mar 03 11:03:35 <[-z-]> z@my-clan.rockz.net
    Mar 03 11:03:38   1. in serious match (like ladder, pickup), you MUST be registered
    Mar 03 11:03:47 <[-z-]> yes
    Mar 03 11:03:53   2. in FFA match, you don't have to be, but if not, you show up as unregistered in the scoreboard
    Mar 03 11:03:56  Not so much into privacy here, when it comes to Nexuiz. But for those who want it, it is good. Afaik you can just change nickname before entering a server.
    Mar 03 11:04:01  the method for which aliases are used could be public knowledge. Aliases woudln't be trakced. They would only be used to apply moderation actions to an account, when necessary.
    Mar 03 11:04:05      maybe can even only use the marine model and non-colored nicks
    Mar 03 11:04:15  This reminds me. I hope Nexuiz will have a menu Friends List at some point
    Mar 03 11:04:31   Taoki: CURRENTLY I can just change my nick :P
    Mar 03 11:04:45   basically... I am fine if I lose features when playing unregisteredly
    Mar 03 11:04:55   like nick colors, player model choice
    Mar 03 11:05:07   but I want to stay able to
    Mar 03 11:05:20   otherwise, I'll have no choice but to create multiple dummy accounts with various email addresses
    Mar 03 11:05:35  div0: I'm mainly asking you to think about the possibilties here that can protect the necessary level of privacy. The main issues with privacy have to do with tracking. The other thing that is useful for a central registration system is to reserve names 
    Mar 03 11:05:39   also, I am fine if some servers enforce the registration
    Mar 03 11:05:49  so nobody could use the alias name "divverent"
    Mar 03 11:05:52   right
    Mar 03 11:05:54   reserving names is good
    Mar 03 11:05:58   but well, on IRC it works too
    Mar 03 11:06:12   if not registered, what if I then always show up as divverent
    Mar 03 11:06:20   and to be divVerent, I need to registere
    Mar 03 11:06:25  hmm
    Mar 03 11:06:27  Right... i even forgot there is a traking system. If there is one... I'm shamed to say i don't know yet (like a system that stores how good you are on servers, atc)
    Mar 03 11:06:37  I woudln't want people to play as Dokujisan
    Mar 03 11:06:44   well
    Mar 03 11:06:47   you can kick them then :P
    Mar 03 11:06:55  rcon is its name iirc
    Mar 03 11:07:01   if you see a Dokujisan and a Dokujisan on a server
    Mar 03 11:07:05   you know which one is the right one :P
    Mar 03 11:07:20  well *I* do...but a mere player.....
    Mar 03 11:07:33   he'll see that you have the cooler color codes
    Mar 03 11:07:38   and the other Dokujisan is just plain white :P
    Mar 03 11:08:00 <[-z-]> maybe he was feeling vanilla and the other one was just being))
    Mar 03 11:08:06   lol
    Mar 03 11:08:10   the unregistered tag could be ))
    Mar 03 11:08:13 <[-z-]> haha
    Mar 03 11:08:27 <[-z-]> halo on xbox live used to have a iconic background
    Mar 03 11:08:32 <[-z-]> in the names list
    Mar 03 11:08:37 <[-z-]> well on the scoreboard
    Mar 03 11:08:56  I think when it comes to privacy issues, instead of saying in a blanket fashion "I want my privacy!" is not helpful, but breaking it down into specific concerns or scenarios is something that can be worked with.
    Mar 03 11:08:57 <[-z-]> for registered (at bungie.net) users
    Mar 03 11:09:10   Dokujisan: but well, if you can figure out a way that allows enforced registration without the server (not the auth server either) knowing who you are
    Mar 03 11:09:14   then I am fine wiht it
    Mar 03 11:09:23   possibly this can be done using digital signatures
    Mar 03 11:09:31  can you help me come up with some solution like that? I would be more than happy to travel down that road.
    Mar 03 11:09:44   I don't know one, but find it possible that one exists
    Mar 03 11:09:52  getty talked about using digital signatures for the PlayerID concept
    Mar 03 11:09:59   like, with RSA such stuff may be possible
    Mar 03 11:10:18   e.g., RSA scheme is "malleable", so you can "edit" an encrypted message without being able tod ecrypt it
    Mar 03 11:10:33   this might be useful to implement the "aliases"
    Mar 03 11:10:56 <[-z-]> Dokujisan: think about integrating the playerID system with wordpress as well.
    Mar 03 11:10:57   they might then appear as valid signatures, but the server doesn't know for whom
    Mar 03 11:11:25   but of course... then the player also cannot be properly banned
    Mar 03 11:12:16  well we all know that any player can just re-register
    Mar 03 11:12:26  but banning is more about creating resistance
    Mar 03 11:12:39  making it a bit harder for them to act inappropriately
    Mar 03 11:14:22   I still wonder if there is a way to combine both
    Mar 03 11:14:26  ip-based banning is more useful. A combination of user account + IP is better.
    Mar 03 11:14:34   what if the "player ID" is a different one when talking to a different server
    Mar 03 11:14:46   e.g. if the cleint doesn't send the player ID, but a hash of the player ID and the server IP
    Mar 03 11:14:51   you then cannot be tracked across servers
    Mar 03 11:14:57   but one server can recognize you
    Mar 03 11:15:52   or even, if every player immediately gets 9 IDs on registration he can freely choose from, and accumulate stats on
    Mar 03 11:16:04   if one is banned, he will of course use the next one
    Mar 03 11:16:08   but he only has 9 chances :P
    Mar 03 11:16:19   still... he then just reregisters
    Mar 03 11:16:47   I am fine if some servers enforce registration of course
    Mar 03 11:16:55   but I can tell you straight away, I won't play on such servers
    Mar 03 11:17:00  yes, I really like the idea of enticing people to act appropriately by offering features that benefit longstanding accounts.
    Mar 03 11:17:21  div0: even if the main privacy issues are dealt with?
    Mar 03 11:17:30   Dokujisan: I do0ubt they CAN be dealt with
    Mar 03 11:17:35   e.g. if a centralized auth server is used
    Mar 03 11:17:40   what if it gets hacked?
    Mar 03 11:17:54   what if the server admin decides it's a good idea to release all sorts of log data from it?
    Mar 03 11:18:02  if the aliases aren't tracked, then that shouldn't affect the privacy issue that you explained earlier (tracking)
    Mar 03 11:18:07   the one piece of ifnormation that I never want to publish, is when and how long I played
    Mar 03 11:18:09  so even if accounts are hacked
    Mar 03 11:18:17   how do I _know_ the aliases are not tracked?
    Mar 03 11:18:33   there should be some technical means so I can trust it without knowing what thze server does
    Mar 03 11:19:14   however, if there are, how could the auth server then possibly recognize me when I am banned?
    Mar 03 11:19:45  every second we're on the internet, we're trusting people. To use a service, there has to be SOME level of trust. When people connect to my nexuiz server, they have to trust me.
    Mar 03 11:19:59   how do they even know it is YOUR server?
    Mar 03 11:20:05   what if mikeeusa names his server the same :P
    Mar 03 11:20:26   okay, you'd notice when you see the crappy maps
    Mar 03 11:20:29   but that is after the fact
    Mar 03 11:20:32  so if we have a policy of explaining publicly how the aliases are used (like they aren't tracked like "normal" names) then that woudl go far to helping to build that trust
    Mar 03 11:20:44   explaining is not enough
    Mar 03 11:20:51   I would demand that they CAN not be tracked
    Mar 03 11:20:54   ensured by technical means
    Mar 03 11:21:05   this might be possible though
    Mar 03 11:21:16  isn't such a claimn (a privacy policy) a legal thing?
    Mar 03 11:21:21   no
    Mar 03 11:21:27   nobody is bound to these things anyway
    Mar 03 11:21:35   I want such a claim based on how the system actually works
    Mar 03 11:21:42   like, based on which info is sent to whom
    Mar 03 11:22:18  how could anyone from a player perspective technically verify that?
    Mar 03 11:22:37   well, if the algorithms are open and it is proven that it ensures anonymity
    Mar 03 11:22:46   then one can verify it on his own, or ask a cryptography professor about it :P
    Mar 03 11:22:51   sort of like how open source works
    Mar 03 11:22:53  and do you always require such technical verification of tracking privacy when you use a service? like irc.quakenet.org?
    Mar 03 11:22:55  I think I missed part of the convo, but an quick idea; When it comes to keeping your privacy from your client that you are connecting through (in terms of not giving away your IP addreess, etc) maye we can make a client switch for that. Although, that would make it easier for people to avoid ip-based bans.
    Mar 03 11:23:14   that is the problem, right
    Mar 03 11:23:32   the IP is nothing I am concenred about, as mine is dynamic anyway
    Mar 03 11:24:13  well ok... if the algorithm is open
    Mar 03 11:24:15  Servers have such an option theirselves. I set mine to allow the IP to be visible.
    Mar 03 11:24:19  then that is another measure to ensure trust
    Mar 03 11:24:23   Dokujisan: exactly
    Mar 03 11:24:32  very much like the claim, but just with a little more evidence
    Mar 03 11:24:33   and basically, I'd like an open algorithm that allows anonymous clienrts
    Mar 03 11:24:38   exactly
    Mar 03 11:25:00   actually, there are means for this, now that I think of it
    Mar 03 11:25:06   actually, there are means for this, now that I think of it
    Mar 03 11:25:13   know the term "electronic money"?
    Mar 03 11:25:26   basically, it's a number generated both by a server and by a client
    Mar 03 11:25:27  ok, if such a thing were to happen, and aliases were not tracked like normal registered names would be (for stats), then if someone "hacked" into the central server...they woudln't have access to anything of value aside from an email address
    Mar 03 11:25:31   but so that it can be verified, is unique
    Mar 03 11:25:41   BUT: the server cannot later find out which client has hte number
    Mar 03 11:25:45   as the client made the final calculation
    Mar 03 11:25:55   so the client uses a number he calculated together with the server
    Mar 03 11:26:06   but the server does not have a way of knowing to which client he gave it
    Mar 03 11:26:12   as it doesn't know the final calculation the client did
    Mar 03 11:26:31   that is how one could generate an anonymous player ID
    Mar 03 11:26:43   it can still be tracked, in that it can be distinguished from others
    Mar 03 11:26:49   but nobody can find out who got that ID and when
    Mar 03 11:27:12   with 4, 5 of these IDs, I think I'd be anonymous enough
    Mar 03 11:27:31   just... why wouldn't XSAX create such an ID too then :P
    Mar 03 11:27:49   basically, thsi creates IDs that are, mathematically, "detached" from the identity who ordered them
    Mar 03 11:27:55   so I would give the web site my email address
    Mar 03 11:28:03   but later it'd be impossible to link the email address to my ID
    Mar 03 11:28:27   the web site still would be able to e.g. limit IDs to at most one per email address per week
    Mar 03 11:28:29  so with such a system in place, a system that goes to great lengths to ensure privacy for those who seek it, would you still elect not to use servers that utilize the central registration system?
    Mar 03 11:28:45   with such a system, I probably would use servers that use such a system
    Mar 03 11:28:53   as I would KNOW that the ID cannot be linked to my identity in any way
    Mar 03 11:29:16   also, I would KNOW I can make a new one every week :P
    Mar 03 11:29:32   so it can't be used for long-term tracking if I don't want to
    Mar 03 11:29:50  you mean the primary player name? or the aliases?
    Mar 03 11:30:05   both
    Mar 03 11:30:13   all player IDs could use such a scheme
    Mar 03 11:30:29   a player is free to associate the ID with his actual name (e.g. by registering his nickname) at any time
    Mar 03 11:30:52   of course, he'd then have to actually KEEP using that ID, or he wouldn't be able to use his nickname any more :P
    Mar 03 11:32:57  so... using the system you described, if I register with the primary name of Dokujisan and I have aliases of Alice and Bob... if I go onto HOCTF server as "Alice" and begin calling people names and spamming. The admin could ban me. If I try to relogin to that server as "Bob", it would maintain the ban? 
    Mar 03 11:33:38   no
    Mar 03 11:33:40  the central system would somehow know that "Bob" was also banned
    Mar 03 11:33:46   that is impossible
    Mar 03 11:33:55   but, you can only register one such ID every week
    Mar 03 11:34:01   so a troll would run out fast
    Mar 03 11:34:07  oh I see
    Mar 03 11:34:12  so that is the limiting mechanism
    Mar 03 11:34:15   basically:
    Mar 03 11:34:28   the ID generating server remembers your address, and prevents too frequent registration
    Mar 03 11:34:33   but: it does not know which the ID is that you got
    Mar 03 11:34:47   the game can verify your ID - but cannot link it to your address or anything else
    Mar 03 11:34:56   unless you voluntarily give the game the info (e.g. by registering your nick)
    Mar 03 11:35:22   I can implement that crypto scheme, BTW
    Mar 03 11:35:28   I remembered how it works
    Mar 03 11:36:43   one keyword for it is "blind signatures"
    Mar 03 11:36:51   http://ntrg.cs.tcd.ie/mepeirce/Project/Press/digibro.html
    Mar 03 11:36:54   like at the end of that page
    Mar 03 11:38:04   in this case, the "bank" does not know which number I wanted it to sign...
    Mar 03 11:38:06   but it is not perfect
    Mar 03 11:38:19   in that specific protocol, I can still cheat a bit
    Mar 03 11:39:01   but that can be prevented too :P
    Mar 03 11:39:20   (by requiring the "x" to have a special pattern, that is unlikely to come when you modify the signature)
    Mar 03 11:40:20   e.g.: x may be a hash value of a string that is like "NEXIUZ PLAYER ID #43984398"
    Mar 03 11:40:33   and as ID, you'd present both the string and the signature
    Mar 03 11:40:45   if the hash function is good, you can't manipulate the signature
    Mar 03 11:41:32   note that that string would not really be your "ID" :P
    Mar 03 11:41:48   so if the number matches between two players, that is no problem, as the signature still would not match
    Mar 03 11:44:08   1. s = "NEXUIZ PLAYER ID #474574598798"
    Mar 03 11:44:09   2. h = SHA1(s)
    Mar 03 11:44:11   3. r = random
    Mar 03 11:44:14   4. x = h*r^publickey
    Mar 03 11:44:15   5. send x to auth server, get back y which auth server calculates as x^privatekey
    Mar 03 11:44:18   6. t = y/r
    Mar 03 11:44:20   7. The full player ID is s together with t
    Mar 03 11:44:34   to verify, the server would check the ID starts with "NEXUIZ PLAYER ID #", and that the signature matches too
    Mar 03 11:46:01   that scheme is from 1983 by the way
    Mar 03 11:46:10   so if it was patented, the patents have expired now
    Mar 03 11:47:14   I'll probbaly code that soon, but first check it for possible other security problems
    Mar 03 11:48:39   have to go now though
    Mar 03 11:48:40  if we could nail down a privacy-safe central user system, that would allow a lot of other features to be added to the game
    Mar 03 11:48:45   I'll look up more stuff on it
    Mar 03 11:48:53   "electronic money" is the keyword for it though
    Mar 03 11:49:13   basically, the general idea is to make sure that not even the owner of the auth server can know WHO owns a specific key
    Mar 03 11:49:40   and to provide banning by limiting the number of keys generated
    Mar 03 11:50:18   this speciifc scheme has a little problem though, but I once saw the solution for that in a book
    Mar 03 11:50:26   I'll check in that book later :P
    Mar 03 11:55:20  in the meantime, -z- and I were scanning around for open domain names as a name alternative to nexuiz
    Mar 03 11:55:25  Alright, while we're all here. I've had a question for a looong time now (separate from all this). What server do the devs play on? I usually play on the DCC servers, but would have liked to play with div0, [-z-] and all the other core devs once.
    Mar 03 11:55:57 <[-z-]> recently the HO servers because they are the most well kept USA servers
    Mar 03 11:56:21 <[-z-]> bbiab, need to get lunch
    Mar 03 11:56:31  Thanks. USA probably means low ping from Europe
    Mar 03 11:58:48 <[-z-]> yes but I've played on DCC before and Over the Lazy Dog
    Mar 03 12:02:12 <[-z-]> lets get brainstorming about names
    Mar 03 12:05:55  NOT AVAILABLE
    Mar 03 12:05:55  nexotic
    Mar 03 12:05:55  nexetic
    Mar 03 12:05:55  nexon
    Mar 03 12:05:55  nexuz
    Mar 03 12:05:55  nexine
    Mar 03 12:05:55  nexean
    Mar 03 12:05:55  nexio
    Mar 03 12:05:55  nexium
    Mar 03 12:05:55  nexun
    Mar 03 12:05:55  xenios
    Mar 03 12:05:55  xenius
    Mar 03 12:05:55  xenoic
    Mar 03 12:05:55  xenotic
    Mar 03 12:05:55  AVAILABLE
    Mar 03 12:05:55  nexotus
    Mar 03 12:05:55  nexaen
    Mar 03 12:05:55  nexilus
    Mar 03 12:05:55  zeniux
    Mar 03 12:20:36  some proposed Nexiuz, already used for the current site redirect (nexiuz.org ). I also thought about naming it Zymotic, after the dead project which was named that way.
    Mar 03 12:21:24  if it's being forked, I wouldn't use something that would be mistaken for Nexuiz. But a similar-style name would be good.
    Mar 03 12:41:40 <[-z-]> wwi own nexiuz.org
    Mar 03 13:05:33   Taoki: I play on whatever is at the top, or my own
    Mar 03 13:05:43   and sometimes arranged stuff with PB
    Mar 03 13:06:14   I recently changed my server to KH only, to give better experience maybe
    Mar 03 13:06:30  I could never get into KH. I tried for a week once
    Mar 03 13:06:40  I like clan arena though
    Mar 03 13:06:49  that was a great addition
    Mar 03 13:34:02  Dokujisan, from the list of names you posted earlier (couldn't think of any on my own, am generally bad with names) the last one, zeniux, sounds prettiest and most fitting. Or a derivate of that.
    Mar 03 13:34:47  But, before finding a new name, I think m0ost important is finding a way to let people who don't visit the forums and such know that Nexuiz was renamed. Otherwise, many players may think it just vanished forever all of a sudden, and find out in months or years it's still there
    Mar 03 13:35:12   well
    Mar 03 13:35:39  Not sure how that could be done... was thinking that maybe we could find all news articles about Nexuiz on google and see how we could modify each
    Mar 03 13:35:41   I do think that Alientrap won't follow the project when we take over
    Mar 03 13:35:43   so...
    Mar 03 13:35:52   it shouldn't be impossible to get it displayed in game :P
    Mar 03 13:36:00   we have ways to show such a notification
    Mar 03 13:36:13   yes, the rotating yellow box :P
    Mar 03 13:36:38   also, we can organize some server admins, and let them show this when people join their server
    Mar 03 13:36:39  How? Does the gamecode support a way to show news from an external page?
    Mar 03 13:36:43   know my "mikeeusa warning"?
    Mar 03 13:36:49   not yet
    Mar 03 13:36:54  Not really
    Mar 03 13:36:57   can onyl show a single line of text in the update notification
    Mar 03 13:37:05   but with csqc, you can show a on-join dialog on a server
    Mar 03 13:37:11   so if enough server admins would take over that code
    Mar 03 13:37:15  Wow, i didn't know thre is an update notification.
    Mar 03 13:37:15   most people will know
    Mar 03 13:37:48  Another good idea would be servers (like DCC) putting the news in their MOTD or periodic helper script messages
    Mar 03 13:38:21   right
    Mar 03 13:38:26   or more visible than MOTD :P
    Mar 03 13:38:31   csqc leaves many possibilities for this
    Mar 03 13:38:48  yeah, there is a way to make a message be echoed to anyone when joining, like normal chat.
    Mar 03 13:39:12   that too
    Mar 03 13:39:15   but well
    Mar 03 13:39:19   we can modify code :P
    Mar 03 13:39:26   I have on my server some more-or-less secret feature
    Mar 03 13:39:31   that warns that a map is by mikeeusa :P
    Mar 03 13:39:52   in form of a dialog box that you have to close by pressing a button
    Mar 03 13:40:44  hehe realy?
    Mar 03 13:41:15  fun :P
    Mar 03 13:41:45  Ooh, right... by having separate CSQC on a server which gets downloaded if it doesn't match yours
    Mar 03 13:41:51  forgot that :P
    Mar 03 13:42:03   right
    Mar 03 13:42:06   we can do a LOT with that
    Mar 03 13:42:50  If we're lucky, we may be able to change the name without loosing a lot of popularity.
    Mar 03 13:43:17   we may even gain more
    Mar 03 13:43:32   because many players probably still think that Nexuiz is the sucky game it was at 1.x times :P
    Mar 03 13:43:44  Then, separately, maybe we can google for all news articles which talk about Nexuiz (be them years old) and ask them to change the names, if the admins and system would allow that. So people finding them won't be confused too
    Mar 03 13:43:58   no, changing news of the past is bad
    Mar 03 13:44:00   don't go there
    Mar 03 13:44:08  hmm ok then
    Mar 03 13:44:10   those who rewrite history are damned to repeat it :P
    Mar 03 13:44:21  makes sense :)
    Mar 03 13:44:26   but, it'd be nice if they could write an update note to the articles :P
    Mar 03 13:45:00  Yeah, would be excellent. Enough so someone who seen Nexuiz disappeared and goodles Nexuiz gets an article on the first page mentioning it got renamed
    Mar 03 13:45:27 <[-z-]> I can still post news
    Mar 03 13:45:34 <[-z-]> I haven't because Vermeulen said he was going to
    Mar 03 13:45:46 <[-z-]> but he hasn't
    Mar 03 13:47:10 <[-z-]> unizex :-P
    Mar 03 13:47:22  :P
    Mar 03 13:47:28 <[-z-]> zenuxi
    Mar 03 13:47:45 <[-z-]> zah new zi
    Mar 03 13:48:43 <[-z-]> have we decided on a name of either the group or game?
    Mar 03 13:48:51  I like Zeniux or something similar... that was a good idea Dokujisan included.
    Mar 03 13:49:50  Or Zenuix, would resemble the old name more
    Mar 03 13:53:26   we should test the name ideas somehow
    Mar 03 13:53:38   like, try them in a typing test software :P
    Mar 03 13:53:44   to see which variant gets more misztakes
    Mar 03 13:55:06 <[-z-]> zenuix sounds the smoothest of all the paladrome names thrown out and is more phonetic than nexuiz :-P
    Mar 03 13:55:06  whatever happens with the name, I would like to spend some time to brainstorm for the right name that has an available .com
    Mar 03 13:55:21  and not pick a name hastily
    Mar 03 13:56:24 <[-z-]> group name first might help decide the game name
    Mar 03 13:57:06 <[-z-]> who are we? what brings us together? what are we looking to achieve? who are we looking to attract?
    Mar 03 13:57:09  oh right
    Mar 03 13:57:11  the group name
    Mar 03 13:57:33  with getty, we came up with conflict industries for that group. That works well. For this group... um.....
    Mar 03 13:58:40  I had been thinking something I mentioned it ysterday. Does anyone believe we may be better without a group name? I seen many projects like that... there are just contributors and no group with a different name. Or they're called "TheProjectName Team"
    Mar 03 13:58:59  This could, from some angles, and some ways, seem a little bit more free too
    Mar 03 13:59:20  the group name really helps. If the group does not intend to make any other games, then it can go without a separate group, but a name based on the game name
    Mar 03 13:59:24 <[-z-]> well... it takes a lot of people working together to design, create and distribute te game.
    Mar 03 14:00:03 <[-z-]> we'll continue to accept contributions and patches from outside parties, divVerent has actually proposed a good way to setup git to accompany this
    Mar 03 14:00:27  like alientrap always intended to make more games than nexuiz. Conflict industries intends to do the same. If this "New Nexuiz" group doesn't intend to make other games, then the group name can be like "Nexuiz Team"
    Mar 03 14:00:40  like my Kickboxing form (called Ax) I call the moderators the "Ax Team"
    Mar 03 14:01:07 <[-z-]> I'd like to hope we could create more games if not projects together
    Mar 03 14:01:16  yeah
    Mar 03 14:01:35 <[-z-]> there are already a few mods that run on top of nexuiz, who knows which way they'll go after the fork
    Mar 03 14:02:03 <[-z-]> if alientrap drops support, then they'll likely run off our game code
    Mar 03 14:03:36  ok I'm not against the idea of this group working on other games. Sounds great. 
    Mar 03 14:03:38  I play two other games (about different things) which are open source, and not officially developed by a specific team. Just for the note  if anyone's curious, they are Vdrift http://vdrift.net/ (best opensource car game imo) and glest http://glest.org/en/index.php (best opensource rts game)
    Mar 03 14:05:11  On the about page of Glest, they say "Glest is made by a bunch of friends, most of them from Spain". Of course this doesn't mean it would be the best idea for Nexuiz.
    Mar 03 14:05:15 <[-z-]> someone still has to be in control at some point
    Mar 03 14:05:27  yeah
    Mar 03 14:05:40 <[-z-]> we're trying to build a group that won't die from having a single or even just 2 leaders
    Mar 03 14:06:00 <[-z-]> but rather a board or committee, divVerent would like to see 3
    Mar 03 14:06:03  ok what is a creative way of describing that arrangement
    Mar 03 14:06:17  even imagery
    Mar 03 14:06:24 <[-z-]> who me or Taoki?
    Mar 03 14:06:28  like a wheel with spokes
    Mar 03 14:06:30  you
    Mar 03 14:07:00  the arrangement of the group, or the method upon which it is created
    Mar 03 14:07:17 <[-z-]> a wheel with spokes connecting to a group (committee) in the center
    Mar 03 14:09:07   shouldn't group name the same as the game name?
    Mar 03 14:09:29  well as I said earlier, that depends on whether the group works on multiple games
    Mar 03 14:09:33  if it's just one game, then sure
    Mar 03 14:09:43   I don't think we want to
    Mar 03 14:09:51   maybe as side projects, with not all members part of it
    Mar 03 14:10:03   but that can then be a new group, cooperating with the "nexuiz group"
    Mar 03 14:10:13  ok. I'm fine with that
    Mar 03 14:10:26   I mean, such groups are not exclusive
    Mar 03 14:10:33 <[-z-]> isn't that just a more complicated way of saying we'll figure out a team name later?
    Mar 03 14:10:37   e.g. Taoki made that spinoff game once, didn't he?
    Mar 03 14:10:41   We could cooperate in that too :P
    Mar 03 14:10:44 <[-z-]> he's still working on it
    Mar 03 14:10:47   e.g. when I provide a build system...
    Mar 03 14:10:57   I can happily use my build system for his project too
    Mar 03 14:11:08  I like the idea of just calling it  Team
    Mar 03 14:11:10   even without being part of his development
    Mar 03 14:11:14   yes, so do I
    Mar 03 14:11:54 <[-z-]> k, whatever, I don't care that much about the name
    Mar 03 14:12:01  That own game i'm making from Nexuiz? I still work on it... just took a brake now since i worked on it a lot at first
    Mar 03 14:12:17  Also waiting for FruitieX's HUD changes, i'll have to merge these with my hud and stuff. But yeah
    Mar 03 14:12:27  I'm also interested in that game, btw
    Mar 03 14:12:30   I just still don't like Zenuix...
    Mar 03 14:12:34  ok
    Mar 03 14:12:40   I am not sure if I am interested in that game
    Mar 03 14:12:48 <[-z-]> it doesn't even have to ben a palindrome
    Mar 03 14:12:53   but even if not, I'd have no reason to not help out with e.g. making its release builds
    Mar 03 14:12:55 <[-z-]> err
    Mar 03 14:12:59  Thanks Dokujisan :) Not sure how it will be like... it will be something of a different theme. Not sure if i can get it to what i want it to be
    Mar 03 14:13:01   anagram
    Mar 03 14:13:04 <[-z-]> yes, that one :)
    Mar 03 14:13:08  well I like the theme that you described
    Mar 03 14:13:14   zenuiz may be better than zenuix BTW
    Mar 03 14:13:21   because, I have typo'd zenuiz when trying to write zenuix
    Mar 03 14:13:49 <[-z-]> xenuiz?
    Mar 03 14:13:52   no
    Mar 03 14:13:55   that sounds like Xen
    Mar 03 14:13:57   which was a flop
    Mar 03 14:14:04  I'd still like the wat the first name sounds more
    Mar 03 14:14:14   which?
    Mar 03 14:14:29  Zenuix
    Mar 03 14:14:44   I just find it too hard to remmeber/type
    Mar 03 14:14:48   sort of the same fault as Nexuiz has
    Mar 03 14:15:06  Yeah, but it kinda sounds and looks prettier
    Mar 03 14:15:29   is it pronounced Zen-u-ix, Ze-nu-ix, ze-nu-i-kku-su, or or Zen-i-us?
    Mar 03 14:15:41 <[-z-]> first
    Mar 03 14:15:46   not zenuikkusu?
    Mar 03 14:15:53 <[-z-]> I mean, you can if you want
    Mar 03 14:16:03   (latter is how the japanese would pronounce zenuix)
    Mar 03 14:16:41 <[-z-]> zenuiz (not japanese)
    Mar 03 14:16:54   that name would be way more japanese friendly :P
    Mar 03 14:16:54 <[-z-]> haha, I just typoed zenuix too
    Mar 03 14:17:10   zenuizu would be their katakana writing of it
    Mar 03 14:17:11 <[-z-]> zen you iz
    Mar 03 14:17:28 <[-z-]> what does zenuizu mean?
    Mar 03 14:17:31   nothing
    Mar 03 14:17:39 <[-z-]> (we're back with an even harder to pronounce name)
    Mar 03 14:17:41   I just spelt it in a sequence of katakana characters
    Mar 03 14:17:52   like the japanese do to all foreign words
    Mar 03 14:17:57 *   Dokujisan is brainstorming names and checking for available .coms
    Mar 03 14:18:01   e.g. floppy disk = fu-ro-ppi de-i-su-ku
    Mar 03 14:18:19 <[-z-]> I'm not sure if zenuiz is just because of muscle memory though
    Mar 03 14:18:27   yes
    Mar 03 14:18:29 <[-z-]> what if you asked a random person to type it
    Mar 03 14:18:29   that may be too
    Mar 03 14:18:43   basically... I think it maybe shouldn't have an ui in it :P
    Mar 03 14:18:47 <[-z-]> haha
    Mar 03 14:18:56 <[-z-]> that actually made it easier for me to spell
    Mar 03 14:18:57   Inflexion Uzi CL
    Mar 03 14:19:02   an anagram to illfonicnexuiz
    Mar 03 14:19:08 <[-z-]> ;)
    Mar 03 14:19:38 <[-z-]> necksuiz
    Mar 03 14:19:49   no, does not solve anything :P
    Mar 03 14:19:55 <[-z-]> makes it worse lol :)
    Mar 03 14:19:58   yes
    Mar 03 14:20:02   zeckniuz
    Mar 03 14:20:14   no
    Mar 03 14:20:19 <[-z-]> zexiznice
    Mar 03 14:20:20   sounds like a zecke, evil animal in germany
    Mar 03 14:20:29   Zexiz
    Mar 03 14:20:32   haha :P
    Mar 03 14:20:33   "Sex-is"
    Mar 03 14:20:40   oh wait
    Mar 03 14:20:46   you actually intended that
    Mar 03 14:20:49 <[-z-]> yeah :-P
    Mar 03 14:21:04 <[-z-]> I would never suggest that as a real game name lol
    Mar 03 14:21:08   Xettius
    Mar 03 14:21:15 <[-z-]> :mind sploded:
    Mar 03 14:21:18   oh, I had first parsed it as "zexis - nice"
    Mar 03 14:21:26   *z
    Mar 03 14:21:29 <[-z-]> hehe
    Mar 03 14:21:49   Textius - the text adventure port
    Mar 03 14:22:03  man... a lot of strange domain names are already taken
    Mar 03 14:22:05 <[-z-]> do we even want to stick with these weird arrangements of letters?
    Mar 03 14:22:08  AVAILABLE .COMs
    Mar 03 14:22:08  nexotus
    Mar 03 14:22:08  nexilus
    Mar 03 14:22:08  zeniux
    Mar 03 14:22:08  xepharis
    Mar 03 14:22:08  xaleco
    Mar 03 14:22:08  xeleka
    Mar 03 14:22:08  xeleca
    Mar 03 14:22:08  xelecon
    Mar 03 14:22:10   You are standing on a pink reflecting floor. You hear rocket noises.+
    Mar 03 14:22:12   > GO LEFT
    Mar 03 14:22:21   does anyone recognize the map?
    Mar 03 14:22:21 <[-z-]> we want a .org though, no?
    Mar 03 14:22:25   see, text adventure works
    Mar 03 14:22:26   yes
    Mar 03 14:22:31  if the .com is available, the .org definitely is
    Mar 03 14:22:34  and I think we should get both
    Mar 03 14:22:38  and redirect the .com
    Mar 03 14:22:44   Xepharis wtf
    Mar 03 14:22:49   reminds of the old Project Alaris
    Mar 03 14:22:57  just brainstorming. I started with nex*
    Mar 03 14:22:58 <[-z-]> xenuiz haha (xenu is)
    Mar 03 14:23:03  haha
    Mar 03 14:23:13   no, cannot accept that with my belief :P
    Mar 03 14:23:22 <[-z-]> haha, I'm just kidding
    Mar 03 14:23:28   but I would never have spotted it
    Mar 03 14:23:42 <[-z-]> ?
    Mar 03 14:23:48   rather rejected that suggestion above because it started with Xen, and Xen was unsuccessful virtualization
    Mar 03 14:23:55 <[-z-]> ah yes :-P
    Mar 03 14:23:58   (replaced by KVM)
    Mar 03 14:24:23   Davius
    Mar 03 14:24:27   from [Dave]
    Mar 03 14:24:30 <[-z-]> :-P
    Mar 03 14:24:33  haha
    Mar 03 14:24:44 <[-z-]> daviuz?
    Mar 03 14:24:48   or maybe even Daviuz
    Mar 03 14:24:57   but it gets in the hard-to-spell region again
    Mar 03 14:25:01   Dave Ius
    Mar 03 14:25:07   "The justice of Dave"+
    Mar 03 14:25:14 <[-z-]> davefps
    Mar 03 14:25:21   DaveDaveDave
    Mar 03 14:25:24 <[-z-]> or just dave
    Mar 03 14:25:30   KillDave
    Mar 03 14:25:38 <[-z-]> killdavekill
    Mar 03 14:26:01 <[-z-]> gokilldave
    Mar 03 14:26:02   OMGTKDave
    Mar 03 14:26:12   (Bastards edition)
    Mar 03 14:26:30   Davidiuz
    Mar 03 14:26:38 <[-z-]> davefps.org is available
    Mar 03 14:26:51   is anyone here called Dave? :P
    Mar 03 14:26:58   I mean, apart from everyone ;)
    Mar 03 14:27:01 <[-z-]> :-P
    Mar 03 14:27:05 <[-z-]> no
    Mar 03 14:27:15   BTW, I had reliable sources tell me that morphed would be in our team too
    Mar 03 14:27:30  I suspect that most would want to move over
    Mar 03 14:27:36   just wanted to say
    Mar 03 14:27:40   if we can even get morphed
    Mar 03 14:27:42  but yes, that is good
    Mar 03 14:27:43   we'd get everyone :P
    Mar 03 14:27:46 <[-z-]> it's good to have his support
    Mar 03 14:28:10   morphed may work uncleanly, and be a bit weird-creative... so he often has to be put in his bounds :P but we need that creativity
    Mar 03 14:28:11 <[-z-]> we need to get setup so we have something for them to move to
    Mar 03 14:28:17  is it possible to do this without telling mikee about it?
    Mar 03 14:28:24   no
    Mar 03 14:28:28  :-)
    Mar 03 14:28:29   but we can wait with telling mikee
    Mar 03 14:28:34   mikee isn't too clever to find out on his own
    Mar 03 14:28:47   it's just that he reads the forum
    Mar 03 14:28:55   as for hosting... well, we could use the icculus repository
    Mar 03 14:29:03   but I'd prefer it on the new domain
    Mar 03 14:29:10 <[-z-]> is everyone good with davefps ?
    Mar 03 14:29:14   [-z-]: how expensive is domain hosting with "sort of unlimited" traffic?
    Mar 03 14:29:18   DaveFPS... not so sure yet
    Mar 03 14:29:20   but maybe
    Mar 03 14:29:21 <[-z-]> ~$120 a year
    Mar 03 14:29:22   a bit too generic maybe
    Mar 03 14:29:24   googling it
    Mar 03 14:29:31   $10 a month... sounds okay
    Mar 03 14:29:35   so we could put the git on it too
    Mar 03 14:29:42   and with shell access?
    Mar 03 14:29:46   (for making the builds)
    Mar 03 14:29:47 <[-z-]> I believe they support git now yes
    Mar 03 14:29:52 <[-z-]> and multiple unix accounts, yes
    Mar 03 14:29:58   they don't have to support git :P
    Mar 03 14:30:01 <[-z-]> and sftp only accounts
    Mar 03 14:30:09   we can install it in one of the unix accounts
    Mar 03 14:30:13   and set up gitolite on it
    Mar 03 14:30:22   that is actually how you host git
    Mar 03 14:30:28 <[-z-]> div0: well they also have a web frontend, I don't know how helpful it is for setting up git though
    Mar 03 14:30:41   only problem wqould be the git daemon, that probably would require asking them and them saying "go ahead, you can use the network port"
    Mar 03 14:30:54   for repository write access you go through ssh anyway
    Mar 03 14:31:10 <[-z-]> http://wiki.dreamhost.com/Git
    Mar 03 14:31:17   for the record, git is port 9418
    Mar 03 14:31:24  I need to go for the next 1-2 hours. See you all when I get back, take care. I'll try to think of a new name more :)
    Mar 03 14:31:37 <[-z-]> okay Taoki, see you
    Mar 03 14:32:19   only problem is, they write that they currently do not support git-daemon
    Mar 03 14:32:21   that is a setback
    Mar 03 14:32:31 <[-z-]> well, why not stay on icculus?
    Mar 03 14:32:45   could do that too, at least for a start
    Mar 03 14:32:47  isn't icculus slow?
    Mar 03 14:32:51   that it is
    Mar 03 14:32:53  I always got that impression from it
    Mar 03 14:32:57   I just think this should be hosted on the project domain, if possible
    Mar 03 14:33:08   if nothing else works, we can still offer the git read access via http
    Mar 03 14:33:12   but that will sometimes fail
    Mar 03 14:33:39   can still have a readonly clone of it on other hosts :P
    Mar 03 14:34:01 <[-z-]> hmm, I can't really offer the vps up if it's going to be running gameservers
    Mar 03 14:34:04   so actually, we could offer readonly access via http or on icculus, and otherwise use dreamhost
    Mar 03 14:34:06   thagt would work
    Mar 03 14:34:41   via http may be good enough, git devs say we should not do that, but I don't know why other than one has to regularily call git-update-server-info
    Mar 03 14:35:17  hmm... ok I'm liking xun* as a prefix
    Mar 03 14:35:40 <[-z-]> I dunno :-\
    Mar 03 14:35:40  man, soooo many strange domain names are taken.
    Mar 03 14:39:37   Xunius?
    Mar 03 14:39:38   Xunion?
    Mar 03 14:43:28  more avialable .coms...
    Mar 03 14:43:29  xuniam
    Mar 03 14:43:29  xuniox
    Mar 03 14:43:29  xunium
    Mar 03 14:43:29  xundem
    Mar 03 14:43:29  xunius
    Mar 03 14:43:29  xuniux
    Mar 03 14:43:29  xudex
    Mar 03 14:44:26  xodim
    Mar 03 14:44:35   [-z-]: does dreamhost support CGI?
    Mar 03 14:46:50   because if it does
    Mar 03 14:46:53 <[-z-]> hmm, I believe so
    Mar 03 14:46:54   we can cleanly host git over HTTP
    Mar 03 14:46:56   (for newer git clients)
    Mar 03 14:47:05   for older clients, it'll fall back to the a bit clumsy HTTP method
    Mar 03 14:47:06   but still work
    Mar 03 14:47:12   just download more data than needed
    Mar 03 14:48:11   oh, cronjobs?
    Mar 03 14:48:39   (not THAT important for us, though)
    Mar 03 14:51:29  xodem
    Mar 03 14:51:29  xotux
    Mar 03 14:51:29  nodium
    Mar 03 14:52:50   Tuxius
    Mar 03 14:52:57   Tuxiuz
    Mar 03 14:52:59   is hard to type
    Mar 03 15:04:02  dellum
    Mar 03 15:04:14  nodius
    Mar 03 15:04:14  xodeos
    Mar 03 15:04:14  modiem
    Mar 03 15:04:14  xovium
    Mar 03 15:04:14  xovim
    Mar 03 15:05:38  xendem
    Mar 03 15:06:13  xelod
    Mar 03 15:06:39  xilod
    Mar 03 15:13:07  microsoftiux
    Mar 03 15:13:10  ..j/k
    Mar 03 17:02:48  Back. Thought abouc a little new bunch of names...
    Mar 03 17:02:50  *about
    Mar 03 17:03:16  Not really the best but oh well. My list is:
    Mar 03 17:03:39  Zenuix, Zenux, Zenus, Nexuz
    Mar 03 17:03:56  the 2nd and 3rd sound best to me. As for team names,
    Mar 03 17:05:17  I'm totally not good at these so my ideas are mostly silly. Was still thinking of something with Alien... the only idea that came to my mind was openAlien (please ignore this though... I mean... :P ) Another idea about the team name, was something related to nexuizninjaz, which imo has been a great resource. Something having to do with that would be nice to
    Mar 03 17:05:38  Like, openNinjaz, Alien Ninjaz... these are just sillq quick thoughts once again
    Mar 03 17:08:35  Sorry for the several typos >.>
    Mar 03 17:12:15  What does everyone think? Would Zenux (without the i like my previous suggestion) or Zenus be anything good?
    Mar 03 17:17:35  I like the idea of something that contains both Z and X
    Mar 03 18:52:36 <[-z-]> hahaah, mikeeusa's suggestion:
    Mar 03 18:52:37 <[-z-]> Nexuiz:Depreciated
    Mar 03 18:53:00 <[-z-]> he goes on to say
    Mar 03 18:53:02 <[-z-]> "but translated into german so it sounds germanish. German is... a dark tounge. Makes everything sound strenghtful."
    Mar 03 18:54:34  hehe
    Mar 03 18:56:15 *   Samual (~sam@c-24-131-80-234.hsd1.pa.comcast.net) has joined #notnexuiz
    Mar 03 18:56:20     Heh
    Mar 03 18:56:21     Clever.
    Mar 03 18:56:31 <[-z-]> welcome Samual
    Mar 03 18:56:43     Who is active/idle?
    Mar 03 18:56:59 <[-z-]> Taoki is active, div0 and Dokujisan might be around
    Mar 03 18:57:20 <[-z-]> we were discussing creating a group based around the fork of the yet to be named game
    Mar 03 18:57:40 <[-z-]> something with a better spread of power distributed across a few "major leaders"
    Mar 03 18:58:12  I'm hre
    Mar 03 18:58:16     Well meh
    Mar 03 18:58:34 <[-z-]> we've talked about servers, repository hosting and what not
    Mar 03 18:58:45 <[-z-]> it sounds like we have enough to continue building releases cross platform
    Mar 03 18:59:26 <[-z-]> we can take the time to get more organized from a web point of view as well
    Mar 03 18:59:28     It's a huge step to abandon Nexuiz though :P
    Mar 03 18:59:37 <[-z-]> do you want to stay under alientrap?
    Mar 03 18:59:52     Well
    Mar 03 19:00:12     Vermeulen fails, but it's -- It's still hard to abandon Nexuiz :P
    Mar 03 19:00:35 <[-z-]> it's no longer nexuiz and the sooner we all accept that, the sooner we can move on
    Mar 03 19:01:35     Meh.
    Mar 03 19:02:14 <[-z-]> it sucks but there isn't much we can do
    Mar 03 19:02:33     I'd much rather work on a game with new content though.
    Mar 03 19:04:05     Not necessarily different gameplay, just new artwork/design. If there's one thing that has been shown with this is that an overall theme for a game can go a long way to making it look consistently good.
    Mar 03 19:09:05  New content will come over time. Hopefully, some new artwork too. Of course, I hope no one is really thinking about throwing away everything that has been done in 5 years and starting from a scratch.
    Mar 03 19:11:24  What was done so far is too good and too important. And I'm sure that in a few years from now, it will be incredible compared to what it is now
    Mar 03 19:11:43  (I'm still dreaming about this project looking like UT3, someday :P )
    Mar 03 19:12:44 <[-z-]> I'm willing to submit more and may be able to get more from others, we just need to outline our needs
    Mar 03 19:14:14  I wish I could model. I can hardly make a boulder in Blender though :(
    Mar 03 19:15:08  I can edit existing models to some point (how I made my vixens from pyria) but new models at the quality of the UT 2k4 / UT 3 guns... those have to be very hard to make
    Mar 03 19:20:58     lawl anyway I think i'm done with Nexuiz officially now, since this person clearly has no intention of changing the name and he doesn't want to listen to the community much.
    Mar 03 19:22:33  It would be sad if you left, Samural. Would be sad if anyone really left...
    Mar 03 19:26:29     lawl well everyone here has been discussing leaving too anyway
    Mar 03 19:26:54 *   [-z-] gives channel operator status to Samual
    Mar 03 19:26:58  If anyone wants to leave, it is of course their choice. I just want to highlight that... in my vision this is not a reason to completely loose faith. Because the project we kept working on for all these years is still here, and will always be here. So if we were with Nexuiz for these years because we liked -it-, although this has undoubtfully upset us greatly, we can keep being with it from now on
    Mar 03 19:27:44 <[-z-]> I just don't want to work for a "Company" that represents such shiesty practices
    Mar 03 19:27:46  It is still th same code, same experience, etc. If the reason was to modify this code, and parts of what the game is now, and to enjoy what exists in it, then this won't stop us
    Mar 03 19:28:43  Whatever its name will change to, its the same thing you will see when you load a map or the menu. Except the name banner which will be changed too. That doesn't go away... if thats what we've been with Nexuiz for we haven't lost anything.
    Mar 03 19:31:15  hey Samual 
    Mar 03 19:31:30     Hai.
    Mar 03 19:31:46  here is what I've searched so far in terms of domain names
    Mar 03 19:31:48  http://pastie.org/private/z1hlw1gs1d4nrxdvbisxsw
    Mar 03 19:33:17  Right... i wax curious what everyone thinks of my last two name ideas
    Mar 03 19:33:18  [00:11:51] <@Taoki> What does everyone think? Would Zenux (without the i like my previous suggestion) or Zenus be anything good?
    Mar 03 19:33:44  I always go by available domain names
    Mar 03 19:33:50  and zenux.com isn't available
    Mar 03 19:34:11  otherwise, that's a good name to consider
    Mar 03 19:34:59  hmm...
    Mar 03 19:38:14  From that list, my favs would be zeniux, xaleco, xuniox, xodeos
    Mar 03 19:38:16 *   Rad_Ished (~Dooley@cpc3-aztw19-0-0-cust362.aztw.cable.virginmedia.com) has joined #notnexuiz
    Mar 03 19:38:21 <[-z-]> hey Rad_Ished
    Mar 03 19:38:25  hi
    Mar 03 19:38:39 <[-z-]> zeniux or zenuiz?
    Mar 03 19:38:40  hey folks, i like not nexuiz
    Mar 03 19:38:43  good name
    Mar 03 19:38:54 <[-z-]> Rad_Ished: we've been trying to come up with a real one :-P
    Mar 03 19:38:59  heh
    Mar 03 19:39:17  z, I would prefer the first between the two
    Mar 03 19:39:18  zenuiz works for me
    Mar 03 19:39:27  ahhh zexnuix
    Mar 03 19:39:37  zeniux
    Mar 03 19:39:39  i meant argh
    Mar 03 19:39:43 <[-z-]> nexzex
    Mar 03 19:39:45  yeh , what he said
    Mar 03 19:39:50  nooo
    Mar 03 19:40:00  zeniux
    Mar 03 19:40:14  i don't feel im really adding anything here
    Mar 03 19:40:24   here is what I've searched so far in terms of domain names
    Mar 03 19:40:24   http://pastie.org/private/z1hlw1gs1d4nrxdvbisxsw
    Mar 03 19:40:46  i  thought that mikee's post was profound
    Mar 03 19:40:49 <[-z-]> we want a .org though, no?
    Mar 03 19:41:21 <[-z-]> xenix lol
    Mar 03 19:41:22 <[-z-]> penix
    Mar 03 19:41:51  Atm, my vote's on zeniux / zenuix / zenius
    Mar 03 19:41:53  :P
    Mar 03 19:42:05  or derivates of these
    Mar 03 19:42:06     Sexuiz is good
    Mar 03 19:42:10     But well
    Mar 03 19:42:12  zenuix
    Mar 03 19:42:13  :))
    Mar 03 19:42:31     Zexun?
    Mar 03 19:42:36 <[-z-]> haha, bit of trivia for ya'll, "throng" is a crowd of people
    Mar 03 19:42:49 <[-z-]> zexin
    Mar 03 19:42:57     Zexin too
    Mar 03 19:43:02     I like that >.>
    Mar 03 19:43:03 <[-z-]>  zexin.org  AVAILABLE
    Mar 03 19:43:19     ^_^
    Mar 03 19:43:23     .com?
    Mar 03 19:43:27 <[-z-]> 5 letters, not bad
    Mar 03 19:43:29 <[-z-]> no .com is taken
    Mar 03 19:43:32 <[-z-]> but do we want .com?
    Mar 03 19:43:32  Zexin sounds goodish, yeah
    Mar 03 19:43:43 <[-z-]> sqautter has it
    Mar 03 19:44:10     Nizex?
    Mar 03 19:44:12     lawl
    Mar 03 19:46:02 <[-z-]>  nexiz.org AVAILABLE
    Mar 03 19:46:09 <[-z-]> probably too similar
    Mar 03 19:46:14     Yeah that's too similar
    Mar 03 19:46:14     lawl
    Mar 03 19:52:29  I really think it's valuable to have the .com
    Mar 03 19:52:44  but if we don't have that as a requirement, then scan through those names I checked that are not available .coms
    Mar 03 19:53:00 <[-z-]> yean but we're not really a company?
    Mar 03 19:53:04 <[-z-]> more an organization
    Mar 03 19:53:06  it's not about that
    Mar 03 19:53:09  people know .coms
    Mar 03 19:53:21  when they look for a website, they look for a .com
    Mar 03 19:53:22  first
    Mar 03 19:53:52  true
    Mar 03 19:55:05  I can't count how many times I accidentally went to alientrap.com 
    Mar 03 19:57:45  From my favorite names, zeniux.com seems to be the only one in that list
    Mar 03 19:58:31  When will the name be finally decided? I think, there are a few choices now. I was thinking of taking our top 5-6 ideas for names (if we have that much) and making a pool on the forums
    Mar 03 19:59:18  I think we should definitely take time to pick the name
    Mar 03 19:59:43  in the meantime, a lot of discussion can be done about other details
    Mar 03 20:01:37 *   Rad_Ished has quit ("haha.. AAAHHHAAAaaARRR!!!  .. ow")
    Mar 03 20:05:16  Well, now that I brought that up. When might Nexuiz have player, item and weapon models that would make it look super-modern like Quake4 / UT3? Of course they won't fall from the sky, but I've wondered that for a while
    Mar 03 20:05:34  http://www.legitreviews.com/images/reviews/365/quake4_t.jpg / http://www.happypenguin.org/images/quake4.jpg Just imagining Nexuiz looking like that sometime... :)
    Mar 03 20:10:29  well one thing that could have been handled better in existing nexuiz is recruitment. I have talked to a large handful of people who were interested in getting involved in nexuiz, but they weren't given enough direction or help with getting involved and they ended up leaving. 
    Mar 03 20:11:06  people who handle recruitment and managing newcomers to the project don't need to be top developers
    Mar 03 20:11:24  especially if there is some sort of outline for that sort of thing
    Mar 03 20:12:15  there was only one official push (to my knowledge) from alientrap to attract new developers, and I think that effort seemed pretty successful in attracting developers
    Mar 03 20:12:24  but a lot of those developers showed and then eventually left
    Mar 03 20:12:47  so more campaigns to attract more talent to the project woudl be very helpful
    Mar 03 20:13:14  these are the kinds of things that should be a part of an open source game like this, imo
    Mar 03 20:20:36  I agree. I seen posts about people who wanted to come and help, but after that we haven't heard anything about them
    Mar 03 20:22:36  I always though that if I were a part of alientrap, I would have personally talked with those people to make sure they are kept informed and busy
    Mar 03 20:23:01  but as a simple member of the community, it wasn't really my place. I didn't even know who was coming to alientrap
    Mar 03 20:26:02  yeah
    Mar 03 20:37:06     I contacted most the people on the "We need developers" thread.
    Mar 03 20:38:08     --- Most of the time they were interested and sent emails back, but they never really showed up.
    Mar 03 21:03:39  Sorry for the delay... got busy with some other things from another channel. Going to bed in a minute too. Anyway, I know some topics were fional works are already released, but there was no feedback given on it.
    Mar 03 21:04:29  blkrbt still has 3 songs ready to be committed for at least 4 months iirc. Same as tZork's songs, about 8 of them I think (if I remember correctly again). There was also someone who made an awesome high quality robot model 6 months ago, no one said anything about that either.
    Mar 03 21:04:35  Maybe i should try finding that topic again
    Mar 03 21:12:40 *   TVR (~TVR@96.49.107.196) has joined #notnexuiz
    Mar 03 21:13:02    Glad to see you are all on board.
    Mar 03 21:14:34  Hello :)
    Mar 03 21:15:41    Hey Taoki, has tZork been notified?
    Mar 03 21:15:49  What about?
    Mar 03 21:20:08    He doesn't seem pleased about the actions of Vermeulen and LordHavoc selling a GPL version of his source code.
    Mar 03 21:21:19  Yeah, he spoke about this on the channel too. Hope he won't be leaving the project, would be sad if anyone did
    Mar 03 21:21:27  Aah, found what I was looking for.
    Mar 03 21:21:34  I'll post all 3 links
    Mar 03 21:23:10    Yes, that would be great.
    Mar 03 21:24:09  http://alientrap.org/forum/viewtopic.php?p=69763#p69763 - The robot model I mentioned. Imo it looks awesome. No one gave any feedback since Novemver 2009.
    Mar 03 21:24:09  http://www.alientrap.org/forum/viewtopic.php?p=74456#p74456 Scorp's songs (not tzork sorry), only the on for the tutorial map included.
    Mar 03 21:24:09  http://forum.alientrap.org/viewtopic.php?p=70446#p70446 3 songs by blkrbt, which haven't been reviewed for many months either
    Mar 03 21:24:31  Sorry about that TVR... posted before mentioning some forgotten contributions previously
    Mar 03 21:25:21  And these are only the ones I know of
    Mar 03 21:26:18    Is that media FOSS?
    Mar 03 21:26:45  Not sure... it shold be gpl iirc
    Mar 03 21:27:23  Anyway, i need to run now. Late here. See you all tomorrow
    Mar 03 21:30:36 <[-z-]> wtf keybord
    Mar 03 21:30:53 <[-z-]> /\ /\nd $ $topped working
    Mar 03 21:32:09    Totally unresponsive?
    Mar 03 21:43:48 *   Taoki has quit (Ping timeout: 364 seconds)
    Mar 03 21:57:48 <[-z-]> working again
    Mar 04 00:13:12    [-z-]: Have you contacted the Free Software Foundation, and/or EFF?
    Mar 04 01:54:12 *   TVR has quit (Remote host closed the connection)
    Mar 04 03:35:37   Zenux is a Linux distro (or should be).
    Mar 04 03:35:46   Zenus... well, I would like to keep the x somewhere :P
    Mar 04 03:35:52   OpenAlien... please not ;)
    Mar 04 03:35:57   (AlienArena, OpenArena...)
    Mar 04 03:36:33   [01:00:49]  Vermeulen fails, but it's -- It's still hard to abandon Nexuiz :P
    Mar 04 03:36:35   [01:01:11] <@[-z-]> it's no longer nexuiz and the sooner we all accept that, the sooner we can move on
    Mar 04 03:36:39   it's not abandoning, but just renaming
    Mar 04 03:36:44   we wouldn't have to abandon much
    Mar 04 03:36:55   maybe we should abandon the old evil* texture sets if we release under a new name anyway
    Mar 04 03:37:34   and half the maps :P
    Mar 04 03:37:45   on the other hand, we CAN include quite some public released maps of our taste :P
    Mar 04 03:37:51   (but please not ANY greatwall)
    Mar 04 03:38:17   So actually... why don't we go for a teamplay focus in the "forked game"?
    Mar 04 03:38:41   let's try to include 5 CTF maps, and 5 DM maps that ALSO are suitable for keyhunt and Domination, and 2 or 3 Onslaught maps
    Mar 04 03:58:06   [03:24:50] <@Taoki> http://www.alientrap.org/forum/viewtopic.php?p=74456#p74456 Scorp's songs (not tzork sorry), only the on for the tutorial map included.
    Mar 04 03:58:08   [03:24:50] <@Taoki> http://forum.alientrap.org/viewtopic.php?p=70446#p70446 3 songs by blkrbt, which haven't been reviewed for many months either
    Mar 04 03:58:18   as for songs: I normally like to include them only when they are actually used by the game
    Mar 04 03:58:27   but well, this would now be a good point to do it, and remove some songs by elysis :P
    Mar 04 05:11:41   okay, I finished the flaw in the player ID system I proposed :P
    Mar 04 05:19:21   http://paste.debian.net/62392/
    Mar 04 05:19:31   note: the patent for Schnorr identification expired last year :P
    Mar 04 05:20:04   so we can actually use it
    Mar 04 05:20:36   this prtoocol generates a player ID the generating server cannot trace back...
    Mar 04 05:20:56   and the old version had the flaw that an attacker who sniffed the ID of another player can impersonate him by simply providing the same ID
    Mar 04 05:33:54   that is then almost the perfect player ID system - nobody has to trust anyone for it to work :P
    Mar 04 05:34:17   (well, one has to trust the client application that it actually does perform the protocol... but in open source that can be verified easily)
    Mar 04 06:15:44   So actually... why don't we go for a teamplay focus in the "forked game"?
    Mar 04 06:15:49  I like that thinking
    Mar 04 06:18:04   it's not abandoning, but just renaming
    Mar 04 06:18:04   we wouldn't have to abandon much
    Mar 04 06:18:25  the one thing that I'm hopeful for is the ability to do the things in this fork that weren't done in previous nexuiz
    Mar 04 06:19:07   which are?
    Mar 04 06:19:44  If I had my way, I would take these community-driven efforts that I've done in nexuiz and ramp them up, place heavy focus on them
    Mar 04 06:20:06   well, which are these?
    Mar 04 06:20:15  ok I'll explain what I've done...
    Mar 04 06:20:28   I mean, do you mean stuff game code-wise, or stuff "representation wise"?
    Mar 04 06:20:45  activity-wise
    Mar 04 06:20:48  like creating tournaments
    Mar 04 06:20:49   ah, great then
    Mar 04 06:20:55   I have ABSOLUTELY no problem with that
    Mar 04 06:20:58  encouraging people to form clans, and helping them form clans
    Mar 04 06:21:04   but I do wonder why not much was done in that direction before
    Mar 04 06:21:07  orgnizing training 
    Mar 04 06:21:11   but well
    Mar 04 06:21:24   what we WILL gain, is a website that does not have to look "professional" like a company site
    Mar 04 06:21:24  setting up a training server and "hiring" some trainers
    Mar 04 06:21:28   so we CAN post recent stuff there
    Mar 04 06:21:34   and announce events, and like that
    Mar 04 06:22:06   also...
    Mar 04 06:22:13   when we don't have to act all "professional"...
    Mar 04 06:22:15  and over the past 6-8 months I have formed a group of people who are mappers, or they learned mapping, and I had them working on various map projects
    Mar 04 06:22:19   why not put some servers in the default favorites?
    Mar 04 06:22:20  like "fixing" maps
    Mar 04 06:22:23   e.g. that training server :P
    Mar 04 06:22:28  and converting maps from DM -> CTF
    Mar 04 06:22:44   actually... I would probably ONLY put that training server, and about two beta test servers there
    Mar 04 06:23:04   but a training server at the top of the server list WILL help a lot
    Mar 04 06:23:26   converting DM -> CTF... not so sure
    Mar 04 06:23:32   this never really works out :P
    Mar 04 06:23:47   minimanctf is one of the few exceptions
    Mar 04 06:23:51  There were two concepts for training servers. There was mine which was a "bootcamp" server which only had a couple maps on it to allow for a group to be taught by a trainer....and there is the Dojo map concept by -z- and mookow which is like an obstacle course that doesn't require a trainer
    Mar 04 06:24:16   not sure if a Dojo server would belong on the top of the server list
    Mar 04 06:24:19   bootcamp probably would
    Mar 04 06:24:20  the dojo seems like it would be for getting the "basics" while the bootcamp would be for refining and going from beginner to intermediate or advanced
    Mar 04 06:24:38   dojo is interesting for new players? THAT is enw to me
    Mar 04 06:24:45  the bootcamp sessions were like martial arts training that I've done before....lots of drills
    Mar 04 06:24:49   IIRC that map was full of very advanced mvoement tricks
    Mar 04 06:25:05   but well...
    Mar 04 06:25:07  div0: you should check out the dojo map that mookow is working on. Some very interesting ideas there
    Mar 04 06:25:16  I'll put it up if you want to see
    Mar 04 06:25:22   I'd suggest just reserving one or two IPs for use as "newbie training" server
    Mar 04 06:25:26   and one more IP for beta tests
    Mar 04 06:26:11  so far, almost everyone that I trained in the bootcamp servers went on to become a nexuiz "regular"
    Mar 04 06:26:11   and all these should be by default in the server list (but the beta test server should only be up when actually there is something new to test)
    Mar 04 06:26:20  so it's a great conversion tool
    Mar 04 06:26:33   thing is... to me the bootcamp idea sounds way more interesting to a new player
    Mar 04 06:26:34  for building a community and retaining players
    Mar 04 06:26:41   obstacle course really isn't everyone's thing
    Mar 04 06:26:43  yeah, but it requires a trainer
    Mar 04 06:26:52  if we can organize trainers properly
    Mar 04 06:26:56  then that will work wonderfully
    Mar 04 06:27:07   even if there is no trainer it can work out
    Mar 04 06:27:11  I already know a handful of people who would be willing to do training
    Mar 04 06:27:15   with cleverly designed maps for it :P
    Mar 04 06:27:25   but, even if there is no trainer, there should be moderators
    Mar 04 06:27:31  well that sounds more like the dojo concept
    Mar 04 06:27:42  where the map is the training tool
    Mar 04 06:27:42   and be it just to keep out the Diablo-D3s who join noob servers and then frag everyone there all the time :P
    Mar 04 06:27:48   well
    Mar 04 06:27:54   I hate putting the focus on obstacle course
    Mar 04 06:27:57   THAT is totally boring to me
    Mar 04 06:28:06  you should really see the map. hang on a sec
    Mar 04 06:28:07   it should rather be actual gaemplay
    Mar 04 06:28:21   it'd be the FIRST obstacle course map that is interesting
    Mar 04 06:28:24  mookow even found a way to play VIDEOS that give an example
    Mar 04 06:28:26  it's amazing
    Mar 04 06:28:29   sure
    Mar 04 06:28:33   but not for everyone
    Mar 04 06:28:54   it's simply for another group of players
    Mar 04 06:29:00   while the bootcamp idea should work for everyone
    Mar 04 06:29:05   because it focuses on actually PLAYING the game
    Mar 04 06:29:21   but yes, it requires a trainer
    Mar 04 06:29:29   probably bootcamp server should only be up when a trainer is there
    Mar 04 06:29:41   (if we put it on top of the server list, that is)
    Mar 04 06:29:55  the way I did bootcamp before was I created an IRC channel where trainers would idle. Then I created a page with a webchat interface pointing to that channel. The webpage explained bootcamp and said "If you want to train, go into chat and request a trainer"
    Mar 04 06:30:06   basically, I don't say the Dojo shouldn't be done...
    Mar 04 06:30:09  and then if a trainer is available, both would go to the bootcamp server for a training session
    Mar 04 06:30:11   of course not, it is a good idea
    Mar 04 06:30:20   I just don't think it should be announced at the top of the server list all the time
    Mar 04 06:30:27   as it may also drive newbies away
    Mar 04 06:30:30   it sure would have driven away me
    Mar 04 06:30:43  ok connect nullgaming.com:27005
    Mar 04 06:30:48   can't, am at work
    Mar 04 06:30:50  oh ok
    Mar 04 06:31:02  basically, the dojo map has various rooms
    Mar 04 06:31:03   basically, the whole obstacle course idea isn't really appealing to me
    Mar 04 06:31:11  and each room has a focus....like movement, weapons, etc
    Mar 04 06:31:18  and within each room, there are doors
    Mar 04 06:31:28   well, I am not saying this would be a bad ides
    Mar 04 06:31:30   a
    Mar 04 06:31:31  and you enter a door and it walks you through how to do a certain thing....like laser jumping
    Mar 04 06:31:34  wall lasering
    Mar 04 06:31:39  rocket jumping
    Mar 04 06:31:40  etc
    Mar 04 06:31:45   as for bootcamp, is there a way to train multiple people at once?
    Mar 04 06:32:07  and before you do the move, you can type "help" and that will start the download of the video. As soon as the video is downloaded, it plays on your screen so you see what you are suppoed to be doing
    Mar 04 06:32:12   I'd prefer such a server where players can join and leave at any time
    Mar 04 06:32:22  bootcamp, absolutely. I've trained up to 6 people at a time
    Mar 04 06:32:33  well, actually I've trained more than that a long time ago before bootcamp was started
    Mar 04 06:32:36   I just say... ideally it should be working WITHOUT having to go to a chat
    Mar 04 06:32:44  but about 6 people works well
    Mar 04 06:32:47   but by joining a public server
    Mar 04 06:33:07  well I would love to see a mechanism for requesting a trainer IN the game. that would be awesome
    Mar 04 06:33:17   you can do HTTP requests from QC
    Mar 04 06:33:18  but using webchat was the best I could think of
    Mar 04 06:33:58   so basically, you could make a HTTP request to a CGI script that will post the request on IRC
    Mar 04 06:34:34  So what I did with bootcamp was I started to create a teaching plan, a curriculum, with various drills that the trainer would have the students walk through. The reason I started doing this was so I could quickly get a trainer onboard and all they would have to do is follow the curriculum
    Mar 04 06:34:39   basically, I envision it this way...
    Mar 04 06:34:44   noob joins training server...
    Mar 04 06:34:52  and of course, they would help create the curriculum as well, help refine it, add more drills
    Mar 04 06:34:54   and can spectate only
    Mar 04 06:35:00   on some button, he can request a trainer
    Mar 04 06:35:10   or request the already on the server trainer's attention
    Mar 04 06:35:16   trainer can then let him in
    Mar 04 06:35:36  can the trainer request be doing based on geography?
    Mar 04 06:35:36   shouldn't be done too much like school though :P
    Mar 04 06:35:46   based on geography, no
    Mar 04 06:35:52  no, I ran it like martial arts training
    Mar 04 06:35:55   but, we could have multiple training servers
    Mar 04 06:36:01   the closer one would be at the top of the list
    Mar 04 06:36:05   and be most likely to be joined
    Mar 04 06:36:10  I explained some things, then we did some drills, then I stoped and explained some more and then we did some drills
    Mar 04 06:36:26   sure
    Mar 04 06:36:28  usually the sessions lasted about an hour, but sometimes they went for 3-4 hours
    Mar 04 06:36:34   I just say... nobody should be "forced" to join at a certain time
    Mar 04 06:36:40   and one should easily be able to skip a session too :P
    Mar 04 06:36:54   it'd be better if players can just join the training when they feel like it
    Mar 04 06:37:02   a curriculum can of course be used to decide what is the focus on what day
    Mar 04 06:37:57  before bootcamp, we tried another approach and that was like running "classes" where we started a nexuiz school server publicly and we went to all of the public severs with people on them and announced "If you want nexuiz training, a class starts in 5 minutes. Go to here"
    Mar 04 06:38:02  but that turned out to be a mess
    Mar 04 06:38:18  we successfully collected a number of players...like as many as 15
    Mar 04 06:38:23   well
    Mar 04 06:38:25  and we certainly did train them in some basics
    Mar 04 06:38:26   I want something in between
    Mar 04 06:38:30  but it was very very very difficult to moderate
    Mar 04 06:38:35  so that idea didn't work
    Mar 04 06:38:36   server should be public, but trainer should decide who he lets in or not
    Mar 04 06:38:42  that is why we came up with bootcamp
    Mar 04 06:38:50   it shouldn't look like a closed community
    Mar 04 06:38:59   it should be free, and one should be able to join it without commitment
    Mar 04 06:39:17   but, moderation should then be done using a whitelist approach
    Mar 04 06:39:25   i.e. anyone can join the server and try to talk to the trainer
    Mar 04 06:39:30   but the trainer decides who gets to actually play
    Mar 04 06:39:33  the teaching server (the first approach) was public and various people would join it and start shooting because they didn't know any better
    Mar 04 06:39:40   EXACTLY :P
    Mar 04 06:39:52   a trainer could e.g. let one player join, tell him what to do, and only then let the next one in
    Mar 04 06:39:58   to avoid that mess
    Mar 04 06:40:05  so yeah if there are mechanisms built into the game to help moderate the bootcamp server experience, that would be great
    Mar 04 06:40:20   basically, I say: the bootcamp should be "really" public
    Mar 04 06:40:29   a public server where anyone can join, with bootcamp specific restrictions
    Mar 04 06:40:34  ok
    Mar 04 06:40:39  that's awesome
    Mar 04 06:40:39   and a feature to request a trainer when none is available
    Mar 04 06:40:51   because: that will get our noobs to actually TRY the bootcamüp
    Mar 04 06:40:58   as it'd be at the top of the server list
    Mar 04 06:41:12  that would be a HUGE conversion tool
    Mar 04 06:41:23   exactly
    Mar 04 06:41:28  for turning new players into intermediate players quickly
    Mar 04 06:41:45   things we need for it: a server should be "spectator only", and someone with master access can let players join the game
    Mar 04 06:42:06   and, there should be a way to send a message to IRC (hehe, rcon2irc sort of can already do that, but this would better be more controlled)
    Mar 04 06:42:11  I ran two bootcamp servers
    Mar 04 06:42:49   BTW: the spectator-only feature also sounds like a good idea for clan matches
    Mar 04 06:42:52  if a session was already started, someone could start a new session on the other server
    Mar 04 06:44:52  the central user system idea would really help with clan activity as it would allow for a proper stats system and clan tag reservation and perhaps ....team slot reservation?? like for this clan match, only members of [o] can join team blue
    Mar 04 06:45:38  that was a difficulty before with running clan matches where people would join and suddenly jump into the game during warmup and start playing and we'd have to tell them to spectate
    Mar 04 06:46:00  and I had to kick some people and they would get mad because they didn't see my messages before 
    Mar 04 06:46:47  it was just a mess. But if we had a way to enforce rules during clan matches based on usernames or clan names, that would help a lot
    Mar 04 06:47:20  then if someone on team blue dropped their connection, a spectator from that same clan could jump into the game (but the other spectators woudln't be allowed)
    Mar 04 06:47:35  that was another difficulty with clan matches, dropped connections
    Mar 04 06:47:51   right
    Mar 04 06:47:58   I have described aw working user system
    Mar 04 06:48:03   that ensures anonymity AND security :P
    Mar 04 06:48:10  that's awesome!
    Mar 04 06:48:10   could sure be used for nick and clan tags too
    Mar 04 06:48:20  I wanna hug you
    Mar 04 06:48:25   (of course, by associating a nick, you lose anonymity, but well, then you KNOW it :P)
    Mar 04 06:48:34  right
    Mar 04 06:48:48  so,,another thing that I've done is organize mapping projects
    Mar 04 06:48:52   it can still be used to ban trolls, as the anonymous IDs would only be given once per week per email address
    Mar 04 06:49:04  and that also involves mapping training too for those who want to learn
    Mar 04 06:49:04   so if you lose your ID, in worst case you have to wait a week to get a new one
    Mar 04 06:49:19   a really elaborate troll could of course request a new ID every week but do nothing
    Mar 04 06:49:26   and then one year later, he can burn 52 IDs :P
    Mar 04 06:49:34   but that is unlikely
    Mar 04 06:49:39  I once created a team of people called NCT = Nexuiz Community Team to help me run some community projects (like organizing bootcamp, organizing clan matches, organizing mapping projects)
    Mar 04 06:50:02  and since I basically gave up on the clan community, the NCT has only been focusing on the mapping projects
    Mar 04 06:50:18  but we made some good progress
    Mar 04 06:51:04  I think Nexuiz should have had an NCT-like group...which is just another way fo saying "you can volunteer to be involved in nexuiz" and then someone would direct and manage those people 
    Mar 04 06:51:17  I mean an NCT sort of group in an official sense
    Mar 04 06:52:17  because it creates more mappers and it allows a lot of new projects to get off the ground quickly because we would already have a group of willing volunteers
    Mar 04 06:52:37  it allows for map testing
    Mar 04 06:52:46   speaking of maps... which maps do we want in "notnexuiz"?
    Mar 04 06:52:50  good question
    Mar 04 06:52:53   (out of the community maps)
    Mar 04 06:53:19  I would think to start that off with "what maps do we NOT want that are currently in nexuiz" and then figure out how many open slots there are
    Mar 04 06:53:29   not really :P
    Mar 04 06:53:35   blockscape is e.g. a good candidate, I'd say
    Mar 04 06:53:44   maybe needs a better compile though
    Mar 04 06:53:57   controlfactor :P
    Mar 04 06:54:01   (needs visual remake)
    Mar 04 06:54:22   too bad we can't use docpython's maps
    Mar 04 06:54:57  I discussed this with Getty with our other project. What is the major reason for having a lot of maps included with the game? I mean aside from those intended to be played in Campaign mode. It seems like 99% of gameplay happens on non-standard maps that get auto-downloaded to the player by the server.
    Mar 04 06:55:13   the included maps represent the game
    Mar 04 06:55:31   currently, what you play online is very different from what the game contains
    Mar 04 06:55:34   that IMHO is not good
    Mar 04 06:55:40  would we require these included maps to have bot waypoints?
    Mar 04 06:55:59   yes
    Mar 04 06:56:08  so someone could feasibly play CTF with some bots
    Mar 04 06:56:09   and possibly use them in campaign too
    Mar 04 06:56:14   right
    Mar 04 06:56:16  ok
    Mar 04 06:56:19   not very well
    Mar 04 06:56:22   but they should work
    Mar 04 06:56:29  since mangina improved the bots, they are actually playable in CTF now, I think
    Mar 04 06:56:31   this BTW speaks against blockscape...
    Mar 04 06:56:36  er mandinga*
    Mar 04 06:56:36   IIRC it cannot be played without laserjumps
    Mar 04 06:56:47  yeah :-/
    Mar 04 06:56:56   controlfactor should work with bots
    Mar 04 06:56:56  it would need some jumppads in certain places maybe?
    Mar 04 06:56:58   but looks outdated
    Mar 04 06:57:21   tznex03, same problem :P
    Mar 04 06:57:35   tznex03 is the closest to classic Quake1/2 CTF we ever got
    Mar 04 06:57:42  we couldn't include any of these q3 conversion maps, could we?
    Mar 04 06:57:47   we can't
    Mar 04 06:57:49  ok
    Mar 04 06:57:49   and should not
    Mar 04 06:58:24   hehe, that is already the full list of CTF maps I really would like to add - blockscape (but bots... can't), controlfactor, tznex03
    Mar 04 06:58:37  many people seem to like gasolinepowered, and I'm sure the new version of it is going to be great
    Mar 04 06:58:43   oh right
    Mar 04 06:58:44  http://www.nullgaming.com/maps/hoctf/
    Mar 04 06:58:46   that one too
    Mar 04 06:58:51   I didn't see that one when scrolling :P
    Mar 04 06:58:57   gasolinepowered is a clear yes
    Mar 04 06:59:04  those are my CTF maps. Though I should remove the ones that I no longer have in the maplist
    Mar 04 06:59:28   all your push are belong to us wtf :P
    Mar 04 06:59:31  and hmm.... I should grab my maplist actually and remove the Q3 conversion maps
    Mar 04 06:59:37  haha that is an april fools joke map
    Mar 04 06:59:54   oh right, hydronex is not official either...#
    Mar 04 07:00:01  OH btw.... marketing is another topic. I have a lot of marketing ideas and with some volunteers involved, that can be a good way to attract new players
    Mar 04 07:00:08  like the april fools mapping project
    Mar 04 07:00:14  which is around the corner....this is good timing
    Mar 04 07:00:46  For example.... we would take existing maps and theme them to funny internet memes
    Mar 04 07:00:49   lol, you once had bonuscheckers on it
    Mar 04 07:00:56  yeah :-/
    Mar 04 07:01:03  we did a remake of bonuscheckers though
    Mar 04 07:01:08   a remake? where
    Mar 04 07:01:13  it's called.....
    Mar 04 07:01:19  courtyard_ctf
    Mar 04 07:01:24  I think
    Mar 04 07:01:31   ah, a serious remake :P
    Mar 04 07:01:39   original was bonusarenactf, BTW :P
    Mar 04 07:01:44   no, bonuscarousel
    Mar 04 07:01:44  grassy has some ideas to improve it further, but the remake was basically successful
    Mar 04 07:02:03  another succesful remake was darkcity_ctf
    Mar 04 07:02:05   have screenshot?
    Mar 04 07:02:08  hang on....
    Mar 04 07:02:10   darkcity remade? cool
    Mar 04 07:02:13   also with keyhunt support?
    Mar 04 07:02:26  hmmm probably didn't include KH support
    Mar 04 07:02:31   I like city maps
    Mar 04 07:02:40   is it a from scratch remake?
    Mar 04 07:02:58   or based on the old one?+
    Mar 04 07:03:04  did you know that mIKEctf2's real name was "Like Spinning Plates"?
    Mar 04 07:03:08   yes
    Mar 04 07:03:31  oh, mookow's recent map called Kings and Queens is really really good, but has a FPS drop problem
    Mar 04 07:03:33   ah, darkcityctf seems to be based on the roiginal one
    Mar 04 07:03:44   bad... cannot use that then for the official game :P
    Mar 04 07:03:52  if the FPS drop could be improved, that could be a good map
    Mar 04 07:03:54   (as the original sure is not GPL compatible)
    Mar 04 07:04:07   but I would really like a nicely detailed city map for keyhunt
    Mar 04 07:04:14  well he did recreate the whole map from scratch at one point because the brushes were so messed up
    Mar 04 07:04:19  for darkcity_ctf
    Mar 04 07:04:26   yes, but he still uses the old textures
    Mar 04 07:04:29  ah I see
    Mar 04 07:04:39   if these could get replaced, that'd be great
    Mar 04 07:05:00  I think agressor_ctf could be good but it needs some fixing around the middle point area where the quad is. That's too much of a bottleneck
    Mar 04 07:05:25   also... which maps could be warpzonized?
    Mar 04 07:05:32   aggressor probbaly cannot
    Mar 04 07:05:41   using warpzones there would turn it into a brain twister :P=
    Mar 04 07:05:42  grassy recently recreated onarail to included 2 trains...it's called on2rails. It's an okay map...it's better than the original
    Mar 04 07:05:56   need to make stoiber remix of it :P
    Mar 04 07:05:59  oh, warpzones. Man, those are great
    Mar 04 07:06:06  what an awesome idea
    Mar 04 07:06:20  I haven't even begun to think about how those could be used for gameplay
    Mar 04 07:06:24   best are used in a way that is compatible to clients that have the extra renders disabled
    Mar 04 07:06:28  like your spiral staircase concept
    Mar 04 07:06:36   like, put teleporter brush behind them :P
    Mar 04 07:06:41  I see
    Mar 04 07:07:06  a lot of dublpaws maps are popular on my server
    Mar 04 07:07:08  dance
    Mar 04 07:07:09  go
    Mar 04 07:07:13   yes, but these are quite low quality
    Mar 04 07:07:14  fighter_bay
    Mar 04 07:07:18   (for inclusion in the game)
    Mar 04 07:07:27   good gameplay though
    Mar 04 07:07:29  low quality in terms of textures?
    Mar 04 07:07:34   yes, and brush detail
    Mar 04 07:07:36  because I could talk with dublpaws about improving those
    Mar 04 07:07:45  he plays on my server all the time
    Mar 04 07:07:55   dance is almost includable though
    Mar 04 07:08:06   the other dublpaws maps, not really
    Mar 04 07:08:10  dib and I were working on an dance_enclosed spin-off
    Mar 04 07:08:23  it was about 90% done and then he dropped it
    Mar 04 07:08:28   dance is just too one-colored :P
    Mar 04 07:08:39   do something better than that wood floor, and it's done
    Mar 04 07:08:40  I happen to like the latest versions of soylent_ctf that makr was working on
    Mar 04 07:08:55  though it needs more testing
    Mar 04 07:09:04  oh....stonecastle
    Mar 04 07:09:08  remake of dm_castle
    Mar 04 07:09:11  everyone loves it
    Mar 04 07:09:18  well except for cortez666 :-P
    Mar 04 07:09:50  I think lavaflag could use a makeover
    Mar 04 07:09:51   given that dm_castle was bad
    Mar 04 07:09:54   I have to try this one
    Mar 04 07:09:59   lavaflag REALLY :P
    Mar 04 07:10:06   isn't that the one with the huge bug?
    Mar 04 07:10:08   hourglass too
    Mar 04 07:10:31   (where you could end up in all black rooms, and hide)
    Mar 04 07:11:03  the gameplay of dm_castle is improved in stonecastle with jumppads in certain places (really helps new players move around the map) and we replaced the machinegun with hagar
    Mar 04 07:11:22 *   Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 04 07:11:31  oh I didn't know about any lavaflag bug :-o
    Mar 04 07:11:46  I like medeivalV2
    Mar 04 07:11:50  but it also needs a makeover
    Mar 04 07:12:21   IIRC lavaflag has the sae bug as hourglass, but elsewhere
    Mar 04 07:12:59  ctf_toxic was on our list of maps to improve...mainly in the middle area of the map where the two halves meet
    Mar 04 07:13:55   my version? sure
    Mar 04 07:14:03   or master's version? :P
    Mar 04 07:14:11  a recent map called Cubical by a new mapper (guy who came from Q2/Q3) is really good. That same guy is working on a Walmart map called NexMart
    Mar 04 07:14:16   my version is the one with the "reaction" stuff
    Mar 04 07:14:30   oh, but Cubical is by FruitieX
    Mar 04 07:14:34   from that mapping contest
    Mar 04 07:14:37  Cubical doesn't look very pretty though. 
    Mar 04 07:14:43  oh he also has a map called cubical??
    Mar 04 07:14:44  oops!
    Mar 04 07:14:55  uh, ok I need to talk with mintox about renaming his then
    Mar 04 07:15:03   not sure if this is needed :P
    Mar 04 07:15:08   not many play FruitieX's map anyway
    Mar 04 07:15:14   actually, it may be mostly forgotten nwo
    Mar 04 07:15:28   basically, if the map is good, FruitieX will probably be fine with itr
    Mar 04 07:15:49   just talk about it to both of them and find a solution
    Mar 04 07:15:56   chances are BTW that the bsp file names do not clash
    Mar 04 07:16:20  Mookow's "Drainage" map had promise, but he never really finished it. 
    Mar 04 07:17:25  Evilspace CTF is popular, but it does have a couple bad gameplay elements. There is a hidden teleporter that leads to the quad and there is that "escape hatch" jump pad right below the flag
    Mar 04 07:17:57   yes
    Mar 04 07:18:00  if those things were fixed and if it had a makeover, it could be good.
    Mar 04 07:18:02   maybe should be fixed
    Mar 04 07:18:25   I do like the idea of the teleporter though, but not of hiding it
    Mar 04 07:18:37  right
    Mar 04 07:18:47  hidden secret stuff in CTF is generally bad for gameplay
    Mar 04 07:18:56  but a teleporter leading to the quad is fine
    Mar 04 07:19:28   right
    Mar 04 07:19:30  everyone really likes gforce2. It could still use some refinement. unfortunately cortez took Gforce3 and 4 in a different direction
    Mar 04 07:19:37   no, I don't like gforce2 :P
    Mar 04 07:19:45   oh wait
    Mar 04 07:19:48   version 2, maybe yes
    Mar 04 07:19:57  Morning everyone :)
    Mar 04 07:19:57   but the turrets ended up too annoying
    Mar 04 07:19:59  unfortunately, gforce2 also has that hidden teleporter leaidng to the nex
    Mar 04 07:20:07   yes
    Mar 04 07:20:12  yeah the turrets were added in v3
    Mar 04 07:20:24  they were "neat" but they ruined the map
    Mar 04 07:20:53  it's interesting to me that cortez creates interesting maps by accident
    Mar 04 07:21:28   and here comes a really controversial question...
    Mar 04 07:21:38  one of the projects was another attempt at remaking dusty to be symmetrical. 
    Mar 04 07:21:41   does anyone volunteer to do good item placement for slimepipe (NOT the ctf version)?
    Mar 04 07:21:49  slimepipe was on the list too!
    Mar 04 07:22:00  out of all of mikee's maps, slimepipe was the one that I felt had potential
    Mar 04 07:22:01   the only good looking mikeeusa map
    Mar 04 07:22:29   even has somewhat okay gameplay
    Mar 04 07:22:33   just item placement is bad
    Mar 04 07:22:41   and the slime trap... not that way, but has potential
    Mar 04 07:22:44  this hasn't been updated in a month, but here is the projects page we were working from
    Mar 04 07:22:45  http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 04 07:22:49  to fix maps and convert maps
    Mar 04 07:23:11   basically, slimepipe probably does not need much work to be includable
    Mar 04 07:23:25   of course, mikee later developed it into the wrong direction
    Mar 04 07:23:40   by making 4 copies of the map, and confusing corridors
    Mar 04 07:23:50   when remaking, watch the license
    Mar 04 07:23:54   doc's maps are not GPL
    Mar 04 07:24:43   Rustvents - also good idea
    Mar 04 07:25:39   for slimepipe, please base on slimepipesmallctf, or even better, slimepipe (not ctf)
    Mar 04 07:25:54  k
    Mar 04 07:28:20  breathium is pretty for a DM map
    Mar 04 07:28:27  I forgot who made it
    Mar 04 07:28:31   oh, great, nexdmlc2 got edited
    Mar 04 07:28:35   I liked that map
    Mar 04 07:28:49   too bad it's nongpl too, it really would have potential
    Mar 04 07:28:58  ahh
    Mar 04 07:29:01   maybe original author can be tracked down
    Mar 04 07:29:11   or was it rebuilt anyway?
    Mar 04 07:29:21  probably not
    Mar 04 07:29:35   because, IIRC it came without .map file
    Mar 04 07:29:35  it was scorpion's first map
    Mar 04 07:29:43  oh? hmmm
    Mar 04 07:29:59   oh, no
    Mar 04 07:30:01   map was included
    Mar 04 07:32:05   basically, many maps in the list have potential, but not many are GPL (or GPL-able)
    Mar 04 07:32:23   the others can of course be played on servers anyway
    Mar 04 07:32:49  yeah we certainly weren't tracking licenses. However, we could adjust that for the goal of maps to be included with the game
    Mar 04 07:33:26   I just am saying - many of these WOULD have potential for inclusion
    Mar 04 07:33:28  but yeah, this map-project management is another thing that I think should be an official effort put forth by the people who run the game
    Mar 04 07:33:34  because then it could be done better
    Mar 04 07:33:37  and reach more people
    Mar 04 07:33:52   and yes, I wouldn't even refuse to include a slimepipe fixed version
    Mar 04 07:33:53  the little effort I've done has created a handful of new mappers
    Mar 04 07:34:18   at least the DM version
    Mar 04 07:34:19  ...and I don't even make maps! I tried before but gtkradient kept crashing in vista
    Mar 04 07:34:22   I am not sure if it can work out as CTF
    Mar 04 07:34:28  I haven't had time to try netradient since
    Mar 04 07:34:58   seriously, I'd say slimepipe could become what reslimed has attempted to be but failed
    Mar 04 07:35:05   (I still prefer slimepit over reslimed)
    Mar 04 07:35:16  is it slimepit or slimepipe?
    Mar 04 07:35:22   mikee's is slimepipe
    Mar 04 07:35:32   I now compare to slimepit (the old one in Nexuiz)
    Mar 04 07:35:37  oooooh
    Mar 04 07:35:51   reslimed, Strahlemann's successor, does look better than slimepit, but I always hit walls on it
    Mar 04 07:35:54   really not fluent
    Mar 04 07:36:02   I'd like a "best of both worlds" map :P
    Mar 04 07:36:28  I liked reslimed, mainly because it is larger
    Mar 04 07:36:45   yes
    Mar 04 07:36:47   that part I like
    Mar 04 07:36:53   but not that it lost of slimepit's fluency
    Mar 04 07:37:02  but I always though the shield area down that long hallway was a bit odd
    Mar 04 07:37:09   on slimepit I can jump all the time, and never get stuck anywhere
    Mar 04 07:37:18   on reslimed, no chance
    Mar 04 07:45:14  if there is any chance of my being put in charge of community development, I'll certainly "sign-up" for that. That is what I've always done for nexuiz and if I can do it on an official basis with the support of those involved in running the game, then these projects can be scaled up to something much bigger.
    Mar 04 07:45:51  that is what I'm planning on doing for the projects I'm working on with Getty
    Mar 04 07:46:08  I'm the community developer or community coordinator for those projects
    Mar 04 07:52:34   Nexitus
    Mar 04 07:52:51   is that available?
    Mar 04 07:53:00   maybe with z at end
    Mar 04 07:55:01  nexitus.com - taken
    Mar 04 07:56:40  nexituz.com available, but that doesn't look as good
    Mar 04 07:57:06  nexidus.com also taken
    Mar 04 07:57:24  nexid.com taken
    Mar 04 07:58:27   damn
    Mar 04 07:59:17  another thing, I helped the aussies build up their community and I was planning on starting up a south american community and possibly an asian community at one point
    Mar 04 07:59:58  I talked with mandinga about the south american community idea
    Mar 04 08:01:30  nexidux.com available
    Mar 04 08:01:55  nexidun.com available
    Mar 04 08:02:31  nexidium.com available
    Mar 04 08:04:03  nexiox.com available
    Mar 04 08:10:18   nexidium - not so bad
    Mar 04 08:11:36  nexilus.com available
    Mar 04 08:14:35   sounds too soft :P
    Mar 04 08:14:46  ya
    Mar 04 08:15:13   also, if it differs just by one letter from a traemark, we can get screwed too
    Mar 04 08:15:34  only of that trademark is in the gaming industry
    Mar 04 08:15:43   true
    Mar 04 08:15:48   maybe in software too
    Mar 04 08:15:52  ya
    Mar 04 08:15:54   NEXCARNATE
    Mar 04 08:16:35  nexiton.com available
    Mar 04 08:16:42   hm... that could work
    Mar 04 08:16:51   the gun could then also be called "The Nexiton"
    Mar 04 08:16:55   or maybe Nexitone
    Mar 04 08:17:05  tone your skin with....nexitone!
    Mar 04 08:17:09   lol
    Mar 04 08:17:15   Nexecution
    Mar 04 08:17:19   no, that is too violent :P
    Mar 04 08:17:31   Nexcathedra ahahahahah))
    Mar 04 08:17:57   NEXHALE
    Mar 04 08:18:18   Nexotherm
    Mar 04 08:18:27   Nexodium
    Mar 04 08:18:38  nexot.com is available
    Mar 04 08:18:41   Nexodus
    Mar 04 08:18:48 <[-z-]> http://nexuizgpl.com/ << run by bennydacks
    Mar 04 08:18:59   Nexogamy - don't even want to know what that would be
    Mar 04 08:19:08  heh, he snatched that domain up quick eh?
    Mar 04 08:19:36  I want to like bennydacks, I really do
    Mar 04 08:19:53   Nexotoxic
    Mar 04 08:20:58 <[-z-]> :-P
    Mar 04 08:21:37  so whenever we pick a name, we need to NOT release it until we make sure we get the appropriate domains that we think we might need
    Mar 04 08:21:40   Nextima (but not sure if that is a bad word, just found extima in /usr/share/dict/words)
    Mar 04 08:21:43   of course
    Mar 04 08:22:04   Nextispex
    Mar 04 08:22:06   wtf :P
    Mar 04 08:23:07  and it would be wonderful if all of the things offered by side websites were actually part of the official site
    Mar 04 08:23:44  like news, training videos, etc
    Mar 04 08:23:55   that is fine, would even allow me to also accept NN as a part of the official side :P
    Mar 04 08:23:56  clan management 
    Mar 04 08:24:01   it just shouldn't be centric to a single community
    Mar 04 08:24:22   but [PB] will stay elsewhere
    Mar 04 08:24:28   don't want to get forced to use good web design ;)
    Mar 04 08:24:35  haha
    Mar 04 08:24:51   but sure - why NOT integrate the various communities
    Mar 04 08:25:35 <[-z-]> yes, I don't mind building out this new site to act like nexuiz ninjaz was planning to be like
    Mar 04 08:25:41  exactly
    Mar 04 08:25:44  that's what I mean
    Mar 04 08:25:58 <[-z-]> I already thought about how to integrate a few host and I'm working on builid a map repo into wordpress
    Mar 04 08:26:06 <[-z-]> I created my first WP plugin yesterday ^_^
    Mar 04 08:26:14  this will give me an excuse to learn wordpress
    Mar 04 08:26:20  I've been avoiding it :-P
    Mar 04 08:26:27 <[-z-]> it's really a nice CMS
    Mar 04 08:28:55 <[-z-]> god damn, can't wait until the weekend, I need sleep
    Mar 04 08:29:03   I just don't want the ninjaz to dominate it :P
    Mar 04 08:29:10   but well, that shouldn't be hard to achieve
    Mar 04 08:29:16 <[-z-]> I understand and agree
    Mar 04 08:29:16   just add enough non-NN content and it's set
    Mar 04 08:29:31   a comprehensive portal page WOULD be good
    Mar 04 08:29:50   it's just, the different interest group all have different opinions...
    Mar 04 08:29:54 <[-z-]> part of the reasons ninjaz were started was because I thought it was too hard to get AT to listen on some things
    Mar 04 08:30:00   but the main page should have a neutral point of view whereever possible
    Mar 04 08:30:13  IMO, there wouldn't have been a "nexuizninjaz" if there were something like it within the core community.
    Mar 04 08:30:24   and how can you be more neutral than by trying to include as many of these special comminities as possible
    Mar 04 08:30:24 <[-z-]> well put
    Mar 04 08:30:54   should probably also include planetnexuiz.de if it still exists :P
    Mar 04 08:33:46  I'm also scanning domain auctions and sales sites because often domains are for sale really cheap...like $15
    Mar 04 08:33:53 <[-z-]> it's a trap
    Mar 04 08:33:58  ?
    Mar 04 08:34:06 <[-z-]> don't by from squatters
    Mar 04 08:34:17  who says they are squatters?
    Mar 04 08:34:33 <[-z-]> 90% chance
    Mar 04 08:35:05 <[-z-]> where you chance sedo or something?
    Mar 04 08:35:22  ok I just scanned godaddy auctions for nex*.com
    Mar 04 08:35:25  didn't find much
    Mar 04 08:35:28 <[-z-]> ahh
    Mar 04 08:35:53  a lot of those godaddy auctions are expired domains that people let lapse
    Mar 04 08:37:43   I do think the name SHOULD still start with nex
    Mar 04 08:37:46 <[-z-]> yeah, godaddy isn't the same as the other sites... but their own brand of evil
    Mar 04 08:37:51   but it isn't really easy to find a good name with that
    Mar 04 08:38:02  it would be really convenient if it began with "nex"
    Mar 04 08:38:07 <[-z-]> nexican
    Mar 04 08:38:08 <[-z-]> ^_^
    Mar 04 08:38:11  haha
    Mar 04 08:38:13   Nexotherm only has 2 google hits
    Mar 04 08:38:16   it may work :P
    Mar 04 08:38:17 <[-z-]> nexicola
    Mar 04 08:38:26   plus, the word makes sense - explosions are exotherm reactions
    Mar 04 08:38:31 <[-z-]> nexifz
    Mar 04 08:38:43 *   [-z-] gives channel operator status to Taoki
    Mar 04 08:38:45  here is my list so far...
    Mar 04 08:38:46  http://pastie.org/private/rwg7zyl2a9gwfcdplmqvqa
    Mar 04 08:39:15  I see some repeats
    Mar 04 08:39:15   Try: Nexepharis
    Mar 04 08:39:16  oh well
    Mar 04 08:39:25  that's kind of a long name
    Mar 04 08:39:33  I was trying for 8 characters or less
    Mar 04 08:39:33   yes, but less weird than Xepharis
    Mar 04 08:39:59   Nexiox is not that bad either
    Mar 04 08:40:00  nexepharis.com available
    Mar 04 08:40:12 <[-z-]> nexephalis
    Mar 04 08:40:19   nexenzephalitis?
    Mar 04 08:40:31 <[-z-]> the logo could be the radar for bleach
    Mar 04 08:40:32  nexameaneggsandwich
    Mar 04 08:40:37   that is what your brain gets when you get nexed too much
    Mar 04 08:40:42 <[-z-]> eabfps
    Mar 04 08:40:48 <[-z-]> (eggs and bacon FPS)
    Mar 04 08:40:53   lol
    Mar 04 08:40:58   NEGGS AND BACON
    Mar 04 08:41:03 <[-z-]> :-P
    Mar 04 08:41:15 <[-z-]> we can call it nexnex
    Mar 04 08:41:31 <[-z-]> nexnex.org AVAILABLE
    Mar 04 08:41:44  I really like some of those names that don't have available .coms....so if we get stuck with this name picking thing, we can always consider that as a backup plan
    Mar 04 08:41:47 <[-z-]> nextnex
    Mar 04 08:42:08 <[-z-]> nextnex.com     AVAILABLE
    Mar 04 08:45:56  I need food...brb
    Mar 04 09:05:14 <[-z-]> alright, see you all from the work place
    Mar 04 09:34:41 *   }-z-{ (z@dojo.nexuizninjaz.com) has joined #notnexuiz
    Mar 04 09:35:03  ok there are some more isuses we need to work out with this transition. We are going to have to recreate a lot of things that exist for nexuiz already...like dev.alientrap.org content and some of the sticky thread information
    Mar 04 09:35:20 <}-z-{> yeah, I can handle all the web and I'll share access with you Dokujisan 
    Mar 04 09:35:24   yes, but that doesn't have to be there from the start
    Mar 04 09:35:28  ok
    Mar 04 09:35:34   plus, [-z-] has access to alientrap.org's databases :P
    Mar 04 09:35:37 <}-z-{> well, getting the web and pm up will help us get organized
    Mar 04 09:35:38  haha
    Mar 04 09:35:53   but we can't get it up without a domain name
    Mar 04 09:36:00 <}-z-{> I was hoping we could come up with a name by the end of today
    Mar 04 09:36:05   well... for a start, it'd be nice if it's on nexiuz.org as you now own it anyway :P
    Mar 04 09:36:12 <}-z-{> but if not, I can just start building on locally
    Mar 04 09:36:24 <}-z-{> yeah, I'll do that when I get home I guess
    Mar 04 09:36:27   it isn't easy to find a good name
    Mar 04 09:36:28 <}-z-{> start it on nexiuz.org
    Mar 04 09:36:35   but we can use nexiuz as "working title", and get a real name later
    Mar 04 09:36:42 <}-z-{> yeah
    Mar 04 09:36:54   just... http://www.nexiuz.org shouldn't contain much info for anyone :P
    Mar 04 09:37:00   more like the illfonic announcement was haha :P
    Mar 04 09:37:04   it should be in a subdir
    Mar 04 09:37:11 <}-z-{> what do you mean?
    Mar 04 09:37:18   alternatively, it shouldn CLEARLY state EVERYWHERE that nexiuz is unlikely to be the final name
    Mar 04 09:37:26 <}-z-{> ahh
    Mar 04 09:37:29   as using that as final name will be a bad move
    Mar 04 09:37:41   (as google will STILL show illfonic's stuff, and assume it's a typo of nexuiz)
    Mar 04 09:38:23  yeah I agree that nexiuz would be a bad choice
    Mar 04 09:39:44   nexidium is out
    Mar 04 09:39:48   Domains Registered on 2007-07-28_2_77 psroom.com - [ Diese Seite übersetzen ]
    Mar 04 09:39:49   nexidium.com
    Mar 04 09:40:02 <}-z-{> sounds like medicine that makes you fall asleep anyway
    Mar 04 09:40:05   even though the domain currently does not exist, it once did
    Mar 04 09:40:07   that too
    Mar 04 09:41:04   Nuper erat Nexicus nunc est vispillo XSAXius.
    Mar 04 09:41:12   Quod vispillo facit, fecerat ed Nexicus.
    Mar 04 09:41:27   *et
    Mar 04 09:41:47 <}-z-{> nexivouz
    Mar 04 09:41:53 <}-z-{> is that too complicated?
    Mar 04 09:41:54   NO PLEASE NOT
    Mar 04 09:41:56 <}-z-{> haha
    Mar 04 09:42:04 <}-z-{> nexivu?
    Mar 04 09:42:12 <}-z-{> like deja vu with nexuiz
    Mar 04 09:42:12   also, you meant nexez-vous
    Mar 04 09:43:32 <}-z-{> nexivu.com AVAILABLE  
    Mar 04 09:43:56   and just has 10 google hits
    Mar 04 09:43:58   seems usable
    Mar 04 09:44:10   but... don't like it much
    Mar 04 09:44:13   still put it on the list
    Mar 04 09:44:18 <}-z-{> nexi.us AVAILABLE  
    Mar 04 09:44:18  added
    Mar 04 09:44:19 <}-z-{> :-P
    Mar 04 09:44:26   also, hard to pronounce
    Mar 04 09:44:30   "Nexi vü"
    Mar 04 09:44:45 <}-z-{> nexii? (like nex 2)
    Mar 04 09:45:06 <}-z-{> damn, nexit is taken
    Mar 04 09:45:06   like the plural of nexius, nexii m.?
    Mar 04 09:45:28   (nexii would be nexius's plural in latin grammar)#
    Mar 04 09:45:32 <}-z-{> :-P
    Mar 04 09:45:47   actually... good one
    Mar 04 09:45:51   plural form indicates teamplay focus
    Mar 04 09:46:21 <}-z-{> ironic because we drop the 'us'
    Mar 04 09:46:31   HAHA :P
    Mar 04 09:46:35  haha
    Mar 04 09:47:11  nexolus.com is available
    Mar 04 09:47:27 <}-z-{> sounds complicated
    Mar 04 09:51:51  nexvium.com is available
    Mar 04 09:52:49 <}-z-{> too hard
    Mar 04 09:55:15   nexvium?
    Mar 04 09:55:16  nexona.com available
    Mar 04 09:55:17   like valium`?
    Mar 04 09:55:26   could write email spam about it :P
    Mar 04 09:56:36  nexori.com available
    Mar 04 09:57:01  nexoric.com available
    Mar 04 09:57:20  nexorin.com available
    Mar 04 09:57:41  nexorn.com available
    Mar 04 09:58:12  nexolic.com available
    Mar 04 09:59:38  nexole.com available
    Mar 04 10:00:19  nexolum.com available
    Mar 04 10:00:48  nexolix.com available
    Mar 04 10:01:26  nexoic.com available
    Mar 04 10:04:51  nexodo.com is not available, but I made a type and noxodo.com is available
    Mar 04 10:05:49  nexorid.com available
    Mar 04 10:06:14   nexolix lol
    Mar 04 10:06:18   Nex...Oh I see!
    Mar 04 10:07:04  would we consider numbers in the name?
    Mar 04 10:07:29   if not too silly, yes
    Mar 04 10:07:30  I don't know what signifigance a number ight have
    Mar 04 10:07:34   n3xu1z = silly
    Mar 04 10:07:56   nex2go - why not
    Mar 04 10:14:53 <}-z-{> nex4.us AVAILABLE
    Mar 04 10:16:08 <}-z-{> zenuis
    Mar 04 10:16:11   hm... maybe, not sure
    Mar 04 10:16:13 <}-z-{> zen u is :-P
    Mar 04 10:18:50  my updated lsit...alphabetized
    Mar 04 10:18:52  http://pastie.org/private/ocjjrj0175nvbbnqycqna
    Mar 04 10:18:53   I'd prefer to keep religion out of it :P
    Mar 04 10:19:33  oh... add nexodic.com to the available list
    Mar 04 10:20:10   nexodiac
    Mar 04 10:20:13   whatever that is
    Mar 04 10:20:15   nexomaniac
    Mar 04 10:20:27   nexiax
    Mar 04 10:20:46   (or nexiacs)
    Mar 04 10:20:52   necsiax please not, though
    Mar 04 10:21:23   can I invite morphed here btw?
    Mar 04 10:21:29  ok so I would suggest a plan A, B and C... Plan A is to aim for nex????.com, Plan B is to consider a nex???.org that doesn't have an available .com...and Plan C is to consider something not beginning with nex????
    Mar 04 10:21:33 <}-z-{> yes, you can
    Mar 04 10:21:58 <}-z-{> and other developers / forces within the community who'd like to help out
    Mar 04 10:22:06   Dokujisan: I'd prefer plan AB
    Mar 04 10:22:06 *   morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 04 10:22:10    hi
    Mar 04 10:22:19   i.e. both .com and .org should be available if possible
    Mar 04 10:22:29   also, google should find less than 100 hits for the name :P
    Mar 04 10:22:30  right now, Plan A isn't turning out too well. Plan B might have some good names in that "taken" list for .coms.... Plan C is wide open
    Mar 04 10:22:47   nex does not have to be at the beginning
    Mar 04 10:22:50    what are the plans ?
    Mar 04 10:23:06   connexius
    Mar 04 10:23:12  If I were doing this on my own, I would go with Plan C, but I understand the desire to stick with the "nex" prefix
    Mar 04 10:23:21   well, let's say
    Mar 04 10:23:26   I don't want to rule out C
    Mar 04 10:23:31   if you have a really good nex-free name, go ahead :P
    Mar 04 10:23:36   we shouldn't be too fixated on it
    Mar 04 10:23:51    open game developers OGD 
    Mar 04 10:23:51   but dellum, modiem, please not :P
    Mar 04 10:23:55  morphed: my lastest list of name searching.... http://pastie.org/private/ocjjrj0175nvbbnqycqna
    Mar 04 10:24:00   morphed: I mean as game name
    Mar 04 10:24:06   OGDFPS isn't too good :P
    Mar 04 10:24:12   DaveFPS is better for that, then :P
    Mar 04 10:24:24    i mean team name 
    Mar 04 10:24:27   also, OGD sounds like OCD
    Mar 04 10:24:36  we discussed that the team name would be based on the game name
    Mar 04 10:24:41  since the team would only focus on this one game
    Mar 04 10:24:41   probably best
    Mar 04 10:24:47   if there are spinoffs, they can have their own team name
    Mar 04 10:24:51   and team wouldn't be exclusive
    Mar 04 10:24:59   so one person can be on multiple teams with no problem :P
    Mar 04 10:25:28   basically, I think we should be "open source development team of $GAME", and not "company developing $GAME" :P
    Mar 04 10:25:39 <}-z-{> div0: what are you going to do about netradiant?
    Mar 04 10:25:47   why?
    Mar 04 10:25:49   that name can stay
    Mar 04 10:25:55   also will stay on icculus
    Mar 04 10:25:56 <}-z-{> under alientrap as well?
    Mar 04 10:26:00   whether on alientrap, not sure
    Mar 04 10:26:03   it's just the wiki there anyway
    Mar 04 10:26:09   can be copied/moved anyway
    Mar 04 10:26:15   development of NR is not alientrap hosted anyway
    Mar 04 10:26:42  that's good
    Mar 04 10:26:43   however - if we make a portal with lots of "newnex" related stuff
    Mar 04 10:26:47   then NR shall go there too
    Mar 04 10:26:52   it'd simply BELONG there
    Mar 04 10:26:58   old page on alientrap can become a redirect
    Mar 04 10:27:05 <}-z-{> which is the point I'm trying to make :-P
    Mar 04 10:27:15 <}-z-{> just something to consider while we talk out all plans
    Mar 04 10:27:33  we can expect to do redirects on alientrap.org? :-o
    Mar 04 10:27:35   just, I doubt redmine wiki can perform a redirect
    Mar 04 10:27:43 <}-z-{> yes we can
    Mar 04 10:27:46   Dokujisan: I really doubt that AT will object to it
    Mar 04 10:27:48 <}-z-{> div0: meta tag at worst
    Mar 04 10:27:48   so yes, we can
    Mar 04 10:27:52  ok
    Mar 04 10:27:52   AT simply wouldn't care :P
    Mar 04 10:27:55 <}-z-{> .htaccess at best
    Mar 04 10:28:05   only alientrap.org/nexuiz we maybe can't get :P
    Mar 04 10:28:05 <}-z-{> nexzen.org AVAILABLE
    Mar 04 10:28:09   dev.alientrap.org sure will be ours
    Mar 04 10:28:24    isnt alientrap.org hosted on willis server ?
    Mar 04 10:28:28   yes, so?
    Mar 04 10:28:35 <}-z-{> zennex.org AVAILABLE
    Mar 04 10:28:38   basically, I am saying... dev.alientrap.org is not public
    Mar 04 10:28:44   if we don't annoy Vermeulen TOO much
    Mar 04 10:28:51   we will sure be able to keep a redirect from there
    Mar 04 10:28:57   (or even the whole hostname in DNS)
    Mar 04 10:29:07   [-z-]: no zen please :P
    Mar 04 10:29:14   it's a religious term
    Mar 04 10:29:18   keep religion out of the game
    Mar 04 10:29:24 <}-z-{> spirital maybe, religious?
    Mar 04 10:29:28   yes
    Mar 04 10:29:31   same thing basically
    Mar 04 10:29:37 <}-z-{> well it does make me think of zencart
    Mar 04 10:29:41 <}-z-{> which is anything but ZEN
    Mar 04 10:29:42   it is a form of belief
    Mar 04 10:29:52 <}-z-{> it's more like an abortion of code
    Mar 04 10:29:55   one one in a God, but still a belief
    Mar 04 10:29:57   so is atheism :P
    Mar 04 10:30:03   *not
    Mar 04 10:30:14 <}-z-{> jesusnexgodbuddha.com
    Mar 04 10:30:17   no :P
    Mar 04 10:30:22   you forgot the flying spaghetti monster
    Mar 04 10:30:25   and xenu
    Mar 04 10:30:26 <}-z-{> :-P
    Mar 04 10:30:27   and and and
    Mar 04 10:30:34 <}-z-{> of course xenu, how could I forget :-P
    Mar 04 10:30:39   but seriously - don't go there
    Mar 04 10:31:02 <}-z-{> renexia ?
    Mar 04 10:31:09   doesn't fit the game
    Mar 04 10:31:12   sounds like a MMORPG
    Mar 04 10:31:29   renexed?
    Mar 04 10:31:32   (like: reslimed)
    Mar 04 10:31:40 <}-z-{> it's available
    Mar 04 10:31:47   but I don't really like it
    Mar 04 10:31:50   it's a bit uninspired :P
    Mar 04 10:32:02   too generic
    Mar 04 10:33:05   NARF ain't a RipofF
    Mar 04 10:33:08 <}-z-{> nexy.us AVAILABLE
    Mar 04 10:33:28   am not a friend of .us, but fine, put in the list
    Mar 04 10:33:39 <}-z-{> we can just call it nexy in that case :-P
    Mar 04 10:33:40   unless the name means we have to take leileilol's models
    Mar 04 10:33:49 <}-z-{> how's that?
    Mar 04 10:33:54   nexy, no, 116000 google hits
    Mar 04 10:34:28   still... try brainstorming for non-nex names
    Mar 04 10:34:36   these have been under-tried :P
    Mar 04 10:34:51   I think we have enough stuff with nex now :P
    Mar 04 10:34:55   Crylix
    Mar 04 10:35:04   Cryluiz
    Mar 04 10:35:07 <}-z-{> makes me think of orange things
    Mar 04 10:35:14   hm...
    Mar 04 10:35:23 <}-z-{> sounds like crylink too :-P
    Mar 04 10:35:25   Hagrix
    Mar 04 10:35:28 <}-z-{> ha
    Mar 04 10:35:32 <}-z-{> I see what you're doing
    Mar 04 10:35:49   right :P
    Mar 04 10:35:52    xolaris 
    Mar 04 10:35:55   don't have to name it after the Nex
    Mar 04 10:36:11   Laseris
    Mar 04 10:36:17   no, bad
    Mar 04 10:36:28   can we rename the laser gun BTW?
    Mar 04 10:36:34   (like, to the new name of the game)
    Mar 04 10:36:43   it is the most important part of the game after all
    Mar 04 10:36:49   should be named like the game
    Mar 04 10:36:56   the sniper gun on the other hand is quite generic :P
    Mar 04 10:37:22   morphed: Xolaris... haha
    Mar 04 10:37:34   just noticed now that it is not named after Solaris but after a player model :P
    Mar 04 10:37:41   Nexitant
    Mar 04 10:37:54   "Skadium"
    Mar 04 10:38:02   "Spexop"
    Mar 04 10:38:11 <}-z-{> I'm the skad man! "skiddly diddly bo boop wow"
    Mar 04 10:38:13   "The Incredible Marine"
    Mar 04 10:38:21 <}-z-{> TIM
    Mar 04 10:38:29   right
    Mar 04 10:38:35 <}-z-{> no more dave
    Mar 04 10:38:40   I am already using that as "working title" for rube goldberg machines :P
    Mar 04 10:38:50 <}-z-{> ;)
    Mar 04 10:38:51   and a possible future TIM-like mod :P
    Mar 04 10:39:01 <}-z-{> I wish there was a good FOSS version of TIM
    Mar 04 10:39:11   I was going to make one based on Nexuiz
    Mar 04 10:39:17 <}-z-{> >.>
    Mar 04 10:39:18   but stopped when finding out how unpredictable ODE is in DP
    Mar 04 10:39:28 <}-z-{> :-\
    Mar 04 10:39:33   I could reset the machine and restart, and it failed in another way
    Mar 04 10:39:47    its realistic that way
    Mar 04 10:39:50   morphed: yes
    Mar 04 10:39:52   but annoying :P
    Mar 04 10:40:10   once that ODE problem is solved
    Mar 04 10:40:15   I _will_ make the TIM-like game
    Mar 04 10:40:16   except in 3D
    Mar 04 10:40:22   so you move in spectator mode around, and move stuff
    Mar 04 10:40:30   and then can start the machine
    Mar 04 10:40:31  ok I'm going to start venturing more into the non-nex names
    Mar 04 10:40:34   watch it from your view
    Mar 04 10:40:42   and at any time, reset and edit further
    Mar 04 10:41:06   but, for this the ODE support must become more stable
    Mar 04 10:41:19  keep in mind that I'm tracking these names I'm trying just for ideas, so even if dellum is obviously bad (which I think it is) it could lead to another idea
    Mar 04 10:41:28   right
    Mar 04 10:41:35   maybe categorize further into bad ideas and possibly okay :P
    Mar 04 10:41:42   we don't have anything really good yet, though
    Mar 04 10:41:44 <}-z-{> Novel Earth Xebec
    Mar 04 10:41:47   the "bad ideas" of course can be revived
    Mar 04 10:42:15   anyway, have to go
    Mar 04 10:42:19   have fun, and  find a good name :P
    Mar 04 10:42:28 <}-z-{> :-P
    Mar 04 10:42:32 <}-z-{> laterz
    Mar 04 10:42:35  cya
    Mar 04 10:42:38   don't worry, unless you call it nextoris, I won't be likely to reject it
    Mar 04 10:42:51   (although, that would go well with Zygotic)
    Mar 04 10:43:46 <}-z-{> nexfork
    Mar 04 10:43:48 <}-z-{> ^_^
    Mar 04 10:47:51  we're going to be letting go of that japanese kanji for "N"
    Mar 04 10:47:58  well that looks like an "N"
    Mar 04 10:48:03  or "n"
    Mar 04 10:48:08  but
    Mar 04 10:48:12 <}-z-{> maybe find a new kanji character?
    Mar 04 10:48:23  that is why I was leaning toward something beginning with 'x'
    Mar 04 10:48:54    celerity
    Mar 04 11:22:26    i used company name generator and this is what it generated for us http://img237.imageshack.us/img237/6928/companyname.jpg :)
    Mar 04 11:27:16  haha
    Mar 04 11:36:23   yes, that onme we want
    Mar 04 11:39:35    but .com is taken :(
    Mar 04 11:42:06    some other company names with .com free to register http://img535.imageshack.us/img535/476/comanynames.jpg ;]
    Mar 04 11:48:09 <}-z-{> haha, fucki
    Mar 04 11:50:00 *   morphed has quit (Ping timeout: 364 seconds)
    Mar 04 11:53:55 *   morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 04 12:11:57  }-z-{: you're in florida now?
    Mar 04 12:15:37 <}-z-{> yes, I am
    Mar 04 12:15:59  which city?
    Mar 04 12:16:10  my dad and brother are in the room and we're discussing possibly moving
    Mar 04 12:16:15 <}-z-{> Tallahassee
    Mar 04 12:16:19 <}-z-{> in tha panhandle
    Mar 04 12:16:29  ah, ok. we're talking about the tampa area
    Mar 04 12:16:34  or sarasota
    Mar 04 12:16:35 <}-z-{> yeah, that's a bit lower :-P
    Mar 04 12:16:38 <}-z-{> 3-4 hours
    Mar 04 12:16:42 <}-z-{> actually more
    Mar 04 12:16:43 <}-z-{> 4-5
    Mar 04 12:16:45 <}-z-{> haha :)
    Mar 04 12:16:55 <}-z-{> I'll be back in a bit, guys are waiting for me to go to lunch
    Mar 04 13:32:58     Umm
    Mar 04 13:33:02     Someone highlighted me above
    Mar 04 13:33:04     But my log cut off
    Mar 04 13:33:10     Could someone post back what it was?
    Mar 04 13:33:31  let me check
    Mar 04 13:34:23     Thanks
    Mar 04 13:37:32  Samual: http://pastie.org/private/wx3tynbiguzpap2zzscvpq
    Mar 04 13:39:27     Hmmm
    Mar 04 13:39:29     That's odd
    Mar 04 13:39:31     It's not in there
    Mar 04 13:39:51     It must be older than that Dokujisan 
    Mar 04 13:40:12     Meh nevermind, i'm sure it wasn't important
    Mar 04 13:40:56  Samual: sorry, it cut off. Div0 quoted what you said right before that
    Mar 04 13:41:04  about verm being lame, but it's hard to leave nexuiz
    Mar 04 13:41:16  or it's hard to abandon
    Mar 04 13:46:35     Ah
    Mar 04 14:00:16 <}-z-{> 10% of my job still requires me to unplug something and plug it back in >_<
    Mar 04 14:08:32     -z-: And what would that be?
    Mar 04 14:08:41     -z-: Get switches :P
    Mar 04 14:48:54     Hey div0
    Mar 04 14:57:56    come on, brainstorm that name goddamnit 
    Mar 04 15:16:34 <}-z-{> it is a switch
    Mar 04 15:16:48 <}-z-{> it's a netgear 48 port switch that I need to unplug once a month when it fucks up
    Mar 04 15:18:00  morphed: I'll do more brainstorming in a bit, but I went through a shitton of names already
    Mar 04 15:19:19  go through this list and remove the ones that you are absolutely against (in the top and bottom lists)
    Mar 04 15:19:21  http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 15:19:53  just go through and indent the ones you don't like
    Mar 04 15:19:56  and give me back the list
    Mar 04 15:20:01  Samual: morphed -z-
    Mar 04 15:20:07  Taoki: 
    Mar 04 15:20:11     Hmm?
    Mar 04 15:20:22     Well
    Mar 04 15:20:24  I'm here for the next minutes
    Mar 04 15:20:30  go through this list and indent the ones that you absolutely don't like and give the list back to me
    Mar 04 15:20:30  http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 15:20:39  in both the top and bottom lists
    Mar 04 15:20:53  ok
    Mar 04 15:20:57    cant we use 2 words for a name ?
    Mar 04 15:21:04  just start with this first
    Mar 04 15:21:09  smaller name would be better
    Mar 04 15:21:24    why ?
    Mar 04 15:21:34  simplicity
    Mar 04 15:21:38     The easier it is to pronounce the better :P
    Mar 04 15:21:49     :P
    Mar 04 15:21:51  I'm open to two names, but that is more like a Plan D
    Mar 04 15:21:55    i dont have problems with modern warfare, or bad company 
    Mar 04 15:22:04  morphed: can you just start with this first?
    Mar 04 15:22:09  and we can get to that idea after
    Mar 04 15:22:23    Dokujisan: im afraid i dont like any name there :(
    Mar 04 15:22:31  pick the better ones
    Mar 04 15:22:37  they're not all equal
    Mar 04 15:23:26    "nexodicok sa
    Mar 04 15:23:26    " really ? :)
    Mar 04 15:23:43  hu?
    Mar 04 15:23:50  oops
    Mar 04 15:23:56  not sure what happened there
    Mar 04 15:24:10    its sounds like mix of nex, dick and cock ;)
    Mar 04 15:24:14  that is supposed to be "nexodic"
    Mar 04 15:24:26  and I accidentlally typed "ok sa" 
    Mar 04 15:24:29  like I was in IRC
    Mar 04 15:24:47  I didn't realize which window was active :-P
    Mar 04 15:25:45     I said Zenux btw
    Mar 04 15:26:30     iirc -z- liked that one :X
    Mar 04 15:26:31    Zenon :)
    Mar 04 15:26:41     morphed, no :P Common :P
    Mar 04 15:26:52    its redneck name in polish :)
    Mar 04 15:37:17 *   FruitieX (~FruitieX@a83-245-194-105.elisa-laajakaista.fi) has joined #notnexuiz
    Mar 04 15:37:21   Evening.
    Mar 04 15:37:53     Ello
    Mar 04 15:38:04  hi
    Mar 04 15:38:07    hi
    Mar 04 15:38:07     Right now we're still trying to find a name if we do fork
    Mar 04 15:38:15    when we do fork
    Mar 04 15:38:17  almmost done with the list here
    Mar 04 15:38:28   Zymotic
    Mar 04 15:38:31   hehe kidding
    Mar 04 15:38:47    old joke ;)
    Mar 04 15:40:24  I actually considered that at first, but nah
    Mar 04 15:41:36    Citomyz ziuxen
    Mar 04 15:44:08  did  you guys go through that list?
    Mar 04 15:44:58    taoki is working on it right now afaik
    Mar 04 15:45:11  yes, almost done here, in a minute
    Mar 04 15:46:29    http://norefuge.net/vgng/vgng.html 
    Mar 04 15:47:34    Amish Assault Pinball 
    Mar 04 15:48:19   Lol
    Mar 04 15:48:21    Battle Shock 
    Mar 04 15:48:21  Done here http://pastebin.com/nWkJF7TD
    Mar 04 15:48:31  Yeah, I left only 4 from the available .coms
    Mar 04 15:48:42  thanks
    Mar 04 15:48:46  Np
    Mar 04 15:49:05  After this, we should probably make a tpo 5-6 and do an elimination, or a forum pool with them
    Mar 04 15:49:09  *top
    Mar 04 15:49:10   does not have to be .com :-)
    Mar 04 15:49:20  thats good
    Mar 04 15:49:34     I personally want Zenux :P
    Mar 04 15:49:48     Or Xenux 
    Mar 04 15:50:31  Yes, same with the first :)
    Mar 04 15:50:39    its it name of a god of some cult ?
    Mar 04 15:50:39  Xenux too, but not as much
    Mar 04 15:51:06  Zenux or Zenuix or even Zeniux were my favorites from the start
    Mar 04 15:51:06     What I would prefer is not having to change the name at all
    Mar 04 15:51:12     But it seems IllFonic doesn't want that.
    Mar 04 15:52:45    everybody have troubles saying nexuiz 
    Mar 04 15:52:53  yep
    Mar 04 15:52:58 <}-z-{> div suggested we call it 'capsized' :-P
    Mar 04 15:53:01  Nexuiz never was a good name
    Mar 04 15:53:13 <}-z-{> as a joke of course but I figured I'd spread the humor
    Mar 04 15:53:17  but the symbol was good and the shortened "Nex" and "Nexers" sounded good
    Mar 04 15:53:31 <}-z-{> nextfps
    Mar 04 15:53:37  so if we can come up with a name that also has good features, but isn't confusing to pronounce, then we'll be doing well
    Mar 04 15:53:55 <}-z-{> nexfor (what's a nex for?)
    Mar 04 15:54:09   22:53:15 < }-z-{> div suggested we call it 'capsized' :-P
    Mar 04 15:54:10   :p
    Mar 04 15:54:12 <}-z-{> there's a dickfore on your face
    Mar 04 15:54:17 <}-z-{> "what's a dick for?"
    Mar 04 15:54:22  Try to imagine the first time you saw the name "Nexuiz"
    Mar 04 15:54:31  remind yourself that your reaction was "wtf?"
    Mar 04 15:54:46  so that way when we are thinking about this new name, we're letting that name go
    Mar 04 15:55:14  we've been conditioned to be used to "Nexuiz" and we're familiar with it now and associate good things with it
    Mar 04 15:55:18  but it's really not an awesome name
    Mar 04 15:55:36 <}-z-{> I said, "oh, must be european"
    Mar 04 15:55:44  likewise, we can build up another name that starts off being more clear to pronounce
    Mar 04 15:55:49     I thought it was alien.....
    Mar 04 15:55:52     .... Alientrap
    Mar 04 15:55:52    iirc when nexuiz was showed first time in tv, presenter had troubles to say it 
    Mar 04 15:55:59 <}-z-{> because we english speaking folk only use language rules that make sense.....
    Mar 04 15:57:28   tbh, me too :D
    Mar 04 15:57:35   I never knew how to spell it, untill the first time I've heard the announcer :D
    Mar 04 15:57:44  I'm talking cubeowl into the fork
    Mar 04 15:57:56  he's kinda heartbroken 
    Mar 04 15:58:08  sorta like Samual  :-P
    Mar 04 15:58:14     Yes >.>
    Mar 04 15:58:18     I liked Nexuiz <.<
    Mar 04 15:58:31     On the other hand, this leaves us open to changes
    Mar 04 15:58:36  exactly!
    Mar 04 15:58:38  good changes!!!
    Mar 04 15:58:39     And it allows us to structure the team better
    Mar 04 15:58:43  yes!!!!!!!
    Mar 04 16:00:25 <}-z-{> yep
    Mar 04 16:00:31 <}-z-{> build a stronger smarter foundation
    Mar 04 16:00:36 <}-z-{> and 'clean out the attic' if you will
    Mar 04 16:01:01    also it will boost motivation and energy 
    Mar 04 16:01:11 <}-z-{> the hardest part of the transition will be to rebuild the infrastructure for development
    Mar 04 16:01:18 <}-z-{> which will take a least 3 servers
    Mar 04 16:01:23  samual, -z-, morphed: did you go through the list?
    Mar 04 16:01:35 <}-z-{> the repository can be handled on icculus git
    Mar 04 16:01:57 <}-z-{> I have a machine (nn vps) I can donate to be used for test builds and test servers, maybe other things
    Mar 04 16:02:17 <}-z-{> and shared hosting for the website, mirrors.  dokujisan I believe also has a webserver for such files
    Mar 04 16:02:25 <}-z-{> I have a mac to do cross platform compiles
    Mar 04 16:02:29 <}-z-{> Dokujisan: not yet
    Mar 04 16:02:52     Dokujisan, I honestly don't like many at all :P lawl Taoki's list is more than what I would've liked
    Mar 04 16:03:21  Samual: this is to help give a direction on more brainstorming
    Mar 04 16:03:31 <}-z-{> zeniux is the smoothest out of the list still but not sure if that's the best and div didn't want to use 'zen'
    Mar 04 16:03:37  pick your best, even if they aren't fully good enough for your liking
    Mar 04 16:03:57     Xenuix?
    Mar 04 16:04:02     Er
    Mar 04 16:04:03 <}-z-{> that's gross
    Mar 04 16:04:04     Xeniux
    Mar 04 16:04:13     stfu fool, I don't see you thinking up anything better
    Mar 04 16:04:25 <}-z-{> that's because you weren't here earlier when we were thinking
    Mar 04 16:04:29 <}-z-{> oooooh
    Mar 04 16:04:34 <}-z-{> gonna need some ice for that burn :-P
    Mar 04 16:04:35     I saw the log
    Mar 04 16:04:46     Dokujisan pastebined it :P
    Mar 04 16:04:47 <}-z-{> how about notnex?
    Mar 04 16:04:48     I wasn't impressed
    Mar 04 16:05:01  Samual: where?
    Mar 04 16:05:09     From this room?
    Mar 04 16:05:09  oh nvm
    Mar 04 16:05:12  I misread
    Mar 04 16:05:14     lawl
    Mar 04 16:05:26 <}-z-{> uzinex
    Mar 04 16:05:48 <}-z-{> zinex.org AVAILABLE
    Mar 04 16:05:56 <}-z-{> 5 letter ones are good if we can get one of derm
    Mar 04 16:06:14  yreah
    Mar 04 16:06:25 <}-z-{> xudex
    Mar 04 16:06:27 <}-z-{> ex you decks
    Mar 04 16:06:34 <}-z-{> welcome to ex you decks
    Mar 04 16:07:01  don't pick each name apart. mainly just skim through and remove the ones that are absolutely horrible
    Mar 04 16:07:03    Dokujisan: my filter http://pastie.org/854491
    Mar 04 16:07:07  k thanks
    Mar 04 16:07:21   zinex.org is something to consider :-)
    Mar 04 16:07:22 <}-z-{> devnex?
    Mar 04 16:07:32    how about we invite tzork here ?
    Mar 04 16:07:37 <}-z-{> go for it
    Mar 04 16:07:38  absolutely
    Mar 04 16:07:40   do it
    Mar 04 16:07:44  I was trying to get cubeowl first
    Mar 04 16:07:47 <}-z-{> dev[elopers][nex]uiz
    Mar 04 16:07:55 <}-z-{> err, I did my boxes rong
    Mar 04 16:08:01 <}-z-{> dev[elopers]nex[uiz]
    Mar 04 16:08:03 <}-z-{> wrong*
    Mar 04 16:08:04 <}-z-{> ^_^
    Mar 04 16:08:15     dex?
    Mar 04 16:08:17     :P
    Mar 04 16:08:23 *   CuBe0wL (~akion@BKTFW13.usn.hu) has joined #notnexuiz
    Mar 04 16:08:26  yay :-D
    Mar 04 16:08:29     Welcome, CuBe0wL 
    Mar 04 16:08:30    hey
    Mar 04 16:08:33 <}-z-{> hey
    Mar 04 16:08:58    hi
    Mar 04 16:09:08  CuBe0wL: go through this list and remove the ones that are absolutely horrible and give the list back to me... http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 16:09:49    or shot some new names 
    Mar 04 16:09:55   hai CuBe0wL 
    Mar 04 16:09:57  do that after
    Mar 04 16:10:39   night
    Mar 04 16:10:41    I think I'll have to read the avaible .coms
    Mar 04 16:10:43   will read backlog in morning :>
    Mar 04 16:10:57     Dokujisan, can you include .org?
    Mar 04 16:11:01  CuBe0wL: we have a plan A and plan B...so choose also the non-available .coms
    Mar 04 16:11:10     How are you generating that list Dokujisan 
    Mar 04 16:11:12  Samual: we'll get to that after
    Mar 04 16:11:14  by hand
    Mar 04 16:11:28     I bet you can get a script to do that
    Mar 04 16:11:31 <}-z-{> biznex haha
    Mar 04 16:11:32 *   Samual looks at -z-
    Mar 04 16:11:46 <}-z-{> was funnier in my head
    Mar 04 16:11:55  Samual: I have a program that will do it actually
    Mar 04 16:11:58 <}-z-{> because it sounds like 'biznazz'
    Mar 04 16:12:08 <}-z-{> Samual: I have one, it's called an intern :-P
    Mar 04 16:12:42     Bitch I have one too
    Mar 04 16:12:46     It's called a bash script
    Mar 04 16:12:52 <}-z-{> more like bitch script
    Mar 04 16:12:54     It just resolves the names :P
    Mar 04 16:12:55     -.-
    Mar 04 16:12:58 <}-z-{> :-P
    Mar 04 16:13:11    Quadriux ?
    Mar 04 16:13:29 <}-z-{> alright, time to hop onto my iron horse and gallop away from the falling sun
    Mar 04 16:13:40 <}-z-{> I will catch you gentlemen later
    Mar 04 16:13:41    pronounced as "Kvadrius"
    Mar 04 16:13:49 <}-z-{> keep me updated on progress
    Mar 04 16:14:03 <}-z-{> quadraplinex
    Mar 04 16:14:16 <}-z-{> cleanex (har har)
    Mar 04 16:14:29 <}-z-{> klennex is a brand of facial tissues
    Mar 04 16:14:31    xodiox ... this one has pottential imhp
    Mar 04 16:14:32     We'd get sued on that one
    Mar 04 16:14:39 <}-z-{> k, pz
    Mar 04 16:14:44     kleenex actually :P
    Mar 04 16:14:44     Cya
    Mar 04 16:14:52    bye }-z-{ 
    Mar 04 16:14:56    CuBe0wL: xanax ;)
    Mar 04 16:15:04    haha
    Mar 04 16:15:30 *   Dokujisan waits for lists :-)
    Mar 04 16:15:34    exacly
    Mar 04 16:15:34    Forxiuz
    Mar 04 16:15:37    :D
    Mar 04 16:15:41 *   Dokujisan looks at Samual 
    Mar 04 16:15:45    CuBe0wL: maybe you know some cool drugs name ? :)
    Mar 04 16:15:54     Oh I didn't actually MAKE the script yet
    Mar 04 16:16:02     Tell -z- to make his interns do shit
    Mar 04 16:16:46    3-4-phosohoribozile-amino-imidazole-suchsinocarboxamid-snthethase :D
    Mar 04 16:16:49   IllNex
    Mar 04 16:16:52   NexFonics
    Mar 04 16:16:56   -s
    Mar 04 16:16:58   k bai :p
    Mar 04 16:17:09  Samual: I don't need the script
    Mar 04 16:17:13  just need input on the names
    Mar 04 16:17:18    that one is an enzyme name btw :D
    Mar 04 16:17:31     I like mainly what Taoki picked out
    Mar 04 16:17:34  ok
    Mar 04 16:17:47     But mostly Zenux or Zeniux or Xenux and etc
    Mar 04 16:17:51    wuzzat?
    Mar 04 16:18:54    zeniux... yeah, then we'll have shaloin monks fighting over what's the best way to place that vase in a map according to latest feng-shui trends
    Mar 04 16:19:31     Haha
    Mar 04 16:19:34     Okay >.>
    Mar 04 16:19:34    zeniux is very silly in polish 
    Mar 04 16:19:47     Yes
    Mar 04 16:20:17    bbl
    Mar 04 16:20:41     Hey another thing we can change
    Mar 04 16:20:43     NEW FONT.
    Mar 04 16:20:46     ..........
    Mar 04 16:20:47     .....................
    Mar 04 16:21:05     amiriteoramirite?
    Mar 04 16:21:09    maybe some cheesy oldschool arcade game name that tells about gameplay ?
    Mar 04 16:21:21    wingdings at least
    Mar 04 16:23:15     SFIACF?
    Mar 04 16:23:16     :X
    Mar 04 16:23:29     Simple, fast, intense and completely free -.-
    Mar 04 16:23:31     Nah i'm kidding.
    Mar 04 16:24:59  ok here are my picks from the list
    Mar 04 16:25:00  http://pastie.org/private/i9x5ccvczyqjajmngwhzwa
    Mar 04 16:25:44 *   tZork (~blah@c-b42f72d5.31-97-64736c10.cust.bredbandsbolaget.se) has joined #notnexuiz
    Mar 04 16:25:53    hi
    Mar 04 16:25:54     Ello tZork
    Mar 04 16:26:01  I mostly like nexeon, nexion, nexotic, nexilus or nexolus out of the whole list....but I could tolerate the others
    Mar 04 16:26:02  hi
    Mar 04 16:26:27     Well
    Mar 04 16:26:44     I would say we could do a forum post and have a poll.....
    Mar 04 16:26:49  nooooooooo
    Mar 04 16:26:52  can't do this publicly
    Mar 04 16:26:54     But do we want to announce that we're doing this --
    Mar 04 16:26:56     Yeah
    Mar 04 16:27:09  to get the basics outa the way first: im not nessesarely pro-fork
    Mar 04 16:27:21  yeah I cubeowl suggested that
    Mar 04 16:27:44  cubeowl wasn't either, but I think I helped clear up some things about it for him. Now he's likely on the fence or better
    Mar 04 16:28:00  tZork: what are your main reasons for not wanting a fork in this case?
    Mar 04 16:28:08  what are the downsides?
    Mar 04 16:28:32  forking / renaming is sort of admitting defeat, and could possibly mean a lengthy conflict over who's got teh right to what.
    Mar 04 16:29:03  ok first point, we've already discussed a plan for management
    Mar 04 16:29:12  im not saying im nessesarely against it eigther; just that its not a all good option.
    Mar 04 16:29:17    i think that we cant win this
    Mar 04 16:29:25  it needs refinement, but keep in mind that Nexuiz had no outline for how to manage things
    Mar 04 16:29:30    and with GPL cant be any conflict
    Mar 04 16:30:07  but with this new game, we're talking about having it run by a select group (which hasn't been decided yet, just the idea mentioned) for major decisions
    Mar 04 16:30:17  not one single leader
    Mar 04 16:30:22  and that already is a plus
    Mar 04 16:30:34  i would nto count on it morphed, the last few says i experianced things i tought gpl would make impossible.
    Mar 04 16:31:05  we're also only going to be committed to this one game, unlike alientrap
    Mar 04 16:31:36  verm admits that he did this choice primarily because he wants to further alientrap.
    Mar 04 16:32:26  so whatever name is chosen for the game, the development team will be called "the  team"
    Mar 04 16:33:01  i sugest keeping the name nexuiz in that case. possibly pre or postfix it.
    Mar 04 16:33:03  so far, we've had some great discussions with div0 over the past 24 hours
    Mar 04 16:33:10  we can't keep the name
    Mar 04 16:33:17  we need to let that go
    Mar 04 16:33:38    also its not such a great name 
    Mar 04 16:33:55  here is what I said just a few minutes before you arrived.....
    Mar 04 16:33:57   Try to imagine the first time you saw the name "Nexuiz"
    Mar 04 16:33:57   remind yourself that your reaction was "wtf?"
    Mar 04 16:33:57   so that way when we are thinking about this new name, we're letting that name go
    Mar 04 16:33:57   we've been conditioned to be used to "Nexuiz" and we're familiar with it now and associate good things with it
    Mar 04 16:33:57   but it's really not an awesome name
    Mar 04 16:33:57  <}-z-{> I said, "oh, must be european"
    Mar 04 16:33:57   likewise, we can build up another name that starts off being more clear to pronounce
    Mar 04 16:34:07  sure we can, noone owns it afaik. so something like Nexuiz::Nextgen is totally ok to use. and as a plus it will draw some media from ill*
    Mar 04 16:34:12  and at
    Mar 04 16:34:57  I would think that alientrap would be able to fight for rights to that trademark....and that means vermeluen
    Mar 04 16:35:07   <}-z-{> I said, "oh, must be european"
    Mar 04 16:35:13  teh fuck lol?
    Mar 04 16:35:23  and I wouldn't feel right about just stealing that name anyway...not to mention that we don't have the domain
    Mar 04 16:35:32  for whatever name we choose, we should have control over the domain
    Mar 04 16:35:44  so nobody can just sell it or give it someone else
    Mar 04 16:36:34  we also discussed numerous other improvements that we can focus on
    Mar 04 16:36:45  like div0 agreed to a central registration system
    Mar 04 16:36:50    tZork: for me it sounds french 
    Mar 04 16:36:57  with ihs certain preferences for protecting privacy
    Mar 04 16:37:02  his*
    Mar 04 16:37:16  and I talked with him at length about doing official training servers
    Mar 04 16:37:27  and organizing mapping projects
    Mar 04 16:37:42  basically, I hope to become an official community organizer in that regard
    Mar 04 16:38:21  "official" being key here. When things are left to be done by only the community, there is a disadvantage. If things are done from the top down, a lot more momentum can be achieved.
    Mar 04 16:38:39  I can hopefully do what I did for nexuiz but on a larger scale
    Mar 04 16:39:07  this is precisely why I wanted a fork for nexuiz last year....but we didn't have a main developer
    Mar 04 16:39:24  Nexuiz is a semi-successful project by accident
    Mar 04 16:39:54  if it were handled properly, it would have achieved so much more by now
    Mar 04 16:40:18  i allready have two other game projects fightning for my attention, beside my regular work. only reaso i stayed with nexuiz was the legacy and the community.
    Mar 04 16:40:20  but it really didn't have any organization or leadership. Div0 lead out of necessity
    Mar 04 16:40:42  well really the community is likely to come along with us
    Mar 04 16:41:03  we're going along with the new fork....and you like us, right? :-D
    Mar 04 16:41:17  .........right? :-o
    Mar 04 16:41:36  :-(
    Mar 04 16:41:44  anyway, yeah I know you're involved with other games
    Mar 04 16:42:04  im sure not against you, but i dont know if i want to get involved at this point
    Mar 04 16:42:14  like with cubeowl, I know you're busy and I wouldn't be asking you to take some official role that takes up all of your time
    Mar 04 16:42:21  just support this new project in the same way you did nexuiz
    Mar 04 16:42:24  better to state that now then let you doos know it later
    Mar 04 16:42:31    tZork: but legacy will stay, and community will follow us 
    Mar 04 16:43:10  morphed: maybe, but its a chanse for me to make a break with it all. its not like im swamped with free time thise days.
    Mar 04 16:43:32  unlike when i first found nexuiz
    Mar 04 16:43:47  I'm familiar with that
    Mar 04 16:44:41  one of my otehr projects is possibly merge-able with this fork tough. it thats doable; the story is diffrent.
    Mar 04 16:44:57    its like heroin, you cant quit :)
    Mar 04 16:45:18  back
    Mar 04 16:45:25  tZork: can you tell us more?
    Mar 04 16:45:30  or is it under wraps?
    Mar 04 16:45:34  Wow, nice to see so many people joined here :)
    Mar 04 16:45:44  not really Dokujisan, theres just not all that much to tell 
    Mar 04 16:46:30  teh idea was to make a game that adress what we tought nexuiz was missing. 
    Mar 04 16:47:15  :-)
    Mar 04 16:47:17  perfect
    Mar 04 16:47:23  and start from a clean codebase
    Mar 04 16:47:28  ah I see
    Mar 04 16:47:39  well that's interesting to me, though I'm not a nexuiz developer
    Mar 04 16:48:28  basicaly just briging along some ideas, both art and code are to be re-built to adress the large issue of legacy bagage nexuiz suffers from.
    Mar 04 16:48:37  I've heard from other developers that there are some things in nexuiz code that need a cleanup
    Mar 04 16:49:39  despite div0's exelent work on it, its sadly still very much a planless design. as sutch adding and chaning and not the least understanding the code takes a massive effort
    Mar 04 16:49:52  at times
    Mar 04 16:49:55  but I think this central user system is a HUGE change that div0 is finally onboard with and he sees the benefits of it
    Mar 04 16:50:30  and that system can allow a lot of other features to be possible
    Mar 04 16:51:19  the second part of l!ft (the oterh project) where to place it in a steam-punk'ish artline. and quite possibly introduce classbased gameplay and PvM gameplay
    Mar 04 16:53:02  I have basically been slowly heading out the door over the past 6 months as far as Nexuiz is concerned. I was too dissatisfied and wanted to focus on something more productive, so I also have other projects that I'm getting involved in
    Mar 04 16:53:13  I gave up on Nexuiz community efforts
    Mar 04 16:53:21  because it was like swimming upstream
    Mar 04 16:53:38  indeed
    Mar 04 16:53:43  and this is why I tried to organize a fork before.... like last August
    Mar 04 16:54:03  but this mistake by vermeleun could turn out to be a wonderful thing
    Mar 04 16:54:05  a clean slate
    Mar 04 16:54:54  and this interests me again
    Mar 04 16:55:08  especially after my conversations with div0 over the past 24 hours
    Mar 04 16:55:35  to be honest, div0 has changed over the past ....I dunno... 8 moths? To me he seems to have changed
    Mar 04 16:56:27  months*
    Mar 04 16:57:27  but it was good conversation, good ideas discussed and if half of them actually happen, the result will be a game a lot better than Nexuiz
    Mar 04 16:57:58  with a bigger and stronger community
    Mar 04 16:58:16  i will air this with the l!ft team and get back
    Mar 04 17:01:11  cool
    Mar 04 17:01:17  i do have a few thing i feel strongly should be done if i are to join this fork, like at the very least trash all current player models and seriosly audit the code. preferably remake it by pulling things over to a new codebase.
    Mar 04 17:01:35  yes we did discuss new player models
    Mar 04 17:01:57  and a new set of default maps
    Mar 04 17:02:13  that too
    Mar 04 17:02:18  I started a list of maps that could use "fixing" and testing before being added
    Mar 04 17:09:11  http://alientrap.org/forum/viewtopic.php?f=19&t=6054 =P
    Mar 04 17:09:32  Been crazy enough to work on that all day
    Mar 04 17:10:51  hahaha
    Mar 04 17:10:55  exelent
    Mar 04 17:11:05  thanks :P
    Mar 04 17:11:18  http://pics.nexuizninjaz.com/images/zbcmceics6shje6u8wk9.jpg
    Mar 04 17:11:42  however.. make red spawn with tuba only. };P
    Mar 04 17:12:13  yarr i lol @ that pic Taoki =)
    Mar 04 17:12:26  hahaha
    Mar 04 17:12:32  I can't stop laughing myself... :D
    Mar 04 17:12:57  very clever :-)
    Mar 04 17:13:33  thx
    Mar 04 17:13:38  Taoki: CTF?
    Mar 04 17:13:42  "where robbing is a way of showing love" omg spot on xD
    Mar 04 17:13:48  I'll put it on HOCTF
    Mar 04 17:13:55  Yeah, TDM and CTF
    Mar 04 17:14:14  TDM is not so good, since you spawn at any spawn point of any team (not sure if that should be fixed)
    Mar 04 17:15:56  heh you spelled "Nexiuz" properly :-)
    Mar 04 17:16:03  yeah :P
    Mar 04 17:20:50    re for a sentence: back on topic, with the serious talking: what do you do with the servers? Let's say, we fork DCC servers to Nexuiz:NeXtgen. how'd you inform the masses, who don't read the forum?
    Mar 04 17:21:04    also, I've just had a BRILLIANT idea for fork name:
    Mar 04 17:21:09    Pheonix
    Mar 04 17:21:22    pronounced ofc. as Phoenix :D
    Mar 04 17:21:46  Hmmm... that soulds pretty. Nice idea :)
    Mar 04 17:21:50  I'll be informing the masses from HOCTF and HODM servers in the states
    Mar 04 17:21:52    homage to Nexuiz typo, and representing the way a killed game is reborn from it's ahes :D
    Mar 04 17:22:12  heh, I made a server once called Phoenix
    Mar 04 17:22:21  As for informing the masses, I spoke about that with div0 yesterday (we all did on the channel iirc). We can make a new csprogs and put it on servers, that will inform about this
    Mar 04 17:22:24  Also, another idea
    Mar 04 17:22:31  it was "rising from the ashes: of Fusion CTF" my previous server
    Mar 04 17:22:35  turns out that name is overplayed
    Mar 04 17:22:48  ok Nexiuz Wars loading on HOCTF1
    Mar 04 17:23:00  Alias a command to chat a message when playing on servers. But not to press it all the time in an annoying spammy way
    Mar 04 17:23:09  I'll do that once the new name is decided
    Mar 04 17:23:11   Pheonix
    Mar 04 17:23:13  +1
    Mar 04 17:23:16  And press it every once in a while on the DCC servers
    Mar 04 17:23:20  yeah
    Mar 04 17:23:53    though I'm still pro Nexuiz, and no forking
    Mar 04 17:23:59    I like spoon better ;)
    Mar 04 17:25:35  haha Taoki there are holes in the floor
    Mar 04 17:25:55  holes?
    Mar 04 17:26:02  yeah I fall through
    Mar 04 17:26:05    OT again before I leave: ffs, we've printed a final draft of my thesis before binding it, to read through once more
    Mar 04 17:26:17  weird. Probably some compilation issues...
    Mar 04 17:26:19  *issues
    Mar 04 17:26:24    I've already written a full A4 page with errors I've found
    Mar 04 17:26:25  right outside the bases
    Mar 04 17:26:38    and I'm still at only the 10th page
    Mar 04 17:26:48  If its on the terrain, might be another issue with patch meshes
    Mar 04 17:31:18 *   DibTop (~chatzilla@c-71-233-23-46.hsd1.ma.comcast.net) has joined #notnexuiz
    Mar 04 17:31:28     hi notnexuiz :)
    Mar 04 17:31:29    phoenix is great idea but without switched letters 
    Mar 04 17:31:37  hello
    Mar 04 17:31:46    hi
    Mar 04 17:31:57     anyone have a pastie of what was already said so no one has to repeat
    Mar 04 17:32:29  i only got a partial
    Mar 04 17:32:29  I rather like CuBe0wL's version with switched letters. It sounds a bit better for a game like Nexuiz (if we can still call it such until its renamed)
    Mar 04 17:33:08     one thing im working on right now is rigging oblivion's latest model
    Mar 04 17:33:14  Dokujisan?
    Mar 04 17:33:22     mostly for practice but if its any good
    Mar 04 17:34:15 DibTop div0 
    Mar 04 17:34:20  DibTop: there has been a ton of conversation
    Mar 04 17:34:25  I'll show you what I have
    Mar 04 17:34:27  hang on
    Mar 04 17:34:30     thanks
    Mar 04 17:35:52  im interested on what was said before i arrived too Dokujisan
    Mar 04 17:36:37  here is the entire chat since I joine #notnexuiz yesterday
    Mar 04 17:36:39  http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:37:43  heh a bit if bedtime reading ^^
    Mar 04 17:37:48  :-)
    Mar 04 17:39:58 *   soul81 (~soul@a83-163-47-227.adsl.xs4all.nl) has joined #notnexuiz
    Mar 04 17:40:05  soul81: ?
    Mar 04 17:40:18  from netherlands?
    Mar 04 17:40:18 *   soul81 is now known as SoulKeeper_p
    Mar 04 17:40:20   ;)
    Mar 04 17:40:20  ahhh
    Mar 04 17:40:33   here is the entire chat since I joine #notnexuiz yesterday
    Mar 04 17:40:33   http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:40:47  a lot of reading...so I suggest just skimming
    Mar 04 17:40:58   tnx Dokujisan 
    Mar 04 17:41:19   tZork, just poked me, thought join chan
    Mar 04 17:41:26     Dokujisan: make it the topic
    Mar 04 17:41:30 *   Dokujisan has changed the topic to: here is most of the conversation so far -- http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:56:51  the interesting part for me starts at Mar 04 06:19:44 
    Mar 04 18:04:58  will have to continiue reading tomorrow, work in 5h, and i better try n get some sleep first.
    Mar 04 18:05:50  k, cya
    Mar 04 18:15:55 *   tZork is now known as tZork|gone
    Mar 04 18:43:19    what about esteel?
    Mar 04 18:43:31    he was a major contributor too
    Mar 04 18:43:46    I think we'd need to invite him here too
    Mar 04 18:44:01    yeah
    Mar 04 18:46:49 <[-z-]> nexion, nexotic, xenux, zenux are mine out of your last list Dokujisan
    Mar 04 18:47:09  k
    Mar 04 18:48:00 <[-z-]> Dokujisan: are you in darkplaces?
    Mar 04 18:48:07 <[-z-]> #darkplaces
    Mar 04 18:48:08  the channel? no
    Mar 04 18:48:11 <[-z-]> ah
    Mar 04 18:48:12 <[-z-]> hold
    Mar 04 18:48:21  should I be?
    Mar 04 18:48:59 <[-z-]> probably
    Mar 04 18:48:59  Any news about the name? Do we have a top 4-5-6 yet?
    Mar 04 18:49:00 <[-z-]> on anynet
    Mar 04 18:49:13 <[-z-]> http://pastie.org/854774
    Mar 04 18:49:28  omg diablo
    Mar 04 18:49:32  I'm not a fan of his
    Mar 04 18:50:02 <[-z-]> there is more log too if you'd like
    Mar 04 18:50:05 <[-z-]> some interesting stuff is said
    Mar 04 18:51:34  eh, if it involves diablo, I probably don't want to read it
    Mar 04 18:51:35  heh
    Mar 04 18:51:41 <[-z-]> http://pastie.org/854777 nope
    Mar 04 18:54:16  [12:59:23 pm]  div0: I share the theory that it will boost popularity of existing Nexuiz
    Mar 04 18:54:17  yikes!
    Mar 04 18:55:24  It's not impossible.
    Mar 04 18:56:23  They own that name now. The game we know and play as Nexuiz is an asterisk
    Mar 04 18:56:45 <[-z-]> omg that's a great name :-P
    Mar 04 18:56:46 <[-z-]> Nexuiz*
    Mar 04 18:56:52  :-)
    Mar 04 18:57:50  Apart from the popularity loss, I kinda have the feeling it was after all just a name. It doesn't change anything that we see while we play, so Nexuiz is still Nexuiz to me.
    Mar 04 18:58:06  the name is a lot
    Mar 04 18:58:13 <[-z-]> yes but that mangled name was ours
    Mar 04 18:58:14  that should not be underestimated
    Mar 04 18:58:25 <[-z-]> and we all worked together to build what it represents
    Mar 04 18:58:30  We invested our time to build up that name
    Mar 04 18:58:31 <[-z-]> and this new image does not represent us
    Mar 04 18:58:39  Well, it does also mean a lot in the sense that... we are used to it so it's like loosing something we cared for
    Mar 04 18:58:49 <[-z-]> but our rolling stone of a father has tried to tell us this is what we need
    Mar 04 18:59:21  vermeulen certainly did nothing to build up that name. In selling the name (directly or indirectly), he sold our effort and investment in the name
    Mar 04 18:59:29    if we change name, we have milions of players that downloaded nexuiz and didnt liked it back then
    Mar 04 18:59:35  and we now lose that which we helped build up
    Mar 04 19:00:05  I can't ignore the fact that if it wasn't for Vermeulen, Nexuiz wouldn't have existed, however.
    Mar 04 19:00:10    they might download new game because they dont know its old nexuiz 
    Mar 04 19:00:13  yes, starting over....especially with the backstory of a failed GPL project, can attract a flood of new players ....if we do it properly
    Mar 04 19:00:36  this fork would attract a lot of attention
    Mar 04 19:00:39  or could
    Mar 04 19:00:40    and by millions i mean actual numbers from sourceforge downloads :)
    Mar 04 19:00:40 <[-z-]> Taoki: but perhaps another game would have
    Mar 04 19:00:47  brb....food
    Mar 04 19:01:49  I'm confused as to why this is called a fork. Wouldn't it be a fork if we split it into two projects?
    Mar 04 19:02:01  Im rather seeing it as a renaming
    Mar 04 19:02:14 <[-z-]> the future of the alientrap AT is unknown
    Mar 04 19:02:20 <[-z-]> at nexuiz*
    Mar 04 19:03:02  Oh... there might still be one? I thought it's just this Nexuiz getting renamed. That would be bad... there would be two GPL Nexuizes
    Mar 04 19:03:18 <[-z-]> well, it would likely die if we fork
    Mar 04 19:03:28 <[-z-]> unless vermeulen finds a new team
    Mar 04 19:04:12  yeah. Two GPL Nexuizes would be a horrible idea imo.
    Mar 04 19:04:26 <[-z-]> well this would be a different game
    Mar 04 19:04:45 <[-z-]> sounds like a lot of people want to take the opportunity to streamline some things
    Mar 04 19:04:57  Of course, if Vermeulen may wish to do a fock himself to still maintain a GPL Nexuiz of his own, with a team of his own, that would be his choice. Though it would hurt everything badly.
    Mar 04 19:05:03  *fork
    Mar 04 19:05:14 <[-z-]> I doubt he'd have the interest
    Mar 04 19:05:18  I hope it son't be the case
    Mar 04 19:05:20  yeah
    Mar 04 19:05:25 <[-z-]> except only to try and defend his honor
    Mar 04 19:05:31 <[-z-]> but doing so might even make it worse
    Mar 04 19:05:53 <[-z-]> There are enough people that feel like the captain abandoned them
    Mar 04 19:06:04  Yeah, most of us do.
    Mar 04 19:06:18 <[-z-]> div0: is it true that Vermeulen paid you?
    Mar 04 19:07:27 <[-z-]> http://alientrap.org/forum/viewtopic.php?f=1&t=6047&start=0#p76262
    Mar 04 19:08:43 <[-z-]> depending on how vermeulen can spin this PR disaster we might not even have to split
    Mar 04 19:10:09  I hope he doesnt own the alientrap.com website, or the forum
    Mar 04 19:13:51     the name should be DiaboliK really  :P
    Mar 04 19:14:28     did someone suggest Phoenix?
    Mar 04 19:14:48  Something similar
    Mar 04 19:14:53  yeah, that too
    Mar 04 19:15:51  I'm curious about the name. Is there any plan as to when it is decided, or a top with the best names for now?
    Mar 04 19:18:40     DiaboliK as a name wouldn't suck actually :P
    Mar 04 19:18:45     lawl
    Mar 04 19:18:51     It's better than some of the other stuff
    Mar 04 19:23:10  whatever happens with the name, and I was saying this yesterday, we should take some time to pick the proper name
    Mar 04 19:23:12  we have some time
    Mar 04 19:27:02  nexion, nexotic
    Mar 04 19:27:11  nexion is sorta taken already in gaming
    Mar 04 19:27:22  and nexon
    Mar 04 19:27:34  but nexotic doesn't have anything game-related that I can find
    Mar 04 19:28:06  an I found a clan naned team nexotic
    Mar 04 19:28:28  a dance crew named nexotic :-)
    Mar 04 19:29:03  Not sure on Nexotic here. Would be a good name though
    Mar 04 19:30:18  I like the idea of making a game where we can create a new symbol for it
    Mar 04 19:30:56     I like Nexotic
    Mar 04 19:31:09  what about Nexodic?
    Mar 04 19:31:15  I like the 't' better
    Mar 04 19:31:22  what about Nexilus?
    Mar 04 19:31:23     t is better imo
    Mar 04 19:31:31     Nexilus is too similar :X
    Mar 04 19:31:44     nexotic.org is available
    Mar 04 19:31:46     btw
    Mar 04 19:31:52  yeah... we discussed our planning for this
    Mar 04 19:31:59  Plan A is to aim for an avialable .com
    Mar 04 19:32:06     Yeah
    Mar 04 19:32:07  plan B is to consider .coms that are taken
    Mar 04 19:32:54  I like the look of a lot of the names beginning with "x"
    Mar 04 19:33:02  but the pronunciation is trickier
    Mar 04 19:33:10  like xodius or something
    Mar 04 19:33:15  xenotic
    Mar 04 19:33:40  and it's like a backwards of 'nex'
    Mar 04 19:33:45  'xen'
    Mar 04 19:34:47  I already picked the ones i support. http://pastebin.com/nWkJF7TD
    Mar 04 19:35:17  ya I have those
    Mar 04 19:35:31     ziuxen
    Mar 04 19:35:46  you really liked nexvium?
    Mar 04 19:35:47  heh
    Mar 04 19:36:00  Not a lot, but it sounds acceptable
    Mar 04 19:36:10  its one of my least favorites from there
    Mar 04 19:36:46  nexolus is too...weak sounding?
    Mar 04 19:37:02  I think that's what div0 said
    Mar 04 19:37:07  using the 'L' sound
    Mar 04 19:37:58 *   mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 04 19:38:05  mand1nga!
    Mar 04 19:38:15   Mr Dokujisan !
    Mar 04 19:38:21   nice to see you man
    Mar 04 19:38:23  read the link in the topic if you want. It's lengthy
    Mar 04 19:38:26     Ello, mand1nga 
    Mar 04 19:38:32   hey Samual 
    Mar 04 19:38:35   alright
    Mar 04 19:38:52   I've exchanged a few words with Lee today
    Mar 04 19:39:13  heh
    Mar 04 19:40:04   nothing relevant, just .. knowing the enemy ;)
    Mar 04 19:40:18     Phoenix make it Phoinex
    Mar 04 19:40:32     thats a bit weird though
    Mar 04 19:40:49   http://pastebin.com/pjqt20YN
    Mar 04 19:40:51  I'm not keen on phoenix. that name is overplayed by now
    Mar 04 19:41:22  I like it having a name that really has no meaning, a made up word
    Mar 04 19:41:38   I have the name
    Mar 04 19:41:45 *   mand1nga <-
    Mar 04 19:41:46   :>
    Mar 04 19:43:24  ugh.. I read comments made by vermeulen and the illfonic guy and Lordhavoc and it seems like you can't get through to them
    Mar 04 19:43:30  and it's also too late, imo
    Mar 04 19:43:35  what's done is done
    Mar 04 19:44:11  I mean he can't undo it
    Mar 04 19:44:15  there are contracts
    Mar 04 19:44:34   well, that'd be a big problem for them
    Mar 04 19:44:48  I'm at peace with the idea we'll be continuing under a new name.
    Mar 04 19:44:56   imho they can't handle the amount of bad press that is coming
    Mar 04 19:45:05  I'm more than at peace. I'm actually excited for it.
    Mar 04 19:45:06  The only thing I worry about now is a fork of Nexuiz GPL. That would destroy everything.
    Mar 04 19:45:24  This would be a fork of Nexiuz GPL
    Mar 04 19:45:27   I think the commercial version will be dead even before reaching the shelves, like I said before
    Mar 04 19:45:41  A fork as in, 2 projects continuing fro it
    Mar 04 19:45:49 <[-z-]> I don't think there is anything to worry about as long as we organize ourselves and our resources properly
    Mar 04 19:46:00 <[-z-]> improve where the project needs improving and better distribute power
    Mar 04 19:46:32   I see those are separated issues 1) the future of GPL nexuiz and 2) do something against LV disrepectful/unlawful actions
    Mar 04 19:46:35  I like everything that's been said so far in this channel since I joined
    Mar 04 19:46:54  LV?
    Mar 04 19:46:58 <[-z-]> lee vermeulen
    Mar 04 19:47:00  oh
    Mar 04 19:47:16   it seems he is the only one to blame
    Mar 04 19:47:27  lordhavoc played a role
    Mar 04 19:47:37  and regardless of what lee says, I still blame illfonic somewhat
    Mar 04 19:47:39 <[-z-]> different said he never really gave explicity permission to LH
    Mar 04 19:47:39   yes, a minor one imho, but still
    Mar 04 19:47:47 <[-z-]> he said it was more a "I might sell this one day" sort of thing
    Mar 04 19:47:55 <[-z-]> he definitely didn't know about the name thing
    Mar 04 19:48:39   I just can't stand the fact that div0 was kept out of this, I never seen such a lack of respect/manners before
    Mar 04 19:48:41     I didn't know about the name being the same
    Mar 04 19:48:46     However, I knew about the project
    Mar 04 19:49:06 <[-z-]> how long ago?
    Mar 04 19:49:07     I've known about it for quite a while too :X
    Mar 04 19:49:13     Since I got commit access to Nexuiz
    Mar 04 19:49:13 *   morphed has quit (Read error: Connection timed out)
    Mar 04 19:49:26 <[-z-]> who told you? LH?
    Mar 04 19:49:27  To me, Illfonic and Vermeulen are equally guilty
    Mar 04 19:49:35     LordHavoc confronted me about it, -z-
    Mar 04 19:49:41 <[-z-]> I figured
    Mar 04 19:49:47   acces to nexuiz or dp?
    Mar 04 19:49:51 <[-z-]> and no one told div??
    Mar 04 19:49:52     Nexuiz
    Mar 04 19:49:52  well div0 was told about a console port, but he didn't know that it was not going to be benefitting the current Nexuiz and that it would be a completely different game...and of course the use of the name
    Mar 04 19:49:55     I had DP earlier
    Mar 04 19:50:02     -z-: I thought he knew
    Mar 04 19:50:04   wow thats crazy
    Mar 04 19:50:19     If not, he figured it out for the most part
    Mar 04 19:50:29     If you look at the commit log, pay attention to most of the GL changes
    Mar 04 19:50:38 <[-z-]> anyone ever remember a fund raiser for divVerent sponsored by Lee???
    Mar 04 19:50:38   got to go, ttyl
    Mar 04 19:50:50   you have all my support guys
    Mar 04 19:50:52     -z-: No, but i've only been here since 2.4.2
    Mar 04 19:50:59   (coming from the l!ft team)
    Mar 04 19:51:02 <[-z-]> that's another thing he claimed in his reply to my ill comment about where the donations were going
    Mar 04 19:51:02   later.
    Mar 04 19:51:08 <[-z-]> bye mand1nga
    Mar 04 19:51:28  thanks mand1nga!
    Mar 04 19:52:53     Anyway I wasn't aware that they were using our game code either
    Mar 04 19:53:03     I just thought they were using the engine and that's it
    Mar 04 19:53:11  that might be true still
    Mar 04 19:53:14     No
    Mar 04 19:53:18  oh?
    Mar 04 19:53:30  They use parts of the gamecode too. I spotted at least the ghost items, and other users confirmed
    Mar 04 19:53:58     That doesn't necessarily need our gamecode, they could've just taken the feature idea
    Mar 04 19:54:01     Which, i'm fine with
    Mar 04 19:54:09     I'm also upset that they're only doing 2 game modes
    Mar 04 19:54:14     AND THEY'RE REMOVING DEATHMATCH....
    Mar 04 19:54:16 <[-z-]> I don't trust anyone that makes an all flash website
    Mar 04 19:54:45     Listen, you don't remove deathmatch from a game which was originally designed to BE a deathmatch game
    Mar 04 19:54:58 <[-z-]> rm deathmatch
    Mar 04 19:55:06     Bitch you forgot permissions
    Mar 04 19:55:06 <[-z-]> rm -f deathmatch
    Mar 04 19:55:14     -.-
    Mar 04 19:55:24 <[-z-]> chown z deathmatch && rm -vf deathmatch
    Mar 04 19:55:36  I agree. Removing deathmatch is something more stupid than concievable. Its the main gametype
    Mar 04 19:55:36     Fine.
    Mar 04 19:55:47 <[-z-]> I'd play a CTF only game
    Mar 04 19:55:53 <[-z-]> but I'd want it to be crazy style ZTF :-P
    Mar 04 19:56:02 <[-z-]> that is multiple flags with multiple values
    Mar 04 19:56:05     That and they won't add Keyhunt or any other game modes which could be very successful
    Mar 04 19:56:20 <[-z-]> ZTF Fortress is the future! :-P
    Mar 04 19:56:23     I personally would want LMS in there :P
    Mar 04 19:56:38     I bet you LMS could be fun when the server is constantly full :P
    Mar 04 19:56:54 <[-z-]> the world may never know
    Mar 04 19:57:07     Actually it could be calculated
    Mar 04 19:57:19  ok I need to sleep....but I'm excited for this thing now.
    Mar 04 19:57:30  so please keep the momentum going
    Mar 04 19:57:34     lawl
    Mar 04 19:57:45 <[-z-]> take care Dokujisan
    Mar 04 19:57:50  cya
    Mar 04 19:57:53     Cya
    Mar 04 19:58:15     But honestly I would be fine with this whole thing if their company did 2 things: 
    Mar 04 19:58:20     Actually.. 3.
    Mar 04 19:58:44     #1: Change the name to something else... We're the ones with the community who built up the name, we're the ones who want to keep it.
    Mar 04 19:59:33     #2: Credit all contributors of code and content that they used in the game. (That does mean in the game credits itself)
    Mar 04 20:00:15     #3: Take heed of the more important things to the community and listen to their opinions about what they want to do with the game.
    Mar 04 20:00:37 <[-z-]> They already have the "we're better than you, we're saving you, the future is awesome, you don't even know" attitude...
    Mar 04 20:00:39     ........... Like me with being upset about only having TDM and CTF :P
    Mar 04 20:00:41 <[-z-]> so goodluck :-P
    Mar 04 20:01:07     Actually
    Mar 04 20:01:13     All of that................... OR.......................
    Mar 04 20:01:15 <[-z-]> we are so honored to have old school quake players who might have played nexuiz once or twice buy out game
    Mar 04 20:01:18     They give us all their artwork.
    Mar 04 20:01:19 <[-z-]> our*
    Mar 04 20:01:20     ^_^
    Mar 04 20:01:21     ^_^
    Mar 04 20:01:30     I want their fucking artwork damnit
    Mar 04 20:01:31     >.>
    Mar 04 20:01:32 <[-z-]> yeah, I can't believe they've been such jerks about content too
    Mar 04 20:01:34 <[-z-]> well
    Mar 04 20:01:38 <[-z-]> as I said to div in pm
    Mar 04 20:01:46 <[-z-]> even if they just made us a few new models for our game
    Mar 04 20:01:51 <[-z-]> it would appease the crowd
    Mar 04 20:02:02     Indeed
    Mar 04 20:02:04     Well
    Mar 04 20:02:08     I want that style :P
    Mar 04 20:02:16 <[-z-]> severance pk3
    Mar 04 20:02:19 <[-z-]> harrr
    Mar 04 20:02:25     Listen, the style they went for with the artwork is what i've always wanted from Nexuiz 
    Mar 04 20:02:33     When I dream of Nexuiz, that's what I see
    Mar 04 20:02:34     :P
    Mar 04 20:02:35     :P
    Mar 04 20:02:39 <[-z-]> samual is in loooooove, samual is in loooooove
    Mar 04 20:02:44     Bullshit
    Mar 04 20:02:46     But well
    Mar 04 20:02:47 <[-z-]> lol
    Mar 04 20:02:51    gn
    Mar 04 20:02:55     Seriously, that artwork is awesome.
    Mar 04 20:02:56 <[-z-]> nice CuBe0wL
    Mar 04 20:03:01     gn CuBe0wL 
    Mar 04 20:03:06     nite*? 
    Mar 04 20:03:33 <[-z-]> nite*
    Mar 04 20:03:35 <[-z-]> :)
    Mar 04 20:03:37     ^_^
    Mar 04 20:04:43     Anyway, those things happening are what would stop me from leaving Alientrap 
    Mar 04 20:05:09 <[-z-]> yeah
    Mar 04 20:05:26 <[-z-]> well Vermeulen said that he cares more about getting the name of alientrap out there than to get the name changed
    Mar 04 20:05:34 <[-z-]> but he already signed the contract
    Mar 04 20:05:43 <[-z-]> so... I think it's too late for conditions
    Mar 04 20:05:57     Well
    Mar 04 20:06:03     Can't IllFonic still change the name?
    Mar 04 20:06:08 <[-z-]> lol
    Mar 04 20:06:14 <[-z-]> they've already stated they will not
    Mar 04 20:06:17 <[-z-]> and to basically stfu about it
    Mar 04 20:06:23     So?
    Mar 04 20:06:32  let it go :-P
    Mar 04 20:06:44 <[-z-]> so do you hit mario blocks when they question mark is already gone?
    Mar 04 20:06:47     Fine... Meh i'm goin out for a bit
    Mar 04 20:06:51     HEY WAIT A SECOND
    Mar 04 20:06:54     DIDN'T YOU GO TO BED?
    Mar 04 20:06:58     ^_^
    Mar 04 20:07:07  I was awoken by your heart breaking
    Mar 04 20:07:08 <[-z-]> he's sleep ircing
    Mar 04 20:07:13  the sound of your heart breaking
    Mar 04 20:07:22     Lies
    Mar 04 20:07:28  and I thought I heard whimpering
    Mar 04 20:07:34  and I didn't realize IRC had sound support
    Mar 04 20:07:49 <[-z-]> rythmic ascii
    Mar 04 20:08:02 <[-z-]> beep boop bop beep boop
    Mar 04 20:08:03     Anyway, bbiab
    Mar 04 20:08:04  ok really now....sleep
    Mar 04 20:08:12     gn Doku :P
    Mar 04 20:08:17 <[-z-]> who wants to play Nexuiz*?
    Mar 04 20:08:31     Hmm
    Mar 04 20:08:40     That may just be enough to keep me here
    Mar 04 20:08:43     :P
    Mar 04 20:08:47 <[-z-]> I'll be jumping around with a bunch of ho's chasing a flag
    Mar 04 20:08:48     Where?
    Mar 04 20:09:07     Hmm well, maybe i'll join in some time
    Mar 04 20:09:17     ^_^
    Mar 04 20:26:41 *   [-z-] gives channel operator status to CuBe0wL DibTop FruitieX
    Mar 04 20:26:42 *   [-z-] gives channel operator status to mand1nga SoulKeeper_p tZork|gone
    Mar 04 20:26:44 *   [-z-] gives channel operator status to }-z-{
    Mar 04 20:47:28 <[-z-]> nexyes.com AVAILABLE
    Mar 04 20:53:25 *   TVR (~TVR@96.49.107.196) has joined #notnexuiz
    Mar 04 20:55:40    Good to see that this cause is gaining more and more support
    Mar 04 20:56:11  Hi TVR. Yeah, indeed
    Mar 04 21:10:02  bed time here. See you all tomorrow
    Mar 04 21:12:36    Later.
    Mar 04 21:13:56 <[-z-]> goodnight
    Mar 04 21:26:36 *   Taoki has quit (Ping timeout: 364 seconds)
    Mar 04 22:34:22 <[-z-]> I just need to vent that I have contributed 5 websites to alientrap and managed many web related things under the name and was not informed a single bit about this information.  Not even that the website was getting hiacked, I mean sold.
    Mar 04 22:36:14 <[-z-]> I really feel like lee could have worked out a better deal on this part
    Mar 04 23:54:39    [-z-]: Economic recession, maybe he needs to money to pay his credit card debt, heh  
    Mar 05 00:09:53   23:38:00 <@Dokujisan> basically, I hope to become an official community organizer in that regard
    Mar 05 00:09:57   23:38:39 <@Dokujisan> "official" being key here. When things are left to be done by only the community, there is a disadvantage. If things are done from the top down, a lot more momentum can be achieved.
    Mar 05 00:10:01   sounds good :)
    Mar 05 00:10:47   23:41:01 <@Dokujisan> well really the community is likely to come along with us
    Mar 05 00:10:57   their other choice is to stick with 2.5.2 (or svn) :P
    Mar 05 00:12:32   23:48:47 < tZork> basicaly just briging along some ideas, both art and code are to be re-built to adress the large issue of legacy bagage nexuiz suffers from.
    Mar 05 00:12:35   :)
    Mar 05 00:15:03   Also, we need CSQC players. (even though that seems to be impossible/ridiculously hard etc)
    Mar 05 00:15:14   00:01:55 <@Dokujisan> yes we did discuss new player models
    Mar 05 00:15:14   00:02:16 <@Dokujisan> and a new set of default maps
    Mar 05 00:15:17   both: absolutely
    Mar 05 00:15:34     FruitieX>   Also, we need CSQC players. (even though that seems to be impossible/ridiculously hard etc)
    Mar 05 00:15:44     lordhavoc said hes gonna work on that when he gets the chance
    Mar 05 00:15:57   00:09:30 <@Taoki> http://alientrap.org/forum/viewtopic.php?f=19&t=6054 =P
    Mar 05 00:16:00   hahahha
    Mar 05 00:20:02   00:22:41 <@Taoki> As for informing the masses, I spoke about that with div0 yesterday (we all did on the channel iirc). We can make a new csprogs and put it on servers, that will inform about this
    Mar 05 00:20:06   Good.
    Mar 05 00:20:25   As for servers... I have a few
    Mar 05 00:20:37   But I'd prefer them to stay Nexrun, which means we need a proper mod system... :P
    Mar 05 00:20:46   Or maybe replace the Havoc button ;) ;) ;)
    Mar 05 00:20:58   "ChallengeMode"? :P
    Mar 05 00:21:27    We should donate Havoc mode to Illfonic
    Mar 05 00:21:29   00:23:31 < tZork>  Pheonix
    Mar 05 00:21:37   +1, good luck getting a domain for that though
    Mar 05 00:23:38    FruitieX: 2.5.3 isn't coming anytime soon, is the water bug fixed in SVN?
    Mar 05 00:24:06    Otherwise, we'll have to revert back to 2.5...
    Mar 05 00:27:08   lol, water bug was fixed maybe a week after releasing 2.5.2 TVR 
    Mar 05 00:27:30    ... and the hotfix is taking this long?
    Mar 05 00:29:24     they dont have a stable engine to release yet
    Mar 05 00:30:58   01:59:52 < morphed> if we change name, we have milions of players that downloaded nexuiz and didnt liked it back then
    Mar 05 00:31:04   Good point, BTW.
    Mar 05 00:31:20   If the name is less confusing, many of these might not be scared off to try it out again :P
    Mar 05 00:32:08   IMO we should be removing (or at least make sure about revamping) old maps which use the e* (not eX) textures
    Mar 05 00:32:55   Possibly making many new textures from photos (e.g. burningwell is a public domain site for that, or just snap yer own), this is basically what I did for stormkeep2 floor and walls
    Mar 05 00:33:17   (still reading backlog btw, cant see what you're posting ;))
    Mar 05 00:34:44   02:05:21 <@Taoki> Of course, if Vermeulen may wish to do a fock himself to still maintain a GPL Nexuiz of his own, with a team of his own, that would be his choice. Though it would hurt everything badly.
    Mar 05 00:34:48   02:05:26 <@Taoki> *fork
    Mar 05 00:34:51   This could sure be bad yes, but I doubt he'd do that
    Mar 05 00:35:02   Also, if it's GPL'd, we can take over his changes (and vice versa) :P
    Mar 05 00:36:16   No matter what happens... Unless illfonic decides to change name/stop working on console Nexuiz we should change the name IMO
    Mar 05 00:41:08   oooh only 3 pages left :P
    Mar 05 00:41:23   07:28:05 < TVR> ... and the hotfix is taking this long?
    Mar 05 00:41:28   Yeah, it never happened
    Mar 05 00:41:36   There was change after change after change
    Mar 05 00:41:50   waiting for one change to mature, then there's another change
    Mar 05 00:41:55   I guess that's pretty much what happened
    Mar 05 00:42:18   and look what we ended up with, warpzones, somewhat fixed black edges on water etc etc
    Mar 05 00:42:26   new decal system
    Mar 05 00:42:30    Unfortunately, it killed the player base.
    Mar 05 00:42:46    Used to be 150 players at peak, now it's around 90
    Mar 05 00:42:49   yep might as well be
    Mar 05 00:43:19    What are warpzones again? I don't have flash
    Mar 05 00:43:37   Wow, you didn't hear about them?
    Mar 05 00:43:48   They are like teleporters, except seamless ones
    Mar 05 00:43:53    Are they portal cams, or actual portals from portal?
    Mar 05 00:43:57   Just like portals in Valve's portal
    Mar 05 00:44:01   actual portals
    Mar 05 00:44:13    How does reorientation work?
    Mar 05 00:44:19   Except they can be as big as the mapper wants, as invisible as the mappers want
    Mar 05 00:44:36   TVR: There's an entity in the warpzones that set the orientation
    Mar 05 00:44:48   the warpzone killtargets this one iirc
    Mar 05 00:45:28    Oh this reminds me of Darkplaces' inability to support vertical model movement
    Mar 05 00:45:38   http://www.youtube.com/watch?v=5-8atWDlfhY
    Mar 05 00:45:52   yep, in this video you will see
    Mar 05 00:46:12   how the player view is always reoriented so the player will stand up straight after jumping into a warpzone
    Mar 05 00:46:46    Remember, I don't have flash...
    Mar 05 00:47:50    btw, does this http://alientrap.org/forum/viewtopic.php?t=6019&p=76283#p76283 demonstrate Darkplaces to the non-English speaking?
    Mar 05 00:50:24   Oh, don't have flash?
    Mar 05 00:50:51    Yep, Gnash doesn't work for Youtube
    Mar 05 00:51:18   haha nice demonstration x)
    Mar 05 00:51:21   that should be fixed BTW
    Mar 05 00:51:32   case we get new playermodels, they really need to be able to move their upper body
    Mar 05 00:51:56    I wonder how Illfonic is dealing with that.
    Mar 05 00:52:26    Is this just a Big Rigs style cash grab?
    Mar 05 00:52:29   That's done in QC
    Mar 05 00:53:00    Segmented models?
    Mar 05 00:53:09   but really, the way it should be fixed is simply, yep, segmented models
    Mar 05 00:53:17   that coupled with what we already have, aiming the gun up/down
    Mar 05 00:53:47    You mean, the viewmodel of the gun?
    Mar 05 00:54:12     i think before we have a new release we should create new playermodels and weapon models
    Mar 05 00:55:46    Let's skip 2.5.3, and head directly to a 3.0 fork
    Mar 05 00:56:07   DibTop: Yeah
    Mar 05 00:56:16     or 2.6 or whatever
    Mar 05 00:56:24     or just 1.0 with a different name
    Mar 05 00:56:29   Some playermodels are really nice, or let's say were really nice before the texture resolution of them was brought down...
    Mar 05 00:56:48     im working on animating GAK by oblivion
    Mar 05 00:57:33    If all else fails, we can always fall back to pinkbox.
    Mar 05 01:02:36   Lol
    Mar 05 01:02:54   What really should be considered is high-res textures for everything
    Mar 05 01:03:03   Or well, models :P
    Mar 05 01:03:36   Players who don't have lots of VRAM have the option of reducing quality, even only for models (default option)
    Mar 05 01:03:48   could set gl_picmip 1 default, which I think it already is
    Mar 05 01:04:49     they dont even need to do that
    Mar 05 01:04:58     there is a command to reduce the quality of just playermodels
    Mar 05 01:05:04     but i forget what it was
    Mar 05 01:07:03     i want to animate obi's newest model too
    Mar 05 01:07:08     or someone should
    Mar 05 01:07:12     its really nice
    Mar 05 01:20:29   08:05:35 <@DibTop> there is a command to reduce the quality of just playermodels
    Mar 05 01:20:32   thats what i meant
    Mar 05 01:20:39   it's not only playermodels afaik, it's all models
    Mar 05 01:20:52     nope there is one to reduce it just for playermodels
    Mar 05 01:20:57     i forgot i though
    Mar 05 01:24:43   cl_playerdetailreduction? (or whatever)
    Mar 05 01:24:45   for lod?
    Mar 05 01:24:49   that's not what i meant :P
    Mar 05 01:25:18     maybe
    Mar 05 01:25:20     i dont know
    Mar 05 01:34:14 *   FruitieX trying to convince Kedhrin to donate some motion caps 8)
    Mar 05 01:35:13     not gonna happen
    Mar 05 01:43:10   TVR: warpzone! http://pics.nexuizninjaz.com/images/adpd7dnuhndv55pqhar.jpg
    Mar 05 01:43:15   BTW
    Mar 05 01:43:21   would like to have this map included :)
    Mar 05 01:43:26   in the possible fork
    Mar 05 01:44:08   http://pics.nexuizninjaz.com/images/44samcbugfwbl2swcmyu.jpg
    Mar 05 01:52:42   [01:50:43] <@Samual> If not, he figured it out for the most part
    Mar 05 01:52:43   [01:50:53] <@Samual> If you look at the commit log, pay attention to most of the GL changes
    Mar 05 01:52:45   [01:51:01] <@[-z-]> anyone ever remember a fund raiser for divVerent sponsored by Lee???
    Mar 05 01:52:55   no?
    Mar 05 01:53:04   as for commit log: this hinted to a PS3 port of the engine
    Mar 05 01:53:11   but NOT that nexuiz will be hijacked
    Mar 05 01:53:33   [07:43:45] <@FruitieX> TVR: warpzone! http://pics.nexuizninjaz.com/images/adpd7dnuhndv55pqhar.jpg
    Mar 05 01:53:36   does this get good fps?
    Mar 05 01:53:40   asking, ebcause the map is open
    Mar 05 01:53:55   but yes, good use of warpzone
    Mar 05 01:54:09   nice idea to put a door threshold in there
    Mar 05 01:54:14   makes the warpzone glitch way less visible :P
    Mar 05 01:54:20   like, thelighting difference
    Mar 05 01:54:51    It's difficult to recognize when bloom or HDR is enabled
    Mar 05 01:55:38    Heh, do dynamic lights travel through warpzones as well?
    Mar 05 01:55:39   indeed div0 that was the point of adding it i'm sure
    Mar 05 01:56:31   TVR: dynamic lights don't travel through one, no
    Mar 05 01:56:35   neither do sounds
    Mar 05 01:56:40    How about hitscan?
    Mar 05 01:56:47   yep does travel through
    Mar 05 01:56:49   and projectiles
    Mar 05 01:57:06    Can it be one-way?
    Mar 05 01:57:27   not sure, at least before it couldn't
    Mar 05 01:57:50   you could of course do stuff like place a trigger_impulse on one side
    Mar 05 01:57:54    Because it wouldn't make sense to be standing on both sides, if it's only one way
    Mar 05 01:57:55   that pushes you away from it
    Mar 05 01:58:10   TVR: one-way theoretically possible but I didn't support that from QC
    Mar 05 01:58:13   do0n't want one-way :P
    Mar 05 01:58:27   also div0 it got pretty good fps yes
    Mar 05 01:58:35   if you make your own QC code.. you can make it one-way :P
    Mar 05 01:58:36   100 average on my laptop iirc
    Mar 05 01:58:45   after i removed the water on the middle, which was a real performance killer
    Mar 05 01:58:51   ah
    Mar 05 01:58:56   so it already HAD extra renders ;)
    Mar 05 01:58:59   yep :P
    Mar 05 01:58:59   then it indeed doesn't get worse
    Mar 05 01:59:28    gn
    Mar 05 01:59:41 *   TVR has quit ("ChatZilla 0.9.86 [Firefox 3.0.14/2009091913]")
    Mar 05 02:13:54   on my desktop i'm getting about 70 fps with reflections set to sharp
    Mar 05 02:14:06   other than that pretty much everything disabled (textures full though)
    Mar 05 02:14:18   nvidia 6600GT, 2.0GHz old sempron CPU (singlecore)
    Mar 05 02:14:32   it's a bit unstable though, which might be cause of having the browser up at the same time
    Mar 05 02:15:51   or maybe, it hasn't got enough VRAM and is swapping
    Mar 05 02:16:11   now it segfaulted x)
    Mar 05 02:24:57   maybe I have to make warpzones and others be able to have different resolution
    Mar 05 02:25:08   either that, or warpzone maps shall use r_water_resolutionmultiplier in mapifno
    Mar 05 02:25:41   maybe it is good to allow them to have different resolutoion, for weaker hardware
    Mar 05 02:45:59   in the new project
    Mar 05 02:46:05   can  we become incompatible to existing maps?
    Mar 05 02:46:12   I'd like to remove the evil* texture sets
    Mar 05 02:46:30   and repack existing custom maps to instead include the textures if they need them
    Mar 05 02:46:42   basically, I'd like to only include high quality textures
    Mar 05 02:47:47   basically: I think I will make a "nexiuz.git" repository that is like nexuiz.git but with certain parts removed (especially maps and textures)
    Mar 05 02:47:54   will keep the models for now though
    Mar 05 02:48:14   as for maps, will probbaly only include aggressor for a start, and tutorial
    Mar 05 02:48:26   maybe dieselpower too
    Mar 05 02:48:52   and then reinclude ONLY the shaders and textures from the evil sets that are missing
    Mar 05 03:38:37   09:46:45 <@div0> can  we become incompatible to existing maps?
    Mar 05 03:38:37   09:46:52 <@div0> I'd like to remove the evil* texture sets
    Mar 05 03:38:40   i sure vote for this
    Mar 05 03:39:46   09:48:54 <@div0> as for maps, will probbaly only include aggressor for a start, and tutorial
    Mar 05 03:39:59   What about stormkeep2? That one uses mostly my custom made textures and eX textures
    Mar 05 03:40:41   I'm ready to retexture a bunch of other favorites (soylent springs to mind immediately :))
    Mar 05 03:41:05   oh right
    Mar 05 03:41:08   stormkeep2 I forgot
    Mar 05 03:41:14   but will first include NO maps, and then reinclude the ones I want
    Mar 05 03:41:22   and yes... stormkeep2, maybe even with warpzone
    Mar 05 03:41:28   yes :)
    Mar 05 03:41:32   even though I am not fully convinced about it yet
    Mar 05 03:41:36   hehe
    Mar 05 03:41:37   maybe simply should make the warpzone more visible
    Mar 05 03:41:42   yes
    Mar 05 03:41:46   like, with a Portal-like texture
    Mar 05 03:41:46   i have thought about this too
    Mar 05 03:41:59   yeah... or simply some shaderwork
    Mar 05 03:42:00   not elliptic though, valve may own that :P
    Mar 05 03:42:08   sure, thinking of both :P
    Mar 05 03:42:17   on the borders, some blue and orange glow
    Mar 05 03:42:22   otherwise, wavy transparent
    Mar 05 03:42:23   would adding a normalmap to it make it slower?
    Mar 05 03:42:27   no
    Mar 05 03:42:28   like, need an extra render pass
    Mar 05 03:42:29   same code anyway
    Mar 05 03:42:32   neat
    Mar 05 03:42:33   it already needs the pass
    Mar 05 03:42:37   alright
    Mar 05 03:42:42   but, it'd prevenmt future optimization :P
    Mar 05 03:42:47   oh :P
    Mar 05 03:42:48   hmm
    Mar 05 03:42:52   if that ever happens anyway
    Mar 05 03:43:05   I am not sure if iteven CAN be optimized in DP's renderer design
    Mar 05 03:43:07   however...
    Mar 05 03:43:17   I think, if it gets optimized, it'll be by a new dp_warpzone shader parametert
    Mar 05 03:43:24   which would make a un-modifying warp
    Mar 05 03:43:33   and not using dp_refract and dp_camera
    Mar 05 03:43:49   this would optimize the common/warpzone shader
    Mar 05 03:43:58   but not custom made shaders that you would use if ysou want to style it
    Mar 05 03:44:16   so, basically: go ahead, and style it
    Mar 05 03:44:50   :P
    Mar 05 03:45:23   the warpzones on gasoline don't need styling
    Mar 05 03:45:29   they do look clearly like warps anyway :P
    Mar 05 03:45:31   which is good
    Mar 05 03:45:53   they wouldn't be irritating :P
    Mar 05 03:46:04   however - if you style the ones on stormkeep, these could be too
    Mar 05 03:46:30   true
    Mar 05 03:49:05   could make some "standard" for how warpzones look
    Mar 05 03:49:21   would of course need to speak with morphed, tZork etc artists
    Mar 05 03:50:56   lol someone has modified wikipedia already: http://en.wikipedia.org/wiki/Nexuiz#Commercialization_and_Death
    Mar 05 03:50:59   "and death"
    Mar 05 03:51:00   bah :P
    Mar 05 03:51:25   mikee? :P
    Mar 05 03:51:43 *   morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:51:54 *   morphed has quit ()
    Mar 05 03:52:05 *   morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:52:05 *   morphed has quit (Client Quit)
    Mar 05 03:52:21 *   morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:52:33 *   morphed has quit (Client Quit)
    Mar 05 04:14:52   div0: after doing a make, what were the remaining steps to do for a functioning netradiant installation?
    Mar 05 04:15:29   i'm currently getting a message "editor binary doesnt match what the latest setup has configured in this directory. Make sure you run the right/latest editor binary you installed"
    Mar 05 04:16:12   i'm sure that i ran the download-gamepacks.sh script though
    Mar 05 04:19:08   no idea
    Mar 05 04:19:14   that message should never come
    Mar 05 04:19:16   hmm
    Mar 05 04:19:22   can you check for files RADIANT_* in install/?
    Mar 05 04:19:25   can you retry make install?
    Mar 05 04:20:13   eh, now it works yes
    Mar 05 04:20:23   so i'm supposed to get the gamepacks BEFORE make
    Mar 05 04:20:26   it seems like...
    Mar 05 04:40:28   div0: for the new version of Nexuiz I'd like to see light data on the maps calculated by a raytracer
    Mar 05 04:40:48   because in my opinion it manages to look quite a lot better on some maps
    Mar 05 04:40:58   at least if done right... :P
    Mar 05 04:41:34   will you NEVER want to release it?
    Mar 05 04:44:04   or do you happen to have a working raytracer for that?
    Mar 05 04:44:22   the DP one WORKS.... but can't save :P
    Mar 05 04:44:27   it does not :P
    Mar 05 04:44:40   I couldn't get it to light up the floor or ceiling on euclidean fail
    Mar 05 04:44:50   if it had worked, it would have motivated me to add loading and saving for it
    Mar 05 04:44:56   no? hmm
    Mar 05 04:45:09   maybe it has been broken since i tested it
    Mar 05 04:45:12   i know it did work for me
    Mar 05 04:45:17   can you try on euclidean fail?
    Mar 05 04:45:20   sure
    Mar 05 04:45:20   maybe the problem is map specific
    Mar 05 04:45:23   it lit up the walls
    Mar 05 04:45:25   are there rtlights on there already?
    Mar 05 04:45:26   but not the floor and ceiling
    Mar 05 04:45:31   I made some in the rtlight editor
    Mar 05 04:45:34   ok
    Mar 05 04:45:37   these properly lit up the floors/ceilings
    Mar 05 04:45:38   brb first though
    Mar 05 04:45:40   I meanä
    Mar 05 04:45:43   the walls :P
    Mar 05 04:59:10   one question is left - do we HAVE to rename+
    Mar 05 04:59:16   given how hard it seems to be to come out wiht a godo name
    Mar 05 04:59:26   [-z-]: if you keep doing SEO as you did for AT, we might not HAVE to rename
    Mar 05 05:00:03   it is just that SEO and spreading the word would become WAY more important than now
    Mar 05 05:01:01   of course, i got a segfault when turning on rt world lights... :P
    Mar 05 05:01:31   BTW, DP's isn't a raytracer :P
    Mar 05 05:01:36   it works very similar to q3map2's
    Mar 05 05:01:40   just less buggy :P
    Mar 05 05:01:45   that is, IF it works
    Mar 05 05:01:49   heh
    Mar 05 05:02:03   speaking of segfault - also often got segfautls with the lights compile stuff :P
    Mar 05 05:02:09   how come i was able to produce some much sweeter looking lightning for aggressor - then? :P
    Mar 05 05:02:17   oh? can I see?
    Mar 05 05:02:19   even if it doesn't have AO and radiosity
    Mar 05 05:02:23   that was a long time ago div0 
    Mar 05 05:02:24   not tried it on already finished maps
    Mar 05 05:02:26   oh
    Mar 05 05:02:27   i have screens though, hold on
    Mar 05 05:02:29   maybe he borked it :P
    Mar 05 05:02:40   indeed thats what i'm thinking too
    Mar 05 05:02:58   but well
    Mar 05 05:03:01   once it renders right
    Mar 05 05:03:05   I will code loading and saving
    Mar 05 05:03:16   will likely use more GPU memory than q3map2 though
    Mar 05 05:03:30   (as it doesn't pack the lightmaps together so well)
    Mar 05 05:03:35   http://pics.nexuizninjaz.com/images/oq8t3xpshhakub5d0a3.jpg
    Mar 05 05:03:48   wtf is that very bright trim light there though? :P
    Mar 05 05:03:49   http://pics.nexuizninjaz.com/images/rm2gjazwaoo85rvxgd59.jpg
    Mar 05 05:04:34   iirc LH said the lightmaps generated by this are of way smaller resolution than those by q3map2
    Mar 05 05:05:05   guess that comes with a cost too - no sharp shadows
    Mar 05 05:05:24   but well
    Mar 05 05:05:29   I don't think this should be a requirement
    Mar 05 05:05:36   rtlights files, however, should be again
    Mar 05 05:05:44   even on e&b :P
    Mar 05 05:05:53   (but there it really shouldn't be hard)
    Mar 05 05:06:25   well, i just think it looks more realistic than what q3map2 generates :)
    Mar 05 05:06:34   true :P
    Mar 05 05:06:48   q3map2's lightning seems oddly boring in some way
    Mar 05 05:07:01   wish we could do this via e.g. blender's internal renderer or so :P
    Mar 05 05:08:39 *   Spaceman (~Spaceman@87.127.156.98) has joined #notnexuiz
    Mar 05 05:09:09   also div0, euclidean fail seems to work here :P
    Mar 05 05:09:15   oh, cool
    Mar 05 05:09:19   maybe thjere has been a fix :P
    Mar 05 05:09:26   screenshot?
    Mar 05 05:09:33   (of EF with one light :P)
    Mar 05 05:09:42   and you did remember to turn off rtlights again after compiling the lights?
    Mar 05 05:10:00   i did
    Mar 05 05:10:04   i never turned them on in fact :P
    Mar 05 05:10:10   as that seems to be almost 100% crash for me
    Mar 05 05:10:15   after spawning a light, that is
    Mar 05 05:10:44   div0: roof seems oddly dark: http://pics.nexuizninjaz.com/images/rq14ns4laha3scdq2gbz.jpg
    Mar 05 05:11:05   oh, you can use rtlight editor without? :P
    Mar 05 05:11:14   yes, apparently :P
    Mar 05 05:11:15   funny, so floor gets hit, ceiling not
    Mar 05 05:11:41   ceiling gets hit a bit
    Mar 05 05:12:04   maybe light being so close causes some bugs...
    Mar 05 05:12:27   I tried lights in the air too
    Mar 05 05:12:30   or make one on  a wall
    Mar 05 05:15:15   near wall (to the right): http://pics.nexuizninjaz.com/images/oi7gdi1t7esvv0hjlun.jpg
    Mar 05 05:15:35   great, so it actually works for you somewhat
    Mar 05 05:15:35   in the air: http://pics.nexuizninjaz.com/images/hqarpb6pmn29nvovsc4w.jpg
    Mar 05 05:15:41   100 units from the roof
    Mar 05 05:15:45   yep last one looks best
    Mar 05 05:16:04   all of them have radius 1000 btw, which is quite much
    Mar 05 05:16:09   but as i'm only using one light... :)
    Mar 05 05:16:34   the first two pics both have their light pushed only 4 units from the surface (default for r_editlights)
    Mar 05 05:16:58   hm... great
    Mar 05 05:17:06   when I get this working too, I will make loading/saving :P
    Mar 05 05:18:04   aah get it working :P
    Mar 05 05:18:21   also need (in order of importance): skybox sun support
    Mar 05 05:18:38   surfacelight shader parameter support
    Mar 05 05:18:50   surfacelight, not sure if doable
    Mar 05 05:18:54   hmm
    Mar 05 05:18:54   as it is based on the rtlights
    Mar 05 05:19:00   sun. NEEDED, whatever the cost
    Mar 05 05:19:04   right well
    Mar 05 05:19:14   hacky way of doing surfacelight should work
    Mar 05 05:19:21   just spawn some lights above the surface... :P
    Mar 05 05:20:21   of course i had to test, even if i knew the outcome: http://pics.nexuizninjaz.com/images/op1ni605okf37c51z62k.jpg
    Mar 05 05:20:28   through warpzone: epic fail :)
    Mar 05 05:21:00   sure :P
    Mar 05 05:21:03   not really avoidable
    Mar 05 05:21:12   lights in the "connection space" might be supportable
    Mar 05 05:21:17   as they could be transformed to the other side
    Mar 05 05:21:28   but other lights, no
    Mar 05 05:21:55   hehe, maybe could be done using a warpzone preprocessor, which reads a rtlights file, and adds warpzoned versions of all lights :P
    Mar 05 05:22:21   hehe
    Mar 05 05:23:23   problem then of course would be, what if there's a room behind the warpzone, and a light near the other warpzone
    Mar 05 05:23:44   if that makes any sense...
    Mar 05 05:23:51   stormkeep would be a good example here :P
    Mar 05 05:26:39   oh :P
    Mar 05 05:26:51   it should only project the light to the other side, if it fits into the trigger brush of the zone
    Mar 05 05:27:08   that wouldn't cause bugs, but would mean some lights will be missing
    Mar 05 05:31:02   ah of course :P
    Mar 05 05:34:14   another BTW: this looks terrible on patches :P
    Mar 05 05:34:46   +1 on Pheonix, tho thats already taken.
    Mar 05 05:35:16   hm
    Mar 05 05:35:23   FruitieX: patches may be fixable
    Mar 05 05:41:55 *   mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 05:45:38   Here some input according name (random order):(seo tested, and domain name proof.)
    Mar 05 05:45:57   * Nexologic
    Mar 05 05:46:15   * Phanomite (phenomite)
    Mar 05 05:46:22   * JustNex
    Mar 05 06:12:38 *   Morphed (~Morphed@aaqd187.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 05 06:20:55   TehRealNexuiz
    Mar 05 06:21:03   Nexuiz - the ORIGINAL
    Mar 05 06:32:36    ?
    Mar 05 06:33:12    so its not pheonix anymore ?
    Mar 05 06:34:20  the name "phoenix" (or the misspelled Pheonix) name is simply overused.
    Mar 05 06:34:54  a unique name would be best
    Mar 05 06:35:06  preferrably something that doesn't already have a meaning
    Mar 05 06:35:13  just like Nexuiz was
    Mar 05 06:36:56    still its best so far :)
    Mar 05 06:38:54   its pitta on pheonix ye.
    Mar 05 06:39:02  I like nexotic, nexilus, xenotic, nexion (although that one is pretty much taken)
    Mar 05 06:39:07   Morphed, you missed:
    Mar 05 06:39:08   * mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 06:39:08    Here some input according name (random order):(seo tested, and domain name proof.)
    Mar 05 06:39:08    * Nexologic
    Mar 05 06:39:08    * Phanomite (phenomite)
    Mar 05 06:39:08    * JustNex
    Mar 05 06:39:10   * Morphed (~Morphed@aaqd187.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 05 06:39:52   + Nexotic
    Mar 05 06:39:58   1*
    Mar 05 06:40:15  for the 'x' names, xodius is decent too
    Mar 05 06:40:27  the thing is, we can't keep the "n" symbol
    Mar 05 06:40:35  so we're going to have to come up with another symbol
    Mar 05 06:40:58  that's one downside to using the "nex" prefix
    Mar 05 06:41:06  or a name that begins with "n"
    Mar 05 06:41:23    maybe kanji symbol for reborn or phoenix :)
    Mar 05 06:41:32   yea, kinna..or the design should differ then the orig n"
    Mar 05 06:42:09  Morphed: now that's a good idea
    Mar 05 06:42:21  the previous symbol was kanji for power or something
    Mar 05 06:42:32    nexologic ?
    Mar 05 06:42:33    Buy it, use it, break it, fix it,
    Mar 05 06:42:33    Trash it, change it, mail - upgrade it,
    Mar 05 06:44:50    http://www.youtube.com/watch?v=YtdWHFwmd2o
    Mar 05 06:46:27   could use the katakana for "n" ;)
    Mar 05 06:46:30   strength symbol iirc.
    Mar 05 06:46:33   Morphed, hehe
    Mar 05 06:46:35   no, hiragana better
    Mar 05 06:46:53   http://images.google.de/imgres?imgurl=http://upload.wikimedia.org/wikipedia/commons/e/e2/N-hiragana.gif&imgrefurl=http://commons.wikimedia.org/wiki/File:N-hiragana.gif&usg=__GBzjYnWOW-oUlc0qBkv0NYa4tNc=&h=100&w=100&sz=3&hl=de&start=1&tbnid=m-p4h4dshSvgOM:&tbnh=82&tbnw=82&prev=/images%3Fq%3Dn%2Bhiragana%26um%3D1%26hl%3Dde%26client%3Dopera%26sa%3DN%26rls%3Den%26tbs%3Disch:1&um=1&itbs=1
    Mar 05 06:47:08    not that cool
    Mar 05 06:49:15 *   Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 05 06:53:30  ok I got the support of the aussienexers
    Mar 05 06:53:48  so whatever we need them to do for this new-nexuiz fork, they are willing to do
    Mar 05 06:53:50   :o
    Mar 05 06:54:05   thing is still... shouldn't we keep our name somehow nexuiz-related so it can be done as long as possible?
    Mar 05 06:54:13   so basically: maybe a name WITH nexuiz somewhere in it is best
    Mar 05 06:55:02   great, so we have the support of Bogan? ;)
    Mar 05 06:55:09  haha
    Mar 05 06:55:21  well he's the most important one..we MUST get him
    Mar 05 06:55:25    we will have support of willis also 
    Mar 05 06:55:48   but basically... we should make one thing clear
    Mar 05 06:55:51   this should NOT be a fork
    Mar 05 06:56:00   but, we should take over the Alientrap project as a free group
    Mar 05 06:56:15   (will happen anyway, if we do what we are going to)
    Mar 05 06:56:40   so, we do not HAVE to use an entirely new name
    Mar 05 06:56:43   this should NOT be a fork
    Mar 05 06:56:44  ?
    Mar 05 06:56:48   well
    Mar 05 06:56:50   assume we fork
    Mar 05 06:57:02   do you really think anyone at alientrap will be left and willing to do their own "nexuiz" development?
    Mar 05 06:57:07   AT will only care for the console one anyway
    Mar 05 06:57:22  well, that's true, but it's at least verm's decision to do that
    Mar 05 06:57:29   sure
    Mar 05 06:57:33  possibly LH would take over
    Mar 05 06:57:38   doubt it
    Mar 05 06:58:14   he sounded not against the idea of taking Nexuiz out of the hands of Alientrap/Vermeulen, and continuing as an actual FLOSS project, when loosely hinting to that this might happen
    Mar 05 06:58:30  hmm
    Mar 05 06:58:40   and actually
    Mar 05 06:58:47   if we do a fork, exactly that will effectively happen
    Mar 05 06:58:52   LH won't continue with it
    Mar 05 06:59:27   so, there will NOT be two competing lines of development
    Mar 05 06:59:45   simply because NONE of the currently active Nexuiz developers (apart from LH) are in any way affiliated with Alientrap
    Mar 05 07:00:05   so it shouldn't be hard to win them over
    Mar 05 07:00:29   and LH on the other hand won't be unhappy to know that he can now work more on Darkwar
    Mar 05 07:01:07   basically: we do NOT have to be much different from current Nexuiz
    Mar 05 07:01:20  Now that we have more people in here, I would like to discuss some ideas for structure. You mentioned the idea of 3 (or 5?) key leaders to make final decisions and a committee underneath and a process for deciding things. 
    Mar 05 07:01:27   we could, maybe, even use the name (but using JUSt the name Nexuiz would probably be bad, with a variation/suffix would work)
    Mar 05 07:01:39   if we do take another name, we should CLEARLY state that the project was once known as Nexuiz
    Mar 05 07:01:44   PureNexuiz
    Mar 05 07:01:47   JustNexuiz
    Mar 05 07:01:57   does that work for search engines?
    Mar 05 07:02:01   [-z-]: ?
    Mar 05 07:02:08  what's been said a lot so far is that "Nexuiz" was never a good name to begin with
    Mar 05 07:02:12   or would we have to spell it "Pure nexuiz"
    Mar 05 07:02:18   that is true
    Mar 05 07:02:28   yet still, a new name means starting from ground zero, popularity wise
    Mar 05 07:02:34   well div0 its hard to het it up since nexuiz is already there on google rank higher up ;)
    Mar 05 07:02:36  so I don't mind carrying on the use of "nex" in the name
    Mar 05 07:02:38   it would be wise to try to figure out how we can at least gain a BIT from illfonic
    Mar 05 07:03:04  I think the buzz from this story, since it is stemming from a failed GPL project, will help us generate a lot of attention
    Mar 05 07:03:07  if we launch this properly
    Mar 05 07:03:32  anytime there is a big story associated with a GPL project, it ends up on digg, reddit, slashdot
    Mar 05 07:03:52   yes, but that is short term
    Mar 05 07:04:06   but sure
    Mar 05 07:06:52   as for organization, I suggest:
    Mar 05 07:06:57  aussienexers asked why this is secret. The main reason I gave was.... " we have a lot of work to do. getting pelted with constant questions would not help that"
    Mar 05 07:07:01   - three "leaders" who should come from different backgrounds
    Mar 05 07:07:20   - otherwise, freedom should reign among the community
    Mar 05 07:07:39   - "big" decisions (like whole new gameplay balance) should be approved by ALL leaders, who stand personally for the community
    Mar 05 07:07:52   - small stuff can be decided by the community directly (e.g. by just performing a change and committing)
    Mar 05 07:08:11   - nobody will be able AT ALL to sell/relicense the project :P
    Mar 05 07:08:37   PureNexuiz and JustNexuiz both domain wise are avail..
    Mar 05 07:08:50  again, "nexuiz" is deemed a not very good name
    Mar 05 07:09:03  we should let it go
    Mar 05 07:09:04   div0, good simple starting rules
    Mar 05 07:09:24  div0: that sounds good so far
    Mar 05 07:09:35   Dokujisan, one says let it go other wants it, best thing is make up ones mind then act. ;)
    Mar 05 07:09:59   different backgrounds: that should ensure no interest group of nexuiz loses too much weight
    Mar 05 07:10:41   I'd mention: competitive background (this leader job will most likely go to Dokujisan, or maybe NN), "play for fun" background (e.g. PB)
    Mar 05 07:10:48   but there'd be more
    Mar 05 07:11:00  my main interest is that I want to be a community organizer and help with recruiting new talent to the project, marketing efforts, manage volunteers from within the community
    Mar 05 07:11:06   sure
    Mar 05 07:11:10   that wouldn't be inhibited :P
    Mar 05 07:11:31   but regarding game relevant decisions, you probably will represent the competitive side, which is good, as that NEEDS to be represented
    Mar 05 07:11:55   and with interest groups, I mean "from the players"
    Mar 05 07:12:10   so... let me ask this way
    Mar 05 07:12:13   why do you play Nexuiz?
    Mar 05 07:12:25  it's my replacement for martial arts heh
    Mar 05 07:12:51  I used to train in martial arts a lot. I don't as much and nexuiz sorta took that spot.
    Mar 05 07:12:57   I mostly play for fun, and therefore like development of new stuff and experimenting... others play competitively, which of course prefers sticking to the roots
    Mar 05 07:13:14   (and requires stability in the "core game")
    Mar 05 07:13:26   I can understand why div0 or tZork|gone does not want to necessarily leave the name "nexuiz" ...they are indd some major pro cons to that.
    Mar 05 07:13:36  and I like the organization-side of business and I get to do some of that within nexuiz
    Mar 05 07:13:43   but there sure is more interest groups
    Mar 05 07:13:53   Dokujisan: well, it should NOT be organized like a business :P
    Mar 05 07:13:57   we have seen what happens then ;)
    Mar 05 07:14:05  certainly not like a business, no
    Mar 05 07:14:18  but the 'organization" aspect of running a business is interesting to me
    Mar 05 07:14:21   but sure, if you are good at it AND flexible in thought (not time)...
    Mar 05 07:14:24   then that is great
    Mar 05 07:14:31   and you indeed seem that way
    Mar 05 07:15:15   also, I always had an interest in the theory of politics... and how it usually fails :P
    Mar 05 07:15:30   which is why I now will try to ensure a structure with a sort of "division of power", but without the bureaucracy
    Mar 05 07:15:42   I mean, we sure shouldn't divide into legislative, executive, judicative :P
    Mar 05 07:16:01  I see
    Mar 05 07:16:08   but, we should indeed learn some lessons from history of politics :P
    Mar 05 07:16:21   like: "much power in one person = FAIL"
    Mar 05 07:16:47  I agree
    Mar 05 07:17:03  a good project needs leadership, but that leadership shouldn't be one single person
    Mar 05 07:17:04   and as we have seen now, it's even MORE fail, if nobody knows/realizes that someone has the much power :P
    Mar 05 07:17:14  haha yeah
    Mar 05 07:17:21   also, as a free project, leadership should not be exerted by force :P
    Mar 05 07:17:40   if someone wants a feature, and the leaders are against it, one should think about a way to get it in in a varied but better fashion
    Mar 05 07:18:15   code wise, I'd go so far - if the code is harmless (e.g. if it can be turned off), and mostly bug free, it can go in - even if I don't like what it brings
    Mar 05 07:18:41   art wise it's a bit more difficult, as there can be many opinions what is good and what is not
    Mar 05 07:19:28   there, I'd only like to avoid bad taste (like, pr0n, or TOO strong displays of violence - after all, the game is meant to be PLAYed, and is not a virtual torture chamber)
    Mar 05 07:19:55   of course, the competitive players ALSO do not want overly strong violence, as it blocks the view :P
    Mar 05 07:20:04  yeah... like leaving out "You pussy!!" voice recordings :-)
    Mar 05 07:20:18  or whaever that thing said
    Mar 05 07:20:20   as a non-native speaker, I mainly think of a cat when hearing that...
    Mar 05 07:20:23   but yes, maybe that should go
    Mar 05 07:20:44   there's enough "verbal violence" in chat, we don't need it in sounds too:P
    Mar 05 07:21:47   basically... I think regarding that, the game should be in a way so that the Pope wouldn't object to playing it, other than him probably not being interested in video games :P
    Mar 05 07:22:14   and there isn't much needed to achieve that... guns are generally accepted as GOOD ;) and the rest is fine, apart from soem voice recordings
    Mar 05 07:22:25  I have to say that I've agreed with 99% of what you've said over the past 48 hours during these chats. The only thing I disagreed with is the privacy concerns with central user system, but we discussed and resolved that now. So I'm very excited and hopefully for where things are going.
    Mar 05 07:22:41  hopeful*
    Mar 05 07:23:18   regarding violence for example: I like that our guns are either unrealistic (electro, hlac), or those which do make sense in real life, aren't overly graphic (like shotgun)
    Mar 05 07:23:53   shooting someone with a Nex IMHO does not count as graphic violence, as nobody would ever take a scifi weapon for real :P
    Mar 05 07:24:20  Yeah, that is true as well.
    Mar 05 07:24:20  I really like the futuristic theme that Nexuiz has grown into. I understand it started out more with an industrial/gritty theme like Quake, but changed over time to more futuristic
    Mar 05 07:24:22  Hi all
    Mar 05 07:24:43   this is also BTW why I don't like mikeeusa's "cutting" idea :P
    Mar 05 07:24:50   I do not WANT lasers to cut player models into parts
    Mar 05 07:25:00  Well, I was at some point pondering pain skins. Like a blood layer being stuck to players based on their health
    Mar 05 07:25:05   but using it for func_breakable to break a window into parts, sure, yeah
    Mar 05 07:25:20   Taoki: I wouldn't care for it violence wise, but it'd eat GPU memory like hell
    Mar 05 07:25:31  For realism... I don't really like gore and stuff
    Mar 05 07:25:38  ah, i see
    Mar 05 07:26:12   breaking THINGS is not exactly graphic violence after all :P
    Mar 05 07:26:17  yeah
    Mar 05 07:26:27   huge explosions, hell yeah
    Mar 05 07:26:30  Well the old Kingpin - Life of Crime (gang game made over the Quake 1 2 or 3 engine, 10 years old at least) had pain skins, but they were 2 different versions of each player skin
    Mar 05 07:26:54   thus I also like the idea that in a fps like Nexuiz, you don't really die
    Mar 05 07:26:57   you just respawn :P
    Mar 05 07:27:13   you respawn and need to collect items again, but you can continue playing
    Mar 05 07:27:29  What i'd like to see though is after-damage effects like in UT2004. eg. You shoot someone with the machinegun, they spray a blood trail for a second. Electro, they have lightning coming out of them for a second, etc.
    Mar 05 07:27:39   that sure makes you way less immersed to the game - but I like it, I like playing "detached" from the game
    Mar 05 07:28:11   Taoki: csqc networked players and we can have it :P
    Mar 05 07:28:16   of course with cl_gentle versions of it ;)
    Mar 05 07:28:30  yeah. It can be enabled only if cl_gentle is
    Mar 05 07:28:38  I tried implementing it a long time ago
    Mar 05 07:28:42   that can be enabled in non-gentle too...
    Mar 05 07:28:45   I do not object to it
    Mar 05 07:28:52   as it doesn't make the game more violent
    Mar 05 07:28:57  But couldn't figure hot to put a constant particle generating entity to a player
    Mar 05 07:29:06   whether the blood is sprayed on hit, or slowly over time, changes not much
    Mar 05 07:29:07  Which then dies off after a time
    Mar 05 07:29:13   but slowly over time looks better and gives better fps
    Mar 05 07:29:17   yes
    Mar 05 07:29:23   this is what you need CSQC networked players for
    Mar 05 07:30:06 *   tZork|gone is now known as tZork
    Mar 05 07:30:08   do not do it on server qc, although you maybe could
    Mar 05 07:30:12   as ti'd be a huge bandwidth hog
    Mar 05 07:30:26   in server qc, sure, you could make a particle emitting ent and make it MOVETYPE_FOLLOW the player
    Mar 05 07:30:31   but don't, that eats BW like hell
    Mar 05 07:31:08   if you want it for your own mod, sure, can code it for you :P
    Mar 05 07:31:15   (the server side variant)
    Mar 05 07:31:22  what a day.. hi fokes.
    Mar 05 07:31:27   hi
    Mar 05 07:32:18   hi
    Mar 05 07:32:27  gebuz the backlog is abt as as logn as Doku's log hehe. will be hard to keep read up on it all. 
    Mar 05 07:32:33  lol
    Mar 05 07:32:45  we just covered ideas on organization
    Mar 05 07:32:52  so scan the recent chat for that
    Mar 05 07:33:27  I'll end up replacing that notnexuiz.log with page giving bullet points
    Mar 05 07:33:36  after some decisions are nailed down
    Mar 05 07:33:55  I need to skim through our discussions about map choices and put those into my notes
    Mar 05 07:35:23 *   Taoki has quit (Ping timeout: 364 seconds)
    Mar 05 07:35:31  a totaly flat organization (as in all votes are equal on all subjects) would be interesting. very likely "to interesting" tough ;)
    Mar 05 07:36:18   totally flat would probably not work :P
    Mar 05 07:36:21   then you can do nothing
    Mar 05 07:36:42   but there should be "enough" leaders, and they should represent various aspects of the game
    Mar 05 07:36:52   especially the aspects that tend to cause controversy
    Mar 05 07:37:07   the goal is to choose leaders so that any possible controversy is also among the leaders :P
    Mar 05 07:37:27  one thing that is difficult with a committee vote is if not everyone is around to vote
    Mar 05 07:37:33  like on vacation or something
    Mar 05 07:37:34   yes
    Mar 05 07:37:51   also, not sure if voting by itself actually works
    Mar 05 07:38:09   and, big decisions that NEED all leaders to agree (and most of the community) don't happen that often
    Mar 05 07:38:21   big gameplay changes can e.g. first be done in a branch, and later applied
    Mar 05 07:38:40   most stuff that is being developed is stuff that does not interfere with anyone else
    Mar 05 07:38:46  div0: tZork was asking about (or suggesting, rather) some code cleanup for nexuiz
    Mar 05 07:38:50  tZork: can you go more into that?
    Mar 05 07:38:57  it does work, when the involved parties are somewhat limited in number, and fairly like minded. in that piticular case (in my own experiance) that model is acctualy superior. but its a rather delicate entity.
    Mar 05 07:39:17   tZork: in case of Nexuiz community, no
    Mar 05 07:39:20   see the CTF scoring case :P
    Mar 05 07:39:24  hehe
    Mar 05 07:39:40   everyone convinced that the old was is bad - but also everyone proposing and insisting on his own way to solve it
    Mar 05 07:39:52   so whatever decision is taken (even "no change at all"), you have 80% against you
    Mar 05 07:40:08  for CTF scoring, we finally did some proper testing, but unfortunately that testing was done "live" as the default. Everyone on my servers thinks the scoring is strange.
    Mar 05 07:40:19  how to fuck up a good idea - just add ppl ;)
    Mar 05 07:40:27  ;-)
    Mar 05 07:41:01  I understand the ideas behind the scoring though. Luckily, scoring isn't a top priority issue. People still love the game even with messed up scoring.
    Mar 05 07:41:03  sure Dokujisan, well my main gippy with nexuiz codebase it its planless. and suffers there of.
    Mar 05 07:41:27   tZork: most stuff is quite clean
    Mar 05 07:41:32   and I don't think we should overthrow it all
    Mar 05 07:41:37   I am rather for slowly reorganizing it
    Mar 05 07:41:51   the parts that probably SHOULD be overthrown and replaced: teamplay.qc :P
    Mar 05 07:41:55  quality wize, yes, tnx to you im most cases div0
    Mar 05 07:42:15  but its following much the random structure it happend to evole into
    Mar 05 07:42:17   what I fear of a "cleanup" is that 80% of the features will be gone
    Mar 05 07:42:43   and THAT I will never approve of
    Mar 05 07:42:52  thus has major unnessesary overhead, and its a bitch to get into for anyone from teh outside.
    Mar 05 07:43:04   well, how are you going to fix that?
    Mar 05 07:43:14   I am certainly rejecting the idea if it emans that all interesting features are gone
    Mar 05 07:43:23  start clean, copy stuff over. but have a plan for it.
    Mar 05 07:43:34   I won't have much time for that, neither much motivation
    Mar 05 07:43:41   also, it WILL mean that most features are gone
    Mar 05 07:44:04   probably all that I did, as I won't have the motivation to implement it all a second time
    Mar 05 07:44:12  successfull evolution means dropping off dead weight.
    Mar 05 07:44:18   depends
    Mar 05 07:44:28   I bet you consider Keyhunt dead weight
    Mar 05 07:44:38   so YOU would not reimplement it
    Mar 05 07:45:15   also, how are you even going to reorganize the bot code? Nobody on earth understands it :P
    Mar 05 07:45:19  not sure, this is a specific case tough, what i want to talk abt it the general idea
    Mar 05 07:45:32   general idea may be fine, but it probably won't eb Nexuiz any more then
    Mar 05 07:45:34  if noone cares enougth to port feature X over, its rather likely that noone cares abt afore
    Mar 05 07:45:35   but a totally different game
    Mar 05 07:45:38  maybe we can do a code review by a number of people (developers) and start taking notes of areas of the code that they feel needs cleanup. 
    Mar 05 07:45:50   tZork: it is not about caring
    Mar 05 07:45:54   but also about having the time for it
    Mar 05 07:45:56  and then we can discuss it better after we know what exactly we're talking about (what areas of code)
    Mar 05 07:46:23   tZork: if it's some hidden feature nobody ever uses, sure, then that can be "reorganized away"
    Mar 05 07:46:32   but what would that be, apart maybe from runematch?
    Mar 05 07:46:40  omg I forgot about runematch
    Mar 05 07:46:42   or certain failed balance_teams modes that all suck
    Mar 05 07:47:29 *   Disconnected (Connection reset by peer).
    **** ENDING LOGGING AT Fri Mar 05 07:47:29 2010

    **** BEGIN LOGGING AT Fri Mar 05 07:48:15 2010

    Mar 05 07:48:15 *   Now talking on #notnexuiz
    Mar 05 07:48:15 *   Topic for #notnexuiz is: here is most of the conversation so far -- http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 05 07:48:15 *   Topic for #notnexuiz set by Dokujisan!~doku-lapt@74-132-116-73.dhcp.insightbb.com at Thu Mar 04 17:41:49 2010
    Mar 05 07:48:23   plus, keyhunt already has quite a good structure
    Mar 05 07:48:27  keyhunt - sure, but id exspect you to wnt to do taht.
    Mar 05 07:48:42   problem is, it is now CLEAR that I will have MUCH less time in the future
    Mar 05 07:48:47   I want keyhunt to stay in Nexuiz and be pushed more
    Mar 05 07:48:53  okay
    Mar 05 07:48:57   but in about 9 months from now, I will SURE not be able to work on it
    Mar 05 07:49:07   (yes, breaking news)
    Mar 05 07:49:38  I like Assault
    Mar 05 07:49:44   so basically, I'd rather think that it should be evolutionary restructured in some way
    Mar 05 07:49:54   the goal should be to bring ALL features over
    Mar 05 07:49:58   maybe mark in the old code what you have
    Mar 05 07:50:08   and continue, keeping only the unimplemented stuff in the old code
    Mar 05 07:50:20   so one can easily track what is done and what not
    Mar 05 07:50:42   the keyhunt code for example shouldn't be too hard to integrate into a new code base, same goes for race
    Mar 05 07:50:51  right
    Mar 05 07:50:54   as the code for it is in its own qc file, and called by callbacks from outside
    Mar 05 07:50:59   all game modes should be that way, of course :P
    Mar 05 07:51:16  this is the kinda stuff i want to see more. 
    Mar 05 07:51:27   but basically, the goal should NOT be stripping the game to "what I like"
    Mar 05 07:51:31   and also NOT reimplementing it
    Mar 05 07:51:36   but JUST reorganizing the code
    Mar 05 07:51:42   not silently removing stuff
    Mar 05 07:51:44    that sounds like a good plan
    Mar 05 07:52:02   and an idea to actually do that, is to keep the old code in a subdir of a branched revision tree
    Mar 05 07:52:05   or even better.
    Mar 05 07:52:13   make a server.new and client.new directory
    Mar 05 07:52:16   and develop the new stuff there
    Mar 05 07:52:23   it shall have the old code in a subdir
    Mar 05 07:52:32   and whenever you have implemented something
    Mar 05 07:52:38   you delete it from the copy of the old code before committing
    Mar 05 07:52:56   so you see how the old code shrinks and shrinks, and the new one grows
    Mar 05 07:53:01 *   Dokujisan has quit (Ping timeout: 364 seconds)
    Mar 05 07:53:02  What needs to be reogranized though, and why?
    Mar 05 07:53:04 *   You are now known as Dokujisan
    Mar 05 07:53:05   when done, the old code will contain a rotten mess with no features
    Mar 05 07:53:10   Taoki: just LOOK at teamplay.qc
    Mar 05 07:53:23   the worst file of all that we have
    Mar 05 07:53:32  *brrr*
    Mar 05 07:53:47   also, stuff that probably can stay as is, is all in common/
    Mar 05 07:53:55   client/ is mostly fine, but stuff needs to be moved into proper files
    Mar 05 07:54:05   Main.qc is cluttered, sbar.qc and View.qc separation is unclear
    Mar 05 07:54:17  better file separation is needed in many places iirc
    Mar 05 07:54:21   right
    Mar 05 07:54:21  yeah, some of that is true.
    Mar 05 07:54:34   in server, a redesign of some code parts probably needs more work than just shiftign around code between files
    Mar 05 07:54:35  and some new subdir perhaps
    Mar 05 07:54:38   although this would likely fix client
    Mar 05 07:54:43  Does it have to be a code remake specifically, or can each part be optimized and rearranged slowly in time?
    Mar 05 07:54:52   Taoki: depends :P
    Mar 05 07:55:05   code remake with "copying" much old code
    Mar 05 07:55:09  doxy style commentarys for auto documentation will let ppl get into it fast
    Mar 05 07:55:14   e.g. many game modes have a somewhat clean implementation that can be taken over as is
    Mar 05 07:55:20   unfortunately that does not include CTF
    Mar 05 07:55:48   but Domination, Keyhunt, Race, and of course TDM (not really a mode) would most likely work with exactly their current code
    Mar 05 07:55:55   14:54:56 <@div0> Main.qc is cluttered, sbar.qc and View.qc separation is unclear
    Mar 05 07:56:00   this should be fixed in the panelhud branch
    Mar 05 07:56:04   ah, great
    Mar 05 07:56:09   even if the idea of the panelhud is not approved
    Mar 05 07:56:18   why would it not be :P
    Mar 05 07:56:21   we'll see what it turs out to be :P
    Mar 05 07:56:24   turns*
    Mar 05 07:56:29   if anything, the idea of configuring this in the menu will not be :P
    Mar 05 07:56:39   but then you can still have different HUD "skins" as cfg files
    Mar 05 07:56:46   it is done in CSQC to 100% right now :P
    Mar 05 07:57:05   yep as cfg files sure
    Mar 05 07:57:05   tZork: basically, a start would be identifying what is rotten
    Mar 05 07:57:10   then making a new clean code base
    Mar 05 07:57:14   and then trying to reintegrate all
    Mar 05 07:57:20   the new clean code base should focus on DM and TDM
    Mar 05 07:57:41   (yes, immediately with TDM support, as that will be important to have other teamplay modes not too complicated)
    Mar 05 07:57:51  div0: ill dig up my l!ft planning, as i started doing just that before i decided to go scratch intsed. if i can find it.
    Mar 05 07:57:55   shouldn't it just be some sort of "interface" for game modes
    Mar 05 07:58:01   and have each and every gamemode separate in different files
    Mar 05 07:58:05   FruitieX: not possible
    Mar 05 07:58:13   oh...
    Mar 05 07:58:13   many game modes must interact to very specific events
    Mar 05 07:58:15   like player dying
    Mar 05 07:58:23  Btw, rendomly remembered. Has anyone taken a look at the forgotten contributions I linked yesterday (or 2 daysd ago) here?
    Mar 05 07:58:30   not yet
    Mar 05 07:58:30  its possible acctualy
    Mar 05 07:58:42   tZork: how do you KNOW all the places that need interaction? :P
    Mar 05 07:58:49  I should probably make a topic with all of them, so they won't be forgotten
    Mar 05 07:58:54   Race also needs quite much interaction (but that oen not with dying, but with spawning)
    Mar 05 07:59:04  the problem is it requiers a re-write
    Mar 05 07:59:16   rewrite is bad, as it means only 20% will be taken over
    Mar 05 07:59:19  div0: registerd events
    Mar 05 07:59:24   but sure
    Mar 05 07:59:30   such a thing wouldn't be a rewrite
    Mar 05 07:59:43   I expect to be able to use existing game mode code, and add an init function that registers the callbacks as event handlers
    Mar 05 07:59:54   THAT is how it should be possible without rewriting all game modes
    Mar 05 08:00:47  mode X registers what events to recive in some form of initialazation, each event handler has slots, or chains so mutators are effectuvly just non exclusive modes.
    Mar 05 08:00:53   basically, I want restructure, not rewrite
    Mar 05 08:01:04  thats roughtly teh idea i had for lift anyway
    Mar 05 08:01:08   most existing "feature specific" code should work as is
    Mar 05 08:01:15   except for an init function registering handlers
    Mar 05 08:01:24   but the generic code base of course need schanging
    Mar 05 08:01:34   probably entirely rewriting
    Mar 05 08:02:04   also, quite some subsystems probably should stay as is
    Mar 05 08:02:09   e.g. waypointsprites and scores subsystem
    Mar 05 08:02:18  also having to stir things up forces a audir of parts one normaly just shun away from. witch is healty.
    Mar 05 08:02:21   of course, both are self-contained .qc files already :P
    Mar 05 08:02:30   sure
    Mar 05 08:02:43   well, MOSTLY self-contained - they use some common "miscfunctions" :P
    Mar 05 08:02:47   but otherwise self-contained
    Mar 05 08:02:59   such stuff most likely can stay as is, as it does not harm anything or influence anything's structure
    Mar 05 08:03:05  right
    Mar 05 08:03:29   what NEEDS cleanup, is teamplay.qc, player death handling, player spawn handling, player think
    Mar 05 08:03:31  no point in rewriting just for teh sake of it.
    Mar 05 08:03:36   sure
    Mar 05 08:03:42   I just say... try to use existing code if you can
    Mar 05 08:03:50   way less debugging work, and better result
    Mar 05 08:04:04  absolutly. 
    Mar 05 08:04:08   try not to rewrite feature specific code unless it goes deep into internals
    Mar 05 08:04:11   (like ready-restart does)
    Mar 05 08:04:32   also one of the messy parts BTW :P
    Mar 05 08:04:48   item handling may also need to be improved, althoguh it is mostly good
    Mar 05 08:04:56   probably it can stay as is, but needs to be divided up into files
    Mar 05 08:05:19   as for the weaponsystem... VERY hard to get THAT right :P
    Mar 05 08:06:04  one thing we have to address asap is how we want to time this. if we want to jank as much as possible of the nexuiz community, we have to be reeeal fast with a release. 
    Mar 05 08:06:20 *   [-z-] gives channel operator status to Dokujisan Morphed Spaceman
    Mar 05 08:06:22 *   [-z-] gives channel operator status to Taoki
    Mar 05 08:06:38  I agree with more frequent releases
    Mar 05 08:06:57 <[-z-]> btw, men h8 mike now
    Mar 05 08:06:59  that also influense the under-the-hood dev plan
    Mar 05 08:07:18 <[-z-]> my /\ /\nd $ key$ /\re bre/\king
    Mar 05 08:08:53   1337
    Mar 05 08:09:09 <[-z-]> not re4lly :(
    Mar 05 08:09:14 <[-z-]> quite 4nnoying
    Mar 05 08:09:23   agree with more frequent releases... we shouldn't need to care THAT much about if the release is stable or not
    Mar 05 08:09:35   as we could just patch that up quickly
    Mar 05 08:09:52  we can also organize more people to get involved in a proper testing / feedback loop
    Mar 05 08:10:18  problem: engine bugs. afaik dp has no viable method of self-upgrade
    Mar 05 08:10:33  I would like to have some open dialog with all of the main server admins
    Mar 05 08:10:58   BTW :P
    Mar 05 08:11:18   next release should be incompatible to old nexuiz releases
    Mar 05 08:11:28  Hmm, what does everyone think about an auto-update system? One that would popup a menu window saying "update available" when you open Nexuiz while connected to the internet? And that could download everything internally... or if not close Nexuiz and take you to the download page
    Mar 05 08:11:29  so just to be clear, we're forking the nexuiz code and we're NOT forking darkplaces into a new engine, right?
    Mar 05 08:11:31   we need to get enough server admins to host servers for that new version...
    Mar 05 08:11:32  But configurable
    Mar 05 08:11:44   and leave the old 2.4.2 minsta servers to rot
    Mar 05 08:11:49  engine bugs issue is the only real reason i for large upgrtades ratehr then frequent.
    Mar 05 08:11:57  i see for*
    Mar 05 08:12:22   Dokujisan: right
    Mar 05 08:12:25   at least i hope so
    Mar 05 08:12:43  not atm at least. 
    Mar 05 08:13:05  I understand that decision. but it is a disadvantage, right?
    Mar 05 08:13:21  hwo so?
    Mar 05 08:13:23  I mean under "alientrap" we had access to making changes to darkplaces
    Mar 05 08:13:29  are we losing that?
    Mar 05 08:13:42  i dont see why - div0
    Mar 05 08:13:47   Samual
    Mar 05 08:13:52  FruitieX: 
    Mar 05 08:13:54  heh
    Mar 05 08:13:56   nope
    Mar 05 08:14:02   i never had access there :)
    Mar 05 08:14:03   anyway, as for rerwrite... shpuld be no goal for next release
    Mar 05 08:14:10  's got repos access and i see no reason for LH ro refuse sane patches / requests
    Mar 05 08:14:13   agree with div0 
    Mar 05 08:14:18   but kept in mind when making new stuff
    Mar 05 08:14:26   we are already so late with our "hotfix"
    Mar 05 08:14:54  haha
    Mar 05 08:15:01   right :p
    Mar 05 08:16:13  its friggin hursefix by now xD
    Mar 05 08:16:20  ok I'm skimming through our discussion about which maps to consider as official maps and which maps need cleanup
    Mar 05 08:17:31  @ media i find the size of the current texture pool problematic. theres to much shit.
    Mar 05 08:17:45  and suplicates
    Mar 05 08:17:46  I was thinking about that. I seen many maps and thought to myself they would be great in SVN
    Mar 05 08:17:57  duplicates*
    Mar 05 08:18:34  otoh removing mean breaking some nex maps. tougth call.
    Mar 05 08:18:35  Maps I'd like to see removed... only one I know for sure I would is EggAndBacon. I don't hate it, but it's just a big box with several weapons thrown around imo.
    Mar 05 08:19:05   tZork: thats what div0 said, remove the evil* packs
    Mar 05 08:19:11   I like egg and bacon because of all the weapons
    Mar 05 08:19:19  Something recent for adding (just updated it myself and posted the update yesterday) is http://www.alientrap.org/forum/viewtopic.php?f=19&t=4945&p=76305#p76305 when vehicvles would be stable. Beautiful map by Sven
    Mar 05 08:19:22   and that bots can capture the flag
    Mar 05 08:19:53  official map pool can be super limited imo. noone oterh then the occasional review or sutch will use just it.
    Mar 05 08:20:20   Yes
    Mar 05 08:20:28   should only consist of really high quality maps
    Mar 05 08:20:29  ok in the log file mentioned in the subject, go to Mar 04 03:36:55
    Mar 05 08:20:30  use  only it i mean
    Mar 05 08:20:36  that is where the map discussion starts
    Mar 05 08:20:41   as for maps to keep for a start: aggressor, stormkeep2, e&b
    Mar 05 08:20:55   e&b uses an evil texture, but that can be changed :P
    Mar 05 08:21:15  Would it be illegal to include some wuake converted maps? Some (like kzlegypt, pukka3 / fascinating senseleness) are very good
    Mar 05 08:21:17  reroute textures with shaders is also possible
    Mar 05 08:21:17   oh, and that factory map
    Mar 05 08:21:18  *quake
    Mar 05 08:21:20   although just DM
    Mar 05 08:21:20  can we at least give e&b a makeover?
    Mar 05 08:21:21   Taoki: yes
    Mar 05 08:21:27   Dokujisan: how would you make a makeover on it?
    Mar 05 08:21:29  oh :(
    Mar 05 08:21:32  make it look interesting... like stormkeep2
    Mar 05 08:21:32   I doubt it CAN be done
    Mar 05 08:21:33   ah, desertfactory
    Mar 05 08:21:36   oh, sure
    Mar 05 08:21:37   absolutely keep that one
    Mar 05 08:21:39   look I don't care for :P
    Mar 05 08:21:44   gameplay, should stay
    Mar 05 08:21:47  the stormkeep2 makeover was just awesome
    Mar 05 08:21:50   sure
    Mar 05 08:21:50  imo
    Mar 05 08:21:57   even more so with warpzones
    Mar 05 08:21:59   also, I'd insist a bit on the wall texture :P
    Mar 05 08:21:59   hint hint :)
    Mar 05 08:22:08   hehe, idea for e&b: two floor warpzones
    Mar 05 08:22:12   oh on stormkeep?
    Mar 05 08:22:14   so you jump in, come out of the other hole :P
    Mar 05 08:22:46   e&b should retain the wall texture feel (like swimming pool or bathroom walls, sort of)
    Mar 05 08:22:59  soylent maybe
    Mar 05 08:22:59   and the obstacle pattern, and that the flags are on a higher ledge
    Mar 05 08:23:05   visually, however, doesn't matter much
    Mar 05 08:23:11   we should ask sev about cleftvillage
    Mar 05 08:23:12   just make it not look generic industrial :P
    Mar 05 08:23:17   if anyone remembers
    Mar 05 08:23:22   the swimming pool/bathroom look is good
    Mar 05 08:23:25   outdoor map
    Mar 05 08:23:28  cleftvillage? ARE YOU SERIOUS?
    Mar 05 08:23:30   with sharks in water :P
    Mar 05 08:23:33   gameplay wise, bad
    Mar 05 08:23:35   look wise, great
    Mar 05 08:23:43  I'd also make the teleporter doors in Aggressor warpzones :P
    Mar 05 08:23:49   cleftvillage is an attempt to clone CTF-LavaGiant a bit
    Mar 05 08:23:51   but fails :P
    Mar 05 08:23:56   Taoki: please not :P
    Mar 05 08:23:58   Taoki: not rly, that's bad
    Mar 05 08:24:01   that would be a brain twister
    Mar 05 08:24:01   aggressor is too small
    Mar 05 08:24:04   do it for a fun map though :P
    Mar 05 08:24:05  The only issue I find major about warpzones is that they require water rreflections to display.
    Mar 05 08:24:07   yep that too haha
    Mar 05 08:24:10   fun map indeed
    Mar 05 08:24:17   Taoki: sure, simply because they ARE that
    Mar 05 08:24:23   you can force it on in mapinfo though
    Mar 05 08:24:36  Ah, I thought that's temporary. I see
    Mar 05 08:24:42  Thought they should display either way
    Mar 05 08:24:45   well, until a better way is found :P
    Mar 05 08:24:47   well
    Mar 05 08:24:49  but are reflections safe on all target hardware?
    Mar 05 08:24:52   the reason to not do that, is performance
    Mar 05 08:24:57   tZork: no, require glsl
    Mar 05 08:25:00   so do warpzones
    Mar 05 08:25:02   what about eg. egyptronex
    Mar 05 08:25:09   but, mesa software rendering got glsl :P
    Mar 05 08:25:20   and clueless newbie's facing worlds
    Mar 05 08:25:21   so, warpzones are NOT safe on all plats
    Mar 05 08:25:28   so warpzones should have teleport texture behind them
    Mar 05 08:25:30  Anyway bbl here
    Mar 05 08:25:32  good thing so many gamers use mesa soft thenm eh? xD
    Mar 05 08:25:32   to not confuse players too much
    Mar 05 08:25:35   tZork: hehe
    Mar 05 08:25:57  the kidna cpu power needed.. i want it.
    Mar 05 08:25:58  :D
    Mar 05 08:26:33  can we consider a soylent_ctf after some tweaks and testing are done?
    Mar 05 08:26:57   BTW
    Mar 05 08:27:01   what about gasolinepowered?
    Mar 05 08:27:17  I think aggressor_ctf also has some potential but needs to improve the middle area
    Mar 05 08:27:17  you know id be happy with something like 1 or two maps for each major mode (but 1 or two maps MADE for taht mode)
    Mar 05 08:27:48  FruitieX: yes gasolinepowered is one that we all thought needed to ge tin
    Mar 05 08:27:49  get in
    Mar 05 08:27:50   runningman/runningmanctf need a retexture IMO
    Mar 05 08:27:59  good call
    Mar 05 08:28:38  the plethora of nexuiz maps shows that the community makes what it wants. i see no reason to maintain a large map-pool in the main release.
    Mar 05 08:28:46   am putting a list together
    Mar 05 08:28:54  that's what I'm doing :-P
    Mar 05 08:29:08  along with the other bullet points from these chats
    Mar 05 08:29:41 <[-z-]> brb, going to try going to gnome
    Mar 05 08:29:53 *   [-z-] has quit (Remote host closed the connection)
    Mar 05 08:30:27  what do we think about treasureisland? I liked the initial one and people love the way it looks. The newer one is a bit strange in gameplay
    Mar 05 08:30:39  it looks great, but needs adjustments, I think
    Mar 05 08:30:46  player models are a preddy urgent tough. if we could make release 1 with even just two good quality models and dump that crap, we definitly would bring soemthing quite real to the table
    Mar 05 08:30:49 *   [-z-] (~detrate@c-98-230-24-23.hsd1.fl.comcast.net) has joined #notnexuiz
    Mar 05 08:31:51  tZork: are there any existing in-progress or dropped player models that people were working on?
    Mar 05 08:31:58  that would be a good candidate
    Mar 05 08:32:07   15:29:47 <@Dokujisan> that's what I'm doing :-P
    Mar 05 08:32:09   ah darnit :P
    Mar 05 08:32:14   currently i got:
    Mar 05 08:32:17  http://www.alientrap.org/forum/viewtopic.php?f=2&t=6051
    Mar 05 08:32:18  or... do we know exactly who can work on a models
    Mar 05 08:32:28  http://www.alientrap.org/forum/viewtopic.php?f=2&t=5997
    Mar 05 08:32:32  FruitieX: PM me your list
    Mar 05 08:33:48  Dokujisan: Oblivion, Morphed, DibTop and me all knows a bit abt assorted sobjects arround it.
    Mar 05 08:34:10  i managed to export animated smd's from blender yesterday
    Mar 05 08:34:22  and turn to dpm
    Mar 05 08:34:23  yeah technical details around player models seem to always been a big problem for nexuiz.
    Mar 05 08:34:27  mainly with animation
    Mar 05 08:34:44  and I understand issues with exporting to md3 or whatever nexuiz needs
    Mar 05 08:34:55 <[-z-]> on a PS2 keyboard so I can use my A and S keys :roll:
    Mar 05 08:35:20 <[-z-]> couldn't even dettach a screen without them
    Mar 05 08:35:34  Dokujisan: yes the artist toolchain of darkpalces is bad
    Mar 05 08:35:43   tZork: holy crap that model looks ace
    Mar 05 08:35:45  tZork: perhaps we need to generate some documentation on "what we know" about player model technical details
    Mar 05 08:36:07   I second that idea
    Mar 05 08:36:13  but with the blender smd thing working, its way more likely ppl can do open models.
    Mar 05 08:36:22 <[-z-]> have we come up with a name yet?
    Mar 05 08:36:40  [-z-]: we're covering other details at the moment. I think name decision comes last or later
    Mar 05 08:36:47  we should take time with that 
    Mar 05 08:36:59  zpankiuz
    Mar 05 08:37:05  ;)
    Mar 05 08:37:09  I'm creating a page to overview the details of our discussions
    Mar 05 08:37:30 <[-z-]> oky, well I'll work on getting the site ready with a fake name
    Mar 05 08:38:28   http://www.alientrap.org/forum/viewtopic.php?f=2&t=5998
    Mar 05 08:38:30   hell yes
    Mar 05 08:38:53  ok new menu skin
    Mar 05 08:38:54  good call
    Mar 05 08:39:09 <[-z-]> as long as it gets finished :)
    Mar 05 08:39:20 <[-z-]> I'm assuming we can get the source files from sev on this?
    Mar 05 08:39:25 <[-z-]> I can remix it for the website design
    Mar 05 08:39:43   someone should learn how to do fonts and do something close to this: http://pics.nexuizninjaz.com/images/jom5sjku3jvcj7r5ezs.jpg
    Mar 05 08:39:46   and of course gpl it :P
    Mar 05 08:39:55  what about stone_castle
    Mar 05 08:40:01  it's much improved over dm_castle
    Mar 05 08:40:03   screenshot?
    Mar 05 08:40:04   oh
    Mar 05 08:40:04 <[-z-]> I like stone castle
    Mar 05 08:40:11   don't think i've seen it
    Mar 05 08:40:43  http://www.alientrap.org/forum/viewtopic.php?f=19&t=5890
    Mar 05 08:40:58  unfortunately his screenshots are at 150 fov or something crazy
    Mar 05 08:42:20  can you guys help me think of names of all of the decent mappers in nexiuz?
    Mar 05 08:43:37 <[-z-]> mookow, FruitieX, dublpaws, sev
    Mar 05 08:43:43   http://pics.nexuizninjaz.com/images/8vettzmezq8nyp7csw5.jpg
    Mar 05 08:43:48   EVIL TEXTURES!!11
    Mar 05 08:43:49   :P
    Mar 05 08:43:58   or wait...
    Mar 05 08:44:00   not at all
    Mar 05 08:44:10   still, part of the "low quality packs" i guess
    Mar 05 08:44:18 <[-z-]> much better flow & he didn't remove the secret jumppads
    Mar 05 08:44:35  Mappers
    Mar 05 08:44:35      FruitieX
    Mar 05 08:44:35      cortez666
    Mar 05 08:44:35      Grasshopper
    Mar 05 08:44:35      Mookow
    Mar 05 08:44:35      Unknown/alphagod
    Mar 05 08:44:35      sev
    Mar 05 08:44:35      dublpaws
    Mar 05 08:44:35      Strahleman
    Mar 05 08:44:35      Diabolik
    Mar 05 08:44:35      djsupport
    Mar 05 08:44:35      lda17h
    Mar 05 08:44:36 <[-z-]> he added jumppads too
    Mar 05 08:44:48   cool
    Mar 05 08:44:58  oh... I thought of a couple more
    Mar 05 08:45:02  cubeowl
    Mar 05 08:45:03 <[-z-]> fbzor
    Mar 05 08:45:18  !define decent mapper
    Mar 05 08:45:23  your definition
    Mar 05 08:45:24 <[-z-]> with some guidance, fabzor can produce awesome maps
    Mar 05 08:45:59  yeah I would love to group together mappers and have more interactive dialog about map projects, like I've been doing with the NCT group
    Mar 05 08:46:20  some of the maps in nexuiz are really close to being great, but need adjustments
    Mar 05 08:46:30   btw, should we use div0's "strafebot proof" physics set? :)
    Mar 05 08:46:38   me likes it somewhat
    Mar 05 08:46:38  dont know Dokujisan, havent kept up 2 date to good. just trying to iluminate theres many things that one can put into that term.
    Mar 05 08:46:48   it'd be really easy for newbies
    Mar 05 08:46:52  tZork: you do makes too right?
    Mar 05 08:47:03  uum yes..
    Mar 05 08:47:09  or did
    Mar 05 08:47:10  does clueless newbie make maps?
    Mar 05 08:47:18  >.o
    Mar 05 08:47:26  yep
    Mar 05 08:47:39  sepelio
    Mar 05 08:48:20  i used to map more (the first ctf map in nexuiz was acctualy mine, got removed later tnk god)
    Mar 05 08:49:14  has everyone seen this? This is the sort of thing I want to create for mappers to work from (especially new mappers)
    Mar 05 08:49:16  http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 05 08:49:37  just some ideas for improving or converting maps
    Mar 05 08:49:42   div0: don't agree with your latest change in the physics set :P
    Mar 05 08:49:54  cool stuff DibTop
    Mar 05 08:49:57  err Dokujisan
    Mar 05 08:50:01   sv_airaccel_sideways_friction -0.3 => 1
    Mar 05 08:50:05   instead you should set it at -1 :P
    Mar 05 08:50:12  Heavy would acctualy be a preddy good official map
    Mar 05 08:50:24  this has been very productive among a small group of mappers. If this is done on a larger scale with ALL nexuiz mappers, we could get a lot done
    Mar 05 08:50:35   this way i think both nexuiz players and quakers will feel more at home
    Mar 05 08:50:54  even better if -z- could create a little app that allows us to edit these entries easier (I'm doing the HTML by hand at the moment)
    Mar 05 08:51:15 <[-z-]> which entrie?
    Mar 05 08:51:22  and of course this would be on the official website, not on my personal site
    Mar 05 08:51:29 *   Taoki has quit ("KVIrc Insomnia 4.0.0, revision: 3830, sources date: 20091222, built on: 2010-01-10 23:31:04 UTC http://www.kvirc.net/")
    Mar 05 08:51:32  http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 05 08:51:38  wow by hand? your like a webdesign caveman then Dokujisan ;) mee too, usualy.
    Mar 05 08:51:50  doing a small webapp to handle that -z-
    Mar 05 08:52:00 <[-z-]> Dokujisan: I'll ee wht I cn whip up tht up
    Mar 05 08:52:06 <[-z-]> fdjipljkcvzxjklkljd ukeybord
    Mar 05 08:52:07  well I don't mind editing that page. it was simple. but I'd like others to have editing ability
    Mar 05 08:52:16  yar
    Mar 05 08:52:36 *   Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 05 08:52:42 <[-z-]> Dokujisan: well I'll ee wht I can do about getting some web stuff setup at nexiuz.org from work
    Mar 05 08:52:46  [-z-]: I created some simple classes for different statuses
    Mar 05 08:52:49 <[-z-]> if it's a slow day
    Mar 05 08:53:15  [-z-]: but we could rethink those classes. I made them up quickly
    Mar 05 08:53:50 <[-z-]> hey, there i  better remke of bonuchecker tht grhopper mde
    Mar 05 08:53:55  Ooh... zeonix.com is not taken (another idea for a name)
    Mar 05 08:54:01  yeah I haven't updated that page in a month or so
    Mar 05 08:54:07 <[-z-]> zeonix sounds cool
    Mar 05 08:54:13  irena, that muse be irena_ctf. the one i made just called iRena it non ctf
    Mar 05 08:54:15   15:52:53 < [-z-]> Dokujisan: I'll ee wht I cn whip up tht up
    Mar 05 08:54:15   15:52:59 < [-z-]> fdjipljkcvzxjklkljd ukeybord
    Mar 05 08:54:16 <[-z-]> okay, I put the PS2 keyboard in the other keyboard's place
    Mar 05 08:54:18   rofl
    Mar 05 08:54:25  it came to mind with the Pheonix suggestion
    Mar 05 08:54:25 <[-z-]> a and s keys dying FruitieX
    Mar 05 08:54:28  Would be nice
    Mar 05 08:54:30 <[-z-]> too much gaming on that keyboard
    Mar 05 08:54:31   yeah i see
    Mar 05 08:54:33   oh lol
    Mar 05 08:54:33  Taoki: added to the list
    Mar 05 08:54:44  Zeonix isn't a bad one at all
    Mar 05 08:54:50  shortened to Zeon
    Mar 05 08:54:55  like we shorten to "Nex"
    Mar 05 08:55:03  yeah
    Mar 05 08:55:43  ok who are the developers?
    Mar 05 08:55:50  game code 
    Mar 05 08:56:03  div0, tZork, mandinga, diabolik, 
    Mar 05 08:56:06  fruitieX
    Mar 05 08:56:10 <[-z-]> I believe samual is in
    Mar 05 08:56:12 <[-z-]> and taoki?
    Mar 05 08:56:15   div0: I would also vote for sv_maxspeed 320 and sv_maxairspeed 320
    Mar 05 08:56:32  I make patches pretty often... I kinda consider myself a half-developer :P
    Mar 05 08:56:37  FruitieX: noted
    Mar 05 08:56:56  what does that do in gameplay terms FruitieX?
    Mar 05 08:57:04   so to sum it all up: current physicsNoQWBunny.cfg + sv_airaccel_sideways_friction -1 + sv_maxspeed 320 + sv_maxairspeed 320
    Mar 05 08:57:29   tZork: that is a slightly different physics config that div0 has been working on
    Mar 05 08:57:33  blub is a developer, right?
    Mar 05 08:57:36  CSQC guy
    Mar 05 08:57:47  is green marine?
    Mar 05 08:57:54   Dokujisan: note that "sum it all up" line ^
    Mar 05 08:58:00  noted
    Mar 05 08:58:29   tZork: try it, it feels like a fuse of nexuiz and CPM a bit
    Mar 05 08:58:36  ok who else besides -z- is a web developer?
    Mar 05 08:58:38  Dokujisan: Spaceman, lda17h, FruitieX
    Mar 05 08:58:52  tZork: for web dev?
    Mar 05 08:58:56  oh does spaceman do maps?
    Mar 05 08:59:02   for a nexuiz player it should feel pretty much the same
    Mar 05 08:59:04  FruitieX: CPM? Is that liek  C perl module? :P
    Mar 05 08:59:05 *   [-z-] has quit (Ping timeout: 120 seconds)
    Mar 05 08:59:06   no, I don't do maps
    Mar 05 08:59:16  Dokujisan: tought you where asking for gamecode devs
    Mar 05 08:59:19   I've fixed a few map bugs
    Mar 05 08:59:51  ok so  lda17h does game coding too?
    Mar 05 09:00:19  and what of green marine?
    Mar 05 09:00:44  FruitieX: i know its some special phys config for ..q3? but tahts abt all. so i havent a clue what a merge of it and nexuiz would be.
    Mar 05 09:01:55  Dokujisan: iirc yes, think he made some dodge patch for nexuiz wich looked decent but got lost in the goo
    Mar 05 09:02:04  Just so I know. Is it alright to talk about the decision to rename Nexuiz outside of this channel yet?
    Mar 05 09:02:17  no
    Mar 05 09:02:25  not in public, imo
    Mar 05 09:02:26  Taoki: no
    Mar 05 09:02:28   Dokujisan: more physics stuff to note that's really fun: sv_doublejump 1, sv_jump_speedcap_max 1, sv_jumpspeedcap_max_disable_on_ramps 1
    Mar 05 09:02:30  ok
    Mar 05 09:02:41  just my opinion tough
    Mar 05 09:02:48  we shouldn't make any of these discussions known outside....except I'm chatting with the aussienexers
    Mar 05 09:02:51  keeping them informed
    Mar 05 09:02:55  certain key people
    Mar 05 09:03:02  and they know not to discuss it publicly too
    Mar 05 09:03:14   ok good
    Mar 05 09:05:22 *   Dokujisan has changed the topic to: Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt
    Mar 05 09:05:43  review that, if you would
    Mar 05 09:05:49    ok who else besides -z- is a web developer?
    Mar 05 09:05:50  help me fill in the empty spots
    Mar 05 09:05:52   Dokujisan, +1
    Mar 05 09:05:58  you?
    Mar 05 09:07:50   Dokujisan, yes
    Mar 05 09:07:57  k
    Mar 05 09:08:17  ok I added the aussie people now to the ROLES list
    Mar 05 09:10:25   well till when it started to overcrowd and everyone was all sudden a webdev ;)
    Mar 05 09:10:41  I can manage the people. I just need to know who does what
    Mar 05 09:10:50  -z- will likely be the head web dev
    Mar 05 09:10:58   i worked as webdesigner/developer/php coder in past, tho try to avoid those...
    Mar 05 09:11:04  ok
    Mar 05 09:11:10  I'll keep you off that list then :-)
    Mar 05 09:11:16   yea }-z-{ does gooed job imho
    Mar 05 09:11:27  I agree
    Mar 05 09:11:33   Dokujisan, sure i help out np.
    Mar 05 09:13:04   FruitieX: please PM me trhat physics info
    Mar 05 09:13:31  ok what about server admins?
    Mar 05 09:13:32   [14:50:50] <@FruitieX> sv_airaccel_sideways_friction -0.3 => 1
    Mar 05 09:13:33   [14:50:54] <@FruitieX> instead you should set it at -1 :P
    Mar 05 09:13:38   why? it gives more control
    Mar 05 09:13:42   but I am undecided about it :P
    Mar 05 09:13:51  you could basicaly put me in all fields as i have a bit of professional experiance in all of them :P but i prefer just game devel and maybe models/maps for now.
    Mar 05 09:13:54   I just don't like that turning gives no penalty
    Mar 05 09:14:02   when turning slowly
    Mar 05 09:14:04  @ Dokujisan
    Mar 05 09:14:05   you still accelerate
    Mar 05 09:14:05  ok tZork 
    Mar 05 09:14:12   ideal would be if turning does not accelerate :P
    Mar 05 09:14:22   but I do not want too much deceleration either
    Mar 05 09:14:35   I will probably change the sidefric code to limit to the previous speed before the move
    Mar 05 09:14:42   and not to the current speed when applying sidefric
    Mar 05 09:14:57   so when turning using CPMA air control, your speed would stay as is (but not increase)
    Mar 05 09:14:59   that was my goal
    Mar 05 09:15:24   but well, it may need slight code changes :P
    Mar 05 09:17:06  ok, I need a list of the Nexuiz Server Admins
    Mar 05 09:17:17   FruitieX: acgtually...
    Mar 05 09:17:20   Hmm
    Mar 05 09:17:23   from the code, sidefric -1 SHOULD do what I want
    Mar 05 09:17:26   maybe it is buggy :P
    Mar 05 09:17:30   :P
    Mar 05 09:17:36   -1 allows deceleration, but only as much as the backwards key would do
    Mar 05 09:17:40   this is actually what I want :P
    Mar 05 09:17:54   maybe need to try -9999 ;)
    Mar 05 09:18:04   will check that out later
    Mar 05 09:18:07   please PM it to me
    Mar 05 09:18:14   I wish I could self-PM to make "reminders":P
    Mar 05 09:18:49   so yes, if -1 does what I wanted it to do in the code ;) then it is exactly what there should be
    Mar 05 09:19:17   heh
    Mar 05 09:20:01   basically what the - should do, is "never decelerate more than the backward key could do"
    Mar 05 09:20:06   to prevent illogical physics
    Mar 05 09:20:20  /msg yournick blah dont work?
    Mar 05 09:20:30  tahts what i usualy do =)
    Mar 05 09:20:34 <}-z-{> I would like to share responsbility with Dokujisan and perhaps another person
    Mar 05 09:20:38   Dokujisan: cubeowl, esteel run DCC; merlijn runs Simba
    Mar 05 09:20:41 <}-z-{> but if possible I would like to do the inital setup
    Mar 05 09:20:47 <}-z-{> cocerning web for this project
    Mar 05 09:20:59   tZork: opens a query window :P
    Mar 05 09:21:39 <}-z-{> I just don't want to be a single point of failure at any point :-P
    Mar 05 09:21:44   sure :P
    Mar 05 09:21:59 <}-z-{> I like the arangement I ad as admin with willis in a way, I would like to keep something like that going
    Mar 05 09:21:59  ok what about SysAdmins? I know that's overlap with web dev and Nexuiz admins, but I'd like a separate list
    Mar 05 09:22:08   I would be one, but not the only one
    Mar 05 09:22:11 <}-z-{> and by the way, it sounded like willis is with us on this
    Mar 05 09:22:14  }-z-{ for Community/Project Organization?
    Mar 05 09:22:21   and yes, Willis as sysadmin is good
    Mar 05 09:22:22 <}-z-{> tZork: ?
    Mar 05 09:22:34  <}-z-{> I would like to share responsbility with Dokujisan and perhaps another person
    Mar 05 09:22:38   maybe FruitieX too
    Mar 05 09:22:52 <}-z-{> ah, tZork for web
    Mar 05 09:22:53   just... community/project organization shoudl not mean "global head of all" :P
    Mar 05 09:23:05 <}-z-{> running the websites, development websites and other web kind of projects
    Mar 05 09:23:10   but rather PR, community websites, also autromatically head moderators, etc.
    Mar 05 09:23:11 *   mand1nga (404c1f0e@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 09:23:15 div0 DibTop 
    Mar 05 09:23:30  oh right, well }-z-{ my web stuff is rusty nowdays. im not a good choise i think,
    Mar 05 09:23:31   I think general PR belongs into that too
    Mar 05 09:23:37   i.e. not just our website, but also other sites :P
    Mar 05 09:23:38  div0: yeah that's what I have in mind. I don't want to boss people around. I consider it more of an organization role than anything
    Mar 05 09:23:52 <}-z-{> tZork: I think if Dokujisan and willis also share this responsibility we'll be good.
    Mar 05 09:24:05 <}-z-{> Dokujisan is good at managing, we've seen this
    Mar 05 09:24:07  I want to be able to establish how things are done and then hopefully remove myself from that role over time
    Mar 05 09:24:16   as for sysadmin... it'd be nice if these also are responsible for making the builds
    Mar 05 09:24:24   as it overlaps quite much :P
    Mar 05 09:24:30 <}-z-{> makes sense
    Mar 05 09:24:35   of course, it'll be mostly automatic
    Mar 05 09:24:41   I envision a cronjob for daily builds
    Mar 05 09:24:43  Dokujisan: i think its acctualy needed continiously, nto nessesarely the same person/s tough.
    Mar 05 09:24:53   and only making of release builds would be manual
    Mar 05 09:24:58   (to put in version number)
    Mar 05 09:25:12   on the other hand, website stuff overlaps with sysadmin too
    Mar 05 09:25:18 <}-z-{> div0: I think we should do that an have an automatic private test server if possible too
    Mar 05 09:25:24   sure
    Mar 05 09:25:46   Dokujisan, prolly forgot: Morphed into >Artists section & modeling (afaik), and you can add me aswell for art/gui/texture(2d).
    Mar 05 09:25:58   yes
    Mar 05 09:26:08   regarding how artwork should LOOK I want no responsibilties...
    Mar 05 09:26:16  hehe
    Mar 05 09:26:18   I just request, or demand, general "good taste" principles :P
    Mar 05 09:26:31   haha
    Mar 05 09:26:31   I don't care how it looks, as long it's no running around goatse :P
    Mar 05 09:26:43   and no, not even a GOOD looking running around goatse please :P
    Mar 05 09:26:53  aww so no leiliololiolioloil? ;)
    Mar 05 09:26:57 <}-z-{> regarding artwork, I think we should gather a list of wants/needs/likes/dislikes
    Mar 05 09:27:05 <}-z-{> to give other artists direction when they are looking to contribute
    Mar 05 09:27:23 <}-z-{> and hopefully that will evolve into some sort of natural style
    Mar 05 09:27:31   16:25:35 <@div0> I envision a cronjob for daily builds
    Mar 05 09:27:33   yes do want
    Mar 05 09:27:50   or one that builds as soon as there's a change in the git master branch
    Mar 05 09:27:53  ok refresh the nexuiz_new_notes.txt
    Mar 05 09:27:53 *   esteel (VDGLpekoeK@planetnexuiz.de) has joined #notnexuiz
    Mar 05 09:27:57  hi esteel :-)
    Mar 05 09:28:00 <}-z-{> hey esteel 
    Mar 05 09:28:04  hi there esteel
    Mar 05 09:28:06     hola
    Mar 05 09:28:07   possibly even one that builds from some select branches
    Mar 05 09:28:10  esteel: glance through the file in the subject
    Mar 05 09:28:19   and gives you an older download link with text BULID FAILED if recent builds fail
    Mar 05 09:28:23   hello esteel 
    Mar 05 09:29:05     laters when in the train.. right now it would be a pita.. mobilephone only ;)
    Mar 05 09:29:16   btw Dokujisan, i also admin a couple of nexuiz servers :P
    Mar 05 09:29:17  ok
    Mar 05 09:29:25 <}-z-{> yeah, actually there is a plugin for redmine concerning builds... you can have it automatically report certain things as bugs, sorry for the vague description :-P
    Mar 05 09:29:30   or well actually, they all run the nexrun mod >_>
    Mar 05 09:29:45  meh if build fail it should send horrid viroidz! taht'd keep yall motivated not to write bugz! xD
    Mar 05 09:29:57   ye tZork :P
    Mar 05 09:31:38  ok one question regarding websites.... I want to invite the aussienexers to have their community join the core website instead of operating a separate website
    Mar 05 09:31:52 <}-z-{> Dokujisan: I was thinking we could wrap in it wordpress MU
    Mar 05 09:32:00  ok
    Mar 05 09:32:22 <}-z-{> I'm not sure what this means for the mybb bridge however
    Mar 05 09:32:50 <}-z-{> they may need an account on the main nexuiz* site for that
    Mar 05 09:32:59 <}-z-{> I have to look into it
    Mar 05 09:38:25 <}-z-{> okay, temporary domains to get setup on: theworthless.net, beertitties.com, cankill.us, withfoss.org
    Mar 05 09:38:36  ok I think I have the aussies onboard with a central website
    Mar 05 09:39:21 <}-z-{> just to setup something external we can all start using as a way to organize information until we better define ourselves
    Mar 05 09:39:59 <}-z-{> I like cankill.us
    Mar 05 09:40:19 <}-z-{> or withfoss.org
    Mar 05 09:41:07  i like both b33f and titties.. so i guess i like beertitties.com ;)
    Mar 05 09:41:14 <}-z-{> :-P
    Mar 05 09:42:23 <}-z-{> Dokujisan: any opinion?
    Mar 05 09:42:23  hey... can we do an official mumble server?
    Mar 05 09:42:33 <}-z-{> most definitely
    Mar 05 09:42:36 <}-z-{> very good idea
    Mar 05 09:42:36  I run a mumble server. I think there is one in Au
    Mar 05 09:42:46  I think my mumble server is very low on resources
    Mar 05 09:42:56 <}-z-{> we can probably integrate that into the website and probably the forums
    Mar 05 09:43:01 <}-z-{> "user is on mumble now" w00t
    Mar 05 09:43:13 <}-z-{> optionally displayed by choice of the user of course
    Mar 05 09:43:23 <}-z-{> they'd have to associate their mumble account as well
    Mar 05 09:43:23  and the lagtime between regions isn't a problem either. I've had people from australia on my mumble server and the chatting is fine
    Mar 05 09:43:34 <}-z-{> Dokujisan: beertitties.com?
    Mar 05 09:43:45  for some reason, the .25 seconds delay doesn't hurt the mumble experience
    Mar 05 09:43:48  :-o
    Mar 05 09:43:53  ya lost me
    Mar 05 09:44:05  oh a temp website domain?
    Mar 05 09:44:08 <}-z-{> I want to setup a temp site we can all collaborate on until we think about the name
    Mar 05 09:44:10  ok
    Mar 05 09:44:11 <}-z-{> yes
    Mar 05 09:44:11  yeah
    Mar 05 09:44:12  good idea
    Mar 05 09:44:38  um it really can be anything
    Mar 05 09:44:44  fukillfonic.com
    Mar 05 09:44:45 <}-z-{> well I already have that registered
    Mar 05 09:44:46  heh 
    Mar 05 09:44:52  haha seriously???
    Mar 05 09:44:54 <}-z-{> yes lol
    Mar 05 09:45:00  wow....I'm not gonna ask
    Mar 05 09:45:05 <}-z-{> haha
    Mar 05 09:45:17  that must have been one drunk domain searching night
    Mar 05 09:45:24  like drunk phone calls
    Mar 05 09:45:31 <}-z-{> drunk in college, "OMG WOULDN'T IT BE GREAT IF WE HAD A WEBSITE THAT INVOLVED BEER AND BOOBIES AND GIRLS SHOWING US BOOBIES WHILE DRINKING BEERS?"
    Mar 05 09:45:54  "You know what's awesome?? Beer is awesome. But you know what else is really awesome???"
    Mar 05 09:46:05  haha
    Mar 05 09:46:37  well I dunno if anyone would be offended by that name
    Mar 05 09:46:42  but it doesn't bother me for a temp site
    Mar 05 09:46:47  well...
    Mar 05 09:46:49 <}-z-{> okey dokey
    Mar 05 09:46:54  ok maybe pick a less offenseive domain if you have one
    Mar 05 09:47:02 <}-z-{> cankill.us ?
    Mar 05 09:47:05  sure
    Mar 05 09:47:07 <}-z-{> withfoss.org ?
    Mar 05 09:47:12  cankill.us
    Mar 05 09:47:15 <}-z-{> okay
    Mar 05 09:49:26 <}-z-{> might take me all day to get setup, I have work work to do as well
    Mar 05 09:51:36 <}-z-{> btw, is redmine's textile based wiki good enough for everyone or should I be considering alternatives?
    Mar 05 09:52:21  beer and boodies is mroe offensive then able to commit murder? =( ;)
    Mar 05 09:52:58 <}-z-{> lol
    Mar 05 09:53:02  the cankill one will be fine for temp id say
    Mar 05 09:58:12  question... do we have to use quakenet? >.<
    Mar 05 09:58:35  other games use other networks like gameradius
    Mar 05 09:58:59 <}-z-{> what is the advantage of other networks?
    Mar 05 09:59:02  for my other project I'm involved with, Getty was showing me a way to have #nexuiz on multiple networks and have them all connect to each other through a bot
    Mar 05 09:59:10  so we would have our own IRC network
    Mar 05 09:59:21  for devchannel, freenode maybe?
    Mar 05 09:59:43 <}-z-{> I'm not sure I understand what you mean Dokujisan 
    Mar 05 09:59:44  and #battlecube channels on quakenet and other networks and they would all echo to/from our network
    Mar 05 09:59:50 <}-z-{> oh I see
    Mar 05 09:59:53  there would be a bot that echos what is typed
    Mar 05 09:59:56  between the various networks
    Mar 05 10:00:01 <}-z-{> well, we can have a poll when we put up the website
    Mar 05 10:00:15 <}-z-{> There are nice survey and poll scripts for wordpress
    Mar 05 10:00:31 <}-z-{> s/scripts/plugins/
    Mar 05 10:06:56  ah forgot about mrBougo
    Mar 05 10:06:59  he's a developer, right?
    Mar 05 10:07:03 <}-z-{> yes
    Mar 05 10:07:07 <}-z-{> and more than that
    Mar 05 10:07:13  give me the list
    Mar 05 10:07:14 <}-z-{> positive energy within the community
    Mar 05 10:07:17  heh
    Mar 05 10:07:19  well...
    Mar 05 10:07:27  in our breakdown of roles
    Mar 05 10:07:31  and skillsets
    Mar 05 10:07:40  game dev and web dev?
    Mar 05 10:07:45  server admin?
    Mar 05 10:07:48  moderator?
    Mar 05 10:08:00 <}-z-{> game dev, server admin, moderator
    Mar 05 10:08:03 <}-z-{> don't know about web dev
    Mar 05 10:08:08 <}-z-{> that'd be up to him
    Mar 05 10:08:29 <}-z-{> by the way, I don't mind repurposing the nexuiz ninjaz game server as a build / test machine
    Mar 05 10:08:40  awesome
    Mar 05 10:08:41 <}-z-{> I'll run a few other services on it but won't be a big deal
    Mar 05 10:08:49 <}-z-{> maybe 1 nexuiz ninjaz server... though we might be 'the ninjaz' by then
    Mar 05 10:09:01 <}-z-{> and I'll use it for irsii, like I'm doing now :-P
    Mar 05 10:09:02  div0 and I had a long discussion about the bootcamp and dojo servers
    Mar 05 10:09:12 <}-z-{> oh yeah?
    Mar 05 10:10:16  I'm updating the notes with it. just a sec
    Mar 05 10:10:23 <}-z-{> okay
    Mar 05 10:10:28 <}-z-{> where are the notes? sorry I don't have the url
    Mar 05 10:11:02  in the subject
    Mar 05 10:11:06  can you see it?
    Mar 05 10:11:09 <}-z-{> hurr durr
    Mar 05 10:11:10 <}-z-{> yes
    Mar 05 10:11:13 <}-z-{> what a great place
    Mar 05 10:11:16 <}-z-{> I feel 'tarded
    Mar 05 10:11:37 <}-z-{> btw Dokujisan there was a documentation generation tool I mentioned in #alientrap-dev ~a month ago
    Mar 05 10:11:45 <}-z-{> I know this may be a little forward thinking
    Mar 05 10:11:54  this is quite interesting 
    Mar 05 10:11:54 <}-z-{> but your style in the notes there just jogged my memory
    Mar 05 10:12:10 <}-z-{> because writing documentation in their psuedo-wiki format would generate HTML and manpages
    Mar 05 10:12:17  wrt to the NDA's afore blamed:
    Mar 05 10:12:18  10-03-05 15:59]  Chris: out of curiosity, are you somehow involved in the deal? 
    Mar 05 10:12:18  [10-03-05 16:00]  no but this has been in the making for some time now
    Mar 05 10:12:18  [10-03-05 16:00]  since last year
    Mar 05 10:12:18  [10-03-05 16:00]  well this concept
    Mar 05 10:12:18  [10-03-05 16:00]  and honestly, I would like to be in contribution to it, and make a good game, and something not fully for this reason but a good reason none the less: something the community would be proud of
    Mar 05 10:12:19 <}-z-{> and I think that could really benefit the project
    Mar 05 10:12:19  [10-03-05 16:01]  I honestly though have a bit of venom to spew to those who feel aggravated by the decision though
    Mar 05 10:12:51  ok refresh the notes again }-z-{ I added the details about training
    Mar 05 10:13:02 <}-z-{> wait chris is upset about people being upset about this?
    Mar 05 10:13:12  taht too , but read agaiun
    Mar 05 10:13:14  again*
    Mar 05 10:13:28 <}-z-{> Dokujisan: I think there should be a board or committee larger than 3 leaders, just for the record
    Mar 05 10:13:35  I was thinking 5
    Mar 05 10:13:39 <}-z-{> 3 I believe to still have weak point
    Mar 05 10:13:42  I was gonna suggest that to div0
    Mar 05 10:13:45 <}-z-{> yeah
    Mar 05 10:14:06  he knows abt it since more then a year, hes not involved in it and yet at and ill refer to NDA not to comment.
    Mar 05 10:14:30  thats the interesting part
    Mar 05 10:14:53  I dunno who Chris is
    Mar 05 10:14:54   oow whenever i said to want cleftwillage i meant
    Mar 05 10:14:57   TREASURE ISLAND :P
    Mar 05 10:15:05  :-) ok
    Mar 05 10:15:08  oh forgot a few lines, thise go atop of the otehr ones:
    Mar 05 10:15:08  10-03-05 15:54]  <@div0> the use of the NAME Nexuiz in that way, NOPE
    Mar 05 10:15:08  [10-03-05 15:54]  I've known about this for months
    Mar 05 10:15:08  [10-03-05 15:54]  and it has been hinted to nexuiz entering a new platform
    Mar 05 10:15:15   cleftvillage is crap :P
    Mar 05 10:15:18  lmao FruitieX
    Mar 05 10:15:40  clefvillage has some very interesting elements
    Mar 05 10:15:44  I like the beach
    Mar 05 10:15:56  but bad gameplay, as it turns out
    Mar 05 10:16:07  it looks good fore sure, but gameplay is.. well its not.
    Mar 05 10:16:28 <}-z-{> Dokujisan: I know div is against hierarchies but I think to a degree perhaps a "committee" of liasions would be beneficial
    Mar 05 10:16:32  maybe for keyhunt =)
    Mar 05 10:16:33  tZork and FruitieX can you think of more to add to the maps section? 
    Mar 05 10:16:48 <}-z-{> the players that can speak between developers and players and grease the wheels, help diffuse tension, etc.
    Mar 05 10:16:56  tbh id keep the maplist as short as possible Dokujisan
    Mar 05 10:17:00  }-z-{: I thought he aggreed to that.... 3 leaders (or 5 perhaps) for major decisions with a committee under it for "most" decisions
    Mar 05 10:17:00   also what about strength?
    Mar 05 10:17:03 <}-z-{> make sure everyone is in touch as they need to be sort of thing
    Mar 05 10:17:10  tZork: yeah but we need a list to start discussion
    Mar 05 10:17:12    re
    Mar 05 10:17:16    what's new?
    Mar 05 10:17:18   it afaik uses mostly eX textures
    Mar 05 10:17:24   CuBe0wL: read topic
    Mar 05 10:17:34  strength is proformance murder, and i cant say i totaly love the gameplay
    Mar 05 10:17:37  tZork: I personally agree with making the game less bloated, only having a few included maps
    Mar 05 10:17:54  ooooh I do like strength. I think it could be redone maybe?
    Mar 05 10:17:58 <}-z-{> bbiab, I have to manually edit a database because an ajax callback seems to be failing due to a fileupload error, yay
    Mar 05 10:18:22   Dokujisan: why redone, i think it is pretty much fine as it is
    Mar 05 10:18:32   maybe redone lightning if we ever get a working raytracer solution
    Mar 05 10:18:48   other than that it has excellent textures, excellent detail, excellent gameplay IMO :)
    Mar 05 10:18:49  eh.... it could be better on FPS and it has some holes in it. I would like to see it a little more cleaner .... like Stormkeep2 :-)
    Mar 05 10:18:59    so we fork, it's official?
    Mar 05 10:19:06  :-D \o/
    Mar 05 10:19:18  nothing official afaik CuBe0wL
    Mar 05 10:19:22    ok
    Mar 05 10:19:23  aww :-(
    Mar 05 10:19:30    but things are bloody serious?
    Mar 05 10:19:41  it seems like this is as official as a fork gets, isn't it?
    Mar 05 10:19:47  brainlack created this mess. lets not give it anotehr chanse.
    Mar 05 10:19:58   agreed Dokujisan it has bad fps, this should be worked on
    Mar 05 10:20:01  we still have a lot of work to do, of course
    Mar 05 10:20:04   but texture/detail wise i have nothing to add
    Mar 05 10:20:18   of course i'd want warpzones again, but they will just halve the fps again :)
    Mar 05 10:20:19 <}-z-{> nevermind, I'm back 1and1 is failing
    Mar 05 10:20:29  i do, eX is booooring
    Mar 05 10:20:32  ;)
    Mar 05 10:20:45  FruitieX: you know how the edges on stormkeep2 look really smooth now? I dunno what it is that changed, but the edge detail is impressive. I would like to see more of that in maps
    Mar 05 10:20:46   lol but we cant have all maps using trak5/4 :P
    Mar 05 10:20:56   edge? :P
    Mar 05 10:21:06  hmm let me grab some screenshots
    Mar 05 10:22:03    woah, that maplist is very slim
    Mar 05 10:22:21  yesh help me add more just for our discussion
    Mar 05 10:22:42   CuBe0wL: yes
    Mar 05 10:22:48  wow I can't find any stormkeep2 screenshots :-(
    Mar 05 10:22:54    well, do we eant to keep the Nexuiz athmospere ?
    Mar 05 10:22:59   only supply very high detail maps is the goal apparently...
    Mar 05 10:23:09  CuBe0wL: not sure what you mean. You mean style?
    Mar 05 10:23:12   which i find good
    Mar 05 10:23:18  irena (not ctf) its playes well in dm/isg games IMO
    Mar 05 10:23:21    yes, and feel im general
    Mar 05 10:23:28   also another goal is to remove the low resolution texture packs (evil* eg)
    Mar 05 10:23:38  tZork: I have irena on my list of map projects to be fixed. Nobody has taken it up yet though
    Mar 05 10:23:39    noooo! I like evil a lot :(
    Mar 05 10:23:48   irena would need a major rehaul imo :P
    Mar 05 10:23:52    or, remake it high res :P
    Mar 05 10:23:54  Dokujisan: tahts the ctf
    Mar 05 10:23:54   looks like warsow without cel-shading :P
    Mar 05 10:23:59  as you mention bases
    Mar 05 10:24:01  tZork: oh there is a non-CTF one?
    Mar 05 10:24:12   CuBe0wL: good luck with that
    Mar 05 10:24:19 <}-z-{> fyi, dance is still a giant warsow logo
    Mar 05 10:24:20   of course, if someone does it is possible to add later
    Mar 05 10:24:29    well, if high quality is a goal, why reslimed is missing from the list?
    Mar 05 10:24:30  yes i made it as non ctf Dokujisan... then it was turned to ctf by someoneo else. its totaly bad for ctf.
    Mar 05 10:24:35   dance needs a remake for sure
    Mar 05 10:24:38   at least retexture
    Mar 05 10:24:46   right reslimed!
    Mar 05 10:24:50   add that Dokujisan, reslimed
    Mar 05 10:24:50    or silvercity , tZork version
    Mar 05 10:24:56  nah
    Mar 05 10:25:06  I really like the silvercity remake, but it's low FPS
    Mar 05 10:25:11    oh
    Mar 05 10:25:13   needs remake, yep fix fps too
    Mar 05 10:25:19    Hot Grounds? :D
    Mar 05 10:25:25   :d
    Mar 05 10:25:28 <}-z-{> hahaha, one of the features of Wordpress MU, "Ambiguity about how to pronounce its name"
    Mar 05 10:25:30   cant remember which that is
    Mar 05 10:25:37    cbdm1 :D
    Mar 05 10:25:37   oh a dm map by you
    Mar 05 10:25:40   i dont think i ever played it
    Mar 05 10:25:45    you should
    Mar 05 10:25:53  I think killall_organic has potential, but needs some adjustments for gameplay
    Mar 05 10:25:57  did a few times, bit to hardcore i think. 
    Mar 05 10:26:15  as in you gotta be on your toes ont to get lava all over your cahones
    Mar 05 10:26:23    Dokujisan, no, killall organic needs a MAJOR overhaul
    Mar 05 10:26:29  it does?
    Mar 05 10:26:32    yes
    Mar 05 10:26:39  ok well I'm putting it on the list anyway :-)
    Mar 05 10:26:48  just for discussion
    Mar 05 10:26:55    and I have plans, but I haven't find time yet to execute it
    Mar 05 10:27:00  and I barely played hotgrounds. It's DM, right?
    Mar 05 10:27:05    yes
    Mar 05 10:27:16  I remember it looks good
    Mar 05 10:27:21    thx
    Mar 05 10:27:38    I plan to revisit greatwall too
    Mar 05 10:27:45    fixing some stuff
    Mar 05 10:27:47  oh no
    Mar 05 10:27:59    like laser fence over the bases
    Mar 05 10:28:09    so it's not a hopin hop out anymore
    Mar 05 10:28:13  personaly i like brokenworlds and irena the best of my maps i think.. well tznex03 too but you get good enougth teams on that map abt once every 100 tries.. and it comes arround in teh rot abt once every month so.. xD
    Mar 05 10:28:26  the main thing I never liked about greatwall is the main feature that is liked it (by those who like it) and that is the jump pads that throw you across the whole map
    Mar 05 10:28:34  is liked about it*
    Mar 05 10:29:07    I planned to make it a bit more difficult
    Mar 05 10:29:12  tZork: brokenworlds 2 looks awesome, but almost everyone I speak with about it prefers brokenworlds 1
    Mar 05 10:29:12    a bit assault like
    Mar 05 10:29:14  for gameplay
    Mar 05 10:29:28    and I mean turrets
    Mar 05 10:29:36  well the gw_overloaded experiment show you cant make gw to difficult ot ppl will hate on it
    Mar 05 10:29:42  I never liked turrets + CTF
    Mar 05 10:29:55    MG turrets looking the air, and killing those who try to just use them
    Mar 05 10:30:15   problem with reslimed is that it uses lots of evil textures
    Mar 05 10:30:36    I want something like you need to active the turrets/destroy them to be able to use the midair route
    Mar 05 10:30:39  frankly original slimepit play better
    Mar 05 10:30:46    Fortress resurrection?
    Mar 05 10:30:52    tZork, I somehow like both
    Mar 05 10:30:55  I feel like the turrets are just an annoyance or distraction to CTF
    Mar 05 10:30:56   i would vote yes on including brokenworlds
    Mar 05 10:31:07   agree with turrets being a distraction
    Mar 05 10:31:18    mannable turrets?
    Mar 05 10:31:29    now that tZorks vehicle code is usable
    Mar 05 10:31:30  me too CuBe0wL, but on a avarage game, slimepit is the better map, gameplay wize. imo.
    Mar 05 10:31:53  http://pastebin.com/PpDSFi4c Is it ok to post this topic on the forum at this current stage?
    Mar 05 10:31:55    ppl on DCC like both, that's my impression
    Mar 05 10:32:01  Dokujisan: if the map wasent designed for it, yeh.
    Mar 05 10:32:07  Or recommended
    Mar 05 10:32:16  manually playable turrets is a whole other discission
    Mar 05 10:32:21  I would love to test that out more
    Mar 05 10:32:35  its horribly boring Dokujisan
    Mar 05 10:32:35  but I haven't been keeping up with the vehicle code stuff in a while
    Mar 05 10:33:13  I remember seeing the spider walker video
    Mar 05 10:33:34   Dokujisan: definitely add reslimed as a map we should consider if we get replacement textures...
    Mar 05 10:33:45  ok
    Mar 05 10:33:46  its like a wheeless tank. you just sit there confined by a rot/pitch speed limuted gun with sub-par damage. (manable turrets)
    Mar 05 10:33:51   eg. retexture or someone remaking the textures in higher res
    Mar 05 10:34:11  FruitieX: also div0 mentioned that reslimed isn't as easy to run around as slimepit. It's easier to get stuck on thigns
    Mar 05 10:34:26   that should be somewhat easy to fix
    Mar 05 10:34:29   add that to the notes
    Mar 05 10:35:27    btw... what about that community petition?
    Mar 05 10:35:34  what petition?
    Mar 05 10:35:43  Anyway, posting that topic, if no one thinks it could get in the way right now or anything
    Mar 05 10:35:45    if we officially fork, there's no real need for that
    Mar 05 10:35:48  relimed is a bit to big for its layout style imo. unless the server's crowded you end up searching more then fighting,
    Mar 05 10:35:50  Taoki: what topic?? :-o
    Mar 05 10:35:50    Taoki, not yet pls
    Mar 05 10:35:57  http://pastebin.com/PpDSFi4c
    Mar 05 10:35:59    I disapprove
    Mar 05 10:36:04  ok, I'll just save it then
    Mar 05 10:36:14   Dokujisan: maybe same thing about final_rage
    Mar 05 10:36:29   also, add desertfactory (div0 mentioned that earlier)
    Mar 05 10:36:40  I was hoping that with the name change, we could apear with some new content and something surprising
    Mar 05 10:37:16    I'd like to stick as much Nexuizish as we can
    Mar 05 10:37:47   I hope this too Taoki 
    Mar 05 10:37:52    eg. I'd keep all models, btu remake them. with the same name. eg. Replace original Nexus with that new one
    Mar 05 10:38:17    who's made that? my brain is fried again, I can't remember the nick
    Mar 05 10:38:34  Dokujisan: manable gun platforms should be designed for that, the current auto turrets use good prediction and targetselect ratehr then firepower. thus maning them makes little sense. manable guns should make up for the lack of movemenbt with firepower, imo.
    Mar 05 10:38:47  Someone should really consider this http://alientrap.org/forum/viewtopic.php?p=69763#p69763 Best forgotten contribution i know of
    Mar 05 10:39:01 Taoki tZork 
    Mar 05 10:39:04  Taoki: I have it added
    Mar 05 10:39:06    Dokujisan, I was talking about this petition: http://alientrap.org/forum/viewtopic.php?f=4&t=6050&start=0
    Mar 05 10:39:30  wow that is a lot of color
    Mar 05 10:39:39   :o indeed
    Mar 05 10:39:44   color is fine :D
    Mar 05 10:39:46  "this post is sponsored by Crayola Crayons"
    Mar 05 10:39:57    :)
    Mar 05 10:40:02    anyway, read up
    Mar 05 10:41:07  I am not in support of any petitions
    Mar 05 10:41:19  contracts have already been signed. Things are already decided.
    Mar 05 10:41:24  and trust is already lost
    Mar 05 10:41:39  and everything that has been said in this channel is....awesome
    Mar 05 10:41:58  what we have been discussing over the past 2 days in here is exactly what nexuiz should have been
    Mar 05 10:42:49  in just having these conversations and doing this planning that we're doing, we'll be getting more done in a month than nexuiz had previously done in a year (imo)
    Mar 05 10:43:16   Indeed.
    Mar 05 10:43:27 <}-z-{> mmm hmm
    Mar 05 10:43:28  we need to start informing more key people
    Mar 05 10:43:59  so they can drop the public outcry and start preparing for the future
    Mar 05 10:44:04    one question remains on my side
    Mar 05 10:44:11    a very achy one
    Mar 05 10:44:17    what about DCC server?
    Mar 05 10:44:27  doesn't esteel run it?
    Mar 05 10:44:31    it's not our own with esteel
    Mar 05 10:44:39    it's not his property I think
    Mar 05 10:44:40  esteel is in this channel
    Mar 05 10:44:46    yes, I see him
    Mar 05 10:44:54   CuBe0wL: sxen?
    Mar 05 10:45:00    yes, he's the guy
    Mar 05 10:45:03   :)
    Mar 05 10:45:04    ollipapa
    Mar 05 10:45:12 <}-z-{> esteel is on this side of the fence
    Mar 05 10:45:16  hrm maybe Procyon2 for the maplist (dm or insta)
    Mar 05 10:45:16 <}-z-{> is he not?
    Mar 05 10:45:37    dunno, I haven't seen him talking, I haven't read the backlogs
    Mar 05 10:45:38   Dokujisan: desertfactory as sure thing on maplist :)
    Mar 05 10:45:41  he hasn't said exactly, but it appears that he is onboard
    Mar 05 10:45:48   that should be the last official map, rest can be supplied as pk3
    Mar 05 10:45:55    what about Kadaverjack?
    Mar 05 10:46:11    he still owns planetnexuiz.de iirc
    Mar 05 10:46:20    and he was a major developer once too
    Mar 05 10:46:34  is he still active in the nexuiz community?
    Mar 05 10:46:41 <}-z-{> active enough
    Mar 05 10:46:49    not so much, but he posts his thoughts now and then
    Mar 05 10:47:29  Ok, here's another question onto the development. I haven't hard anything about ODE support ever since the first tests were done and videos of it working were put on Youtube. Everything went silent after... what is the status of ODE support in DP? Why aren't physical brushes already in entities.def?
    Mar 05 10:48:14  what is ODE?
    Mar 05 10:48:41  physics engine
    Mar 05 10:48:43  Open Dynamics Engine. Physics engine, for realistic physics like moving crates, stuff rolling around etc
    Mar 05 10:48:44  ahh
    Mar 05 10:49:15   indeed what happened to that...
    Mar 05 10:49:20  Was pretty excited about that at first :) But at some point it went silent
    Mar 05 10:50:13   [16:36:20] <@CuBe0wL> btw... what about that community petition?
    Mar 05 10:50:19   why? AT would LET us take over, I am sure
    Mar 05 10:50:55 <}-z-{> to vermeulen's credit?
    Mar 05 10:51:21  is paperclips a developer?
    Mar 05 10:51:34  or contributor of some sort
    Mar 05 10:51:35   no i dont think so
    Mar 05 10:51:37 <}-z-{> I didn't think he was, maybe mapper?
    Mar 05 10:52:19  ode sorta clashes with the 'normal' game iirc eg interaction between old quake objects and ode is shitty. 
    Mar 05 10:52:21  }-z-{: can you query the unique usernames of people who created topics under "Map Releases">
    Mar 05 10:52:23  ?
    Mar 05 10:52:43  id imagine thats one of the things that stopped the ode use sofar
    Mar 05 10:52:48 <}-z-{> not easily and not right now
    Mar 05 10:52:52  ok
    Mar 05 10:52:58 <}-z-{> apparently redmin can't accept a database password starting with #
    Mar 05 10:53:09 <}-z-{> because it's telling me this on rake: Access denied for user 'db_cankill'@'silversurfer.dreamhost.com' (using password: NO)
    Mar 05 10:54:04  Who is "Chris"? a developer?
    Mar 05 10:54:18 <}-z-{> isn't he a qc guy? from i3d land?
    Mar 05 10:54:20    nexuiz_new_notes : vcall rename text "Pheonix notes"
    Mar 05 10:54:51  no
    Mar 05 10:54:59    :(
    Mar 05 10:55:00  I think we already shot down pheonix as a name
    Mar 05 10:55:04    when?
    Mar 05 10:55:08     Ello
    Mar 05 10:55:13  Dokujisan: some dood lurkign arround #darkplaces. developer of some sort iirc.
    Mar 05 10:55:23   nexitron?
    Mar 05 10:55:25  the name Phoenix is overused a lot, a misspelling of it is even worse.
    Mar 05 10:55:32     Chris is a developer making his own game with Darkplaces
    Mar 05 10:55:35     Ignore him
    Mar 05 10:55:45  I think we really want a name that doesn't have an existing meaning, just like nexuiz
    Mar 05 10:55:48     iirc he's making a realistic game
    Mar 05 10:56:09  CuBe0wL: but.... someone did suggest we use a symbol that means phoenix or something like it
    Mar 05 10:56:20  for the game symbol, since we can't use the 'n' kanji anymore
    Mar 05 10:56:22    Dokujisan, imho what was so awesome in the name of Nexuiz, that it really made ppl say "wtf"
    Mar 05 10:56:38  CuBe0wL: well... not awesome. It's not a good name
    Mar 05 10:56:45  so "wtf" was more like.... who came up with that?
    Mar 05 10:56:46    playfull
    Mar 05 10:56:50  Samual: well dont always ignore him. read backlog on him here for a interresting part.
    Mar 05 10:56:54    I always liked it
    Mar 05 10:57:07  CuBe0wL: you already admitted that you thought it was strange :-)
    Mar 05 10:57:10  at first
    Mar 05 10:57:28  really any name that we come up with is going to grow to have meaning to us, just like nexuiz
    Mar 05 10:57:32    yes, but I never said I didn't like it from the first read
    Mar 05 10:57:37  but I thikn we should still take some time with the choice
    Mar 05 10:57:44    k
    Mar 05 10:57:46     [10:57:14am]  Samual: well dont always ignore him. read backlog on him here for a interresting part.
    Mar 05 10:57:50  well I never "hated" it. I just thought it was odd
    Mar 05 10:57:52     I don't have time to read the whole #darkplaces log
    Mar 05 10:58:08  _backlog on him here_
    Mar 05 10:58:11  I would really like a name that people can pronounce
    Mar 05 10:58:17   +1
    Mar 05 10:58:17  use search you lazy toad
    Mar 05 10:58:20   +1000 :P
    Mar 05 10:58:26  haha
    Mar 05 10:58:37     I can't, my logs fail :P
    Mar 05 10:58:42  Hmm... I have an idea for the symbol. Hold on
    Mar 05 10:58:50  .|.. 
    Mar 05 10:58:52    I still stand by my suggestion, it should be considered as a name. (also, Pheonix is pronouncabel, and we can still pronounce it as phoenix)
    Mar 05 10:58:55  taht one? };P
    Mar 05 10:59:01  CuBe0wL: but yeah we can find some kanji that has the same meaning as "phoenix"
    Mar 05 10:59:13    hey, not a bad idea
    Mar 05 10:59:42    btw. what I always liked in Nexuiz are the in community jokes
    Mar 05 11:00:06  http://img46.imageshack.us/img46/1096/kojndragonstrength.png }-z-{ gave me this an year ago (it was to make a ninja player model... I'm sorry I haven't made it even today :( ) Anyway, something like that could be pretty.
    Mar 05 11:00:32    "epic", "AGY))", "Nexuiz", the fact that Specop (not SPACE COP) is a woman...
    Mar 05 11:00:39  Not -that- one, but something similar
    Mar 05 11:01:21    Pheonix would be a similar ingame joke, that roots back to Nexuiz. Playfull, and still brings back good memories for those, who knew it
    Mar 05 11:01:55    for those who will join later, it might be a wtf, but it'll be still funny when it get's explained
    Mar 05 11:02:16    community building, on the remains of the old one
    Mar 05 11:02:53  Pheonix could be a good name for a default character
    Mar 05 11:03:07  another good idea
    Mar 05 11:03:27  or they could have a phoenix symbol on their chest
    Mar 05 11:03:33  yeah
    Mar 05 11:03:49    hmm... Nexus renamed to Pheonix ?
    Mar 05 11:04:06    feels a bit too distant
    Mar 05 11:04:08  is that the main character name? Nexus?
    Mar 05 11:04:35    well, I always thought about Nexus and Xolar as their race is the main one
    Mar 05 11:04:48  I like using the symbolism of "phoenix" but I can't say I like the name. I once tried to use it for a server name "Phoenix CTF" as it was rising from the ashes of my previous server "Fusion CTF"....but it turned out to be a bad name
    Mar 05 11:04:52    their description says: "Nexuiz's soldier"
    Mar 05 11:04:57  We could add a new character. I believe that with this name change we should also add something new
    Mar 05 11:06:02   pheonix sounds good
    Mar 05 11:06:08    I kinda like the style of Nexuiz's player models
    Mar 05 11:06:14   phoenix would be bad simply because it'd be near impossible to get google hits :)
    Mar 05 11:06:34  pnehoix?
    Mar 05 11:06:57     tZork, easier to pronounce than Nexuiz for sure
    Mar 05 11:06:59    that's sounds like a diseas, not a game
    Mar 05 11:07:09  soz gettin a bit silly.. 
    Mar 05 11:07:58    also, a phoenix is a bird
    Mar 05 11:08:06    birds are always the symbol to be free
    Mar 05 11:08:16   Hmm
    Mar 05 11:08:17    Pheonix is free as a bird
    Mar 05 11:08:43    haha
    Mar 05 11:08:45   good luck getting a domain for either though...
    Mar 05 11:09:11    we could implement the game mode: catch the chicken... just with phoenix :D
    Mar 05 11:09:36    pheonixgame.org ?
    Mar 05 11:09:57  hehe
    Mar 05 11:10:02  freeonix
    Mar 05 11:10:19  sounds like a oddball os tough
    Mar 05 11:10:28    +1 :D
    Mar 05 11:10:36   pheonixgame.org is available
    Mar 05 11:10:46   .com is taken :O
    Mar 05 11:11:09  or juz 1337 speak it. ph3onix.com
    Mar 05 11:11:21  ew
    Mar 05 11:11:53  can we establish a rule that we aren't allowed to use 1337 speak in anything? :-)
    Mar 05 11:12:29  sure, just as long as its allowed to break it ;)
    Mar 05 11:12:50  rules are made to be br0k3n
    Mar 05 11:12:56    lol :D http://pheonixgame.com/default.aspx
    Mar 05 11:13:09   yes wtf
    Mar 05 11:13:13   awesome web design
    Mar 05 11:13:18  email based game
    Mar 05 11:13:27  epic colors ate my eyes
    Mar 05 11:13:34    yep, email based RPG
    Mar 05 11:13:37   >_<
    Mar 05 11:13:49  btw did you see this parody map? http://alientrap.org/forum/viewtopic.php?f=19&t=6054
    Mar 05 11:13:58   by Taoki? yes :D
    Mar 05 11:14:09    freepheonix.com is available!
    Mar 05 11:14:19  :P
    Mar 05 11:14:22  HERE ARE THE RULES:
    Mar 05 11:14:23  CLICK HERE TO DONATE TO CREATION AND MAINTENANCE
    Mar 05 11:14:40  roflamao
    Mar 05 11:15:10  rolling on the floor laughing and maiming an orphan?
    Mar 05 11:15:36  ok... I have no idea about our timeline with this fork
    Mar 05 11:15:37  however
    Mar 05 11:15:46    pheonixgame.org is available!
    Mar 05 11:15:57  I was already starting to plan the April Fools day mapping project
    Mar 05 11:16:14  the halloween mapping thing failed, but last year's april fool's mapping project was a success
    Mar 05 11:16:21    hey
    Mar 05 11:16:29    I contributed to halloween :P
    Mar 05 11:16:39  I know, but it was a failed project overall
    Mar 05 11:16:44    true
    Mar 05 11:18:35    btw... I'be just realised yesterday I could reopen the locked Illfonic's thread :D
    Mar 05 11:18:41    should I? >:D
    Mar 05 11:18:49  oh they locked it?
    Mar 05 11:19:04  that was quite a pointless thread
    Mar 05 11:19:38    lol Dokujisan are you reading the forum nowadays at all? :D
    Mar 05 11:19:43  "I'd like to get feedback from you guys" ... "Ok, I hear your feedback, but it's going to change absolutely nothing. Do you have any other feedback?"
    Mar 05 11:20:00  yeah I do a bit. not as much as I used to though
    Mar 05 11:20:15  I usually scan just the map releases forum
    Mar 05 11:20:18  which is...not active lately
    Mar 05 11:20:27    I'd like to get feedback abour OUR game, OUR, NOT YOURS, I DON'T GIVE A FLYING FUCK FOR THAT. :D
    Mar 05 11:21:13    oh, about maps, I think "Vociferous" is starting to get in shape...
    Mar 05 11:22:08  this? http://www.alientrap.org/forum/viewtopic.php?f=19&t=4807
    Mar 05 11:23:18    yes
    Mar 05 11:23:20    http://alientrap.org/forum/viewtopic.php?p=75629#p75629
    Mar 05 11:23:20   BTW had this idea: http://en.wikipedia.org/wiki/Nu_(letter)
    Mar 05 11:23:26   what about NuNex? :P
    Mar 05 11:23:35   would be pronounced like "New Nex" wouldnt it
    Mar 05 11:23:49   well almost
    Mar 05 11:23:59  hmm, I would really like to see a name that is it's own
    Mar 05 11:24:12  a year from now, we're not going to be thinking "Nexuiz" anymore
    Mar 05 11:24:20   http://en.wikipedia.org/wiki/Phoenix_(mythology) 
    Mar 05 11:24:42   mentions "simurgh"
    Mar 05 11:25:02    I instantly associated with Nu with Elfen lied
    Mar 05 11:25:07    Elven Lied, sorry
    Mar 05 11:25:58   Nex Juice?
    Mar 05 11:26:04   :P
    Mar 05 11:26:08   NuNex -> nun ex
    Mar 05 11:26:17  hey mand1nga :-) 
    Mar 05 11:26:19   Nü Nex
    Mar 05 11:26:23  did you read the text file in the subject?
    Mar 05 11:26:24    http://bluejaunte.files.wordpress.com/2009/11/tactical_facepalm.jpg
    Mar 05 11:26:26   hey Doku
    Mar 05 11:26:42   most of it, but haven't finished yet
    Mar 05 11:26:59    I think I've had
    Mar 05 11:27:08    ooops
    Mar 05 11:27:10   and I agree on everything I read, I suppose we'd be on the same page
    Mar 05 11:27:19    sorry, I thikn I've edited the topic
    Mar 05 11:27:37    lemme check that link in my history
    Mar 05 11:27:51 *   CuBe0wL has changed the topic to: Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt
    Mar 05 11:27:54  tactical facepalm?
    Mar 05 11:28:03    for those idiot ideas
    Mar 05 11:28:05  thats...
    Mar 05 11:28:41    oh, one thing for models, if there be any... TAUNT ANIMATIONS!
    Mar 05 11:28:42     I've seen that before
    Mar 05 11:28:47    we need facepalm
    Mar 05 11:29:23   only when Samual talks
    Mar 05 11:29:27    some kind of a dance
    Mar 05 11:29:33   :>
    Mar 05 11:29:40     [11:29:48am]  only when Samual talks
    Mar 05 11:29:43     ...
    Mar 05 11:29:57   I'm kidding you fool :P
    Mar 05 11:30:00    imagine pyria doing a sexy dance when you get fragged by her ;)
    Mar 05 11:30:03     >.>
    Mar 05 11:31:25   pyria has a sexy animation
    Mar 05 11:31:58   but I can't remember how to use it
    Mar 05 11:32:04    oO
    Mar 05 11:32:13    look at the codes pls
    Mar 05 11:32:19    I wanna see it :D
    Mar 05 11:32:22   ask MrBougo
    Mar 05 11:32:31   I like the idea of having three leaders
    Mar 05 11:32:37   F?nix
    Mar 05 11:33:09   I don't know who these leaders will be
    Mar 05 11:33:31   In Japan, the phoenix is called h?-? (kanji:"??") or fushich? (????), literally "Immortal Bird".
    Mar 05 11:33:50  stop putting in the same sentance. they to not belong.
    Mar 05 11:34:10  err stop puttin oyria and sexy *
    Mar 05 11:35:50  ok guys... let's resume our name discussions.... please read this and PICK FROM THE LIST YOUR TOP CHOICES and send me your list. Keep in mind that you're picking the ones that don't completely suck. They dont have to be perfect, but they can give us a direction.
    Mar 05 11:35:52  http://www.nullgaming.com/stuff/nexuiz_new_name.txt
    Mar 05 11:35:52   I'd like to have a strict anti-mikee policy on this project
    Mar 05 11:36:05  think this kbd is giving in. i usualy fark up words, but some go missing
    Mar 05 11:36:13  but now* 
    Mar 05 11:36:24   Dokujisan: I suggest to make a poll somewhere so we decide the name
    Mar 05 11:36:33  mand1nga: we can get to that after you dwindle down
    Mar 05 11:36:35   unless it has been decided already
    Mar 05 11:36:45   dwindle?
    Mar 05 11:36:57  we need to start with a bulk list. We still hve more brainstorming for names to do. This isn't the final list
    Mar 05 11:37:14  but you guys picking from this list will help with future brainstorming
    Mar 05 11:37:58   Dokujisan: what do you mean by dwindle down?
    Mar 05 11:37:59   sexy pyria http://www.flickr.com/photos/23986967@N05/2506000688/in/set-72157605143265605/
    Mar 05 11:38:09  mand1nga: reduce in number
    Mar 05 11:38:52   I still don't get it, can you rephrase please?
    Mar 05 11:39:05   Spaceman: come on she has no legs there :o
    Mar 05 11:39:18  theree are 50 or so on that list. we need to reduce that to 10 or so
    Mar 05 11:39:53   I wasn't looking at her legs :p
    Mar 05 11:40:53   wow those names are crazy
    Mar 05 11:41:16     Honestly
    Mar 05 11:41:17   lol how about nexodus
    Mar 05 11:41:20     I think we could do Sexuiz
    Mar 05 11:41:30     I bet it would be the best opensource game of all time
    Mar 05 11:41:48     Open Arena already has the scene right now, but they're doing it wrong
    Mar 05 11:41:54     Needs moar graphix :X
    Mar 05 11:41:58   lol nexzilla wtf I can't take this list seriously
    Mar 05 11:42:30  these are just for picking a direction and I included everything mentioned
    Mar 05 11:45:04  ok CuBe0wL I looked at vociferous. I used to have this map on my HODM server. It has some flaws in this beta version, but you probably know that
    Mar 05 11:46:06  like big long hallways with no place to evade, and teleporter exists look like teleporter entrances and that's a little confusing
    Mar 05 11:46:25    MY PICKS: nexetic, nexira, nexonic, xenotic. I gotta puke for all avaible ones, most of them sounds like medicine names. Also, some suggestions: Reborn, NeXT, Pheonix
    Mar 05 11:46:39  noted
    Mar 05 11:46:58 <}-z-{> http://dev.xonotic.org we can start getting organized here
    Mar 05 11:47:18   I think a word in japanese might fit as a new name
    Mar 05 11:47:39     Xenotic
    Mar 05 11:47:41   I'd like to try other things apart of random names including z and x
    Mar 05 11:47:41     I like that
    Mar 05 11:47:53     >.>
    Mar 05 11:47:58  sure, we can get to foreign/non-english names. Right now, we're aiming for made-up words that have no meaning (like nexuiz was)
    Mar 05 11:48:00     lawl well I still like Xenotic.
    Mar 05 11:48:00   :P
    Mar 05 11:48:18   something like ryūshutsu :)
    Mar 05 11:48:29   (exodus in japanese)
    Mar 05 11:48:33  "- We should have a name that people can pronounce"
    Mar 05 11:48:46   I know, that was a sample
    Mar 05 11:48:48  otherwise, I'm not against using a japanese word
    Mar 05 11:49:05   I like Xenotic too somewhat :P
    Mar 05 11:49:12  but let's start with one thing at a time. We can do another phase of searching for foreign names
    Mar 05 11:49:24  after this step
    Mar 05 11:50:10   also remember we can postfix with "game"
    Mar 05 11:50:16   eg. xenoticgame.com is available
    Mar 05 11:50:29  read the top of my names file
    Mar 05 11:50:29 <}-z-{> too long
    Mar 05 11:50:34  it says that is a plan B
    Mar 05 11:50:40   oh okay
    Mar 05 11:51:04  FruitieX: is xenotic the only one on your list?
    Mar 05 11:51:07 <}-z-{> Dokujisan: want to start moving that file to the wiki in dev.xonotic.org?
    Mar 05 11:51:13 <}-z-{> that text file
    Mar 05 11:51:14  absolutely
    Mar 05 11:51:19  I want to move both of these
    Mar 05 11:51:29 <}-z-{> I'll need more time with wordpress mu
    Mar 05 11:51:32  k
    Mar 05 11:51:35 <}-z-{> still trying to do my real work too :-P
    Mar 05 11:51:35   I'd rather sex.cankill.us :P
    Mar 05 11:51:38   nah i'll take a look at the others Dokujisan 
    Mar 05 11:51:44 <}-z-{> mand1nga: it's just temporary :-P
    Mar 05 11:51:48    Zymotic
    Mar 05 11:51:50    :D
    Mar 05 11:51:51 <}-z-{> was a short domain name I had already
    Mar 05 11:51:56   I vote for divox
    Mar 05 11:51:58   CuBe0wL: oold
    Mar 05 11:52:05 <}-z-{> divx? :-P
    Mar 05 11:52:07   (totally kidding :P)
    Mar 05 11:52:08    divox eh?
    Mar 05 11:52:30    why not kinky, or diva
    Mar 05 11:52:40    tactical facepalm in....
    Mar 05 11:52:41    3
    Mar 05 11:52:42    2
    Mar 05 11:52:43    1
    Mar 05 11:52:44  mand1nga: consider how strange the word "nexuiz" is and we found a way to appreciate it anyway over time
    Mar 05 11:52:48 *   CuBe0wL FACEPALM!
    Mar 05 11:53:17  mand1nga: likewise, the new name we end up using might also have a name that grows on you (but is not spelled oddly and can be pronounced easily)
    Mar 05 11:53:19   Dokujisan: sure, but I say lets try other approaches too
    Mar 05 11:53:26   in an organized way of course
    Mar 05 11:53:29  mand1nga: yep, as I said, we'll do that after this step
    Mar 05 11:53:42 <}-z-{> superhappyfun game
    Mar 05 11:53:54  greek, japanese and latin words are usually good for picking names
    Mar 05 11:54:24  and as part of that, we can do a variation of a greek/japanese/latin word.... 
    Mar 05 11:54:29    Itoma?
    Mar 05 11:54:43   18:54:41 <@}-z-{> superhappyfun game
    Mar 05 11:54:45   dot com
    Mar 05 11:54:49    means "free" in Japan, and also a wave goodbye
    Mar 05 11:55:07   :o that sounds good CuBe0wL 
    Mar 05 11:55:20    also, it means free time too :D
    Mar 05 11:55:27   haha
    Mar 05 11:55:33  that's better than pheonix :-)
    Mar 05 11:55:51    or spare time :)
    Mar 05 11:56:59   well I kinda like one name on the list: zeonix but I'm sure I'd like more a random japanese word
    Mar 05 11:57:02    but itoma domain is taken
    Mar 05 11:57:19   ItomaFPS is free, domain seo wise.
    Mar 05 11:57:27   itomagame :P
    Mar 05 11:57:35   is free both com and org
    Mar 05 11:59:20    Itoma feels... both odd and cool at the same time
    Mar 05 11:59:36   yeh
    Mar 05 11:59:43    Toritoma? :D
    Mar 05 11:59:49   it feels odd at one time for me :P
    Mar 05 11:59:49    sounds like tomato
    Mar 05 12:00:03   Nexitoma? :P
    Mar 05 12:00:10   kontesuto = contest
    Mar 05 12:00:17    too long
    Mar 05 12:00:28   sokudo = speed
    Mar 05 12:00:37     meh, connection on the train is really bad atm..
    Mar 05 12:00:39    or simply... Tori?
    Mar 05 12:00:44    hi esteel 
    Mar 05 12:00:49     hi CuBe0wL 
    Mar 05 12:00:54    Tori means "bird" if I'm not mostaken
    Mar 05 12:00:56  sudoku? :S
    Mar 05 12:01:01   CuBe0wL: that makes me think of the game Toribash
    Mar 05 12:01:01   :P
    Mar 05 12:01:10    me too, but that's cool :D
    Mar 05 12:01:30 *   pavlvs (pavlvs@75.39.134.107) has joined #notnexuiz
    Mar 05 12:01:58     yo
    Mar 05 12:02:04  hi pavlvs
    Mar 05 12:02:12     hi tZork 
    Mar 05 12:02:44    Saikai? it means resumption
    Mar 05 12:02:45   hi pavlvs 
    Mar 05 12:02:59     hm looks like almost everyone necessary is in here
    Mar 05 12:03:31  :-)
    Mar 05 12:03:34    I was just going to tell ask :D
    Mar 05 12:03:38    afk I mean
    Mar 05 12:03:43    I'm starving :(
    Mar 05 12:04:02    I'll go check and see what can I find in the deep freezer
    Mar 05 12:04:04   Really though, Itoma sounded nice :-)
    Mar 05 12:04:48   dunno
    Mar 05 12:04:59  it's up there
    Mar 05 12:05:06  in quality, I mean
    Mar 05 12:05:10  I haven't added it yet
    Mar 05 12:05:34 <}-z-{> erosdon't see anyone registered yet
    Mar 05 12:05:38 <}-z-{> don't*
    Mar 05 12:05:42  I just did
    Mar 05 12:05:49  but does it sent a confirmation email?
    Mar 05 12:05:54 <}-z-{> it should
    Mar 05 12:06:07   registering domains already? :o
    Mar 05 12:06:12 <}-z-{> no
    Mar 05 12:06:17 <}-z-{> just using a temp one to get organized
    Mar 05 12:06:38   right
    Mar 05 12:06:39 <}-z-{> Dokujisan: I activiated you
    Mar 05 12:06:41  ok
    Mar 05 12:06:52 <}-z-{> and made you admin
    Mar 05 12:07:01 <}-z-{> did you set a password, do you need a password?
    Mar 05 12:07:08     tori? saikai? loking for new names?  Superiuz.. similar to superior :P
    Mar 05 12:07:10  I'm in
    Mar 05 12:07:33    too bad there's Toribash
    Mar 05 12:07:44    Tori would be a nice pick
    Mar 05 12:08:56    esteel, what kind of irc client do you use? mirggi?
    Mar 05 12:09:19 <}-z-{> Dokujisan: I hit a bump in the road
    Mar 05 12:09:20 <}-z-{> NOTICE
    Mar 05 12:09:25 <}-z-{> "WordPress MU is not allowed to be run on our shared hosting servers. If you intend on running this under your account, you are required to be on a Private Server"
    Mar 05 12:09:41  :-o
    Mar 05 12:09:45  hmmm
    Mar 05 12:09:51  so do I need to host it?
    Mar 05 12:10:09  and give you access
    Mar 05 12:10:16    brb
    Mar 05 12:10:26 <}-z-{> can you give me SSH and PHPMyAdmin?
    Mar 05 12:11:14  hmm... well is this going to end up as a permanent solution?
    Mar 05 12:11:18  or just a temporary thing
    Mar 05 12:11:22 <}-z-{> perm
    Mar 05 12:11:30  ok let me think about that.....
    Mar 05 12:11:50 <}-z-{> okay, I'm looking into Dreamhost PS
    Mar 05 12:11:58 <}-z-{> I don't want to put mu on the would be build server
    Mar 05 12:12:15     CuBe0wL: weechat
    Mar 05 12:12:39 <}-z-{> man dh ps is 'spensive
    Mar 05 12:12:45 <}-z-{> might as well buy another VPS at that price lol
    Mar 05 12:12:54 <}-z-{> minimum is $15/mo for 150mb
    Mar 05 12:13:04    }-z-{, what will you do with nexuiz ninjaz btw ?
    Mar 05 12:13:20 <}-z-{> I can fork that 'the ninjaz'
    Mar 05 12:13:32 <}-z-{> and be more general but put most of my efforts towards this project
    Mar 05 12:13:40   ItomaNinjaz?
    Mar 05 12:13:49 <}-z-{> maybe illfonic will offer money for the domain and we can pay for the build server for a year :-P
    Mar 05 12:14:05    {X}ItomaNinjaz ? :D
    Mar 05 12:14:35     hey, where are all those names coming from? :P
    Mar 05 12:15:04 <}-z-{> Dokujisan: it's probably best if we do a separate VPS or dedicated anyway, it's better to have full control over apache for this
    Mar 05 12:15:15     i can consider something
    Mar 05 12:15:24     Well
    Mar 05 12:15:28     I have a VPS too
    Mar 05 12:15:31     Actually I have two
    Mar 05 12:15:48     Although I don't personally own them :P
    Mar 05 12:15:50  }-z-{: yes I would think that is best
    Mar 05 12:15:54 <}-z-{> probably need 512mb RAM, multicore processor prefered, 5gb MINIMUM but want ~20 to be comfortable
    Mar 05 12:15:56     I'd have to ask the owner if we could use them if needed.
    Mar 05 12:16:01 <}-z-{> gb space
    Mar 05 12:16:27     My server has 728mb memory, 20GB hard drive, and it's a quad core (They fucked up, it was supposed to be dual core)
    Mar 05 12:16:31     Er
    Mar 05 12:16:35     768*
    Mar 05 12:16:37 <}-z-{> yes but it's not dedicated to this, correct?
    Mar 05 12:16:50     Well, right now it just runs my Nexuiz server :P
    Mar 05 12:16:53     hm
    Mar 05 12:16:59     Which takes up all of 100mb of the ram :P
    Mar 05 12:17:06     wthis is neede for something processing intensive?
    Mar 05 12:17:07    brb, I need to boild my veegtable dish I've found in the fridge
    Mar 05 12:17:08 *   merlijn (merlijn@84.245.21.196) has joined #notnexuiz
    Mar 05 12:17:56 <}-z-{> pavlvs: just apache and mysql
    Mar 05 12:18:01 <}-z-{> which _can_ be processor intensive
    Mar 05 12:18:05 <}-z-{> but not necessarily
    Mar 05 12:18:15 <}-z-{> I propose we keep the development site on another server
    Mar 05 12:18:27 <}-z-{> because running rails on top of apache will kill our resources a bit
    Mar 05 12:18:27  ok I just chatted with dublpaws and he is willing to give Dance a makeover to have it considered for inclusion in the game
    Mar 05 12:18:45 <}-z-{> also, if one site goes down, we can still communicate to users via the other
    Mar 05 12:18:46  and if anyone wants to help him with that, collaborate, he is open to that
    Mar 05 12:18:57     }-z-{: [prae] has a dual quad with 8gb ram, soon to be 12gb
    Mar 05 12:19:04  728 megs on a quad? wth=
    Mar 05 12:19:08 <}-z-{> wow yeah, that'd be very helpful :-P
    Mar 05 12:19:16 <}-z-{> that's fully dedicated I assume?
    Mar 05 12:19:21     tZork, it was supposed to be a dual core :P
    Mar 05 12:19:22     yes colo'd
    Mar 05 12:19:26 <}-z-{> very nice
    Mar 05 12:19:28 <}-z-{> what OS?
    Mar 05 12:19:34     }-z-{: i run xen so i could spin up a VM sometime
    Mar 05 12:19:36  its still ftw Samual
    Mar 05 12:19:38     debian
    Mar 05 12:19:51 <}-z-{> okay
    Mar 05 12:20:02 <}-z-{> debian or ubuntu should be good
    Mar 05 12:20:13 <}-z-{> can you give me ssh and possbily sudo?
    Mar 05 12:20:17  Samual: rented, virtual? tahtäd explain it..
    Mar 05 12:20:24     of course
    Mar 05 12:20:28 <}-z-{> awesome
    Mar 05 12:20:31     such is the beauty of vm's
    Mar 05 12:20:33  perfect :-)
    Mar 05 12:20:35 <}-z-{> :)
    Mar 05 12:20:40     Virtual and rented
    Mar 05 12:20:44  pavlvs: if you host that, then I think I can continue hosting HOCTF/HODM
    Mar 05 12:20:45     but yeah ill have to see if we have resources available
    Mar 05 12:21:03 <}-z-{> what they hell else can you be using all those resources for? :-P
    Mar 05 12:21:04  actually, I would prefer to now with this fork
    Mar 05 12:21:22  I was planning on transitioning my servers over to pavlvs
    Mar 05 12:21:30  HOCTF/HODM
    Mar 05 12:21:38     need about $30-40 more in my ram fund to get to that 12gb
    Mar 05 12:21:52 <}-z-{> you're really using 8gb already?
    Mar 05 12:22:20 <}-z-{> you gotta be running at least 18 nexuiz servers for that :-P
    Mar 05 12:22:26     well, if i were to run all the nexuiz servers i was planning on running
    Mar 05 12:22:33     which is 15
    Mar 05 12:22:37     ;p
    Mar 05 12:22:39 <}-z-{> I can run 10 servers under 2gb
    Mar 05 12:22:54     i also have 3 tf2 servers and a l4d2 server
    Mar 05 12:22:58 <}-z-{> ah well
    Mar 05 12:23:02 <}-z-{> that's another story :-P
    Mar 05 12:23:02     and email and various apaches
    Mar 05 12:23:07  oh...this is perfect, because pavlvs also runs a mumble server
    Mar 05 12:23:12     the zimbra takes ridiculous ram
    Mar 05 12:23:13 <}-z-{> ah nice
    Mar 05 12:23:15     yes
    Mar 05 12:23:19     praeclan.com
    Mar 05 12:23:19 <}-z-{> yeah, I've heard zimbra is a hog
    Mar 05 12:23:20  Samual: less of a prob then since its likely not 728 total mem. the thing is a modern cpu (onr core) easly chug tough a gig of ram proccessing its stuff. less then one g per code oin a didecated is just stupid. 
    Mar 05 12:23:27    hiya, I'm just trying to read up on the stuff that happened, any other stuff besides topic I should read?
    Mar 05 12:23:39  pavlvs: we talked about having an official mumble server for the game
    Mar 05 12:23:42 <}-z-{> pavlvs: how soon can this be ready for our use?
    Mar 05 12:23:50  hi merlijn
    Mar 05 12:23:54  but I dont' think mumble uses much in terms of resources
    Mar 05 12:23:56     i guess i dont have plans tonight...
    Mar 05 12:23:57    re
    Mar 05 12:24:05    also I can provide any server stuff you're needing
    Mar 05 12:24:17  hey merlijn :-D
    Mar 05 12:24:38 *   }-z-{ has changed the topic to:  Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt  -- http://dev.xonotic.org -- temporary development site to get organized
    Mar 05 12:24:40  merlijn: that file in the topic is a pretty good overview
    Mar 05 12:24:50 <}-z-{> Dokujisan: should I make dev.xonotic.org register only for now?
    Mar 05 12:24:59  yes
    Mar 05 12:25:06  good call
    Mar 05 12:25:09    I still don't get what the main reason for forking is, just getting rid of vermeulen/alientrap?
    Mar 05 12:25:21 <}-z-{> that's a large part
    Mar 05 12:25:21  merlijn: well there are a lot of reasons actually
    Mar 05 12:25:31  to me, this is actually a chance for a clean slate
    Mar 05 12:25:31 <}-z-{> but we're already streamlining a lot of things
    Mar 05 12:25:53   BTW maps, what about race maps?
    Mar 05 12:26:00  if you read through those notes, you'll see a lot of ideas have been put forth, including a structure for how the game is managed
    Mar 05 12:26:03  which nexuiz never had
    Mar 05 12:26:04   we should probably skip the piece-o-cake map
    Mar 05 12:26:05    +1 for race
    Mar 05 12:26:09   in fact, probably no nexrun maps at all
    Mar 05 12:26:13   in the official release
    Mar 05 12:26:22  FruitieX: I know nothing about race maps, so let me know what you guys come up with
    Mar 05 12:26:30    why, they are good, and GPL'ed
    Mar 05 12:26:34   or depends, if anyone's interested in having nexrun as a "havoc mode" replacement :P
    Mar 05 12:26:35    we've had multiple attempts at streamlining and better organisation - why is this one going to work?
    Mar 05 12:26:56 <}-z-{> Dokujisan: I've started the wiki for the plan here: http://dev.xonotic.org/projects/notnexuiz/wiki/Plan
    Mar 05 12:27:08 <}-z-{> just a dump of your text file right now
    Mar 05 12:27:09    btw, I'm not being negative just some healthy scepticism :)
    Mar 05 12:27:19   development can kill us
    Mar 05 12:27:21   :P
    Mar 05 12:27:23 <}-z-{> :-P
    Mar 05 12:27:44  thanks }-z-{ 
    Mar 05 12:27:57 <}-z-{> I'll help you clean it up a bit
    Mar 05 12:28:10 <}-z-{> pavlvs: do you have an IP I can set an A record for?
    Mar 05 12:28:13    one thing I really suggest we should inform the community on the forum of our forking plan ASAP
    Mar 05 12:28:18 <}-z-{> for the temporary domain name
    Mar 05 12:28:27 <}-z-{> CuBe0wL: I'd like to get more organized first
    Mar 05 12:28:38     }-z-{: we'll have to figure out ip/domain stuff 
    Mar 05 12:28:40 <}-z-{> so we don't come off as a bunch of idiots
    Mar 05 12:28:43 <}-z-{> okay pavlvs 
    Mar 05 12:28:44  merlijn: I think it's because we're starting from scratch with organization. I lost interest in Nexuiz 8-9 months ago, but this gives me a surge of interest again, and I think that is probably the same for others
    Mar 05 12:28:44     its a bid weird with my xen config
    Mar 05 12:28:58 <}-z-{> I should be able to add an A record and you can do a virtual host on apache
    Mar 05 12:29:03     }-z-{: i need to do some homework and go to class, i'll be back at 5 EST
    Mar 05 12:29:08 <}-z-{> okay pavlvs 
    Mar 05 12:29:16     }-z-{: also i have a bind server if that helps
    Mar 05 12:29:34  merlijn: I've always wanted a nexuiz fork because of this very problem of lack-of-management and leadership for the game. But now it appears that everyone is onboard with plans to do everything Nexuiz should have had.
    Mar 05 12:29:46 <}-z-{> yes pavlvs it will for wordpress mu
    Mar 05 12:29:55    Dokujisan: new ideas usually generate a lot of energy at first, question is whether that will stay
    Mar 05 12:29:56     wight
    Mar 05 12:29:59 <}-z-{> so we can setup subdomains
    Mar 05 12:30:01 <}-z-{> and such
    Mar 05 12:30:18     well then the nameserver is 208.94.245.226
    Mar 05 12:30:21 <}-z-{> Dokujisan: give me 5 minutes to clean up this wiki page, then have it
    Mar 05 12:30:27     praeclan.com
    Mar 05 12:30:34  merlijn: well the goal with my ideas is to establish methods for how things will work....so that will carry the momentum
    Mar 05 12:30:42 <}-z-{> pavlvs: I'd prefer if I can use use an arecord to you machines IP
    Mar 05 12:30:54 <}-z-{> so I can leave DNS on dreamhost which is currently serving dev.xonotic.org
    Mar 05 12:31:01     okie
    Mar 05 12:31:03 <}-z-{> A record*
    Mar 05 12:31:13  merlijn: I'm going to be doing a lot of the community organization and part of that involves delegating and recruiting. As we recruit, those new people add even more energy to the project
    Mar 05 12:31:17 <}-z-{> do you know how to handle apache virtual hosts?
    Mar 05 12:31:46    Dokujisan: and what about the nexuiz name? wouldn't it at least me a good idea to benefit from the promotion on the IllFonic side of things?
    Mar 05 12:32:10  merlijn: the promotion of "Nexuiz" by illfonic will only benefit Illfonic's name.
    Mar 05 12:32:24  got b33r? - http://tzork.dvrdns.org/tmp/gotbeer.jpg :D
    Mar 05 12:32:27  a year from now, when googling for "Nexuiz", people will start to find the game by Illfonic
    Mar 05 12:32:30    Dokujisan: why are you so sure about that?
    Mar 05 12:32:34  and it will be harder to find "our" game
    Mar 05 12:32:57    maybe, but a new game will be hard to find anyway
    Mar 05 12:33:41  the fact that they have nexuiz.com alone is bad enough. When people try to find our Nexuiz game (assuming they hear about it) they will end up on Nexuiz.com and that will be all console stuff.
    Mar 05 12:33:46    I don't think so
    Mar 05 12:34:09    I was repying to merlijn 
    Mar 05 12:34:18     i do.. or at least that tiiiiiny 'pc nexuiz' link currently on is a bad sign..
    Mar 05 12:34:53    tiny and gray 
    Mar 05 12:35:06   aww tZork 
    Mar 05 12:35:07    unimportant
    Mar 05 12:35:18    very importand 
    Mar 05 12:35:25 <}-z-{> really hate that redmin crosses out my name
    Mar 05 12:35:32    also bottom right corner is worst place on website 
    Mar 05 12:35:39 <}-z-{> anyway, Dokujisan http://dev.xonotic.org/projects/notnexuiz/wiki/Plan updated
    Mar 05 12:35:44 <}-z-{> now wiki styled
    Mar 05 12:35:53  awesome
    Mar 05 12:36:05 *   CuBe0wL requests login
    Mar 05 12:36:10 <}-z-{> CuBe0wL: register ;)
    Mar 05 12:36:16 <}-z-{> I will approve you
    Mar 05 12:36:27 <}-z-{> that goes for everyone
    Mar 05 12:36:33    hmm, I see some people in that list that I didn't even know were part of the nexuiz community
    Mar 05 12:36:39 <}-z-{> this site will migrate to the official one when we determine a name and register a domain
    Mar 05 12:36:40    like jayvee
    Mar 05 12:36:43  so basically "our nexuiz" is left to be an asterisk next to the big "Nexiuz" that now has a marketing budget with a for-profit company behind it
    Mar 05 12:36:59  we would be competing for attention
    Mar 05 12:37:02  without the nexuiz.com domain
    Mar 05 12:37:03  mand1nga: messy still, but i still havent built it all yet. when its done it will be a compleat pub with beer pump and all. and homemade beer, wich is what im testing now =)
    Mar 05 12:37:06 <}-z-{> "a link back to the gpl nexuiz will remain on our website FOR MARKETING PURPOSES"
    Mar 05 12:37:12 <}-z-{> is what illfonic said
    Mar 05 12:37:26 <}-z-{> I think that summarizes their view of our game
    Mar 05 12:37:34     maybe they meant for marketing of gpl nexuiz?
    Mar 05 12:37:40 <}-z-{> ;o) maybe
    Mar 05 12:37:47    im sure they did :P
    Mar 05 12:38:02     still, i think vermeulen screwed up pretty hard by his overscretcy..
    Mar 05 12:38:09     too much bad blood already
    Mar 05 12:38:20  with this new fork, we'll NEVER be in a position like this again
    Mar 05 12:38:25  ever
    Mar 05 12:38:27   tZork: that's amazing :)
    Mar 05 12:38:27 <}-z-{> yes and hasn't worked hard enough to fix it
    Mar 05 12:38:40 <}-z-{> he seems to be spreading lies about some things too
    Mar 05 12:38:50 <}-z-{> claimed to have run a fundraiser for div0???
    Mar 05 12:38:55 <}-z-{> wtf, I never heard of that and neither did div0
    Mar 05 12:39:34  agreed esteel, if this had been done with.. hell even just a polite tone it would never got this offensive.
    Mar 05 12:39:34     }-z-{: well to be fair i can imagine he is pretty busy atm.. still, it should have been better
    Mar 05 12:40:02    who cares if he is busy ? he got paid to do it
    Mar 05 12:40:22   its a bloody vampire
    Mar 05 12:40:35 <}-z-{> alright, I need to grab some lunch
    Mar 05 12:40:36  "to bzy to stand in line; shot the otehrs before me" 
    Mar 05 12:40:37 <}-z-{> bbl
    Mar 05 12:40:45  dont think the law will accept that
    Mar 05 12:40:51 <}-z-{> vermeulen doesn't seem like the type to fall on his sword
    Mar 05 12:40:59     tZork: hehe
    Mar 05 12:41:01 <}-z-{> but rather throw his team under the bus
    Mar 05 12:41:49     btw, have registered..
    Mar 05 12:42:06    tZork, once you have something edible, tell me :) I'll pay for the shipment price, but I want to taste your b33r :D
    Mar 05 12:42:16    but speaking of legal matters - the fork has to be GPL and nobody is stopping anyone from merging our code into the old nexuiz
    Mar 05 12:42:31    I just hope it's not made the way the sweet lemanode is made in shut up woman, get on my horse ;)
    Mar 05 12:42:49  CuBe0wL: its quite ok acctualy, but a bti thin this time. still learning =)
    Mar 05 12:42:51    merlijn, so?
    Mar 05 12:42:52  merlijn: they are supposedly dealing with that. I think they are only using DP code and not Nexuiz code, or not very much Nexuiz game code? Something like that.
    Mar 05 12:43:22    what if Vermeulen wants to keep "his" nexuiz alive and imports our changes?
    Mar 05 12:43:22  and LH made it seem like they were dealing with the permission aspect of relicensing contributed code
    Mar 05 12:43:23  no Dokujisan
    Mar 05 12:43:39  tZork: they are using game code?
    Mar 05 12:43:39  if we want to release fast we basicaly have to use nexuiz gamecode
    Mar 05 12:43:48  oh they
    Mar 05 12:43:49  oh I don't mean us. I meant illfonic
    Mar 05 12:43:52  as in ill*
    Mar 05 12:44:01  tehy use nexuiz gamecode too
    Mar 05 12:44:05  afaik
    Mar 05 12:44:05  I see
    Mar 05 12:44:16  or well tehy do
    Mar 05 12:44:19  lh said so
    Mar 05 12:44:58    merlijn, then we will let ppl know about it on slashdot and gain free marketing 
    Mar 05 12:45:11  with some unusual elements ripped out, liek my turrets.
    Mar 05 12:45:17    also, since we're reorganizing stuff - can we PLEASE have mailing lists?
    Mar 05 12:45:27  Does anyone here want to collaborate with Dublpaws to give "dance" a makeover?
    Mar 05 12:45:34  FruitieX: ?
    Mar 05 12:45:40    to be back ontopic with the name: I think the best would be to let the original Nexuiz community (or at least the part that follwos us) to decide about the name of the new project. this would mean it's truly "ours", it's the community's project. The best would be to make a list we put together, and let the masses decide about the name
    Mar 05 12:45:57  we can't make the name choice public
    Mar 05 12:46:04    why?
    Mar 05 12:46:04  people will grab domains faster than we can blink
    Mar 05 12:46:11   merlijn: that is an interesting idea
    Mar 05 12:46:13    I see
    Mar 05 12:46:19  unfortunatly Dokujisan is right
    Mar 05 12:46:32    technical aspect, I understand
    Mar 05 12:46:33  we need to make sure we solidify our decision AND make sure we have the domains we need (and IRC channels or whatever) before announcing
    Mar 05 12:46:36   Dokujisan: I could
    Mar 05 12:46:43   never really played the map much though
    Mar 05 12:46:52  n00b!
    Mar 05 12:46:52  FruitieX: it's pretty popular on my HOCTF server
    Mar 05 12:46:55  ;)
    Mar 05 12:47:07   yep i know
    Mar 05 12:47:11   what, n00b? :P
    Mar 05 12:47:15   only played pickup duels ;)
    Mar 05 12:47:16  its a decent map
    Mar 05 12:47:18   and tdm/ctf
    Mar 05 12:47:26  see? noob! :D
    Mar 05 12:47:30 *   merlijn votes for kicking FruitieX for not knowing every square qu of dance by heart
    Mar 05 12:47:31    :D
    Mar 05 12:47:39   :)
    Mar 05 12:47:42  haha
    Mar 05 12:47:49    umm... I don't know the map either :D
    Mar 05 12:47:53    at least not by name
    Mar 05 12:48:10    sure I'd recognise it form a screenshot
    Mar 05 12:48:17  http://rm.endoftheinternet.org/~nexuiz/maps/mapshots/dance.jpg
    Mar 05 12:48:22   but in pickup ctf, they only play runningmanctf, castle, mikectf2/3, facing, greatwall
    Mar 05 12:48:25   :P
    Mar 05 12:48:29    oh yes
    Mar 05 12:48:33 <}-z-{> esteel and Morphed, you've been approved on teh dev system
    Mar 05 12:48:34    how do I hate it :D
    Mar 05 12:48:38  FruitieX: sadly yes
    Mar 05 12:48:41   dance is fun :)
    Mar 05 12:48:48   }-z-{: you can add me too if you want
    Mar 05 12:48:53 <}-z-{> mand1nga: you have to sign up
    Mar 05 12:48:56 <}-z-{> I activate the accounts
    Mar 05 12:48:58   seems like a fun project to remake
    Mar 05 12:48:58  FruitieX: not bad maps, but its so limited
    Mar 05 12:49:00   okay
    Mar 05 12:49:03  FruitieX: can you join #nexuiz.nct on quakenet? I'm inviting dublpaws there
    Mar 05 12:49:05   indeed tZork 
    Mar 05 12:49:22 <}-z-{> Dokujisan: I will give you ssh to the redmine server after we decide on the name and go forward for real
    Mar 05 12:49:26   can you invite him to #nexuiz.editing instead? :P
    Mar 05 12:49:36 *   CuBe0wL registered too
    Mar 05 12:49:42 <}-z-{> I don't imagine you'll need it for much but it's a "just in case" sort of thing
    Mar 05 12:49:49 <}-z-{> I should be able to handle maintainence and backups
    Mar 05 12:50:16 *   CuBe0wL gives channel operator status to esteel mand1nga merlijn pavlvs
    Mar 05 12:50:16 *   CuBe0wL gives channel operator status to Taoki
    Mar 05 12:50:22 <}-z-{> mand1nga: CuBe0wL, you'd been activated
    Mar 05 12:50:29    again if you need server capacity, I can easily plug in a bunch of servers at work
    Mar 05 12:50:34    is this btw. the full "developer" group ?
    Mar 05 12:50:36 *   FruitieX registered three
    Mar 05 12:50:41 <}-z-{> CuBe0wL: not yet I don't think
    Mar 05 12:50:44   ty zee
    Mar 05 12:50:45 <}-z-{> please check the wiki page
    Mar 05 12:50:46   not yet
    Mar 05 12:50:50   e.g. MrBougo missing
    Mar 05 12:50:56 <}-z-{> merlijn: that's good to know, we will keep that in mind
    Mar 05 12:51:02   well i think :p
    Mar 05 12:51:03     hmm, ill need new domain too.. planetXYZ.de :P
    Mar 05 12:51:16  hm reg where? 
    Mar 05 12:51:30 <}-z-{> http://dev.xonotic.org is the temp development site for us to get organized at
    Mar 05 12:51:34    Application error
    Mar 05 12:51:34    Rails application failed to start properly :D
    Mar 05 12:51:38    we'd actually have to hijack lots of nexuiz domains and forward that to the new game :P
    Mar 05 12:51:41 <}-z-{> where? CuBe0wL ?
    Mar 05 12:51:48    http://dev.xonotic.org/my/page
    Mar 05 12:51:56 <}-z-{> works for me
    Mar 05 12:51:57 <}-z-{> refresh
    Mar 05 12:52:01  urlcatch totaly faild that. freeky.
    Mar 05 12:52:26   Invalid user or password
    Mar 05 12:52:27   gah
    Mar 05 12:52:31   just registered
    Mar 05 12:52:36   do you have to approve it?
    Mar 05 12:52:40     merlijn: like which domains?
    Mar 05 12:53:01    esteel: well your planetnexuiz.de for example :P
    Mar 05 12:53:45    there needs to be a way for people that search for nexuiz to find the forked game
    Mar 05 12:54:20   indeed
    Mar 05 12:54:31   DCC delight are luckers :]
    Mar 05 12:54:41   Nexrun might need to change name too
    Mar 05 12:54:56   and the Nex weapon
    Mar 05 12:55:02   :p
    Mar 05 12:55:06    just delete the nex
    Mar 05 12:55:08    :P
    Mar 05 12:55:11   +1
    Mar 05 12:55:15     FruitieX: do you mean the mod? maybe a general mode-name like "runners" would be good?
    Mar 05 12:55:41    }-z-{, Nexuiz Admins wuzzat ?
    Mar 05 12:55:49    you mean server admins ?
    Mar 05 12:55:55   some flag textures will need to change
    Mar 05 12:55:57 <}-z-{> Dokujisan: will have to clarify
    Mar 05 12:56:11 <}-z-{> Dokujisan: I just aded some server resources if you want to expand on them
    Mar 05 12:56:14 <}-z-{> I'm going to lunch for real now
    Mar 05 12:56:15 <}-z-{> bbiab
    Mar 05 12:56:41    NEx = Tiuffgun
    Mar 05 12:56:45     :PP
    Mar 05 12:56:57     i see you want your sounds mods to be default..
    Mar 05 12:57:03    haha
    Mar 05 12:57:04  harr
    Mar 05 12:57:31     merlijn: well i can change that domain easily
    Mar 05 12:57:33    well, it could be an option to use roflsounds and roflgfx :D
    Mar 05 12:57:58  yes nexuiz admins meant nexuiz server admins
    Mar 05 12:58:02     in fact hyvin.de also points to it :P  i just learned to late that it was badly translated.. FruitieX woulud be able to tell :P
    Mar 05 12:58:22    Dokujisan, I'd like to keep my mod status too pls :D
    Mar 05 12:58:27   wtf is that
    Mar 05 12:58:28   :P
    Mar 05 12:58:49     FruitieX: should be 'good'  in english? no?
    Mar 05 12:58:50  CuBe0wL: ok
    Mar 05 12:58:54     or rather goodly..
    Mar 05 12:58:54    esteel, so can I keep my ftp too? :D
    Mar 05 12:59:00   yes or well
    Mar 05 12:59:07   good = hyvä
    Mar 05 12:59:20    haha
    Mar 05 12:59:21    epic
    Mar 05 12:59:25     CuBe0wL: yeah.. just not sure how long the old pn.de will be there then :P
    Mar 05 12:59:46    but I'll still be able to use it under a diffrent name?
    Mar 05 13:00:05     FruitieX: yeah, that what i found out too late.. i just asked google for 'good' in finnish.. said hyvin :P
    Mar 05 13:00:12     CuBe0wL: sure, why not?
    Mar 05 13:00:38    (just to mention, if you have ssh access to my home @ pn.de, you can read my thesis :D)
    Mar 05 13:00:51    but pls, don't steal or sell it :D
    Mar 05 13:00:57   is there any git support for redmine?
    Mar 05 13:01:15   can you invite him to #nexuiz.editing instead? :P
    Mar 05 13:01:21    CuBe0wL: is your thesis about which medicine can easily be turned into drugs?
    Mar 05 13:01:25  I don't think we want any discussion of a fork leaked by accident
    Mar 05 13:01:29    otherwise I'm probably not interested :P
    Mar 05 13:01:33  haha
    Mar 05 13:01:35    chances I'll be able to write an article, and it might published in  a medical journal
    Mar 05 13:01:39  I know #nexuiz.nct is a safe plcae to discuss mapping
    Mar 05 13:02:07  eh I just make sure he knows not to mention the fork
    Mar 05 13:02:08  ok
    Mar 05 13:02:10    merlijn, no, I've written my thesis in "Image analyzis in medicine technology"
    Mar 05 13:02:27     CuBe0wL: i'll offer your thesis to vermeulen :PPP harhar
    Mar 05 13:02:32    :D
    Mar 05 13:02:33  interesting subejct
    Mar 05 13:02:34    haha
    Mar 05 13:02:52    tZork, indeed
    Mar 05 13:03:43    in case we publish an abstract or the full article in english too, I'll handle you guys it to read if you want :)
    Mar 05 13:03:52     meh, tunnels and mobile internet to not like each other..
    Mar 05 13:04:00  im definitly interested =)
    Mar 05 13:04:19  bbiab, better get me some food 
    Mar 05 13:04:26    have a good one
    Mar 05 13:04:34   Dokujisan: oh okay
    Mar 05 13:04:36   coming
    Mar 05 13:04:37     enjoy tZork 
    Mar 05 13:04:43    where's MrBougo anyway?
    Mar 05 13:07:05    MrB usually isn't online all that much
    Mar 05 13:07:18   afaik he didn't like the idea of forking
    Mar 05 13:07:23   I told him about this channel yesterday
    Mar 05 13:07:23    Spaceman: you can probably run stats on when MrB is likely to appear :P
    Mar 05 13:08:21    to be fair, I don't fully like the idea of forking either
    Mar 05 13:08:51     yer
    Mar 05 13:08:58  I love it
    Mar 05 13:09:00    hmm?
    Mar 05 13:09:04  it's healthy medicine
    Mar 05 13:09:10    Vermeulen has now actually made some money on Nexuiz now, maybe he'd just let us take over and we can rename it anyway
    Mar 05 13:09:17    MrBougo is always online in #pb.nexuiz
    Mar 05 13:09:42  merlijn: what benefit does that give?
    Mar 05 13:10:12    Dokujisan: less troublesome than forking, plus I think that for now we can at least benefit from all the fuzz about nexuiz
    Mar 05 13:10:26    forking implies that BOTH projects move forward
    Mar 05 13:10:37    I don't think that is a good idea
    Mar 05 13:10:46     ++
    Mar 05 13:10:59    and even if they don't both move forward, the old nexuiz will still exist
    Mar 05 13:11:00  well the "troublesome" part, to me, is the good part, because that means overhauling and resetting, which will really help this project greatly.
    Mar 05 13:11:14    I'm not at all against that
    Mar 05 13:11:32   got to say I'm support doku here :)
    Mar 05 13:11:33    merlijn, well, all the major brainpower will move on this project
    Mar 05 13:11:36   I*
    Mar 05 13:11:40  and the buzz around this drama can benefit a fork, because problems in GPL projects always gain attention on digg/reddit/slashdot, etc
    Mar 05 13:11:48    CuBe0wL: is LH in on this?
    Mar 05 13:12:00    proly not
    Mar 05 13:12:05   afaik he is at least not against it
    Mar 05 13:12:05    at least not tha I know of
    Mar 05 13:12:27    what I was trying to say
    Mar 05 13:12:34    I think LH is the only one who can do certain things as he knows everything about the engine
    Mar 05 13:12:35    wo developers, Nexuiz will die
    Mar 05 13:12:46    but it's only the title
    Mar 05 13:13:02    it's not the name that makes Nexuiz to be Nexuiz
    Mar 05 13:13:13    it's the people who play and develope it
    Mar 05 13:13:19    I think we should only fork if we can't get what we want in the original nexuiz project - but from what I understand nobody has investigated that option
    Mar 05 13:13:20   merlijn: MrBougo's join time on a Friday is fairy random
    Mar 05 13:13:43  I think what we're doing with this fork is taking ALL of the good things about nexuiz and improving ALL of the bad things
    Mar 05 13:13:57  All of the good things about nexuiz is.. you guys
    Mar 05 13:14:03  and some others
    Mar 05 13:14:14    honored
    Mar 05 13:14:22   it would be nice to keep the nexuiz name
    Mar 05 13:14:42    it would be nice if fukcfonic would rename it's game
    Mar 05 13:14:54   that would be a lot better
    Mar 05 13:15:23    if that'd happen, I probably won't think the fork as a very good idea
    Mar 05 13:15:28  I still say I never really like the name "nexuiz" but I just grew to accept it :-)
    Mar 05 13:15:46   it's just a group of letters
    Mar 05 13:15:46    anyway, I'm going to do some other stuff now - just a small word of wisdom before I go: carefully evaluate your options before making hasty decisions
    Mar 05 13:15:53    but kehdrin or what's the guy's name said, they won't change it, period.
    Mar 05 13:15:59  I did like the 'n' symbol though. That was good.
    Mar 05 13:16:10    merlijn, we won't rush anything
    Mar 05 13:17:03  I mean, put simply, nexuiz was a sinking ship to me. I was on my way out
    Mar 05 13:17:11  but this changes everything
    Mar 05 13:17:36  I mean I was on my way out well before this illfonic mess
    Mar 05 13:23:26   by the way, this idea will be useful in our fork i think: http://www.youtube.com/watch?v=NotqttdZUoQ
    Mar 05 13:23:33   I'm very open for ideas now concerning that :)
    Mar 05 13:36:09     bbl, switching trains :P
    Mar 05 13:41:32 <}-z-{> Dokujisan: we need another community/project manager
    Mar 05 13:41:54     Hmm
    Mar 05 13:42:10 <}-z-{> is that a task you're interested in Samual?
    Mar 05 13:42:38     Meh
    Mar 05 13:42:41     People don't like me
    Mar 05 13:42:43     And i'm too lazy
    Mar 05 13:42:55    oh, one thing came to my mind, while I'm mapping right now: PLEASE GIVE THE RAILGUN IT'S OWN AMMO!!!
    Mar 05 13:43:04 <}-z-{> okay lol
    Mar 05 13:43:11     No :P I still don't like that idea CuBe0wL 
    Mar 05 13:43:11 <}-z-{> CuBe0wL: well that can be discuess for sure
    Mar 05 13:43:22     I'll still be doing the balance I think :P
    Mar 05 13:43:32 <}-z-{> okay
    Mar 05 13:43:39    RAGEQUIT!
    Mar 05 13:43:42 *   CuBe0wL (~akion@BKTFW13.usn.hu) has left #notnexuiz (Távozom)
    Mar 05 13:43:43     -.-
    Mar 05 13:43:47 *   CuBe0wL (~akion@BKTFW13.usn.hu) has joined #notnexuiz
    Mar 05 13:43:52    jsut kidding :D
    Mar 05 13:44:10    aww, I've lost me op :(
    Mar 05 13:44:28 *   }-z-{ gives channel operator status to CuBe0wL
    Mar 05 13:45:20 *   ProjektGhost (~raygalina@64.107.218.2) has joined #notnexuiz
    Mar 05 13:45:29   that's better
    Mar 05 13:45:31     Ghost: Keep quiet :P
    Mar 05 13:45:36   okay, fine
    Mar 05 13:45:39     He wants to suggest names
    Mar 05 13:45:40   anyway, new name
    Mar 05 13:45:49   Nexius
    Mar 05 13:45:52     -.-
    Mar 05 13:45:55   you get to correct the name now
    Mar 05 13:45:58   no, seriously
    Mar 05 13:46:06   it's close enough to be familiar, but still different
    Mar 05 13:46:09   it's perfect, IMO
    Mar 05 13:46:23     .com name is taken
    Mar 05 13:46:35     Plan A: .com name
    Mar 05 13:46:50     Plan B: Consider already taken .com names
    Mar 05 13:47:08     Plan C: multiple words in the name
    Mar 05 13:47:12     Plan D: .org name
    Mar 05 13:47:14     ^_^
    Mar 05 13:47:23    he?
    Mar 05 13:47:30     At least I think that's how Doku put it 
    Mar 05 13:47:41    what about the names we tried out from Japan?
    Mar 05 13:48:14   are they going to use the Nexuiz logo?
    Mar 05 13:48:21   the Chinese character for Strength?
    Mar 05 13:48:24    Illfonic?
    Mar 05 13:48:24     Probably not
    Mar 05 13:48:28     Oh
    Mar 05 13:48:30     IllFonic will
    Mar 05 13:48:35    they already do
    Mar 05 13:48:42   then call is Strenght, or a synonym
    Mar 05 13:50:47   "Kings of Valor" or something
    Mar 05 13:51:21   sounds too RPG-ish, though
    Mar 05 13:52:25 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-big-large-great.html http://www.tribalshapes.com/categories/kanji/kanji-blood.html http://www.tribalshapes.com/categories/kanji/kanji-chaos.html
    Mar 05 13:53:56 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-conquer-overcome.html http://www.tribalshapes.com/categories/kanji/kanji-fast.html
    Mar 05 13:54:48 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-friend.html
    Mar 05 13:55:28     strength ftw
    Mar 05 13:55:36   what about Zen
    Mar 05 13:55:40 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-good-luck.html http://www.tribalshapes.com/categories/kanji/kanji-group.html
    Mar 05 13:55:42   get the symbol for that
    Mar 05 13:55:43   =p
    Mar 05 13:55:44 <}-z-{> div didn't want to use zen
    Mar 05 13:55:49   lame
    Mar 05 13:58:00     http://www.tribalshapes.com/categories/kanji/kanji-ability-talent.html
    Mar 05 13:58:10     >.>
    Mar 05 13:58:20 <}-z-{> too complicated
    Mar 05 13:58:22 <}-z-{> it's 2 symbols
    Mar 05 13:58:26 <}-z-{> we only want 1
    Mar 05 13:58:29     lawl I know
    Mar 05 13:58:35     I was just pointing at the bottom one
    Mar 05 13:58:35 <}-z-{> group might be the best yet
    Mar 05 13:58:38     Because it's epic
    Mar 05 13:59:43 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-learning-studies-science.html
    Mar 05 13:59:47 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-loyalty-faithfulness.html
    Mar 05 14:00:11  good resource
    Mar 05 14:01:07  ok if that kanji for ability/talent is two characters, what does the first character by itself mean?
    Mar 05 14:01:36  that would be a good symbol for a name beginning with a T
    Mar 05 14:03:16 <}-z-{> I posted a t looking one
    Mar 05 14:03:47  for group
    Mar 05 14:03:49   tabellion, tabefaction 
    Mar 05 14:03:51 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-now-the-present.html
    Mar 05 14:04:07    http://www.tribalshapes.com/img/tattoos/friend.gif
    Mar 05 14:04:10    this is the best
    Mar 05 14:04:14    easy to write
    Mar 05 14:04:24 <}-z-{> http://www.tribalshapes.com/categories/kanji/kanji-people-nation.html
    Mar 05 14:04:35    and has a little resamblence to the original strenght logo
    Mar 05 14:04:55 <}-z-{> group is one of my favorites so far
    Mar 05 14:05:05    I like that kanji symbol of friend very much
    Mar 05 14:05:25    why group?
    Mar 05 14:05:39 <}-z-{> I has a nice feel to it and represens us being a group or community
    Mar 05 14:05:46    ok
    Mar 05 14:05:50 <}-z-{> easy to draw too
    Mar 05 14:06:09 <}-z-{> but friend is nice too
    Mar 05 14:06:16   btw, should we focus on a better singleplayer campaign too?
    Mar 05 14:06:23 <}-z-{> sure FruitieX 
    Mar 05 14:06:39   needs better story, possibly against monsters instead of bots
    Mar 05 14:06:45   hopefully at least :P
    Mar 05 14:07:46 <}-z-{> good K one > http://www.tribalshapes.com/categories/kanji/kanji-water.html
    Mar 05 14:08:24 <}-z-{> can you guys be sure to annotate wiki edits?
    Mar 05 14:10:51  k, I did for one
    Mar 05 14:10:54  I'll do it more
    Mar 05 14:12:34  }-z-{: there is a mumble server listing (php script) that I use on http://nullgaming.com/batcaves/
    Mar 05 14:12:53 <}-z-{> yes, remind me when we have wordpress mu running
    Mar 05 14:12:57  k
    Mar 05 14:13:05 <}-z-{> what are your feelings on buddy press?
    Mar 05 14:13:15 <}-z-{> do you prefer to use buddypress or mybb for forums?
    Mar 05 14:13:30  I've never looked at buddypress
    Mar 05 14:13:41 <}-z-{> buddy press might be too confusing for some
    Mar 05 14:13:53 <}-z-{> it's a wordpress mu wrapper
    Mar 05 14:13:57 <}-z-{> www.nexuizclans.com uses it
    Mar 05 14:16:21     tZork: what were you saying cool stuff about?
    Mar 05 14:16:33    }-z-{, do you have an nvidia card?
    Mar 05 14:16:41 <}-z-{> yes
    Mar 05 14:16:48    and you use two monitors, don't you?
    Mar 05 14:16:52 <}-z-{> correct
    Mar 05 14:17:03    ok, how do you start nexuiz on only one monitor?
    Mar 05 14:17:10    it auto streches for me to both
    Mar 05 14:17:22 <}-z-{> fullscreen 0
    Mar 05 14:17:23 <}-z-{> :-P
    Mar 05 14:17:28    bah
    Mar 05 14:17:33    no other way ?
    Mar 05 14:17:35 <}-z-{> I play in windowed mode
    Mar 05 14:17:35 <}-z-{> well
    Mar 05 14:17:40 <}-z-{> are you using twinview?
    Mar 05 14:17:43    yep
    Mar 05 14:18:15 <}-z-{> when I used to play fullscreen, I just defined my resolution and twinview handled it as I expected
    Mar 05 14:18:26 <}-z-{> it was like a psuedo fullscreen though
    Mar 05 14:18:35 <}-z-{> if you click off it, your panels will rise above it type thing
    Mar 05 14:18:51 <}-z-{> I couldn't specify my dimensions in the gui
    Mar 05 14:18:55 <}-z-{> had to do it in my autoexec
    Mar 05 14:18:57    well, it streches me to noth monitors, and I can't set the resolution to anything
    Mar 05 14:19:08 <}-z-{> autoexec :-P
    Mar 05 14:19:16    I have that in my autoexec
    Mar 05 14:19:25     FruitieX: im working on rigging obi's newest model :)
    Mar 05 14:19:29    but once I set the res, it's not accepted
    Mar 05 14:19:38 <}-z-{> did you do the cod_vid_width and height too?
    Mar 05 14:19:41 <}-z-{> con*
    Mar 05 14:20:00    umm.. wtf, con has it's own resolution? oO
    Mar 05 14:20:04    no btw :D
    Mar 05 14:20:05   DibTop: good :)
    Mar 05 14:20:15    k, that could have been the problem :D
    Mar 05 14:20:59 *   ProjektGhost (~raygalina@64.107.218.2) has left #notnexuiz
    Mar 05 14:21:05 <}-z-{> CuBe0wL: yeah it defines text size/shape too :-P
    Mar 05 14:25:37 <}-z-{> I wish flash didn't crash all the time
    Mar 05 14:26:00   FruitieX: im working on rigging obi's newest model :)
    Mar 05 14:26:01  :-o
    Mar 05 14:26:06 <}-z-{> nice
    Mar 05 14:26:21 DibTop div0 
    Mar 05 14:33:06   DibTop: earlier in #nexuiz lda17h wanted some info about nexuiz animations, he wants to modify some of nexuiz anims
    Mar 05 14:33:26   FruitieX: can you remove the border from the HUD elements?
    Mar 05 14:34:39   yes you can
    Mar 05 14:34:50   you can also make it look just the way you want with skins ala menu :)
    Mar 05 14:34:58     [14:19:26pm]  well, it streches me to noth monitors, and I can't set the resolution to anything
    Mar 05 14:34:59     lawl
    Mar 05 14:35:00   make the border as thick you want even (per-panel setting)
    Mar 05 14:35:05     Mine stretches to all three monitors
    Mar 05 14:35:10     5760x1200
    Mar 05 14:35:13     I just have to deal with it
    Mar 05 14:35:16     -.-
    Mar 05 14:35:18 <}-z-{> http://ie6funeral.com/
    Mar 05 14:35:35  on a side note, can someone help me test a website? Go here and scroll to the bottom and post a few symbols like... euro and pound sterling and maybe some other common characters used in europe. User name= testuser1  password=9999
    Mar 05 14:35:59  or any other characters you want to try
    Mar 05 14:36:12 <}-z-{> do we guess the url? :-P
    Mar 05 14:36:17   go where?
    Mar 05 14:36:24  hang on...
    Mar 05 14:36:33  http://message.axkickboxing.com/newdesign/index.phtml?action=dispthread&topic=29479
    Mar 05 14:36:45 <}-z-{> ahh, still having issues with that
    Mar 05 14:36:56  well I converted the database to UTF-8 yesterday. 
    Mar 05 14:37:00 <}-z-{> ahh
    Mar 05 14:37:03  made a copy and converted that, rather
    Mar 05 14:37:05 <}-z-{> damn, how long did that take?
    Mar 05 14:37:13  but I am still learning about character encoding
    Mar 05 14:37:46  I need to make sure someone from europe, with whatever keyboard layout they might use, can enter characters and it will show up properly
    Mar 05 14:37:56  the only thing I can do is copy/paste
    Mar 05 14:38:17 <}-z-{> I can type chinese
    Mar 05 14:38:19 <}-z-{> :-P
    Mar 05 14:38:31  ah yeah I can type japanese if i install the keyboard utility
    Mar 05 14:38:33  forgot about that
    Mar 05 14:38:57  the database dump file is 1.2GB or so
    Mar 05 14:39:28  and it took just a few minutes to do each step... export / conversion / import
    Mar 05 14:39:30 <}-z-{> 打开哦开发似的卡0
    Mar 05 14:39:43 <}-z-{> yeah, I'd imagine it'd be big
    Mar 05 14:40:07 <}-z-{> Your message could not be posted because the password you submitted was wrong.
    Mar 05 14:40:13  ok hang on
    Mar 05 14:40:27  testuser1
    Mar 05 14:40:29  9999
    Mar 05 14:40:42 <}-z-{> yep, still getting that error
    Mar 05 14:40:44  case sensitive names
    Mar 05 14:41:31  hmmm ok it failed for me too. Let me get that figured out
    Mar 05 14:41:43 <}-z-{> :
    Mar 05 14:41:46 <}-z-{> oooh noes
    Mar 05 14:41:57 <}-z-{> the chinese messed up my irsii lol
    Mar 05 14:42:04 <}-z-{> okay, all better
    Mar 05 14:42:07 <}-z-{> that was whacky
    Mar 05 14:42:45 <}-z-{> oh hey, do we have any reviews of other projects workflows?
    Mar 05 14:42:54 <}-z-{> such as warsow and tremulous?
    Mar 05 14:43:13 <}-z-{> is warsow development even open?
    Mar 05 14:45:04  }-z-{: ok try login:testuser1 pw:4781
    Mar 05 14:45:07  er testuser2
    Mar 05 14:45:27 <}-z-{> posted chinese okay
    Mar 05 14:45:58  can someone here from Europe post some euro characters?
    Mar 05 14:46:10   i'm trying
    Mar 05 14:46:42 <}-z-{> I don't see how warsow's development is public
    Mar 05 14:47:41   the euro's look good ?
    Mar 05 14:48:38  haha what the hell
    Mar 05 14:48:45    and Z҉A҉L҉G҉O̚̕̚ too
    Mar 05 14:48:50  lol
    Mar 05 14:48:53 <}-z-{> lol
    Mar 05 14:48:55  who posted that?
    Mar 05 14:48:58 <}-z-{> CuBe0wL: 
    Mar 05 14:49:01 <}-z-{> I'm guessing :-P
    Mar 05 14:49:06 <}-z-{> cryllic millions
    Mar 05 14:49:13  crazy :-)
    Mar 05 14:49:16  ok just a second guys
    Mar 05 14:49:21  we're gonna do a comparison
    Mar 05 14:49:22    Z҉A҉L҉G҉O̚̕̚ !!!
    Mar 05 14:49:38  http://message.axkickboxing.com/index.phtml?action=dispthread&topic=29479
    Mar 05 14:49:39    H̡́͝E ̨W̢̛H̡̧O͟͏ W̧A̵̡͘I̷̢͜TS͘͟ ̢́BE̛͝H̡͜I͏̨N͡D҉̨ ̀T̵H̸́E ̨W͏͢AL̴͠L͜!̸͟͞!̶!́
    Mar 05 14:49:41  do the same on that address
    Mar 05 14:49:57  it's the same topic on another set of PHP and another database
    Mar 05 14:49:58 <}-z-{> ಠ_ಠ
    Mar 05 14:50:02 <}-z-{> http://en.wikipedia.org/wiki/Combining_Cyrillic_Millions
    Mar 05 14:50:09  same username + password
    Mar 05 14:50:29  and I fugured it why testuser1 didn't work. It's a different database >.<
    Mar 05 14:50:54 <}-z-{> :-P
    Mar 05 14:51:18 <}-z-{> for the wiki, are we good with the dev wiki or do we want one that is part of the user site as well?
    Mar 05 14:52:16  we could use both, probably
    Mar 05 14:52:30  dev wiki might have some notes related to...development
    Mar 05 14:52:46  the other wiki would be more like OUNS was
    Mar 05 14:53:29  CuBe0wL: so zalgo didn't work that time?
    Mar 05 14:53:59    sure it Z҉A҉L҉G҉O̚̕
    Mar 05 14:54:27  oh I see the issue. When the encoding is switched to utf8 in the HTML, that is when that breaks
    Mar 05 14:54:29  ok
    Mar 05 14:54:30 <}-z-{> okay, so the next question is, how intense of a wiki do we need, do you think we can get away with a wp plugin for starters?
    Mar 05 14:54:31    Z̵̴̡̬͚̘̗̯͓A͏͇L͇̜̩͜G̙̳͚̹̰̣̖͢͝O̭̦͢ ̲̗̗̀Z̮̬̹A̢̨͖̱͙͔L͖̖͙̘̣̤͘G̴̢͖̲̭O̖͈̺̻̻̖͎̻͟ ͚͓̯͙̱Z̘̯̗̖̩A͏͎̣͡L̢̬̭̀G̗̞̼͔O̫̺̯̖̹͠ ̦̟̜͉̟͉̀I̗̫̪L̞̯͖̫͢͝L̴̙̮͉͔͟͠F̪̗̱̩͓̻͕̞̘̀̕͡O͇̺̗̤̘̘̳͍N̡͔̖̻̰͙I̹̦͕͇̖͢Ç̩̘̺̜͉ ̪̦̭̻̤̻Z̥̹̝͔Ą̵͍̰L̷̻̥̗̮̳̫̟̞G̢̨̯͓͠O͏̸̹̳̤̣̼͉͉̪̟̠Z̵̴̡̬͚̘̗̯͓A͏͇L͇̜̩͜G̙̳͚͢͝
    Mar 05 14:54:31    ̹̰̣̖O̭̦͢ ̲̗̗̀s. ̕҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉Z ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉ ̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̚̕̕̚̕̚͡ ALGO ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉ ̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̚̕̕̚̕̚͡ ͡҉҉grows. ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓
    Mar 05 14:54:32    ̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̕̚̕̚͡ ̒̓̔̕̚ZAL҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̕̚̕̚͡ ̒̓̔̕̚GO commeth.
    Mar 05 14:54:45  then the test passed! The new site with the new database seems to work 
    Mar 05 14:55:32    Dokujisan, well, I can see   Z҉A҉L҉G҉O̚̕ on both pages (he is still H҉̵̞̟̠̖̗̘Ȅ̐̑̒̚̕̚ IS C̒̓̔̿̿̿̕̚̚̕̚̕̚̕̚̕̚̕̚OMI҉̵̞̟̠̖̗̘NG > ͡҉҉ ̵̡̢̛̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̿̿̿̚ ҉ ҉҉̡̢̡̢̛̛̖̗̘̙̜̝̞̟̠̖̗̘̙̜̝̞̟̠̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑ ͡҉҉ )
    Mar 05 14:55:49  CuBe0wL: yes but change the character encoding of the second one to UTF8
    Mar 05 14:55:49 <}-z-{> I'd like to propose we use this for future documentation of the project: http://www.methods.co.nz/asciidoc/
    Mar 05 14:55:52  in your browser
    Mar 05 14:55:58     CuBe0wL, O.o
    Mar 05 14:56:04  CuBe0wL: it should break after that
    Mar 05 14:56:08    Samual?
    Mar 05 14:57:27     Font is fun ^_^
    Mar 05 14:59:08    http://www.zalgo.org/wp-content/gallery/zalgo/1237835262258.jpg
    Mar 05 14:59:19 <}-z-{> this is used: http://www.methods.co.nz/asciidoc/asciidoc.txt
    Mar 05 14:59:25 <}-z-{> to generate this: http://www.methods.co.nz/asciidoc/asciidoc.css-embedded.html
    Mar 05 15:00:01  and the other thing that works is the search. I can search for '£'
    Mar 05 15:00:03  on the new site
    Mar 05 15:00:16 <}-z-{> Dokujisan: have we thought of anyone who can help with documentation?
    Mar 05 15:00:23 <}-z-{> shaggy maybe still interested?
    Mar 05 15:00:30  }-z-{: we need a serious discussion for that topic, certainly
    Mar 05 15:00:36  it will be hard to recruit for that
    Mar 05 15:00:39  but I think it's possible
    Mar 05 15:00:43 <}-z-{> yeah
    Mar 05 15:01:01 <}-z-{> I think this is something we can streamline with the build system too
    Mar 05 15:01:12  anyway thanks for helpign to test that, CuBe0wL, Spaceman and -z-
    Mar 05 15:01:38 <}-z-{> so even the nightly builds on the test server, we can provide up-to-date documentation in HTML form if needed (for example)
    Mar 05 15:01:47  wow -z-
    Mar 05 15:01:49 <}-z-{> obviously the other thing I want to get going is a nightly cvar/cmd list searcher
    Mar 05 15:01:50  how does that work?
    Mar 05 15:02:04 <}-z-{> with the asciidoc tool
    Mar 05 15:02:05 <}-z-{> http://www.methods.co.nz/asciidoc/asciidoc.txt
    Mar 05 15:02:08 <}-z-{> http://www.methods.co.nz/asciidoc/
    Mar 05 15:04:11    it seems LH is online
    Mar 05 15:04:20    does he know about this palce?
    Mar 05 15:05:12     Probably not
    Mar 05 15:05:24     Do we WANT him to know?
    Mar 05 15:05:27 <}-z-{> no
    Mar 05 15:05:29 <}-z-{> at least not yet
    Mar 05 15:05:32 <}-z-{> he was in on the deal
    Mar 05 15:05:39     Indeed
    Mar 05 15:05:57 <}-z-{> he more or less let the community get hurt for his own good.
    Mar 05 15:07:28    I still think he should know about it... just for the reason, he's the only DP coder
    Mar 05 15:07:56    what will we do with the engine, if we can't solve a problem, and he's not interested in forked Nexuiz at all?
    Mar 05 15:08:18 <}-z-{> will that really be the case though?
    Mar 05 15:08:42 <}-z-{> I just think at this point telling him might do more harm than good
    Mar 05 15:09:44    I certainly won't tell, I don't think it's my job
    Mar 05 15:09:55    I was just wondering, ya know
    Mar 05 15:10:02 <}-z-{> I think div0 really has the voice on this decision
    Mar 05 15:10:11    div0, 
    Mar 05 15:10:14    we summon you
    Mar 05 15:10:26 <}-z-{> btw, willis has informed me that for the past month or so nexuiz.com was a 301 redirect so alientrap.org/nexuiz
    Mar 05 15:10:29    man, this will take ages like this :(
    Mar 05 15:11:11 <}-z-{> ages like what?
    Mar 05 15:11:29    btw. it's interesting to note, that Vermeulen still hasn't sold nexuiz.com
    Mar 05 15:11:36    he just let Illfonic to use it
    Mar 05 15:11:41    but he still owns it
    Mar 05 15:11:43    what for?
    Mar 05 15:11:47 <}-z-{> yeah but he made a shitty deal with them
    Mar 05 15:12:05 <}-z-{> could have gotten our project more space on the homepage as part of the deal
    Mar 05 15:12:23    and a difference in name of Illfonics side
    Mar 05 15:12:24 <}-z-{> 301 means that search engines have been indexing alientra.org/nexuiz for the past month, not nexuiz.com
    Mar 05 15:13:09    lol, I've just realised what kedhrin said by "But, I am not going to put my team in here to defend themselves and our company decisions."
    Mar 05 15:13:31    he took it a total insult that I've invited his men to join our conversation
    Mar 05 15:14:08    what an elitist fucktard... how do people sink that low?
    Mar 05 15:14:45 <}-z-{> "The GPL Nexuiz is still linked on this web-site. This is necessary for the commercial marketing of the project."
    Mar 05 15:15:01 <}-z-{> that one still gets me the most
    Mar 05 15:16:47    I still don't know if I should write the whole scandal to hup.hu or not
    Mar 05 15:16:52 <}-z-{> zeniux still sticks out in my head
    Mar 05 15:17:07 <}-z-{> Dokujisan: can you put that names list on the wiki?
    Mar 05 15:17:34  yeah
    Mar 05 15:18:11    don't forget Pheonix and Itoma
    Mar 05 15:18:21 <}-z-{> don't really like either of those to be honest
    Mar 05 15:18:58    hmmm
    Mar 05 15:19:15    I've just realised zeniux has the same letters as Nexuiz
    Mar 05 15:19:20    just scrambled
    Mar 05 15:19:23 <}-z-{> yes
    Mar 05 15:19:32    but I don't like the sound of it
    Mar 05 15:19:33  }-z-{: how do you add a new page to this wiki o_O
    Mar 05 15:19:43    create new page link? :P
    Mar 05 15:19:53  I don't see it
    Mar 05 15:20:17  I see "new file" where I can attach a file
    Mar 05 15:21:41 <}-z-{> just go to the url
    Mar 05 15:21:45 <}-z-{> or create a link in an existing page
    Mar 05 15:21:54 <}-z-{> [click me for new page](my_new_page)
    Mar 05 15:23:02    shouldn't we hide this channel? 
    Mar 05 15:23:14 <}-z-{> isn't it p?
    Mar 05 15:23:16 <}-z-{> omg it was
    Mar 05 15:23:18    iirc alientrap-dev was hidden too for  a time
    Mar 05 15:23:27 *   }-z-{ sets mode +p #notnexuiz
    Mar 05 15:23:33    well, I can see the channel if I whois myself
    Mar 05 15:23:34 <}-z-{> or did I want +s?
    Mar 05 15:23:42 <}-z-{> oh it is s
    Mar 05 15:24:14 *   }-z-{ sets mode -p #notnexuiz
    Mar 05 15:24:23  it seems to still be +s
    Mar 05 15:24:29 <}-z-{> yes, +p is deprecated
    Mar 05 15:24:33 <}-z-{> +s is what we want
    Mar 05 15:26:39  testing dance_beta1 on bc1
    Mar 05 15:28:58    heh... Fri Mar 05, 2010 9:14 am last visit from Kedhrin on the AT forum
    Mar 05 15:30:44 <}-z-{> maybe we should consider setting up an etherpad for the project as well
    Mar 05 15:36:02 <}-z-{> just as a little tool we can offer on the site
    Mar 05 15:37:51  CuBe0wL: can you check out dance on bc1?
    Mar 05 15:45:07    Dokujisan, umm... sure
    Mar 05 15:45:23  nullgaming.com:26001
    Mar 05 15:45:49    }-z-{, how'd you say in english that .. hmm... somebody tells you good news without hiding the real intention behind it, but that's actually the opposite?
    Mar 05 15:46:08    or by telling you that it'll be good for you, but in the end you'll recieve nothing?
    Mar 05 15:46:08 <}-z-{> vested interest?
    Mar 05 15:47:03    I'm trying to tell LordHavoc what Illfonic tries to do with us by dropping half truths, and giving promises full of "maybe"'s
    Mar 05 15:47:16    but in the end, I'm certain we won't gain anything
    Mar 05 15:47:37 <}-z-{> I mean, I can see their point... but it also defeats the purpose of what I thought our project was
    Mar 05 15:48:30 <}-z-{> 'hustle' is another word you might be looking for
    Mar 05 15:48:44 <}-z-{> Hustle may mean: work a scam, intentionally "mis-direct" someone to achieve a personal gain from that person being mis-directed. The hustle, or scam, is usually performed in a fast paced environment as does not allow time to reflect on all options available to the victim, and usually plays on the greed or kindness of people and has an element of chance, although tipped overly into the favor of the "hustler", which is in proportion to how the hustlee views
    Mar 05 15:49:29    holding out a carrot with sy
    Mar 05 15:49:35    that was what I searched for
    Mar 05 15:50:34 <}-z-{> ah
    Mar 05 15:51:01    they behave as some mega corporation or some important politician
    Mar 05 15:53:33 <}-z-{> CuBe0wL: the reason you can see the channel if your own whois is because you are joined in the channel
    Mar 05 15:53:38 <}-z-{> if you leave and whois me, you will not see it
    Mar 05 15:53:40    I see
    Mar 05 15:54:10    I've gone into an open conversation with LH on the topic of the Future of the two games
    Mar 05 15:54:18    I wonder how he'll respond
    Mar 05 15:54:54    one zillion nexuiz credits he'll start referring to NDA's and other papers ha had to sign, so he can't tell anything
    Mar 05 15:55:25 <}-z-{> :-P
    Mar 05 15:56:50     One billion internets
    Mar 05 16:09:23    omfg, I still can't believe how devoted some guys are towards Nexuiz :)
    Mar 05 16:09:41    after all this hassle, I thougt everybody will stop developing for just a few days
    Mar 05 16:09:47    FruitieX, you're a hero :D
    Mar 05 16:10:26    gotta check the commit logs for others too
    Mar 05 16:11:33   wohoo an hero
    Mar 05 16:11:43     an hero?
    Mar 05 16:11:52     No "an hero" is committing suicide
    Mar 05 16:11:52   yes
    Mar 05 16:11:54     Don't an hero
    Mar 05 16:12:02     ^_^
    Mar 05 16:12:20     Go to urban dictionary if you don't believe me
    Mar 05 16:12:40   I do believe you.
    Mar 05 16:14:40   why is he aN hero?
    Mar 05 16:15:33   nvm :)
    Mar 05 16:16:25   maybe i'm a NaN hero :)
    Mar 05 16:16:43    you're gathering another tactical facepalm :D
    Mar 05 16:18:30   darn, didn't quite manage to get a tactical DOUBLE facepalm :D
    Mar 05 16:26:04 <}-z-{> lol a NaN hero
    Mar 05 16:36:53 <}-z-{> Dokujisan: names list?
    Mar 05 16:38:46 DibTop div0 
    Mar 05 16:38:47  wow...  DibTop 
    Mar 05 16:38:58  I just threw the last version of dance_enclosed on hoctf to test
    Mar 05 16:39:00  and people liked it
    Mar 05 16:39:20  they bitched immediately of course, but after about 3 mintues of gameplay, people started liking it
    Mar 05 16:39:45    as always :)
    Mar 05 16:40:04  after the match, I asked players to rate it, most rated it 7
    Mar 05 16:40:07  out of 10
    Mar 05 16:40:07    huh... I've just looked back at the 4 years I've had with Nexuiz
    Mar 05 16:40:12    4...
    Mar 05 16:40:17  :-)
    Mar 05 16:40:18    that can't be correct
    Mar 05 16:40:29  i thikn I've been here more than 3
    Mar 05 16:40:29    it's my 6th year at the uni
    Mar 05 16:40:57    and I remember I was playing Nexuiz when I started it
    Mar 05 16:41:12    and I was away too for a half year or so
    Mar 05 16:41:33    because I was pissed that they've changed to push force of the laser :D
    Mar 05 16:41:37 <}-z-{> Dokujisan: names list?
    Mar 05 16:42:20    looking back this far, I feel far more heartbroken we need to fork, or just generally stop playing at all
    Mar 05 16:42:43 *   mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 16:42:52 <}-z-{> 21:31:11 < motorsep> now I am wondering if guys will suck it up and continue with Nexuiz or start new project
    Mar 05 16:42:55 <}-z-{> 21:34:43 < }-z-{> I guess a lot of that depends on how Vermeulen goes about fixing this mess and earning back respect of some of the most influential contributors
    Mar 05 16:42:59 <}-z-{> 21:42:18 < Vermeulen> like i said before, there are certain developers I do need to discuss with and basically apologize for mishandling a number of things
    Mar 05 16:43:02 <}-z-{> 21:42:30 < Vermeulen> but when it comes to the name and the issue community members are having with the change, that was a decision i made that i am fine with taking the wrath for
    Mar 05 16:43:07 <}-z-{> 42:49 < Vermeulen> I should have been more open with the plans but it was always the intention to fund further nexuiz development with these funds. I didn't plan before about promising to be open with the exact royalty split but I  think that'll be the best way to make up for the mishandlings on my part with developers
    Mar 05 16:43:47    it seems he has quite hard days too
    Mar 05 16:44:07    he changes his opinion on the topic day by day
    Mar 05 16:44:34    he is in the middle of a crossfire and wants to keep both parties happy
    Mar 05 16:44:55 <}-z-{> he created the crossfire
    Mar 05 16:45:22    sure, but we all make mistakes
    Mar 05 16:45:27  <}-z-{> Dokujisan: names list?
    Mar 05 16:45:32  I don't know how to create a page on that wiki
    Mar 05 16:45:37  I don't see the option
    Mar 05 16:45:54 <}-z-{> I told you two ways
    Mar 05 16:46:02 <}-z-{> extend the url ...wiki/my_new_page
    Mar 05 16:46:07 <}-z-{> or create a link on an existing page
    Mar 05 16:46:18 <}-z-{> [linking text](my_new_page)
    Mar 05 16:46:19  ok
    Mar 05 16:52:37  http://dev.xonotic.org/projects/notnexuiz/wiki/Names
    Mar 05 16:52:47 <}-z-{> noice
    Mar 05 16:54:18    }-z-{: I just signed up for the redmine thing, can you approve?
    Mar 05 16:54:25 <}-z-{> certainly
    Mar 05 16:54:45 <}-z-{> pavlvs too
    Mar 05 16:55:03     ty
    Mar 05 16:56:41 <}-z-{> added names list to the main wiki page
    Mar 05 16:59:25 <}-z-{> I'm leaving work now, ttyl
    Mar 05 17:13:50     evening..
    Mar 05 17:14:14   evening
    Mar 05 17:17:38     hi Spaceman ;)
    Mar 05 17:34:53 *   mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 17:35:12   man, we should set like a deadline
    Mar 05 17:35:16   once we get everything ready
    Mar 05 17:35:31   and leave every alientrap-related thing, like irc, forum, etc
    Mar 05 17:35:41   everyone at once
    Mar 05 17:35:55  hey guys... grasshoppers new map is looking really nice
    Mar 05 17:35:56  http://pics.nexuizninjaz.com/viewer.php?file=3336oqc2tvlt8p6tsna1.jpg
    Mar 05 17:35:56   it'd be fun :P
    Mar 05 17:36:13  he's putting a lot of emphasis on details with it
    Mar 05 17:36:53   haha yeah  mand1nga that would be interesting :-)
    Mar 05 17:39:45 *   [-z-] (~detrate@c-98-230-24-23.hsd1.fl.comcast.net) has joined #notnexuiz
    Mar 05 17:39:48   well there is no easy way of just leaving the forum, but maybe we all change our signatures the very same day, telling something about the cause
    Mar 05 17:40:36   it'd have a message and would be fun
    Mar 05 17:42:45 <}-z-{> I'm not usually malicious but it would be possible to add something to the theme, like a banner about vermeulen that says, "all your work are belong to me. I sell it for the $$$" and make it very hard to remove
    Mar 05 17:43:04 <}-z-{> but then again, it's probably just not worth it
    Mar 05 17:43:19 <}-z-{> he just doesn't seem to get how he's hurt people
    Mar 05 17:43:34 <}-z-{> he seems to act like it's all just going to blow over without him greasing the wheels at all
    Mar 05 17:43:58   its best to leave on amicable terms
    Mar 05 17:44:06   yes I perceive the same
    Mar 05 17:44:26 <[-z-]> yeah
    Mar 05 17:44:41   just because verm* has been underhanded doesn't mean anybody else has to be
    Mar 05 17:44:44   Spaceman: well, sure, leaving without saying a single word will have a really strong effect too imho
    Mar 05 17:45:04   that's a better method
    Mar 05 17:45:15 <[-z-]> there is still the power of the pen beyond that
    Mar 05 17:45:25 <[-z-]> it'd be better to let a 3rd party write about the situation
    Mar 05 17:45:30 <[-z-]> after it's all gone down
    Mar 05 17:45:32   can new nex copy the forum from alientrap?
    Mar 05 17:45:40 <[-z-]> I'd rather not
    Mar 05 17:45:53 <[-z-]> 1) it's huge, 2) it's phpbb, 3) then we'd just be stealing right back
    Mar 05 17:46:00   there is a lot of information there
    Mar 05 17:46:03   [-z-]: sure
    Mar 05 17:46:14     You don't like phpbb?
    Mar 05 17:46:17 <[-z-]> Spaceman: and we can port it all to the wiki
    Mar 05 17:46:27   I'm surprised this thing didn't reach /. yet
    Mar 05 17:46:30 <[-z-]> Samual: they don't even have function hooks
    Mar 05 17:46:36 <[-z-]> you have to hard mod your files
    Mar 05 17:46:42   maybe if individuals ask to transfer their posts
    Mar 05 17:46:52   but there would be lots of holes
    Mar 05 17:46:58     [17:46:02pm]  I'm surprised this thing didn't reach /. yet
    Mar 05 17:47:01   and it would look crap
    Mar 05 17:47:03     It will soon most likely
    Mar 05 17:47:05 <[-z-]> Spaceman: I think it's better to just reorganize on the new website
    Mar 05 17:47:08   talking about phpbb, please I'd like to have a strict no mikee-like trolls allowed under any circumpstance
    Mar 05 17:47:13 <[-z-]> we'll have an official picture, video and map repository
    Mar 05 17:47:30 <[-z-]> mand1nga: there is a friend and foe list in mybb
    Mar 05 17:48:03   amazing
    Mar 05 17:48:28 <[-z-]> I learned that mybb isn't the greatest for mass bans, hopefully that won't come into play soon though :-P
    Mar 05 17:48:57 <[-z-]> because in a well moderated forum, you shouldn't need to do a mass ban / deletion of the banee's posts
    Mar 05 17:49:18   how then?
    Mar 05 17:49:26 <[-z-]> how what?
    Mar 05 17:49:34   I mean if a mikee guy fills the forum with crap
    Mar 05 17:49:59   the only thing you can do is a mass deletion, etc
    Mar 05 17:50:19 <[-z-]> well I don't think we'll need to use it
    Mar 05 17:50:26 <[-z-]> there is also a warning system in mybb
    Mar 05 17:50:44 <[-z-]> http://wiki.mybboard.net/index.php/Warning_System
    Mar 05 17:51:04   you say the the problem will solve itself with a reputation system and/or an ignore feature, more or less?
    Mar 05 17:51:22 <[-z-]> yes they should and we should be able to ban users on a per user basis
    Mar 05 17:51:33 <[-z-]> if we were trying to ban say 30 people at once, it wouldn't be so simple
    Mar 05 17:51:48 <[-z-]> but you really shouldn't be trying to ban 30 users at once unless you have a poorly moderated forum
    Mar 05 17:52:06 <[-z-]> this will likely solve itself as the frontend of the admin backend continues in development
    Mar 05 17:52:13 <[-z-]> they did a major rewrite ~a year ago
    Mar 05 17:52:26 <[-z-]> but the code is really well organized and the plugin system is well made
    Mar 05 17:52:32 <[-z-]> there is also a bridge available to wordpress
    Mar 05 17:52:35   sure, or beign under attack, 30 ppl sounds quite massive to me
    Mar 05 17:52:36 <[-z-]> so it seems like a good choice
    Mar 05 17:52:50 <[-z-]> yes but being under attack, we disable user registration
    Mar 05 17:52:58 <[-z-]> possible the forums, depending on the degree of the attack
    Mar 05 17:53:00   sure
    Mar 05 17:53:02 <[-z-]> and then deal with ip tables from there
    Mar 05 17:53:24   I like those systems were one can report users doing funky things
    Mar 05 17:53:47 <[-z-]> yes, you can do that with mybb too
    Mar 05 17:54:29   well .. unfortunately I think we should get ready on that, more than likely mikee will try to spread his crap again whenever we start a new forum
    Mar 05 17:54:45 <[-z-]> yeah, shouldn't be a problem
    Mar 05 17:54:52 <[-z-]> he was contained on the NN forums
    Mar 05 17:54:57   how many people have registered for the AT forums and how many are active?
    Mar 05 17:55:07 <[-z-]> probably 1/8 or less are active
    Mar 05 17:55:10   cool
    Mar 05 17:55:17 <[-z-]> Total members 2993
    Mar 05 17:55:22 <[-z-]> yeah, I'd say ~100-300 active
    Mar 05 17:56:04 <[-z-]> phpbb admitted does a few moderation controls better on the front-end but the foundation of the system is not as agile
    Mar 05 17:56:41 <[-z-]> Users per day:      2.04
    Mar 05 17:56:46 <[-z-]>     Topics per day:     3.86
    Mar 05 17:56:51 <[-z-]> Posts per day:      50.45
    Mar 05 17:57:34   small but interesting forum
    Mar 05 17:57:46 <[-z-]> ~450 inactive accounts... not sure what classifies them as 'inactive' though
    Mar 05 17:58:31   I thought there were way more registered users, like 10k
    Mar 05 17:58:39 <[-z-]> nahaha
    Mar 05 17:58:46 <[-z-]> we're a small community
    Mar 05 17:58:58   indeed
    Mar 05 17:59:06 <[-z-]> especially compared to urban terror
    Mar 05 17:59:56     Urban Terror can suck my dick
    Mar 05 18:00:10 <[-z-]> yeah well, they capped a lot of CS kids
    Mar 05 18:00:15     Actually
    Mar 05 18:00:20 <[-z-]> I can't seem to get a number on their forums
    Mar 05 18:00:21   I'm creator/moderator of a Nexuiz forum here in my country, we're mostly argentinians and chileans
    Mar 05 18:00:22     I wouldn't even let that filth do that
    Mar 05 18:00:25   about 10 active users :P
    Mar 05 18:00:25 <[-z-]> but their servers were quite popular
    Mar 05 18:00:45 <[-z-]> mand1nga: :)
    Mar 05 18:00:55 <[-z-]> Nexuiz Diplomat of Chile
    Mar 05 18:00:56     Urban Terror has 27 major problems with it
    Mar 05 18:01:05     1-26: It's a rip off of CS
    Mar 05 18:01:05 <[-z-]> 27? lol
    Mar 05 18:01:11   connectivity with other countries like peru, colombia, ecuador, etc its pretty bad for playing, not sure why
    Mar 05 18:01:26     27: It's a rip off of CS and it also takes the CS community
    Mar 05 18:01:33   makes me thing maybe we should consider opening sections for specific languages
    Mar 05 18:01:36 <[-z-]> Samual: those are weak reasons
    Mar 05 18:01:43   for non english writers/readers :P
    Mar 05 18:01:43     Oh you want actual reasons?
    Mar 05 18:01:48     It's easy to hack/cheat,
    Mar 05 18:01:56     The serverlist takes a longass time to populate
    Mar 05 18:01:59 <[-z-]> do they distribute the source?
    Mar 05 18:01:59     The engine is ugly as hell
    Mar 05 18:02:14     Yes?
    Mar 05 18:02:14 <[-z-]> I thought the engine was decent
    Mar 05 18:02:17 <[-z-]> I haven't looked at the code
    Mar 05 18:02:26     I see so many aimbots on that game
    Mar 05 18:02:27 <[-z-]> I wouldn't even know what to think if I did :-P
    Mar 05 18:02:28     You have no idea
    Mar 05 18:02:34   they have some sort of ragdoll support it seems
    Mar 05 18:02:41     That's hacked together :P
    Mar 05 18:02:41   but gfx are ugly imho
    Mar 05 18:02:45 <[-z-]> no, I haven't logged into your brain in a while, so I have no idea :-P
    Mar 05 18:03:12     Good
    Mar 05 18:03:24     imo you aren't worthy
    Mar 05 18:03:27   maybe ppl enjoy more to shoot ppl like models
    Mar 05 18:03:38   I'm the opposite
    Mar 05 18:03:57   I'd rather to shoot an alien like thing :P
    Mar 05 18:04:22     I'd rather shoot people
    Mar 05 18:04:30     Not models, but people
    Mar 05 18:04:33     But well
    Mar 05 18:04:40 <[-z-]> ls ~/samuals_brain
    Mar 05 18:04:44 <[-z-]> microsoft.doc
    Mar 05 18:04:48     ..............
    Mar 05 18:04:52   lmao
    Mar 05 18:04:52     ......................................
    Mar 05 18:04:52 <[-z-]> porn/
    Mar 05 18:04:52  lol
    Mar 05 18:05:05 <[-z-]> stupid_things_z_says.txt
    Mar 05 18:05:08   "ls command not found"
    Mar 05 18:05:12  microsoft_porn/
    Mar 05 18:05:16 <[-z-]> haha :-P
    Mar 05 18:05:56   tZork: cheers mate, having a b33r here :)
    Mar 05 18:06:14  balmer in pink latex dress. disturbing dont wuite cut it as description.. :D
    Mar 05 18:06:30  cheers mand1nga =) 
    Mar 05 18:06:34   lol
    Mar 05 18:06:53     ls ~/tylers_brain           ls: cannot access tylers_brain: No such file or directory
    Mar 05 18:07:12     Bitch.
    Mar 05 18:07:18 <[-z-]> 2 minutes and 13 seconds... new record time for a good comeback
    Mar 05 18:07:20 <[-z-]> impressive
    Mar 05 18:07:26     stfu
    Mar 05 18:07:29 <[-z-]> "that was awesome"
    Mar 05 18:07:30     Also: The game
    Mar 05 18:07:31   this thing I'm drinking, called "barley wine" beer has about 10% of alcohol 
    Mar 05 18:07:40 <[-z-]> nice mand1nga, what brand?
    Mar 05 18:07:41   quite strong and tasty :)
    Mar 05 18:07:46 <[-z-]> I like me a good barley wine
    Mar 05 18:07:51   Antares, a local brand
    Mar 05 18:07:55 <[-z-]> ahh
    Mar 05 18:07:55   nice :)
    Mar 05 18:08:04   its quite good I must say
    Mar 05 18:08:05 <[-z-]> do you get american imports?
    Mar 05 18:08:18   not really .... mostly from europe
    Mar 05 18:08:23 <[-z-]> yeah, I figured :-P
    Mar 05 18:08:24   belgium, germany, etc
    Mar 05 18:08:35 <[-z-]> you got some good cabranets, eh?
    Mar 05 18:08:39  hmm interesting. teh rather strong stuff (7+) usualy arent that great in my experiance. but the exceptions can be quite amazing
    Mar 05 18:08:42 <[-z-]> in your region
    Mar 05 18:08:46   I don't know a single really good american beer .. sadly
    Mar 05 18:08:53 <[-z-]> haha :-P
    Mar 05 18:09:05   cabranets? whats that?
    Mar 05 18:09:11 <[-z-]> wine
    Mar 05 18:09:12 <[-z-]> red wine
    Mar 05 18:09:14   cabernets? :P wine?
    Mar 05 18:09:19   oh sure :)
    Mar 05 18:09:23 <[-z-]> my bad :-P
    Mar 05 18:09:36 <[-z-]> not my wine of choice but when I have ones from chile, they are always good and cheap
    Mar 05 18:09:39   yes we have quite good wine
    Mar 05 18:09:59 <[-z-]> malbec is native to your region?
    Mar 05 18:09:59   yes, price/quality is fine
    Mar 05 18:10:12   not sure .. I don't know really
    Mar 05 18:10:13 <[-z-]> http://www.greatdivide.com/ << good american beer
    Mar 05 18:10:16  i have good experianc of wine from chile too
    Mar 05 18:10:23   but its my favourite type :)
    Mar 05 18:10:39 <[-z-]> seriously mand1nga, I've had $5 dollar wines from chile they kicked the crap out of a $40 bottle
    Mar 05 18:10:42   new zealand and france will always have better wines
    Mar 05 18:10:55 <[-z-]> because of their long fertile soil?
    Mar 05 18:11:05 <[-z-]> possibly their latitude
    Mar 05 18:11:19   I know, I think we're trying hard to get better on that
    Mar 05 18:11:31 <[-z-]> I'm very please so far :-P
    Mar 05 18:11:33   probably the soil, not sure
    Mar 05 18:11:36 <[-z-]> you guys are the google of redwine
    Mar 05 18:11:39  heh i think i tasted old ruffian at some pont.. but i cant remerb if it was good. just the name stuck :P
    Mar 05 18:11:49 <[-z-]> tZork: that's a goodie
    Mar 05 18:11:50   hahaha
    Mar 05 18:12:02  (wrt to greatdivide)
    Mar 05 18:12:12 <[-z-]> yeah, I got that ;)
    Mar 05 18:12:53  hm ale
    Mar 05 18:13:01 <[-z-]> that's in a great place in the united states for beer and skiing/snowboarding
    Mar 05 18:13:04 <[-z-]> Colorado
    Mar 05 18:13:10   nice
    Mar 05 18:13:25   [-z-]: tell me a nice beer brand from there
    Mar 05 18:13:49 <[-z-]> from colorado? great divide
    Mar 05 18:14:03 <[-z-]> dogfish head I think is in New Hampsire, which is east coast
    Mar 05 18:14:10 <[-z-]> that's another good american brewery
    Mar 05 18:14:30   in fact I had a few nice beers while I was in ny but I don't remember the names at all :>
    Mar 05 18:14:43 <[-z-]> I read an article about the owner in entrepreneur magazine and he seems like a really cool guy that knows what he's doing and loves beer
    Mar 05 18:15:18 <[-z-]> hmm delaware
    Mar 05 18:15:20 <[-z-]> http://www.dogfish.com/
    Mar 05 18:15:25   at the mc gees and .. the blue note jazz club
    Mar 05 18:16:12     nighty
    Mar 05 18:16:19   nn esteel 
    Mar 05 18:16:20 <[-z-]> night
    Mar 05 18:16:24 <[-z-]> mand1nga: I haven't been to either
    Mar 05 18:16:28 <[-z-]> NYC is huge :)
    Mar 05 18:18:30   no doubt :P
    Mar 05 18:18:30   well sadly this was the last one
    Mar 05 18:18:31   but I have fernet, probably you never heard about that 
    Mar 05 18:19:41   http://en.wikipedia.org/wiki/Fernet
    Mar 05 18:19:48 <[-z-]> nope :-P
    Mar 05 18:20:03 <[-z-]> sounds nice
    Mar 05 18:20:04     cool Dokujisan 
    Mar 05 18:20:06   this must be my 3rd favorite beverage
    Mar 05 18:20:12     i guess ill work on it again 
    Mar 05 18:20:18 <[-z-]> I wonder if they carry it around here
    Mar 05 18:20:25   beer, wine, fernet .. wishkey might do .. but I'm not that old yet :P
    Mar 05 18:20:26 <[-z-]> do you usually mix it?
    Mar 05 18:20:37   whisky*
    Mar 05 18:20:54   yes, with coca cola/pepsi/tonic
    Mar 05 18:20:55 DibTop div0 
    Mar 05 18:21:09  DibTop: we played a second match on it and again it played well. It was a little tiny bit campy
    Mar 05 18:21:14  but generally not bad
    Mar 05 18:21:17 DibTop div0 
    Mar 05 18:21:20     cool stuff
    Mar 05 18:21:21   its really popular here, seems to be a thing from Italy though
    Mar 05 18:21:22     that map is old
    Mar 05 18:21:28  DibTop: also dublpaws is giving dance a makeover
    Mar 05 18:21:36     cool
    Mar 05 18:21:41  dunno if you want to try to mimic the new style or not
    Mar 05 18:22:02  it's on bc1 as dance_beta1
    Mar 05 18:22:21 <[-z-]> Dokujisan: are you aware that have have a revision of zion?
    Mar 05 18:22:28  no
    Mar 05 18:22:33 <[-z-]> it's not quite finished
    Mar 05 18:22:41 <[-z-]> I need to work on the bases and maybe textures
    Mar 05 18:22:46 <[-z-]> but it's a lot more in depth
    Mar 05 18:22:48  ok
    Mar 05 18:23:16 <[-z-]> now my mouse cursor disappears over my channel list...
    Mar 05 18:23:37 <[-z-]> I hate computers sometimes
    Mar 05 18:23:56  :-)
    Mar 05 18:24:35     lawl
    Mar 05 18:24:39     I see three mouse pointers
    Mar 05 18:24:49     xinerama draws one for every x screen
    Mar 05 18:24:49 <[-z-]> I have the stupid kde-cursor now too
    Mar 05 18:24:59     Yes I do too for firefox
    Mar 05 18:25:02 <[-z-]> Samual: ever see xdmx?
    Mar 05 18:25:07     No?
    Mar 05 18:25:08 <[-z-]> http://dmx.sourceforge.net
    Mar 05 18:25:08     What is it?
    Mar 05 18:25:18 <[-z-]> distributed multihead x
    Mar 05 18:25:27 <[-z-]> probably slow as hell but 1337!
    Mar 05 18:25:41     Hmm
    Mar 05 18:25:48     xserver-xgl is fast at least
    Mar 05 18:25:56     I'll check it out later though
    Mar 05 18:26:11 <[-z-]> xserver-xgl?
    Mar 05 18:26:18     btw i think we should stop changing physics
    Mar 05 18:26:31     for nexuiz i mean 2.6 or whatever
    Mar 05 18:26:36 <[-z-]> after we implement moonjumping ability for 10 seconds after a headshot
    Mar 05 18:29:43 *   mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 18:32:07     xserver-xgl = old shit which isn't being developed anymore
    Mar 05 18:32:13     It allows my 3 monitors to work with compiz
    Mar 05 18:32:42 <[-z-]> ah
    Mar 05 18:46:00 *   mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 19:12:13    gn all
    Mar 05 19:12:27  night
    Mar 05 20:59:53 *   tZork is now known as tZork|gone
    Mar 05 21:16:27 *   Dokujisan has changed the topic to:  Details are posted on the Wiki -- http://dev.xonotic.org -- temporary development site to get organized
    Mar 05 21:20:41 *   Samual gives channel operator status to mand1nga
    Mar 05 21:20:46 *   Samual gives channel operator status to [-z-]
    Mar 05 21:50:33 *   johngalt (~mshade@ip98-169-164-171.dc.dc.cox.net) has joined #notnexuiz
    Mar 05 21:50:56   hi guys
    Mar 05 21:51:22  :-)
    Mar 05 21:51:33  johngalt: go here and register
    Mar 05 21:51:34  http://dev.xonotic.org
    Mar 05 21:51:41  and i'll activate you
    Mar 05 21:51:45  so you can read the Wiki
    Mar 05 21:52:03   reg'd
    Mar 05 21:52:10   can I let Deiz in on this?
    Mar 05 21:52:20  activated
    Mar 05 21:52:24  who is Deiz?
    Mar 05 21:52:39     Hey John
    Mar 05 21:52:43   old school player, good friend of mine.  
    Mar 05 21:52:50   if you want it admin only, thats definitely cool
    Mar 05 21:53:02   understand the need for keeping close to the vest
    Mar 05 21:53:06  I mean... sure there will be lots of people who get involved, but not everyone is in this channel
    Mar 05 21:53:11  yeah
    Mar 05 21:53:25  for example, I'm keeping the Aussies updated, but they are in another channel
    Mar 05 21:54:03  we'll get more people in on the discussions after some of this initial stuff is covered
    Mar 05 21:55:12   k
    Mar 05 21:55:43     hi johngalt :)
    Mar 05 21:55:47   hiya
    Mar 05 21:56:01     howve you been?
    Mar 05 21:56:09 *   Deiz_ (~swh@69-196-147-186.dsl.teksavvy.com) has joined #notnexuiz
    Mar 05 21:57:02   good
    Mar 05 21:57:14   busy as hell
    Mar 05 21:57:33     hah i bet, i havent seen you in a very long time
    Mar 05 21:57:36 *   mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 21:57:41   i had server up again for a short while
    Mar 05 21:57:50  yeah I saw that. Was that with softlayer?
    Mar 05 21:58:12   it was on peer1
    Mar 05 21:58:17   serverbeach reseller
    Mar 05 21:58:26   damn good price i got on that actually
    Mar 05 21:58:36     yup so that
    Mar 05 21:58:41   but the community had changed so much i couldn't get into it much.  then this
    Mar 05 21:58:54   took it down a day or two before this whole illfonic thing came to light
    Mar 05 21:59:27     ya
    Mar 05 21:59:33     im just mad at lee
    Mar 05 21:59:39     not even mad at illfonic atm
    Mar 05 21:59:45   i think we all are.  a no show for the last however long
    Mar 05 22:00:00     seems a lot of people are lashing out illfonic
    Mar 05 22:00:01   and then... "Oh, yes, it's all about the community.  This is good for you.  Take your medicine."
    Mar 05 22:00:15     i honestly hold lee responsible for it
    Mar 05 22:00:17   illfonic are just the opportunists, not the root.
    Mar 05 22:00:20   anyway
    Mar 05 22:00:27   we know what happened, that's why we're here.
    Mar 05 22:00:31 *   johngalt reads wiki
    Mar 05 22:00:32     johngalt>   illfonic are just the opportunists, not the root.
    Mar 05 22:00:33     exactly
    Mar 05 22:00:42  http://pics.nexuizninjaz.com/viewer.php?file=rogou3t1yz0f4qpo9x.jpg
    Mar 05 22:00:52  It was a good opportunity, potentially.
    Mar 05 22:01:02  The name licensing and attempted rebranding squandered it.
    Mar 05 22:01:32  The disingenuous babble from the Illfonic rep didn't help, though.
    Mar 05 22:02:03  How's (license) mobility to be combined with safety from a future incident?
    Mar 05 22:02:41  nice to meet ya Deiz_ 
    Mar 05 22:02:56  Hello.
    Mar 05 22:03:19  We've met, I think, but I've been out for ages.
    Mar 05 22:04:00     i think im gonna work on modeling mostly
    Mar 05 22:04:18     thats where we seriously lack
    Mar 05 22:04:24  yes!
    Mar 05 22:04:27  definitely
    Mar 05 22:04:30     and i dont think we should release until we have new models
    Mar 05 22:04:35 DibTop div0 
    Mar 05 22:04:40   DibTop: do you have modeling experience?
    Mar 05 22:04:41     i think we can show up the console nexuiz
    Mar 05 22:04:43   rigging?
    Mar 05 22:04:44  DibTop: how are you learning about rigging models?
    Mar 05 22:04:48     johngalt: not modeling but some animating
    Mar 05 22:04:54     already know how to rig Dokujisan 
    Mar 05 22:04:59  how did you learn
    Mar 05 22:05:02   Rigging Dokujisan is easy.
    Mar 05 22:05:06     blender tut
    Mar 05 22:05:09     need it?
    Mar 05 22:05:09   Just get him excited, he rigs himself.
    Mar 05 22:05:42  well, so anyone can follow a blender animation tutorial and they can animate models for nexuiz? or is there more information needed about nexuiz to finalize it?
    Mar 05 22:05:52     more info needed
    Mar 05 22:05:59     and im still working on documenting that
    Mar 05 22:06:01  ok where did you get info?
    Mar 05 22:06:05  yeah that's what I'm getting at
    Mar 05 22:06:10     it needs to be documented
    Mar 05 22:06:24  Who in Nexuiz has that information though, currently?
    Mar 05 22:06:25     ill write something up after i get it in nexuiz and working
    Mar 05 22:06:33     i think Morphed does
    Mar 05 22:06:35   is there anything we need to look at legally for a fork?
    Mar 05 22:06:36  ok
    Mar 05 22:06:37     but only for 3ds max
    Mar 05 22:06:43     he dosent use blender
    Mar 05 22:06:51     tzork has some knowledge as well
    Mar 05 22:06:55     more with 3ds though
    Mar 05 22:07:01     obi = 3ds too
    Mar 05 22:07:15  johngalt: I don't think so. Everything in Nexuiz content wise was GPL compatible, and unlike illfonic, we're forking into another GPL game
    Mar 05 22:07:28  we may need to strip out references to "nexuiz"
    Mar 05 22:07:35   i think that's correct.
    Mar 05 22:07:40   just putting the question out there.
    Mar 05 22:09:47  Licensing hurts my brain.
    Mar 05 22:09:50  heh
    Mar 05 22:10:05   so much of GPL is untested
    Mar 05 22:10:12   and most of it misunderstood :)
    Mar 05 22:10:38   so as far as naming goes, are we trying to keep to something similar, or is anything fair game?
    Mar 05 22:10:44  It gets extended.
    Mar 05 22:11:02  there are ideas started for names in the wiki
    Mar 05 22:11:08   yeah, I'm looking at that now
    Mar 05 22:11:08  that's just a step 1 though
    Mar 05 22:11:12  You can't close my code, it's GPLed... You can't remove that load-bearing wall, it's GPLed.
    Mar 05 22:11:52  I'm assuming the game code  license will be set in stone, as changing it'd require all past contributors to be in agreement.
    Mar 05 22:12:03  The Nexuiz repo never had copyright assignment like Darkplaces, did it?
    Mar 05 22:12:04  each time I mention the fork, that's an immediate question about the name, understandably. I think it's wise to take proper time to figure out the name.
    Mar 05 22:12:43  It's hard to do worse than "Neck-see-us" which is spelled "Neck-shoe-is".
    Mar 05 22:12:48  yep :-)
    Mar 05 22:12:52   Dokujisan: absolutely. name is least important aspect. 
    Mar 05 22:12:52  that's the point i keep making
    Mar 05 22:13:00  that "nexuiz" is actually a pretty bad name
    Mar 05 22:13:03   at least immediately
    Mar 05 22:13:21  "Nexiuz" wouldn't have been a bad name though
    Mar 05 22:13:38  and then kanji "n" symbol looked good
    Mar 05 22:14:08  Heh
    Mar 05 22:14:16  On that map screenshot, the texture on the right side is backwards.
    Mar 05 22:14:42   which screenshot?
    Mar 05 22:14:48  http://pics.nexuizninjaz.com/viewer.php?file=rogou3t1yz0f4qpo9x.jpg
    Mar 05 22:14:56   ah
    Mar 05 22:17:02  http://pics.nexuizninjaz.com/viewer.php?file=zbcmceics6shje6u8wk9.jpg
    Mar 05 22:17:06  that one is funny :-)
    Mar 05 22:17:33   hahah
    Mar 05 22:17:52  Was he incommunicado for that entire time, or just making very minor contributions?
    Mar 05 22:20:48   Deiz_: http://dev.alientrap.org/repositories/stats/nexuiz
    Mar 05 22:21:22  Heh. Insufficient resolution to make out whether it's non-zero.
    Mar 05 22:21:32   well he's on there twice
    Mar 05 22:21:40   vermeulen and vermeulenl
    Mar 05 22:21:43  Ah, yes.
    Mar 05 22:23:20  http://www.ohloh.net/p/nexuiz/contributors/1595580376992
    Mar 05 22:24:27  So, no major commit flurries since mid-2005.
    Mar 05 22:24:30  alright I gotta crash. Cya later...
    Mar 05 22:24:40   seeya doku
    Mar 05 22:29:32     http://www.ohloh.net/p/nexuiz/contributors/1595580541087
    Mar 05 22:29:33     Yay
    Mar 05 22:29:38     I feel important
    Mar 05 22:30:03     http://www.ohloh.net/p/nexuiz/contributors/1595580541086
    Mar 05 22:30:04     ohshi
    Mar 05 22:30:09     FruitieX > Me
    Mar 05 22:30:27     oh hello Deiz_ 
    Mar 05 22:33:33     hrm i wonder if someone can retexture the marine model
    Mar 05 22:33:39     cause its really not that bad
    Mar 05 22:33:57     just needs new art
    Mar 05 22:37:43   hiya pavlvs 
    Mar 05 22:37:56     hi johngalt 
    Mar 05 22:37:58 *   Taoki has quit (Ping timeout: 120 seconds)
    Mar 05 22:41:46     BTW, div0's work: This developer has been contributing to this project since March 2006, with a total of 43 person-months of code development. He or she made a total of 4652 commits and the main programming language used was C.
    Mar 05 22:42:01 *   pavlvs327 (pavlvs@adsl-75-39-134-107.dsl.tpkaks.sbcglobal.net) has joined #notnexuiz
    Mar 05 22:42:03     4652 commits :P
    Mar 05 22:42:17   yep.  div0 *is* nexuiz.
    Mar 05 22:42:22   or isnot nexuiz
    Mar 05 22:42:35 *   esteel1 (OQBFtg94ui@planetnexuiz.de) has joined #notnexuiz
    Mar 05 22:42:35     That's more than half damnit :P
    Mar 05 22:42:58 *   Spaceman_1 (~Spaceman@87.127.156.98) has joined #notnexuiz
    Mar 05 22:43:04 *   esteel has quit (Ping timeout: 120 seconds)
    Mar 05 22:43:04 *   Spaceman has quit (Ping timeout: 120 seconds)
    Mar 05 22:43:04 *   pavlvs has quit (Ping timeout: 120 seconds)
    Mar 06 01:22:04 <[-z-]> wasn't the marine just retextured?
    Mar 06 01:31:13     -z- not really
    Mar 06 01:31:26 <[-z-]> o rly?
    Mar 06 01:31:27     well it was kind of but maybe 6 months ago
    Mar 06 01:31:34     it could use gloss, bump etc
    Mar 06 01:31:39     to make it look better
    Mar 06 01:35:25 <[-z-]> http://image.com.com/gamespot/images/2010/060/990996_20100302_790screen006.jpg
    Mar 06 01:35:36 <[-z-]> am I wrong or is that shot not coming out of the gun?
    Mar 06 01:36:38  persistent trails?
    Mar 06 01:36:58 *   pavlvs327 is now known as pavlvs
    Mar 06 01:36:59 <[-z-]> so it was shot and that's the trail fading?
    Mar 06 01:37:10     tahts my assumption
    Mar 06 01:38:07     similar to the nex affect probably
    Mar 06 01:38:58     althoguh if they're using nexuiz gamecode... ;p
    Mar 06 01:39:11 <[-z-]> HLAC seems suspicious
    Mar 06 01:39:13     shot origins have been pretty messed up :)
    Mar 06 01:39:58 <[-z-]> where did I jus tread the weapons list about their game?
    Mar 06 01:41:17 <[-z-]> LOL, this page comes up in a google search for Nexuiz weapons http://dev.alientrap.org/wiki/1/Weapons
    Mar 06 01:41:28     [-z-]: the first post of the original illfonic thread, 2nnd para of GDC header
    Mar 06 01:41:28     iirc
    Mar 06 01:41:36 <[-z-]> ah
    Mar 06 01:41:45 <[-z-]> yeah is the hlac from another game?
    Mar 06 01:42:26     no its from this one
    Mar 06 01:42:37     tzork was pretty pissed about that :S
    Mar 06 01:42:39     no
    Mar 06 01:42:39     tZork|gone invented it
    Mar 06 01:42:45 <[-z-]> yeah, I'd be pissed too
    Mar 06 01:42:50     me too
    Mar 06 01:42:52     i was using it as an example of where Lee didnt get appropriate permission
    Mar 06 01:42:56 <[-z-]> vermeulen really screwed up this time
    Mar 06 01:43:05     this time?
    Mar 06 01:43:10     hes screwed up before?
    Mar 06 01:43:26 <[-z-]> he's made some odd moves in the past
    Mar 06 01:43:53 <[-z-]> I have some personal discoveries with him
    Mar 06 01:43:54     this was a good move in all honesty just horrendous outcome/planning
    Mar 06 01:44:10 <[-z-]> yeah the screwed the pooch on execution
    Mar 06 01:44:42 <[-z-]> I don't think it would have been hard to get the community on board
    Mar 06 01:44:58 <[-z-]> but instead of asking "for permission", he's asking "for forgiveness"
    Mar 06 01:45:05 <[-z-]> but he's really not even asking for forgiveness
    Mar 06 01:45:12 <[-z-]> which pisses me off even more
    Mar 06 01:45:14     yup
    Mar 06 01:45:58 <[-z-]> I tried to bring this up to him, saying maybe he should hunt down the contributors it's affected the most
    Mar 06 01:46:28 <[-z-]> and he seemed to think that without royalities, the contributors wouldn't care... but I don't think anyone is really concerned about the money
    Mar 06 01:47:28 <[-z-]> more so a better explanation, an apology and a plan of action
    Mar 06 01:57:06     i should sue if they use accuracy stats :P
    Mar 06 01:57:42     well the problem is
    Mar 06 01:57:56     its closed source, so you dont know if they reused your code or not
    Mar 06 01:58:06     so you have to sue for the code
    Mar 06 01:58:43     haha true true
    Mar 06 03:09:35   01:02:46 < mand1nga> they have some sort of ragdoll support it seems
    Mar 06 03:09:44   UrbanTerror? Ragdoll? errrrrr. NO. :P
    Mar 06 03:11:26   o, maybe new release
    Mar 06 03:35:26    i wonder if that console nexuiz will have ragdolls 
    Mar 06 04:06:42    morning
    Mar 06 04:08:03    hi
    Mar 06 04:27:32    google Agents for Games and Simulations: Trends in Techniques, Concepts and Design (Frank Dignum) :D
    Mar 06 05:01:21 *   mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 06 05:11:43 *   Spaceman_1 is now known as Spaceman
    Mar 06 05:46:02 *   Morphed_ (Morphed@aapi142.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 06 05:47:47 *   esteel1 is now known as esteel
    Mar 06 05:49:17 *   Morphed has quit (Ping timeout: 364 seconds)
    Mar 06 06:16:48 *   MrBougo (~MrBougo@ip-213-49-242-191.dsl.scarlet.be) has joined #notnexuiz
    Mar 06 06:16:55    welp.
    Mar 06 06:17:14   hello MrBougo
    Mar 06 06:17:29    I'm interested in the motives of this, why do you guys think it is beneficial to fork?
    Mar 06 06:18:50     looks like new name
    Mar 06 06:19:27     and the obvious reason to get out of alientrap so an absentee "owner" cant sell it out
    Mar 06 06:19:47     not sure if that part requires a fork really
    Mar 06 06:20:12    so you're planning to "move out", taking the community as a whole away from alientrap
    Mar 06 06:20:18    how would this work out?
    Mar 06 06:20:30    would lee give up his project?
    Mar 06 06:21:39   there would still be the possibility of a GPL Nexuiz
    Mar 06 06:22:03    how so?
    Mar 06 06:22:08    it still is possible
    Mar 06 06:22:09   a gpl nexuiz could use the code from the fork version
    Mar 06 06:22:16   forked*
    Mar 06 06:22:27    nexuiz is still gpl
    Mar 06 06:22:33    I mean, nexuiz pc
    Mar 06 06:23:23    the part I still don't like is that if there is a fork, both projects would coexist for a while at least
    Mar 06 06:23:38    this^
    Mar 06 06:23:38     yeah same
    Mar 06 06:23:55   sorry, I meant that there would be the possibility of new version of gpl nexuix being published in th e future
    Mar 06 06:24:01    that's why this seems risky to me
    Mar 06 06:24:05    how do you move a whole community
    Mar 06 06:24:20    granted, it isn't that big, and the main elements will surely change if they see the others do
    Mar 06 06:24:35    one question
    Mar 06 06:24:37    I'd want alientrap.org/nexuiz to say something along the lines of "Nexuiz is discontinued, however it is revamped by project XXX"
    Mar 06 06:24:42     div0 still hasnt said anyhting in here
    Mar 06 06:24:47    will all the developers move too?
    Mar 06 06:24:48     i am kinda waiting on his thoughts
    Mar 06 06:25:22    and what prevents nexuiz from importing notnexuiz's changes as they come
    Mar 06 06:26:04    of course they can't sell it anymore then :p
    Mar 06 06:26:15   who will publish the gpl nexuiz version?
    Mar 06 06:26:24    bbl
    Mar 06 06:26:39   I'm assuming the developers will abandon alientrap for the new project#
    Mar 06 06:27:04   pavlvs: div0 has said lots
    Mar 06 06:27:11   all devs that have some self respect :)
    Mar 06 06:34:35   Dokujisan: can you add log from http://www.nullgaming.com/stuff/notnexuiz.log to the wiki
    Mar 06 07:09:39 *   Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 06 07:32:09    Spaceman, 404
    Mar 06 07:32:21    who logs this channel?
    Mar 06 07:32:52   the url was working yesterday
    Mar 06 07:33:21   the wiki was added last night and some of the log has been added to the wike
    Mar 06 07:33:24   wiki
    Mar 06 07:34:46   MrBougo: I can add my log but it only started 10:00 yesterday
    Mar 06 07:35:58    put "this channel is logged" in the topic at least :p
    Mar 06 07:37:22    Morphed, that was off-topic and uncalled for
    Mar 06 07:37:43  Spaceman: sure
    Mar 06 07:38:02   how do you add a page to the wiki?
    Mar 06 07:38:08    you guys should get some info page up
    Mar 06 07:38:53    explaining your motives, why you believe it's a good thing, and where you think this is going
    Mar 06 07:38:58  Spaceman: the easiest way is to add a name to end of the URL
    Mar 06 07:39:20  MrBougo: have you registered wtih the site and looked through the wiki?
    Mar 06 07:39:25    no
    Mar 06 07:39:32    and I mean a public page
    Mar 06 07:39:32  http://dev.xonotic.org
    Mar 06 07:39:39  we'll do that eventually
    Mar 06 07:39:42    unless this is a secret project
    Mar 06 07:39:55  it is somewhat secret at the moment, only to help us focus
    Mar 06 07:39:59    are you going to get this started when things settle down?
    Mar 06 07:40:03   I tried http://dev.xonotic.org/projects/notnexuiz/wiki/test
    Mar 06 07:40:17   404 The page you were trying to access doesn't exist or has been removed.
    Mar 06 07:40:29  Spaceman: you might not have page creation rights
    Mar 06 07:40:33   maybe I need to be an admin
    Mar 06 07:40:42  that URL opens a blank edit screen for me
    Mar 06 07:40:46 *   Spaceman prods [-z-]
    Mar 06 07:40:55  Spaceman: what did you want to add?
    Mar 06 07:41:01  I can change your permissions
    Mar 06 07:41:03    Spaceman, meanwhule ask somebody whocan :p
    Mar 06 07:41:04    woops
    Mar 06 07:41:07    typos
    Mar 06 07:41:08   my irc log
    Mar 06 07:41:23  Spaceman: I'm gonna add my entire IRC log from when I first entered this channel
    Mar 06 07:41:34   that is even better
    Mar 06 07:41:34  so that should include your log
    Mar 06 07:41:36  k
    Mar 06 07:41:47   mine is only 26 hours
    Mar 06 07:41:57   thanks
