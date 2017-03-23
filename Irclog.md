Irclog
======

    **** BEGIN LOGGING AT Wed Mar 03 10:28:36 2010

    Mar 03 10:28:36 *	Now talking on #notnexuiz
    Mar 03 10:28:41 <Taoki>	Hi
    Mar 03 10:28:44 <Dokujisan>	hello
    Mar 03 10:28:52 <[-z-]>	why hello
    Mar 03 10:28:55 *	[-z-] gives channel operator status to Dokujisan Taoki
    Mar 03 10:29:46 *	div0 (Fg8deKX0@rm.endoftheinternet.org) has joined #notnexuiz
    Mar 03 10:30:07 *	[-z-] gives channel operator status to div0
    Mar 03 10:30:11 <div0>	Welcome to Noxious.
    Mar 03 10:31:07 <[-z-]>	I've talked to div0 and Dokujisan in private about different aspects in moving forward with a fork away from Nexuiz and away from Alientrap
    Mar 03 10:32:07 <[-z-]>	we've begin discussing project organization, server availabiltiy, repository, name, interested parties, possible repurcussions and where we go from here
    Mar 03 10:32:11 <div0>	just not sure if it will be an actual fork
    Mar 03 10:32:20 <div0>	or rather, whether AT will even continue with Nexuiz then
    Mar 03 10:32:38 <div0>	to summarize a bit:
    Mar 03 10:32:56 <div0>	- repository I can provide, on icculus.org. In fact, I already have a Nexuiz repo there.
    Mar 03 10:33:10 <Taoki>	I'm always with this project no matter what new name it will have, team name, etc. What happened happened, i mainly care what is best for this project now
    Mar 03 10:33:13 <div0>	- project organization: there should be not "one leader who speaks for everyone".
    Mar 03 10:33:27 <div0>	  to make things like what had happened to not happen again
    Mar 03 10:34:04 <div0>	I suggest a scheme that ensures 3 "leaders", and big decisions have to be agreed upon by all three, and they also should be "somewhat responsible" for the rest of the community
    Mar 03 10:34:16 <div0>	e.g. no persons who are so detached that they simply do not care for the community any more
    Mar 03 10:34:34 <Dokujisan>	I told -z- that I think all good projects need some sort of leadership to be succesful. The 3-leader idea isn't bad.
    Mar 03 10:34:40 <[-z-]>	and perhaps a board or committee under that
    Mar 03 10:34:45 <div0>	in AT, LordHavoc maybe somewhat still can represent the community - Vermeulen certainly can't
    Mar 03 10:35:25 <div0>	2 leaders aren't enough, as at times there would be only one leader available :P
    Mar 03 10:35:28 <[-z-]>	also for project reorganization, I've begun talking about better package management and distribution
    Mar 03 10:35:33 <div0>	I think the existence of a "dictator" should eb avoided
    Mar 03 10:35:44 <div0>	hm... how?
    Mar 03 10:36:04 <[-z-]>	how? the whole upload test package and alert servers thing I was talking about
    Mar 03 10:36:11 <Taoki>	I can confess I am a tiny little bit upset at LordHavoc too, because he could have declined this whole thing and not ported the engine to xbox. But I still like him and am not upset on him or anything... just wish he would have thought more at first maybe
    Mar 03 10:36:21 <Taoki>	erm ps3
    Mar 03 10:36:48 <div0>	[-z-]: oh
    Mar 03 10:36:53 <div0>	you don't mean packaging of the game :P
    Mar 03 10:37:01 <[-z-]>	oh no no
    Mar 03 10:37:03 <div0>	because, regarding that I think the old Nexuiz way was right
    Mar 03 10:37:11 <[-z-]>	yeah, there is a good workflow there
    Mar 03 10:37:13 <div0>	other than that I am working on a new build script that works more efficiently wiht git
    Mar 03 10:37:16 <[-z-]>	I wouldn't want to modify that
    Mar 03 10:37:22 <div0>	but that doesn't change the result
    Mar 03 10:37:32 <[-z-]>	you know best about that area
    Mar 03 10:37:42 <div0>	still, we ARE doing oddball packaging
    Mar 03 10:37:48 <[-z-]>	I want to start getting this project more organized though
    Mar 03 10:37:51 <div0>	so MAYBE we should make it more "standard" anyway
    Mar 03 10:37:56 <div0>	but well
    Mar 03 10:37:59 <[-z-]>	and built the website into the workflow
    Mar 03 10:38:02 <div0>	it is oddball that we put all platforms in one download
    Mar 03 10:38:06 <div0>	but it has its advantages too
    Mar 03 10:38:22 <[-z-]>	I want to build everything into wordpress/mybb and get the build script putting out cvar / command lists for the tool I'll integrate into the site.
    Mar 03 10:38:32 <div0>	I wouldn't want to touch that for now, but do some attempts at making platform specific versions too
    Mar 03 10:38:42 <div0>	I e.g. have recently made an engine feature that allows attaching a pk3 to a executable
    Mar 03 10:38:49 <div0>	so we could make a single selfcontained exe file for the game
    Mar 03 10:38:51 <div0>	(a 900MB one...)
    Mar 03 10:39:32 <div0>	for OS X, such a thing can already be accomplished because applications are just folders anyway
    Mar 03 10:39:33 <Taoki>	I hope there aren't plans to distribute Nexuiz like that in the future.
    Mar 03 10:39:39 <div0>	and Linux users don't care about that structure anyway :P
    Mar 03 10:39:53 <div0>	Taoki: I don 't want to exclude it, but probably it won't happen
    Mar 03 10:40:01 <div0>	except maybe for DSN :P
    Mar 03 10:40:22 <div0>	I think the advantages of the multiplatform zip overweigh that
    Mar 03 10:40:27 <Taoki>	I don't support that personally. The data being in a pk3 file is very important for flexibility and the like imo
    Mar 03 10:40:31 <[-z-]>	I think it would be helpful in some cases where users prefer simplicity
    Mar 03 10:40:33 <div0>	it stays just as flexible
    Mar 03 10:40:34 <[-z-]>	but never a forced thing
    Mar 03 10:40:37 <div0>	if you cat the pk3 to an executable
    Mar 03 10:40:44 <div0>	you can rename the result to zip and work with it normally
    Mar 03 10:40:50 <div0>	it is no less flexible than the pk3 way
    Mar 03 10:41:07 <div0>	zip self extractors work that way too :P
    Mar 03 10:41:16 <Taoki>	Hmm, I see
    Mar 03 10:41:20 <div0>	still
    Mar 03 10:41:26 <div0>	it means different downloads for different platforms
    Mar 03 10:41:32 <div0>	which somewhat hides that the game is multiplatform
    Mar 03 10:41:48 <div0>	and that is the part that I don't like about it
    Mar 03 10:42:03 <div0>	for damn small nexuiz this is no issue htough :P
    Mar 03 10:42:11 <Taoki>	I still like the way it is packed now myself. Don't think we should change that.
    Mar 03 10:42:15 <div0>	right
    Mar 03 10:42:17 <div0>	I like it too
    Mar 03 10:42:26 <div0>	this is, again, more an idea for specialized "distributions" like DSN
    Mar 03 10:43:15 <div0>	[16:38:43] <@[-z-]> I want to build everything into wordpress/mybb and get the build script putting
    Mar 03 10:43:17 <div0>	                    out cvar / command lists for the tool I'll integrate into the site.
    Mar 03 10:43:27 <div0>	you want the buoild script accessible from a web interface... not sure if that is good
    Mar 03 10:43:49 <div0>	another thing however that I would like, is more frequent public releases
    Mar 03 10:43:56 <div0>	with git, we can easily separate into different branches
    Mar 03 10:44:03 <div0>	and merge features into the main branch when they are done
    Mar 03 10:44:19 <Taoki>	Yeah, same div0. New versions seem to be released once or twice an year
    Mar 03 10:44:27 <div0>	so we should be able to make "weekly" test releases, and make actual minor releases every 3 months
    Mar 03 10:44:31 <Taoki>	Maybe once every 3-4 months at most wouldn't be bad
    Mar 03 10:44:55 <div0>	just like I did my work on Nexuiz/DP lately
    Mar 03 10:45:08 <div0>	I e.g. finished the warpzones code before putting it into the main branch
    Mar 03 10:45:53 <div0>	the problem is just, I cannot enforce such a policy on darkplaces
    Mar 03 10:46:04 <Dokujisan>	div0: I have wanted a fork of nexuiz for a long while. The reasons were mainly because of missing elements of project management. We (I discussed this with a handful of others) couldn't do a fork before because we didn't have someone like you, a primary developer who knows the code very well. But if YOU are involved in a Nexuiz fork, that changes things. I would be onboard as long as we have an outline of management....and some i
    Mar 03 10:46:04 <Dokujisan>	ntention of doing "official" community development, "official" marketing efforts, "official" testing procedures with a select group of volunteer testers, etc.
    Mar 03 10:46:07 <div0>	for that I am maintaining a "stable branch", but unstabilities still happen once in a while in DP
    Mar 03 10:46:14 <div0>	as I often simply cannot properlya judge if something is stable
    Mar 03 10:46:35 <div0>	select group of testers... not sure :P
    Mar 03 10:46:44 <div0>	I don't think testing should be limited
    Mar 03 10:46:52 <div0>	everyone should be allowed, and even encouraged, to
    Mar 03 10:47:11 <div0>	but, some select group for "heavier" testing is still a very good idea
    Mar 03 10:47:20 <div0>	i.e. people who should feel responsible for actually testing it :P
    Mar 03 10:47:23 <Taoki>	Not sure to whom I mentioned this, but for a while ago I've started making an own game from Nexuiz as well. Obviously, one that will be named differently and remain GPL too :P Probably a little game which is just like, a sort of story i wanted to make for myself
    Mar 03 10:47:30 <Dokujisan>	well of course features can be experienced by all, but a select group would do some proper feedback and have better communication with the dev team
    Mar 03 10:47:39 <div0>	right
    Mar 03 10:47:44 <div0>	I just say... we shouldn't restrict
    Mar 03 10:47:49 <[-z-]>	sorry went to make tea, let me catch up
    Mar 03 10:47:51 <div0>	a testing team should not be exclusive
    Mar 03 10:47:58 <div0>	but it should eb responsible for the testing
    Mar 03 10:48:07 <div0>	anyone else still is free to test too :P
    Mar 03 10:48:16 <Dokujisan>	anyone could give feedback....my point is that this type of subject should be discussed. The whole game balance issues that we went through (before and after LH rejoined the project) could have been handled better
    Mar 03 10:48:19 <Taoki>	Yeah, SVn should always be public imo
    Mar 03 10:48:22 <[-z-]>	div0: the cvar and command lists would be text files reformated as json and accessible through a web application
    Mar 03 10:48:35 <div0>	Taoki: not just svn
    Mar 03 10:48:37 <div0>	also binary builds
    Mar 03 10:48:42 <Taoki>	sure
    Mar 03 10:48:44 <[-z-]>	wordpress is an open format many developers know and love and it will be easy for us to scale
    Mar 03 10:48:50 <div0>	my goal is weekly binary builds from the "stable" branch
    Mar 03 10:49:04 <div0>	feature freeze would simply mean no feature branches get merged into main, only bugfixes would
    Mar 03 10:49:10 <div0>	other devs can then still work on features :P
    Mar 03 10:49:27 <div0>	they just won't appear in the release the freeze is for
    Mar 03 10:49:42 <[-z-]>	This will help give us a stronger community because we can build user auth into other parts of the site, like a map repository.
    Mar 03 10:49:58 <div0>	as for cvar list...
    Mar 03 10:50:05 <div0>	don't know how to properly generate json from shell script
    Mar 03 10:50:12 <[-z-]>	you don't have to
    Mar 03 10:50:12 <div0>	but well, I do know how to make a full cvar list text file :P
    Mar 03 10:50:16 <[-z-]>	yes
    Mar 03 10:50:18 <[-z-]>	that's all I need
    Mar 03 10:50:20 <[-z-]>	that's how it works
    Mar 03 10:50:22 <[-z-]>	I have it in git
    Mar 03 10:50:24 <Dokujisan>	I'm strongly in favor of a central user system
    Mar 03 10:50:27 <div0>	once did that by actually running the engine, and doing cvarlist :P
    Mar 03 10:50:41 <[-z-]>	Dokujisan: I don't think it's a completely central user system
    Mar 03 10:50:50 <[-z-]>	and I'm open to creating a distributed network
    Mar 03 10:51:06 <div0>	I don't think repository access and web user auth can be combined
    Mar 03 10:51:12 <[-z-]>	div0: this is how it works http://github.com/z/ncacs
    Mar 03 10:51:17 <div0>	but all the rest should be able to
    Mar 03 10:51:40 <[-z-]>	so just a cronjob to generate the list and upload it to a web server
    Mar 03 10:51:42 <Taoki>	Heh, I realize now i never thouht about any such changes, now that it is talked about. Nexuiz, for a free and opensource project, always seemed perfect to me. Never thought anything could or should be improved in how it's managed etc.
    Mar 03 10:51:46 <div0>	only problem: this lacks cvars that are specific to some builds
    Mar 03 10:51:58 <div0>	like renderer stuff
    Mar 03 10:52:01 <Taoki>	Except that patches could be checked more often, been struggling with that for the last months
    Mar 03 10:52:04 <[-z-]>	div0: well, we can further separate it
    Mar 03 10:52:05 <Dokujisan>	div0: I'm working on another gaming project with Getty and we're planning something called a PlayerID which is to be a central user system that even other games other than ours could use
    Mar 03 10:52:14 <div0>	Taoki: thing is
    Mar 03 10:52:24 <div0>	working with such patches is quite tedious
    Mar 03 10:52:36 <div0>	I say, when using git, more people should get commit access to branches
    Mar 03 10:52:43 <div0>	and merging gets easier then too
    Mar 03 10:53:11 <Taoki>	Yeah, i'm still not so familiar with git. It is more difficult to understand than SVN, ad least over Windows with Tortoise
    Mar 03 10:53:16 <div0>	Dokujisan: you know I am against an enforced user system for the game
    Mar 03 10:53:20 <div0>	I want to play anonymously
    Mar 03 10:53:26 <div0>	even though that means proper banning cannot happen
    Mar 03 10:53:34 <div0>	an optioanl registration for stats, why not
    Mar 03 10:53:37 <Dokujisan>	div0: even if you register a name, isn't that still anonymous?
    Mar 03 10:53:50 <div0>	not really, one can easily find out :P
    Mar 03 10:53:55 <[-z-]>	well, I wasn't even thinking about stats but we can do that too... I was thinking more for content submissions
    Mar 03 10:54:04 <div0>	I basically don't want to be trackable in game
    Mar 03 10:54:09 <Dokujisan>	why not?
    Mar 03 10:54:10 <div0>	I sometimes play with other nicks
    Mar 03 10:54:23 <div0>	because e.g. employers are not supposed to know that I sometimes play 3 hours on a day
    Mar 03 10:54:32 <[-z-]>	:-P
    Mar 03 10:54:32 <div0>	they are prone to expect you to be there for the company all day
    Mar 03 10:54:41 <div0>	the times of 8hr/day are over
    Mar 03 10:55:13 <div0>	and no, I do not mean playing from work.
    Mar 03 10:55:16 <div0>	not doing THAT :P
    Mar 03 10:55:17 <Dokujisan>	what if each user account is allowed 3 hidden aliases tied to the account?
    Mar 03 10:55:21 <div0>	no
    Mar 03 10:55:25 <Dokujisan>	or some other variation
    Mar 03 10:55:28 <div0>	why do you want to enforce accounts?
    Mar 03 10:55:40 <div0>	even though _I_ know my email address won't eb abused
    Mar 03 10:55:44 <div0>	how would anyone else be sure?
    Mar 03 10:55:58 <div0>	(I would know because I'd have control over that system :P)
    Mar 03 10:56:10 <Dokujisan>	the moderation features alone are worth the central user system
    Mar 03 10:56:14 <Dokujisan>	but as far as trusting people
    Mar 03 10:56:28 <div0>	banning is not worth tracking
    Mar 03 10:56:31 <Dokujisan>	we could win people's faith because of being an open source project with open values
    Mar 03 10:56:34 <div0>	how would hidden aliases even work?
    Mar 03 10:56:41 <div0>	i mean, if you use it for banning
    Mar 03 10:56:45 <Dokujisan>	div0: that can be discussed. I just thought of that off the top of my head
    Mar 03 10:57:06 <div0>	other way round, for positive display of trust - sure
    Mar 03 10:57:13 <div0>	people SHOULD be able to register others as friends
    Mar 03 10:57:25 <div0>	and I can always opt to play as an "unknown" :P
    Mar 03 10:57:36 <div0>	think of IRC nickname registration
    Mar 03 10:57:50 <div0>	that is optional, although you sort of have to do it if you want to have some sort of status (e.g. op in a channel)
    Mar 03 10:58:07 <div0>	I'd have no problem if this user auth system is tied to e.g. vote masterä
    Mar 03 10:58:09 <[-z-]>	Hey, can we rewind for a second and brain storm names for this group and project so we can go forward with setting up resources to outline the project and discuss these things with a wiki / forum?
    Mar 03 10:58:13 <div0>	or even required for being allowed to start a vote
    Mar 03 10:58:25 <Dokujisan>	well your main concern is with tracking, like stats of tracking the times that you are online playing.... the aliases would be for avoiding that. You could use your alias names when you don't want to be tracked publicly.
    Mar 03 10:58:38 <div0>	how would that even help?
    Mar 03 10:58:46 <div0>	the server would probably know that I am the same person
    Mar 03 10:58:49 <div0>	and just display other info
    Mar 03 10:59:12 <div0>	I do not WANT the server to know, as I don't have good reasons to trust it
    Mar 03 10:59:42 <Dokujisan>	yes the central server would be the only thing knowing the link between the user account and the alias
    Mar 03 10:59:47 <div0>	thing is basically... in the open source community, many people are also friends of privacy :P
    Mar 03 10:59:51 <Dokujisan>	I'm not sure why you wouldn't trust that
    Mar 03 11:00:03 <Dokujisan>	well this is still supporting privacy, I think
    Mar 03 11:00:04 <div0>	_I_ would because I would have access to that server, and know how it works
    Mar 03 11:00:08 <div0>	how could anyone else be able to trust it?
    Mar 03 11:00:12 <[-z-]>	wouldn't the solution here be for servers to opt into this centralized service?
    Mar 03 11:00:12 <div0>	any "mere player"?
    Mar 03 11:00:38 <Dokujisan>	don't mere players trust websites all the time anyway?
    Mar 03 11:00:43 <div0>	not all
    Mar 03 11:00:45 <Dokujisan>	with registering
    Mar 03 11:00:50 <div0>	e.g. what about all the noscript users? :P
    Mar 03 11:00:58 <div0>	or, you do know bugmenot.com? :P
    Mar 03 11:01:08 <Dokujisan>	well I mean with your example of trusting someone with your email address
    Mar 03 11:01:15 <Dokujisan>	that's one scenario
    Mar 03 11:01:16 <div0>	there IS a large group who is on the side of privacy
    Mar 03 11:01:23 <div0>	I am part of that
    Mar 03 11:01:34 <div0>	I do not want others to be able to track me, when I don't positively allow them to
    Mar 03 11:01:41 <div0>	in a forum it can't be avoided, so it's fine by me
    Mar 03 11:01:52 <div0>	but in a game, it should be avoided
    Mar 03 11:02:02 <div0>	still, you can give good incentives for registering in the game
    Mar 03 11:02:06 <div0>	#just shouldn't enforce it
    Mar 03 11:02:15 <div0>	even nick name coloring could depend on it :P
    Mar 03 11:02:17 <Dokujisan>	do you want to be allowed to spam servers like nadz does?
    Mar 03 11:02:26 <div0>	it can't be helped
    Mar 03 11:02:26 <[-z-]>	just make it an opt in feature
    Mar 03 11:02:29 <div0>	I want to ensure my privacy
    Mar 03 11:02:30 <[-z-]>	by the server admin
    Mar 03 11:02:31 <Dokujisan>	I'm wondering what level of freedom you are after
    Mar 03 11:02:45 <div0>	basically:
    Mar 03 11:02:46 <[-z-]>	90% of the internet uses google, so they clearly don't give a shit about privacy :-P
    Mar 03 11:02:49 <Dokujisan>	this is just a game here. The goal should always be about allowing players to....play the game
    Mar 03 11:02:57 <Dokujisan>	and that is really what moderation is about...or should be about
    Mar 03 11:03:01 <[-z-]>	plus, we can mask their ips from the server if they feel so inclined
    Mar 03 11:03:10 <div0>	IPs are already masked :P
    Mar 03 11:03:12 <div0>	that isn't the problem
    Mar 03 11:03:18 <[-z-]>	yes but I mean with cool names
    Mar 03 11:03:23 <div0>	well
    Mar 03 11:03:25 <[-z-]>	or annoying depending on how you look at them :-P
    Mar 03 11:03:29 <div0>	what about this:
    Mar 03 11:03:35 <[-z-]>	z@my-clan.rockz.net
    Mar 03 11:03:38 <div0>	1. in serious match (like ladder, pickup), you MUST be registered
    Mar 03 11:03:47 <[-z-]>	yes
    Mar 03 11:03:53 <div0>	2. in FFA match, you don't have to be, but if not, you show up as unregistered in the scoreboard
    Mar 03 11:03:56 <Taoki>	Not so much into privacy here, when it comes to Nexuiz. But for those who want it, it is good. Afaik you can just change nickname before entering a server.
    Mar 03 11:04:01 <Dokujisan>	the method for which aliases are used could be public knowledge. Aliases woudln't be trakced. They would only be used to apply moderation actions to an account, when necessary.
    Mar 03 11:04:05 <div0>	   maybe can even only use the marine model and non-colored nicks
    Mar 03 11:04:15 <Taoki>	This reminds me. I hope Nexuiz will have a menu Friends List at some point
    Mar 03 11:04:31 <div0>	Taoki: CURRENTLY I can just change my nick :P
    Mar 03 11:04:45 <div0>	basically... I am fine if I lose features when playing unregisteredly
    Mar 03 11:04:55 <div0>	like nick colors, player model choice
    Mar 03 11:05:07 <div0>	but I want to stay able to
    Mar 03 11:05:20 <div0>	otherwise, I'll have no choice but to create multiple dummy accounts with various email addresses
    Mar 03 11:05:35 <Dokujisan>	div0: I'm mainly asking you to think about the possibilties here that can protect the necessary level of privacy. The main issues with privacy have to do with tracking. The other thing that is useful for a central registration system is to reserve names 
    Mar 03 11:05:39 <div0>	also, I am fine if some servers enforce the registration
    Mar 03 11:05:49 <Dokujisan>	so nobody could use the alias name "divverent"
    Mar 03 11:05:52 <div0>	right
    Mar 03 11:05:54 <div0>	reserving names is good
    Mar 03 11:05:58 <div0>	but well, on IRC it works too
    Mar 03 11:06:12 <div0>	if not registered, what if I then always show up as divverent<UNREGISTERED>
    Mar 03 11:06:20 <div0>	and to be divVerent, I need to registere
    Mar 03 11:06:25 <Dokujisan>	hmm
    Mar 03 11:06:27 <Taoki>	Right... i even forgot there is a traking system. If there is one... I'm shamed to say i don't know yet (like a system that stores how good you are on servers, atc)
    Mar 03 11:06:37 <Dokujisan>	I woudln't want people to play as Dokujisan<UNREGISTERED>
    Mar 03 11:06:44 <div0>	well
    Mar 03 11:06:47 <div0>	you can kick them then :P
    Mar 03 11:06:55 <Taoki>	rcon is its name iirc
    Mar 03 11:07:01 <div0>	if you see a Dokujisan<UNREGISTERED> and a Dokujisan on a server
    Mar 03 11:07:05 <div0>	you know which one is the right one :P
    Mar 03 11:07:20 <Dokujisan>	well *I* do...but a mere player.....
    Mar 03 11:07:33 <div0>	he'll see that you have the cooler color codes
    Mar 03 11:07:38 <div0>	and the other Dokujisan is just plain white :P
    Mar 03 11:08:00 <[-z-]>	maybe he was feeling vanilla and the other one was just being))
    Mar 03 11:08:06 <div0>	lol
    Mar 03 11:08:10 <div0>	the unregistered tag could be ))
    Mar 03 11:08:13 <[-z-]>	haha
    Mar 03 11:08:27 <[-z-]>	halo on xbox live used to have a iconic background
    Mar 03 11:08:32 <[-z-]>	in the names list
    Mar 03 11:08:37 <[-z-]>	well on the scoreboard
    Mar 03 11:08:56 <Dokujisan>	I think when it comes to privacy issues, instead of saying in a blanket fashion "I want my privacy!" is not helpful, but breaking it down into specific concerns or scenarios is something that can be worked with.
    Mar 03 11:08:57 <[-z-]>	for registered (at bungie.net) users
    Mar 03 11:09:10 <div0>	Dokujisan: but well, if you can figure out a way that allows enforced registration without the server (not the auth server either) knowing who you are
    Mar 03 11:09:14 <div0>	then I am fine wiht it
    Mar 03 11:09:23 <div0>	possibly this can be done using digital signatures
    Mar 03 11:09:31 <Dokujisan>	can you help me come up with some solution like that? I would be more than happy to travel down that road.
    Mar 03 11:09:44 <div0>	I don't know one, but find it possible that one exists
    Mar 03 11:09:52 <Dokujisan>	getty talked about using digital signatures for the PlayerID concept
    Mar 03 11:09:59 <div0>	like, with RSA such stuff may be possible
    Mar 03 11:10:18 <div0>	e.g., RSA scheme is "malleable", so you can "edit" an encrypted message without being able tod ecrypt it
    Mar 03 11:10:33 <div0>	this might be useful to implement the "aliases"
    Mar 03 11:10:56 <[-z-]>	Dokujisan: think about integrating the playerID system with wordpress as well.
    Mar 03 11:10:57 <div0>	they might then appear as valid signatures, but the server doesn't know for whom
    Mar 03 11:11:25 <div0>	but of course... then the player also cannot be properly banned
    Mar 03 11:12:16 <Dokujisan>	well we all know that any player can just re-register
    Mar 03 11:12:26 <Dokujisan>	but banning is more about creating resistance
    Mar 03 11:12:39 <Dokujisan>	making it a bit harder for them to act inappropriately
    Mar 03 11:14:22 <div0>	I still wonder if there is a way to combine both
    Mar 03 11:14:26 <Dokujisan>	ip-based banning is more useful. A combination of user account + IP is better.
    Mar 03 11:14:34 <div0>	what if the "player ID" is a different one when talking to a different server
    Mar 03 11:14:46 <div0>	e.g. if the cleint doesn't send the player ID, but a hash of the player ID and the server IP
    Mar 03 11:14:51 <div0>	you then cannot be tracked across servers
    Mar 03 11:14:57 <div0>	but one server can recognize you
    Mar 03 11:15:52 <div0>	or even, if every player immediately gets 9 IDs on registration he can freely choose from, and accumulate stats on
    Mar 03 11:16:04 <div0>	if one is banned, he will of course use the next one
    Mar 03 11:16:08 <div0>	but he only has 9 chances :P
    Mar 03 11:16:19 <div0>	still... he then just reregisters
    Mar 03 11:16:47 <div0>	I am fine if some servers enforce registration of course
    Mar 03 11:16:55 <div0>	but I can tell you straight away, I won't play on such servers
    Mar 03 11:17:00 <Dokujisan>	yes, I really like the idea of enticing people to act appropriately by offering features that benefit longstanding accounts.
    Mar 03 11:17:21 <Dokujisan>	div0: even if the main privacy issues are dealt with?
    Mar 03 11:17:30 <div0>	Dokujisan: I do0ubt they CAN be dealt with
    Mar 03 11:17:35 <div0>	e.g. if a centralized auth server is used
    Mar 03 11:17:40 <div0>	what if it gets hacked?
    Mar 03 11:17:54 <div0>	what if the server admin decides it's a good idea to release all sorts of log data from it?
    Mar 03 11:18:02 <Dokujisan>	if the aliases aren't tracked, then that shouldn't affect the privacy issue that you explained earlier (tracking)
    Mar 03 11:18:07 <div0>	the one piece of ifnormation that I never want to publish, is when and how long I played
    Mar 03 11:18:09 <Dokujisan>	so even if accounts are hacked
    Mar 03 11:18:17 <div0>	how do I _know_ the aliases are not tracked?
    Mar 03 11:18:33 <div0>	there should be some technical means so I can trust it without knowing what thze server does
    Mar 03 11:19:14 <div0>	however, if there are, how could the auth server then possibly recognize me when I am banned?
    Mar 03 11:19:45 <Dokujisan>	every second we're on the internet, we're trusting people. To use a service, there has to be SOME level of trust. When people connect to my nexuiz server, they have to trust me.
    Mar 03 11:19:59 <div0>	how do they even know it is YOUR server?
    Mar 03 11:20:05 <div0>	what if mikeeusa names his server the same :P
    Mar 03 11:20:26 <div0>	okay, you'd notice when you see the crappy maps
    Mar 03 11:20:29 <div0>	but that is after the fact
    Mar 03 11:20:32 <Dokujisan>	so if we have a policy of explaining publicly how the aliases are used (like they aren't tracked like "normal" names) then that woudl go far to helping to build that trust
    Mar 03 11:20:44 <div0>	explaining is not enough
    Mar 03 11:20:51 <div0>	I would demand that they CAN not be tracked
    Mar 03 11:20:54 <div0>	ensured by technical means
    Mar 03 11:21:05 <div0>	this might be possible though
    Mar 03 11:21:16 <Dokujisan>	isn't such a claimn (a privacy policy) a legal thing?
    Mar 03 11:21:21 <div0>	no
    Mar 03 11:21:27 <div0>	nobody is bound to these things anyway
    Mar 03 11:21:35 <div0>	I want such a claim based on how the system actually works
    Mar 03 11:21:42 <div0>	like, based on which info is sent to whom
    Mar 03 11:22:18 <Dokujisan>	how could anyone from a player perspective technically verify that?
    Mar 03 11:22:37 <div0>	well, if the algorithms are open and it is proven that it ensures anonymity
    Mar 03 11:22:46 <div0>	then one can verify it on his own, or ask a cryptography professor about it :P
    Mar 03 11:22:51 <div0>	sort of like how open source works
    Mar 03 11:22:53 <Dokujisan>	and do you always require such technical verification of tracking privacy when you use a service? like irc.quakenet.org?
    Mar 03 11:22:55 <Taoki>	I think I missed part of the convo, but an quick idea; When it comes to keeping your privacy from your client that you are connecting through (in terms of not giving away your IP addreess, etc) maye we can make a client switch for that. Although, that would make it easier for people to avoid ip-based bans.
    Mar 03 11:23:14 <div0>	that is the problem, right
    Mar 03 11:23:32 <div0>	the IP is nothing I am concenred about, as mine is dynamic anyway
    Mar 03 11:24:13 <Dokujisan>	well ok... if the algorithm is open
    Mar 03 11:24:15 <Taoki>	Servers have such an option theirselves. I set mine to allow the IP to be visible.
    Mar 03 11:24:19 <Dokujisan>	then that is another measure to ensure trust
    Mar 03 11:24:23 <div0>	Dokujisan: exactly
    Mar 03 11:24:32 <Dokujisan>	very much like the claim, but just with a little more evidence
    Mar 03 11:24:33 <div0>	and basically, I'd like an open algorithm that allows anonymous clienrts
    Mar 03 11:24:38 <div0>	exactly
    Mar 03 11:25:00 <div0>	actually, there are means for this, now that I think of it
    Mar 03 11:25:06 <div0>	actually, there are means for this, now that I think of it
    Mar 03 11:25:13 <div0>	know the term "electronic money"?
    Mar 03 11:25:26 <div0>	basically, it's a number generated both by a server and by a client
    Mar 03 11:25:27 <Dokujisan>	ok, if such a thing were to happen, and aliases were not tracked like normal registered names would be (for stats), then if someone "hacked" into the central server...they woudln't have access to anything of value aside from an email address
    Mar 03 11:25:31 <div0>	but so that it can be verified, is unique
    Mar 03 11:25:41 <div0>	BUT: the server cannot later find out which client has hte number
    Mar 03 11:25:45 <div0>	as the client made the final calculation
    Mar 03 11:25:55 <div0>	so the client uses a number he calculated together with the server
    Mar 03 11:26:06 <div0>	but the server does not have a way of knowing to which client he gave it
    Mar 03 11:26:12 <div0>	as it doesn't know the final calculation the client did
    Mar 03 11:26:31 <div0>	that is how one could generate an anonymous player ID
    Mar 03 11:26:43 <div0>	it can still be tracked, in that it can be distinguished from others
    Mar 03 11:26:49 <div0>	but nobody can find out who got that ID and when
    Mar 03 11:27:12 <div0>	with 4, 5 of these IDs, I think I'd be anonymous enough
    Mar 03 11:27:31 <div0>	just... why wouldn't XSAX create such an ID too then :P
    Mar 03 11:27:49 <div0>	basically, thsi creates IDs that are, mathematically, "detached" from the identity who ordered them
    Mar 03 11:27:55 <div0>	so I would give the web site my email address
    Mar 03 11:28:03 <div0>	but later it'd be impossible to link the email address to my ID
    Mar 03 11:28:27 <div0>	the web site still would be able to e.g. limit IDs to at most one per email address per week
    Mar 03 11:28:29 <Dokujisan>	so with such a system in place, a system that goes to great lengths to ensure privacy for those who seek it, would you still elect not to use servers that utilize the central registration system?
    Mar 03 11:28:45 <div0>	with such a system, I probably would use servers that use such a system
    Mar 03 11:28:53 <div0>	as I would KNOW that the ID cannot be linked to my identity in any way
    Mar 03 11:29:16 <div0>	also, I would KNOW I can make a new one every week :P
    Mar 03 11:29:32 <div0>	so it can't be used for long-term tracking if I don't want to
    Mar 03 11:29:50 <Dokujisan>	you mean the primary player name? or the aliases?
    Mar 03 11:30:05 <div0>	both
    Mar 03 11:30:13 <div0>	all player IDs could use such a scheme
    Mar 03 11:30:29 <div0>	a player is free to associate the ID with his actual name (e.g. by registering his nickname) at any time
    Mar 03 11:30:52 <div0>	of course, he'd then have to actually KEEP using that ID, or he wouldn't be able to use his nickname any more :P
    Mar 03 11:32:57 <Dokujisan>	so... using the system you described, if I register with the primary name of Dokujisan and I have aliases of Alice and Bob... if I go onto HOCTF server as "Alice" and begin calling people names and spamming. The admin could ban me. If I try to relogin to that server as "Bob", it would maintain the ban? 
    Mar 03 11:33:38 <div0>	no
    Mar 03 11:33:40 <Dokujisan>	the central system would somehow know that "Bob" was also banned
    Mar 03 11:33:46 <div0>	that is impossible
    Mar 03 11:33:55 <div0>	but, you can only register one such ID every week
    Mar 03 11:34:01 <div0>	so a troll would run out fast
    Mar 03 11:34:07 <Dokujisan>	oh I see
    Mar 03 11:34:12 <Dokujisan>	so that is the limiting mechanism
    Mar 03 11:34:15 <div0>	basically:
    Mar 03 11:34:28 <div0>	the ID generating server remembers your address, and prevents too frequent registration
    Mar 03 11:34:33 <div0>	but: it does not know which the ID is that you got
    Mar 03 11:34:47 <div0>	the game can verify your ID - but cannot link it to your address or anything else
    Mar 03 11:34:56 <div0>	unless you voluntarily give the game the info (e.g. by registering your nick)
    Mar 03 11:35:22 <div0>	I can implement that crypto scheme, BTW
    Mar 03 11:35:28 <div0>	I remembered how it works
    Mar 03 11:36:43 <div0>	one keyword for it is "blind signatures"
    Mar 03 11:36:51 <div0>	http://ntrg.cs.tcd.ie/mepeirce/Project/Press/digibro.html
    Mar 03 11:36:54 <div0>	like at the end of that page
    Mar 03 11:38:04 <div0>	in this case, the "bank" does not know which number I wanted it to sign...
    Mar 03 11:38:06 <div0>	but it is not perfect
    Mar 03 11:38:19 <div0>	in that specific protocol, I can still cheat a bit
    Mar 03 11:39:01 <div0>	but that can be prevented too :P
    Mar 03 11:39:20 <div0>	(by requiring the "x" to have a special pattern, that is unlikely to come when you modify the signature)
    Mar 03 11:40:20 <div0>	e.g.: x may be a hash value of a string that is like "NEXIUZ PLAYER ID #43984398"
    Mar 03 11:40:33 <div0>	and as ID, you'd present both the string and the signature
    Mar 03 11:40:45 <div0>	if the hash function is good, you can't manipulate the signature
    Mar 03 11:41:32 <div0>	note that that string would not really be your "ID" :P
    Mar 03 11:41:48 <div0>	so if the number matches between two players, that is no problem, as the signature still would not match
    Mar 03 11:44:08 <div0>	1. s = "NEXUIZ PLAYER ID #474574598798"
    Mar 03 11:44:09 <div0>	2. h = SHA1(s)
    Mar 03 11:44:11 <div0>	3. r = random
    Mar 03 11:44:14 <div0>	4. x = h*r^publickey
    Mar 03 11:44:15 <div0>	5. send x to auth server, get back y which auth server calculates as x^privatekey
    Mar 03 11:44:18 <div0>	6. t = y/r
    Mar 03 11:44:20 <div0>	7. The full player ID is s together with t
    Mar 03 11:44:34 <div0>	to verify, the server would check the ID starts with "NEXUIZ PLAYER ID #", and that the signature matches too
    Mar 03 11:46:01 <div0>	that scheme is from 1983 by the way
    Mar 03 11:46:10 <div0>	so if it was patented, the patents have expired now
    Mar 03 11:47:14 <div0>	I'll probbaly code that soon, but first check it for possible other security problems
    Mar 03 11:48:39 <div0>	have to go now though
    Mar 03 11:48:40 <Dokujisan>	if we could nail down a privacy-safe central user system, that would allow a lot of other features to be added to the game
    Mar 03 11:48:45 <div0>	I'll look up more stuff on it
    Mar 03 11:48:53 <div0>	"electronic money" is the keyword for it though
    Mar 03 11:49:13 <div0>	basically, the general idea is to make sure that not even the owner of the auth server can know WHO owns a specific key
    Mar 03 11:49:40 <div0>	and to provide banning by limiting the number of keys generated
    Mar 03 11:50:18 <div0>	this speciifc scheme has a little problem though, but I once saw the solution for that in a book
    Mar 03 11:50:26 <div0>	I'll check in that book later :P
    Mar 03 11:55:20 <Dokujisan>	in the meantime, -z- and I were scanning around for open domain names as a name alternative to nexuiz
    Mar 03 11:55:25 <Taoki>	Alright, while we're all here. I've had a question for a looong time now (separate from all this). What server do the devs play on? I usually play on the DCC servers, but would have liked to play with div0, [-z-] and all the other core devs once.
    Mar 03 11:55:57 <[-z-]>	recently the HO servers because they are the most well kept USA servers
    Mar 03 11:56:21 <[-z-]>	bbiab, need to get lunch
    Mar 03 11:56:31 <Taoki>	Thanks. USA probably means low ping from Europe
    Mar 03 11:58:48 <[-z-]>	yes but I've played on DCC before and Over the Lazy Dog
    Mar 03 12:02:12 <[-z-]>	lets get brainstorming about names
    Mar 03 12:05:55 <Dokujisan>	NOT AVAILABLE
    Mar 03 12:05:55 <Dokujisan>	nexotic
    Mar 03 12:05:55 <Dokujisan>	nexetic
    Mar 03 12:05:55 <Dokujisan>	nexon
    Mar 03 12:05:55 <Dokujisan>	nexuz
    Mar 03 12:05:55 <Dokujisan>	nexine
    Mar 03 12:05:55 <Dokujisan>	nexean
    Mar 03 12:05:55 <Dokujisan>	nexio
    Mar 03 12:05:55 <Dokujisan>	nexium
    Mar 03 12:05:55 <Dokujisan>	nexun
    Mar 03 12:05:55 <Dokujisan>	xenios
    Mar 03 12:05:55 <Dokujisan>	xenius
    Mar 03 12:05:55 <Dokujisan>	xenoic
    Mar 03 12:05:55 <Dokujisan>	xenotic
    Mar 03 12:05:55 <Dokujisan>	AVAILABLE
    Mar 03 12:05:55 <Dokujisan>	nexotus
    Mar 03 12:05:55 <Dokujisan>	nexaen
    Mar 03 12:05:55 <Dokujisan>	nexilus
    Mar 03 12:05:55 <Dokujisan>	zeniux
    Mar 03 12:20:36 <Taoki>	some proposed Nexiuz, already used for the current site redirect (nexiuz.org ). I also thought about naming it Zymotic, after the dead project which was named that way.
    Mar 03 12:21:24 <Dokujisan>	if it's being forked, I wouldn't use something that would be mistaken for Nexuiz. But a similar-style name would be good.
    Mar 03 12:41:40 <[-z-]>	wwi own nexiuz.org
    Mar 03 13:05:33 <div0>	Taoki: I play on whatever is at the top, or my own
    Mar 03 13:05:43 <div0>	and sometimes arranged stuff with PB
    Mar 03 13:06:14 <div0>	I recently changed my server to KH only, to give better experience maybe
    Mar 03 13:06:30 <Dokujisan>	I could never get into KH. I tried for a week once
    Mar 03 13:06:40 <Dokujisan>	I like clan arena though
    Mar 03 13:06:49 <Dokujisan>	that was a great addition
    Mar 03 13:34:02 <Taoki>	Dokujisan, from the list of names you posted earlier (couldn't think of any on my own, am generally bad with names) the last one, zeniux, sounds prettiest and most fitting. Or a derivate of that.
    Mar 03 13:34:47 <Taoki>	But, before finding a new name, I think m0ost important is finding a way to let people who don't visit the forums and such know that Nexuiz was renamed. Otherwise, many players may think it just vanished forever all of a sudden, and find out in months or years it's still there
    Mar 03 13:35:12 <div0>	well
    Mar 03 13:35:39 <Taoki>	Not sure how that could be done... was thinking that maybe we could find all news articles about Nexuiz on google and see how we could modify each
    Mar 03 13:35:41 <div0>	I do think that Alientrap won't follow the project when we take over
    Mar 03 13:35:43 <div0>	so...
    Mar 03 13:35:52 <div0>	it shouldn't be impossible to get it displayed in game :P
    Mar 03 13:36:00 <div0>	we have ways to show such a notification
    Mar 03 13:36:13 <div0>	yes, the rotating yellow box :P
    Mar 03 13:36:38 <div0>	also, we can organize some server admins, and let them show this when people join their server
    Mar 03 13:36:39 <Taoki>	How? Does the gamecode support a way to show news from an external page?
    Mar 03 13:36:43 <div0>	know my "mikeeusa warning"?
    Mar 03 13:36:49 <div0>	not yet
    Mar 03 13:36:54 <Taoki>	Not really
    Mar 03 13:36:57 <div0>	can onyl show a single line of text in the update notification
    Mar 03 13:37:05 <div0>	but with csqc, you can show a on-join dialog on a server
    Mar 03 13:37:11 <div0>	so if enough server admins would take over that code
    Mar 03 13:37:15 <Taoki>	Wow, i didn't know thre is an update notification.
    Mar 03 13:37:15 <div0>	most people will know
    Mar 03 13:37:48 <Taoki>	Another good idea would be servers (like DCC) putting the news in their MOTD or periodic helper script messages
    Mar 03 13:38:21 <div0>	right
    Mar 03 13:38:26 <div0>	or more visible than MOTD :P
    Mar 03 13:38:31 <div0>	csqc leaves many possibilities for this
    Mar 03 13:38:48 <Taoki>	yeah, there is a way to make a message be echoed to anyone when joining, like normal chat.
    Mar 03 13:39:12 <div0>	that too
    Mar 03 13:39:15 <div0>	but well
    Mar 03 13:39:19 <div0>	we can modify code :P
    Mar 03 13:39:26 <div0>	I have on my server some more-or-less secret feature
    Mar 03 13:39:31 <div0>	that warns that a map is by mikeeusa :P
    Mar 03 13:39:52 <div0>	in form of a dialog box that you have to close by pressing a button
    Mar 03 13:40:44 <Taoki>	hehe realy?
    Mar 03 13:41:15 <Taoki>	fun :P
    Mar 03 13:41:45 <Taoki>	Ooh, right... by having separate CSQC on a server which gets downloaded if it doesn't match yours
    Mar 03 13:41:51 <Taoki>	forgot that :P
    Mar 03 13:42:03 <div0>	right
    Mar 03 13:42:06 <div0>	we can do a LOT with that
    Mar 03 13:42:50 <Taoki>	If we're lucky, we may be able to change the name without loosing a lot of popularity.
    Mar 03 13:43:17 <div0>	we may even gain more
    Mar 03 13:43:32 <div0>	because many players probably still think that Nexuiz is the sucky game it was at 1.x times :P
    Mar 03 13:43:44 <Taoki>	Then, separately, maybe we can google for all news articles which talk about Nexuiz (be them years old) and ask them to change the names, if the admins and system would allow that. So people finding them won't be confused too
    Mar 03 13:43:58 <div0>	no, changing news of the past is bad
    Mar 03 13:44:00 <div0>	don't go there
    Mar 03 13:44:08 <Taoki>	hmm ok then
    Mar 03 13:44:10 <div0>	those who rewrite history are damned to repeat it :P
    Mar 03 13:44:21 <Taoki>	makes sense :)
    Mar 03 13:44:26 <div0>	but, it'd be nice if they could write an update note to the articles :P
    Mar 03 13:45:00 <Taoki>	Yeah, would be excellent. Enough so someone who seen Nexuiz disappeared and goodles Nexuiz gets an article on the first page mentioning it got renamed
    Mar 03 13:45:27 <[-z-]>	I can still post news
    Mar 03 13:45:34 <[-z-]>	I haven't because Vermeulen said he was going to
    Mar 03 13:45:46 <[-z-]>	but he hasn't
    Mar 03 13:47:10 <[-z-]>	unizex :-P
    Mar 03 13:47:22 <Taoki>	:P
    Mar 03 13:47:28 <[-z-]>	zenuxi
    Mar 03 13:47:45 <[-z-]>	zah new zi
    Mar 03 13:48:43 <[-z-]>	have we decided on a name of either the group or game?
    Mar 03 13:48:51 <Taoki>	I like Zeniux or something similar... that was a good idea Dokujisan included.
    Mar 03 13:49:50 <Taoki>	Or Zenuix, would resemble the old name more
    Mar 03 13:53:26 <div0>	we should test the name ideas somehow
    Mar 03 13:53:38 <div0>	like, try them in a typing test software :P
    Mar 03 13:53:44 <div0>	to see which variant gets more misztakes
    Mar 03 13:55:06 <[-z-]>	zenuix sounds the smoothest of all the paladrome names thrown out and is more phonetic than nexuiz :-P
    Mar 03 13:55:06 <Dokujisan>	whatever happens with the name, I would like to spend some time to brainstorm for the right name that has an available .com
    Mar 03 13:55:21 <Dokujisan>	and not pick a name hastily
    Mar 03 13:56:24 <[-z-]>	group name first might help decide the game name
    Mar 03 13:57:06 <[-z-]>	who are we? what brings us together? what are we looking to achieve? who are we looking to attract?
    Mar 03 13:57:09 <Dokujisan>	oh right
    Mar 03 13:57:11 <Dokujisan>	the group name
    Mar 03 13:57:33 <Dokujisan>	with getty, we came up with conflict industries for that group. That works well. For this group... um.....
    Mar 03 13:58:40 <Taoki>	I had been thinking something I mentioned it ysterday. Does anyone believe we may be better without a group name? I seen many projects like that... there are just contributors and no group with a different name. Or they're called "TheProjectName Team"
    Mar 03 13:58:59 <Taoki>	This could, from some angles, and some ways, seem a little bit more free too
    Mar 03 13:59:20 <Dokujisan>	the group name really helps. If the group does not intend to make any other games, then it can go without a separate group, but a name based on the game name
    Mar 03 13:59:24 <[-z-]>	well... it takes a lot of people working together to design, create and distribute te game.
    Mar 03 14:00:03 <[-z-]>	we'll continue to accept contributions and patches from outside parties, divVerent has actually proposed a good way to setup git to accompany this
    Mar 03 14:00:27 <Dokujisan>	like alientrap always intended to make more games than nexuiz. Conflict industries intends to do the same. If this "New Nexuiz" group doesn't intend to make other games, then the group name can be like "Nexuiz Team"
    Mar 03 14:00:40 <Dokujisan>	like my Kickboxing form (called Ax) I call the moderators the "Ax Team"
    Mar 03 14:01:07 <[-z-]>	I'd like to hope we could create more games if not projects together
    Mar 03 14:01:16 <Taoki>	yeah
    Mar 03 14:01:35 <[-z-]>	there are already a few mods that run on top of nexuiz, who knows which way they'll go after the fork
    Mar 03 14:02:03 <[-z-]>	if alientrap drops support, then they'll likely run off our game code
    Mar 03 14:03:36 <Dokujisan>	ok I'm not against the idea of this group working on other games. Sounds great. 
    Mar 03 14:03:38 <Taoki>	I play two other games (about different things) which are open source, and not officially developed by a specific team. Just for the note  if anyone's curious, they are Vdrift http://vdrift.net/ (best opensource car game imo) and glest http://glest.org/en/index.php (best opensource rts game)
    Mar 03 14:05:11 <Taoki>	On the about page of Glest, they say "Glest is made by a bunch of friends, most of them from Spain". Of course this doesn't mean it would be the best idea for Nexuiz.
    Mar 03 14:05:15 <[-z-]>	someone still has to be in control at some point
    Mar 03 14:05:27 <Taoki>	yeah
    Mar 03 14:05:40 <[-z-]>	we're trying to build a group that won't die from having a single or even just 2 leaders
    Mar 03 14:06:00 <[-z-]>	but rather a board or committee, divVerent would like to see 3
    Mar 03 14:06:03 <Dokujisan>	ok what is a creative way of describing that arrangement
    Mar 03 14:06:17 <Dokujisan>	even imagery
    Mar 03 14:06:24 <[-z-]>	who me or Taoki?
    Mar 03 14:06:28 <Dokujisan>	like a wheel with spokes
    Mar 03 14:06:30 <Dokujisan>	you
    Mar 03 14:07:00 <Dokujisan>	the arrangement of the group, or the method upon which it is created
    Mar 03 14:07:17 <[-z-]>	a wheel with spokes connecting to a group (committee) in the center
    Mar 03 14:09:07 <div0>	shouldn't group name the same as the game name?
    Mar 03 14:09:29 <Dokujisan>	well as I said earlier, that depends on whether the group works on multiple games
    Mar 03 14:09:33 <Dokujisan>	if it's just one game, then sure
    Mar 03 14:09:43 <div0>	I don't think we want to
    Mar 03 14:09:51 <div0>	maybe as side projects, with not all members part of it
    Mar 03 14:10:03 <div0>	but that can then be a new group, cooperating with the "nexuiz group"
    Mar 03 14:10:13 <Dokujisan>	ok. I'm fine with that
    Mar 03 14:10:26 <div0>	I mean, such groups are not exclusive
    Mar 03 14:10:33 <[-z-]>	isn't that just a more complicated way of saying we'll figure out a team name later?
    Mar 03 14:10:37 <div0>	e.g. Taoki made that spinoff game once, didn't he?
    Mar 03 14:10:41 <div0>	We could cooperate in that too :P
    Mar 03 14:10:44 <[-z-]>	he's still working on it
    Mar 03 14:10:47 <div0>	e.g. when I provide a build system...
    Mar 03 14:10:57 <div0>	I can happily use my build system for his project too
    Mar 03 14:11:08 <Dokujisan>	I like the idea of just calling it <gamename> Team
    Mar 03 14:11:10 <div0>	even without being part of his development
    Mar 03 14:11:14 <div0>	yes, so do I
    Mar 03 14:11:54 <[-z-]>	k, whatever, I don't care that much about the name
    Mar 03 14:12:01 <Taoki>	That own game i'm making from Nexuiz? I still work on it... just took a brake now since i worked on it a lot at first
    Mar 03 14:12:17 <Taoki>	Also waiting for FruitieX's HUD changes, i'll have to merge these with my hud and stuff. But yeah
    Mar 03 14:12:27 <Dokujisan>	I'm also interested in that game, btw
    Mar 03 14:12:30 <div0>	I just still don't like Zenuix...
    Mar 03 14:12:34 <Dokujisan>	ok
    Mar 03 14:12:40 <div0>	I am not sure if I am interested in that game
    Mar 03 14:12:48 <[-z-]>	it doesn't even have to ben a palindrome
    Mar 03 14:12:53 <div0>	but even if not, I'd have no reason to not help out with e.g. making its release builds
    Mar 03 14:12:55 <[-z-]>	err
    Mar 03 14:12:59 <Taoki>	Thanks Dokujisan :) Not sure how it will be like... it will be something of a different theme. Not sure if i can get it to what i want it to be
    Mar 03 14:13:01 <div0>	anagram
    Mar 03 14:13:04 <[-z-]>	yes, that one :)
    Mar 03 14:13:08 <Dokujisan>	well I like the theme that you described
    Mar 03 14:13:14 <div0>	zenuiz may be better than zenuix BTW
    Mar 03 14:13:21 <div0>	because, I have typo'd zenuiz when trying to write zenuix
    Mar 03 14:13:49 <[-z-]>	xenuiz?
    Mar 03 14:13:52 <div0>	no
    Mar 03 14:13:55 <div0>	that sounds like Xen
    Mar 03 14:13:57 <div0>	which was a flop
    Mar 03 14:14:04 <Taoki>	I'd still like the wat the first name sounds more
    Mar 03 14:14:14 <div0>	which?
    Mar 03 14:14:29 <Taoki>	Zenuix
    Mar 03 14:14:44 <div0>	I just find it too hard to remmeber/type
    Mar 03 14:14:48 <div0>	sort of the same fault as Nexuiz has
    Mar 03 14:15:06 <Taoki>	Yeah, but it kinda sounds and looks prettier
    Mar 03 14:15:29 <div0>	is it pronounced Zen-u-ix, Ze-nu-ix, ze-nu-i-kku-su, or or Zen-i-us?
    Mar 03 14:15:41 <[-z-]>	first
    Mar 03 14:15:46 <div0>	not zenuikkusu?
    Mar 03 14:15:53 <[-z-]>	I mean, you can if you want
    Mar 03 14:16:03 <div0>	(latter is how the japanese would pronounce zenuix)
    Mar 03 14:16:41 <[-z-]>	zenuiz (not japanese)
    Mar 03 14:16:54 <div0>	that name would be way more japanese friendly :P
    Mar 03 14:16:54 <[-z-]>	haha, I just typoed zenuix too
    Mar 03 14:17:10 <div0>	zenuizu would be their katakana writing of it
    Mar 03 14:17:11 <[-z-]>	zen you iz
    Mar 03 14:17:28 <[-z-]>	what does zenuizu mean?
    Mar 03 14:17:31 <div0>	nothing
    Mar 03 14:17:39 <[-z-]>	(we're back with an even harder to pronounce name)
    Mar 03 14:17:41 <div0>	I just spelt it in a sequence of katakana characters
    Mar 03 14:17:52 <div0>	like the japanese do to all foreign words
    Mar 03 14:17:57 *	Dokujisan is brainstorming names and checking for available .coms
    Mar 03 14:18:01 <div0>	e.g. floppy disk = fu-ro-ppi de-i-su-ku
    Mar 03 14:18:19 <[-z-]>	I'm not sure if zenuiz is just because of muscle memory though
    Mar 03 14:18:27 <div0>	yes
    Mar 03 14:18:29 <[-z-]>	what if you asked a random person to type it
    Mar 03 14:18:29 <div0>	that may be too
    Mar 03 14:18:43 <div0>	basically... I think it maybe shouldn't have an ui in it :P
    Mar 03 14:18:47 <[-z-]>	haha
    Mar 03 14:18:56 <[-z-]>	that actually made it easier for me to spell
    Mar 03 14:18:57 <div0>	Inflexion Uzi CL
    Mar 03 14:19:02 <div0>	an anagram to illfonicnexuiz
    Mar 03 14:19:08 <[-z-]>	;)
    Mar 03 14:19:38 <[-z-]>	necksuiz
    Mar 03 14:19:49 <div0>	no, does not solve anything :P
    Mar 03 14:19:55 <[-z-]>	makes it worse lol :)
    Mar 03 14:19:58 <div0>	yes
    Mar 03 14:20:02 <div0>	zeckniuz
    Mar 03 14:20:14 <div0>	no
    Mar 03 14:20:19 <[-z-]>	zexiznice
    Mar 03 14:20:20 <div0>	sounds like a zecke, evil animal in germany
    Mar 03 14:20:29 <div0>	Zexiz
    Mar 03 14:20:32 <div0>	haha :P
    Mar 03 14:20:33 <div0>	"Sex-is"
    Mar 03 14:20:40 <div0>	oh wait
    Mar 03 14:20:46 <div0>	you actually intended that
    Mar 03 14:20:49 <[-z-]>	yeah :-P
    Mar 03 14:21:04 <[-z-]>	I would never suggest that as a real game name lol
    Mar 03 14:21:08 <div0>	Xettius
    Mar 03 14:21:15 <[-z-]>	:mind sploded:
    Mar 03 14:21:18 <div0>	oh, I had first parsed it as "zexis - nice"
    Mar 03 14:21:26 <div0>	*z
    Mar 03 14:21:29 <[-z-]>	hehe
    Mar 03 14:21:49 <div0>	Textius - the text adventure port
    Mar 03 14:22:03 <Dokujisan>	man... a lot of strange domain names are already taken
    Mar 03 14:22:05 <[-z-]>	do we even want to stick with these weird arrangements of letters?
    Mar 03 14:22:08 <Dokujisan>	AVAILABLE .COMs
    Mar 03 14:22:08 <Dokujisan>	nexotus
    Mar 03 14:22:08 <Dokujisan>	nexilus
    Mar 03 14:22:08 <Dokujisan>	zeniux
    Mar 03 14:22:08 <Dokujisan>	xepharis
    Mar 03 14:22:08 <Dokujisan>	xaleco
    Mar 03 14:22:08 <Dokujisan>	xeleka
    Mar 03 14:22:08 <Dokujisan>	xeleca
    Mar 03 14:22:08 <Dokujisan>	xelecon
    Mar 03 14:22:10 <div0>	You are standing on a pink reflecting floor. You hear rocket noises.+
    Mar 03 14:22:12 <div0>	> GO LEFT
    Mar 03 14:22:21 <div0>	does anyone recognize the map?
    Mar 03 14:22:21 <[-z-]>	we want a .org though, no?
    Mar 03 14:22:25 <div0>	see, text adventure works
    Mar 03 14:22:26 <div0>	yes
    Mar 03 14:22:31 <Dokujisan>	if the .com is available, the .org definitely is
    Mar 03 14:22:34 <Dokujisan>	and I think we should get both
    Mar 03 14:22:38 <Dokujisan>	and redirect the .com
    Mar 03 14:22:44 <div0>	Xepharis wtf
    Mar 03 14:22:49 <div0>	reminds of the old Project Alaris
    Mar 03 14:22:57 <Dokujisan>	just brainstorming. I started with nex*
    Mar 03 14:22:58 <[-z-]>	xenuiz haha (xenu is)
    Mar 03 14:23:03 <Dokujisan>	haha
    Mar 03 14:23:13 <div0>	no, cannot accept that with my belief :P
    Mar 03 14:23:22 <[-z-]>	haha, I'm just kidding
    Mar 03 14:23:28 <div0>	but I would never have spotted it
    Mar 03 14:23:42 <[-z-]>	?
    Mar 03 14:23:48 <div0>	rather rejected that suggestion above because it started with Xen, and Xen was unsuccessful virtualization
    Mar 03 14:23:55 <[-z-]>	ah yes :-P
    Mar 03 14:23:58 <div0>	(replaced by KVM)
    Mar 03 14:24:23 <div0>	Davius
    Mar 03 14:24:27 <div0>	from [Dave]
    Mar 03 14:24:30 <[-z-]>	:-P
    Mar 03 14:24:33 <Dokujisan>	haha
    Mar 03 14:24:44 <[-z-]>	daviuz?
    Mar 03 14:24:48 <div0>	or maybe even Daviuz
    Mar 03 14:24:57 <div0>	but it gets in the hard-to-spell region again
    Mar 03 14:25:01 <div0>	Dave Ius
    Mar 03 14:25:07 <div0>	"The justice of Dave"+
    Mar 03 14:25:14 <[-z-]>	davefps
    Mar 03 14:25:21 <div0>	DaveDaveDave
    Mar 03 14:25:24 <[-z-]>	or just dave
    Mar 03 14:25:30 <div0>	KillDave
    Mar 03 14:25:38 <[-z-]>	killdavekill
    Mar 03 14:26:01 <[-z-]>	gokilldave
    Mar 03 14:26:02 <div0>	OMGTKDave
    Mar 03 14:26:12 <div0>	(Bastards edition)
    Mar 03 14:26:30 <div0>	Davidiuz
    Mar 03 14:26:38 <[-z-]>	davefps.org is available
    Mar 03 14:26:51 <div0>	is anyone here called Dave? :P
    Mar 03 14:26:58 <div0>	I mean, apart from everyone ;)
    Mar 03 14:27:01 <[-z-]>	:-P
    Mar 03 14:27:05 <[-z-]>	no
    Mar 03 14:27:15 <div0>	BTW, I had reliable sources tell me that morphed would be in our team too
    Mar 03 14:27:30 <Dokujisan>	I suspect that most would want to move over
    Mar 03 14:27:36 <div0>	just wanted to say
    Mar 03 14:27:40 <div0>	if we can even get morphed
    Mar 03 14:27:42 <Dokujisan>	but yes, that is good
    Mar 03 14:27:43 <div0>	we'd get everyone :P
    Mar 03 14:27:46 <[-z-]>	it's good to have his support
    Mar 03 14:28:10 <div0>	morphed may work uncleanly, and be a bit weird-creative... so he often has to be put in his bounds :P but we need that creativity
    Mar 03 14:28:11 <[-z-]>	we need to get setup so we have something for them to move to
    Mar 03 14:28:17 <Dokujisan>	is it possible to do this without telling mikee about it?
    Mar 03 14:28:24 <div0>	no
    Mar 03 14:28:28 <Dokujisan>	:-)
    Mar 03 14:28:29 <div0>	but we can wait with telling mikee
    Mar 03 14:28:34 <div0>	mikee isn't too clever to find out on his own
    Mar 03 14:28:47 <div0>	it's just that he reads the forum
    Mar 03 14:28:55 <div0>	as for hosting... well, we could use the icculus repository
    Mar 03 14:29:03 <div0>	but I'd prefer it on the new domain
    Mar 03 14:29:10 <[-z-]>	is everyone good with davefps ?
    Mar 03 14:29:14 <div0>	[-z-]: how expensive is domain hosting with "sort of unlimited" traffic?
    Mar 03 14:29:18 <div0>	DaveFPS... not so sure yet
    Mar 03 14:29:20 <div0>	but maybe
    Mar 03 14:29:21 <[-z-]>	~$120 a year
    Mar 03 14:29:22 <div0>	a bit too generic maybe
    Mar 03 14:29:24 <div0>	googling it
    Mar 03 14:29:31 <div0>	$10 a month... sounds okay
    Mar 03 14:29:35 <div0>	so we could put the git on it too
    Mar 03 14:29:42 <div0>	and with shell access?
    Mar 03 14:29:46 <div0>	(for making the builds)
    Mar 03 14:29:47 <[-z-]>	I believe they support git now yes
    Mar 03 14:29:52 <[-z-]>	and multiple unix accounts, yes
    Mar 03 14:29:58 <div0>	they don't have to support git :P
    Mar 03 14:30:01 <[-z-]>	and sftp only accounts
    Mar 03 14:30:09 <div0>	we can install it in one of the unix accounts
    Mar 03 14:30:13 <div0>	and set up gitolite on it
    Mar 03 14:30:22 <div0>	that is actually how you host git
    Mar 03 14:30:28 <[-z-]>	div0: well they also have a web frontend, I don't know how helpful it is for setting up git though
    Mar 03 14:30:41 <div0>	only problem wqould be the git daemon, that probably would require asking them and them saying "go ahead, you can use the network port"
    Mar 03 14:30:54 <div0>	for repository write access you go through ssh anyway
    Mar 03 14:31:10 <[-z-]>	http://wiki.dreamhost.com/Git
    Mar 03 14:31:17 <div0>	for the record, git is port 9418
    Mar 03 14:31:24 <Taoki>	I need to go for the next 1-2 hours. See you all when I get back, take care. I'll try to think of a new name more :)
    Mar 03 14:31:37 <[-z-]>	okay Taoki, see you
    Mar 03 14:32:19 <div0>	only problem is, they write that they currently do not support git-daemon
    Mar 03 14:32:21 <div0>	that is a setback
    Mar 03 14:32:31 <[-z-]>	well, why not stay on icculus?
    Mar 03 14:32:45 <div0>	could do that too, at least for a start
    Mar 03 14:32:47 <Dokujisan>	isn't icculus slow?
    Mar 03 14:32:51 <div0>	that it is
    Mar 03 14:32:53 <Dokujisan>	I always got that impression from it
    Mar 03 14:32:57 <div0>	I just think this should be hosted on the project domain, if possible
    Mar 03 14:33:08 <div0>	if nothing else works, we can still offer the git read access via http
    Mar 03 14:33:12 <div0>	but that will sometimes fail
    Mar 03 14:33:39 <div0>	can still have a readonly clone of it on other hosts :P
    Mar 03 14:34:01 <[-z-]>	hmm, I can't really offer the vps up if it's going to be running gameservers
    Mar 03 14:34:04 <div0>	so actually, we could offer readonly access via http or on icculus, and otherwise use dreamhost
    Mar 03 14:34:06 <div0>	thagt would work
    Mar 03 14:34:41 <div0>	via http may be good enough, git devs say we should not do that, but I don't know why other than one has to regularily call git-update-server-info
    Mar 03 14:35:17 <Dokujisan>	hmm... ok I'm liking xun* as a prefix
    Mar 03 14:35:40 <[-z-]>	I dunno :-\
    Mar 03 14:35:40 <Dokujisan>	man, soooo many strange domain names are taken.
    Mar 03 14:39:37 <div0>	Xunius?
    Mar 03 14:39:38 <div0>	Xunion?
    Mar 03 14:43:28 <Dokujisan>	more avialable .coms...
    Mar 03 14:43:29 <Dokujisan>	xuniam
    Mar 03 14:43:29 <Dokujisan>	xuniox
    Mar 03 14:43:29 <Dokujisan>	xunium
    Mar 03 14:43:29 <Dokujisan>	xundem
    Mar 03 14:43:29 <Dokujisan>	xunius
    Mar 03 14:43:29 <Dokujisan>	xuniux
    Mar 03 14:43:29 <Dokujisan>	xudex
    Mar 03 14:44:26 <Dokujisan>	xodim
    Mar 03 14:44:35 <div0>	[-z-]: does dreamhost support CGI?
    Mar 03 14:46:50 <div0>	because if it does
    Mar 03 14:46:53 <[-z-]>	hmm, I believe so
    Mar 03 14:46:54 <div0>	we can cleanly host git over HTTP
    Mar 03 14:46:56 <div0>	(for newer git clients)
    Mar 03 14:47:05 <div0>	for older clients, it'll fall back to the a bit clumsy HTTP method
    Mar 03 14:47:06 <div0>	but still work
    Mar 03 14:47:12 <div0>	just download more data than needed
    Mar 03 14:48:11 <div0>	oh, cronjobs?
    Mar 03 14:48:39 <div0>	(not THAT important for us, though)
    Mar 03 14:51:29 <Dokujisan>	xodem
    Mar 03 14:51:29 <Dokujisan>	xotux
    Mar 03 14:51:29 <Dokujisan>	nodium
    Mar 03 14:52:50 <div0>	Tuxius
    Mar 03 14:52:57 <div0>	Tuxiuz
    Mar 03 14:52:59 <div0>	is hard to type
    Mar 03 15:04:02 <Dokujisan>	dellum
    Mar 03 15:04:14 <Dokujisan>	nodius
    Mar 03 15:04:14 <Dokujisan>	xodeos
    Mar 03 15:04:14 <Dokujisan>	modiem
    Mar 03 15:04:14 <Dokujisan>	xovium
    Mar 03 15:04:14 <Dokujisan>	xovim
    Mar 03 15:05:38 <Dokujisan>	xendem
    Mar 03 15:06:13 <Dokujisan>	xelod
    Mar 03 15:06:39 <Dokujisan>	xilod
    Mar 03 15:13:07 <Dokujisan>	microsoftiux
    Mar 03 15:13:10 <Dokujisan>	..j/k
    Mar 03 17:02:48 <Taoki>	Back. Thought abouc a little new bunch of names...
    Mar 03 17:02:50 <Taoki>	*about
    Mar 03 17:03:16 <Taoki>	Not really the best but oh well. My list is:
    Mar 03 17:03:39 <Taoki>	Zenuix, Zenux, Zenus, Nexuz
    Mar 03 17:03:56 <Taoki>	the 2nd and 3rd sound best to me. As for team names,
    Mar 03 17:05:17 <Taoki>	I'm totally not good at these so my ideas are mostly silly. Was still thinking of something with Alien... the only idea that came to my mind was openAlien (please ignore this though... I mean... :P ) Another idea about the team name, was something related to nexuizninjaz, which imo has been a great resource. Something having to do with that would be nice to
    Mar 03 17:05:38 <Taoki>	Like, openNinjaz, Alien Ninjaz... these are just sillq quick thoughts once again
    Mar 03 17:08:35 <Taoki>	Sorry for the several typos >.>
    Mar 03 17:12:15 <Taoki>	What does everyone think? Would Zenux (without the i like my previous suggestion) or Zenus be anything good?
    Mar 03 17:17:35 <Taoki>	I like the idea of something that contains both Z and X
    Mar 03 18:52:36 <[-z-]>	hahaah, mikeeusa's suggestion:
    Mar 03 18:52:37 <[-z-]>	Nexuiz:Depreciated
    Mar 03 18:53:00 <[-z-]>	he goes on to say
    Mar 03 18:53:02 <[-z-]>	"but translated into german so it sounds germanish. German is... a dark tounge. Makes everything sound strenghtful."
    Mar 03 18:54:34 <Taoki>	hehe
    Mar 03 18:56:15 *	Samual (~sam@c-24-131-80-234.hsd1.pa.comcast.net) has joined #notnexuiz
    Mar 03 18:56:20 <Samual>	Heh
    Mar 03 18:56:21 <Samual>	Clever.
    Mar 03 18:56:31 <[-z-]>	welcome Samual
    Mar 03 18:56:43 <Samual>	Who is active/idle?
    Mar 03 18:56:59 <[-z-]>	Taoki is active, div0 and Dokujisan might be around
    Mar 03 18:57:20 <[-z-]>	we were discussing creating a group based around the fork of the yet to be named game
    Mar 03 18:57:40 <[-z-]>	something with a better spread of power distributed across a few "major leaders"
    Mar 03 18:58:12 <Taoki>	I'm hre
    Mar 03 18:58:16 <Samual>	Well meh
    Mar 03 18:58:34 <[-z-]>	we've talked about servers, repository hosting and what not
    Mar 03 18:58:45 <[-z-]>	it sounds like we have enough to continue building releases cross platform
    Mar 03 18:59:26 <[-z-]>	we can take the time to get more organized from a web point of view as well
    Mar 03 18:59:28 <Samual>	It's a huge step to abandon Nexuiz though :P
    Mar 03 18:59:37 <[-z-]>	do you want to stay under alientrap?
    Mar 03 18:59:52 <Samual>	Well
    Mar 03 19:00:12 <Samual>	Vermeulen fails, but it's -- It's still hard to abandon Nexuiz :P
    Mar 03 19:00:35 <[-z-]>	it's no longer nexuiz and the sooner we all accept that, the sooner we can move on
    Mar 03 19:01:35 <Samual>	Meh.
    Mar 03 19:02:14 <[-z-]>	it sucks but there isn't much we can do
    Mar 03 19:02:33 <Samual>	I'd much rather work on a game with new content though.
    Mar 03 19:04:05 <Samual>	Not necessarily different gameplay, just new artwork/design. If there's one thing that has been shown with this is that an overall theme for a game can go a long way to making it look consistently good.
    Mar 03 19:09:05 <Taoki>	New content will come over time. Hopefully, some new artwork too. Of course, I hope no one is really thinking about throwing away everything that has been done in 5 years and starting from a scratch.
    Mar 03 19:11:24 <Taoki>	What was done so far is too good and too important. And I'm sure that in a few years from now, it will be incredible compared to what it is now
    Mar 03 19:11:43 <Taoki>	(I'm still dreaming about this project looking like UT3, someday :P )
    Mar 03 19:12:44 <[-z-]>	I'm willing to submit more and may be able to get more from others, we just need to outline our needs
    Mar 03 19:14:14 <Taoki>	I wish I could model. I can hardly make a boulder in Blender though :(
    Mar 03 19:15:08 <Taoki>	I can edit existing models to some point (how I made my vixens from pyria) but new models at the quality of the UT 2k4 / UT 3 guns... those have to be very hard to make
    Mar 03 19:20:58 <Samual>	lawl anyway I think i'm done with Nexuiz officially now, since this person clearly has no intention of changing the name and he doesn't want to listen to the community much.
    Mar 03 19:22:33 <Taoki>	It would be sad if you left, Samural. Would be sad if anyone really left...
    Mar 03 19:26:29 <Samual>	lawl well everyone here has been discussing leaving too anyway
    Mar 03 19:26:54 *	[-z-] gives channel operator status to Samual
    Mar 03 19:26:58 <Taoki>	If anyone wants to leave, it is of course their choice. I just want to highlight that... in my vision this is not a reason to completely loose faith. Because the project we kept working on for all these years is still here, and will always be here. So if we were with Nexuiz for these years because we liked -it-, although this has undoubtfully upset us greatly, we can keep being with it from now on
    Mar 03 19:27:44 <[-z-]>	I just don't want to work for a "Company" that represents such shiesty practices
    Mar 03 19:27:46 <Taoki>	It is still th same code, same experience, etc. If the reason was to modify this code, and parts of what the game is now, and to enjoy what exists in it, then this won't stop us
    Mar 03 19:28:43 <Taoki>	Whatever its name will change to, its the same thing you will see when you load a map or the menu. Except the name banner which will be changed too. That doesn't go away... if thats what we've been with Nexuiz for we haven't lost anything.
    Mar 03 19:31:15 <Dokujisan>	hey Samual 
    Mar 03 19:31:30 <Samual>	Hai.
    Mar 03 19:31:46 <Dokujisan>	here is what I've searched so far in terms of domain names
    Mar 03 19:31:48 <Dokujisan>	http://pastie.org/private/z1hlw1gs1d4nrxdvbisxsw
    Mar 03 19:33:17 <Taoki>	Right... i wax curious what everyone thinks of my last two name ideas
    Mar 03 19:33:18 <Taoki>	[00:11:51] <@Taoki> What does everyone think? Would Zenux (without the i like my previous suggestion) or Zenus be anything good?
    Mar 03 19:33:44 <Dokujisan>	I always go by available domain names
    Mar 03 19:33:50 <Dokujisan>	and zenux.com isn't available
    Mar 03 19:34:11 <Dokujisan>	otherwise, that's a good name to consider
    Mar 03 19:34:59 <Taoki>	hmm...
    Mar 03 19:38:14 <Taoki>	From that list, my favs would be zeniux, xaleco, xuniox, xodeos
    Mar 03 19:38:16 *	Rad_Ished (~Dooley@cpc3-aztw19-0-0-cust362.aztw.cable.virginmedia.com) has joined #notnexuiz
    Mar 03 19:38:21 <[-z-]>	hey Rad_Ished
    Mar 03 19:38:25 <Taoki>	hi
    Mar 03 19:38:39 <[-z-]>	zeniux or zenuiz?
    Mar 03 19:38:40 <Rad_Ished>	hey folks, i like not nexuiz
    Mar 03 19:38:43 <Rad_Ished>	good name
    Mar 03 19:38:54 <[-z-]>	Rad_Ished: we've been trying to come up with a real one :-P
    Mar 03 19:38:59 <Rad_Ished>	heh
    Mar 03 19:39:17 <Taoki>	z, I would prefer the first between the two
    Mar 03 19:39:18 <Rad_Ished>	zenuiz works for me
    Mar 03 19:39:27 <Rad_Ished>	ahhh zexnuix
    Mar 03 19:39:37 <Taoki>	zeniux
    Mar 03 19:39:39 <Rad_Ished>	i meant argh
    Mar 03 19:39:43 <[-z-]>	nexzex
    Mar 03 19:39:45 <Rad_Ished>	yeh , what he said
    Mar 03 19:39:50 <Rad_Ished>	nooo
    Mar 03 19:40:00 <Rad_Ished>	zeniux
    Mar 03 19:40:14 <Rad_Ished>	i don't feel im really adding anything here
    Mar 03 19:40:24 <Dokujisan>	<Dokujisan> here is what I've searched so far in terms of domain names
    Mar 03 19:40:24 <Dokujisan>	<Dokujisan> http://pastie.org/private/z1hlw1gs1d4nrxdvbisxsw
    Mar 03 19:40:46 <Rad_Ished>	i  thought that mikee's post was profound
    Mar 03 19:40:49 <[-z-]>	we want a .org though, no?
    Mar 03 19:41:21 <[-z-]>	xenix lol
    Mar 03 19:41:22 <[-z-]>	penix
    Mar 03 19:41:51 <Taoki>	Atm, my vote's on zeniux / zenuix / zenius
    Mar 03 19:41:53 <Taoki>	:P
    Mar 03 19:42:05 <Taoki>	or derivates of these
    Mar 03 19:42:06 <Samual>	Sexuiz is good
    Mar 03 19:42:10 <Samual>	But well
    Mar 03 19:42:12 <Rad_Ished>	zenuix
    Mar 03 19:42:13 <Taoki>	:))
    Mar 03 19:42:31 <Samual>	Zexun?
    Mar 03 19:42:36 <[-z-]>	haha, bit of trivia for ya'll, "throng" is a crowd of people
    Mar 03 19:42:49 <[-z-]>	zexin
    Mar 03 19:42:57 <Samual>	Zexin too
    Mar 03 19:43:02 <Samual>	I like that >.>
    Mar 03 19:43:03 <[-z-]>	 zexin.org	AVAILABLE
    Mar 03 19:43:19 <Samual>	^_^
    Mar 03 19:43:23 <Samual>	.com?
    Mar 03 19:43:27 <[-z-]>	5 letters, not bad
    Mar 03 19:43:29 <[-z-]>	no .com is taken
    Mar 03 19:43:32 <[-z-]>	but do we want .com?
    Mar 03 19:43:32 <Taoki>	Zexin sounds goodish, yeah
    Mar 03 19:43:43 <[-z-]>	sqautter has it
    Mar 03 19:44:10 <Samual>	Nizex?
    Mar 03 19:44:12 <Samual>	lawl
    Mar 03 19:46:02 <[-z-]>	 nexiz.org AVAILABLE
    Mar 03 19:46:09 <[-z-]>	probably too similar
    Mar 03 19:46:14 <Samual>	Yeah that's too similar
    Mar 03 19:46:14 <Samual>	lawl
    Mar 03 19:52:29 <Dokujisan>	I really think it's valuable to have the .com
    Mar 03 19:52:44 <Dokujisan>	but if we don't have that as a requirement, then scan through those names I checked that are not available .coms
    Mar 03 19:53:00 <[-z-]>	yean but we're not really a company?
    Mar 03 19:53:04 <[-z-]>	more an organization
    Mar 03 19:53:06 <Dokujisan>	it's not about that
    Mar 03 19:53:09 <Dokujisan>	people know .coms
    Mar 03 19:53:21 <Dokujisan>	when they look for a website, they look for a .com
    Mar 03 19:53:22 <Dokujisan>	first
    Mar 03 19:53:52 <Taoki>	true
    Mar 03 19:55:05 <Dokujisan>	I can't count how many times I accidentally went to alientrap.com 
    Mar 03 19:57:45 <Taoki>	From my favorite names, zeniux.com seems to be the only one in that list
    Mar 03 19:58:31 <Taoki>	When will the name be finally decided? I think, there are a few choices now. I was thinking of taking our top 5-6 ideas for names (if we have that much) and making a pool on the forums
    Mar 03 19:59:18 <Dokujisan>	I think we should definitely take time to pick the name
    Mar 03 19:59:43 <Dokujisan>	in the meantime, a lot of discussion can be done about other details
    Mar 03 20:01:37 *	Rad_Ished has quit ("haha.. AAAHHHAAAaaARRR!!!  .. ow")
    Mar 03 20:05:16 <Taoki>	Well, now that I brought that up. When might Nexuiz have player, item and weapon models that would make it look super-modern like Quake4 / UT3? Of course they won't fall from the sky, but I've wondered that for a while
    Mar 03 20:05:34 <Taoki>	http://www.legitreviews.com/images/reviews/365/quake4_t.jpg / http://www.happypenguin.org/images/quake4.jpg Just imagining Nexuiz looking like that sometime... :)
    Mar 03 20:10:29 <Dokujisan>	well one thing that could have been handled better in existing nexuiz is recruitment. I have talked to a large handful of people who were interested in getting involved in nexuiz, but they weren't given enough direction or help with getting involved and they ended up leaving. 
    Mar 03 20:11:06 <Dokujisan>	people who handle recruitment and managing newcomers to the project don't need to be top developers
    Mar 03 20:11:24 <Dokujisan>	especially if there is some sort of outline for that sort of thing
    Mar 03 20:12:15 <Dokujisan>	there was only one official push (to my knowledge) from alientrap to attract new developers, and I think that effort seemed pretty successful in attracting developers
    Mar 03 20:12:24 <Dokujisan>	but a lot of those developers showed and then eventually left
    Mar 03 20:12:47 <Dokujisan>	so more campaigns to attract more talent to the project woudl be very helpful
    Mar 03 20:13:14 <Dokujisan>	these are the kinds of things that should be a part of an open source game like this, imo
    Mar 03 20:20:36 <Taoki>	I agree. I seen posts about people who wanted to come and help, but after that we haven't heard anything about them
    Mar 03 20:22:36 <Dokujisan>	I always though that if I were a part of alientrap, I would have personally talked with those people to make sure they are kept informed and busy
    Mar 03 20:23:01 <Dokujisan>	but as a simple member of the community, it wasn't really my place. I didn't even know who was coming to alientrap
    Mar 03 20:26:02 <Taoki>	yeah
    Mar 03 20:37:06 <Samual>	I contacted most the people on the "We need developers" thread.
    Mar 03 20:38:08 <Samual>	--- Most of the time they were interested and sent emails back, but they never really showed up.
    Mar 03 21:03:39 <Taoki>	Sorry for the delay... got busy with some other things from another channel. Going to bed in a minute too. Anyway, I know some topics were fional works are already released, but there was no feedback given on it.
    Mar 03 21:04:29 <Taoki>	blkrbt still has 3 songs ready to be committed for at least 4 months iirc. Same as tZork's songs, about 8 of them I think (if I remember correctly again). There was also someone who made an awesome high quality robot model 6 months ago, no one said anything about that either.
    Mar 03 21:04:35 <Taoki>	Maybe i should try finding that topic again
    Mar 03 21:12:40 *	TVR (~TVR@96.49.107.196) has joined #notnexuiz
    Mar 03 21:13:02 <TVR>	Glad to see you are all on board.
    Mar 03 21:14:34 <Taoki>	Hello :)
    Mar 03 21:15:41 <TVR>	Hey Taoki, has tZork been notified?
    Mar 03 21:15:49 <Taoki>	What about?
    Mar 03 21:20:08 <TVR>	He doesn't seem pleased about the actions of Vermeulen and LordHavoc selling a GPL version of his source code.
    Mar 03 21:21:19 <Taoki>	Yeah, he spoke about this on the channel too. Hope he won't be leaving the project, would be sad if anyone did
    Mar 03 21:21:27 <Taoki>	Aah, found what I was looking for.
    Mar 03 21:21:34 <Taoki>	I'll post all 3 links
    Mar 03 21:23:10 <TVR>	Yes, that would be great.
    Mar 03 21:24:09 <Taoki>	http://alientrap.org/forum/viewtopic.php?p=69763#p69763 - The robot model I mentioned. Imo it looks awesome. No one gave any feedback since Novemver 2009.
    Mar 03 21:24:09 <Taoki>	http://www.alientrap.org/forum/viewtopic.php?p=74456#p74456 Scorp's songs (not tzork sorry), only the on for the tutorial map included.
    Mar 03 21:24:09 <Taoki>	http://forum.alientrap.org/viewtopic.php?p=70446#p70446 3 songs by blkrbt, which haven't been reviewed for many months either
    Mar 03 21:24:31 <Taoki>	Sorry about that TVR... posted before mentioning some forgotten contributions previously
    Mar 03 21:25:21 <Taoki>	And these are only the ones I know of
    Mar 03 21:26:18 <TVR>	Is that media FOSS?
    Mar 03 21:26:45 <Taoki>	Not sure... it shold be gpl iirc
    Mar 03 21:27:23 <Taoki>	Anyway, i need to run now. Late here. See you all tomorrow
    Mar 03 21:30:36 <[-z-]>	wtf keybord
    Mar 03 21:30:53 <[-z-]>	/\ /\nd $ $topped working
    Mar 03 21:32:09 <TVR>	Totally unresponsive?
    Mar 03 21:43:48 *	Taoki has quit (Ping timeout: 364 seconds)
    Mar 03 21:57:48 <[-z-]>	working again
    Mar 04 00:13:12 <TVR>	[-z-]: Have you contacted the Free Software Foundation, and/or EFF?
    Mar 04 01:54:12 *	TVR has quit (Remote host closed the connection)
    Mar 04 03:35:37 <div0>	Zenux is a Linux distro (or should be).
    Mar 04 03:35:46 <div0>	Zenus... well, I would like to keep the x somewhere :P
    Mar 04 03:35:52 <div0>	OpenAlien... please not ;)
    Mar 04 03:35:57 <div0>	(AlienArena, OpenArena...)
    Mar 04 03:36:33 <div0>	[01:00:49] <Samual> Vermeulen fails, but it's -- It's still hard to abandon Nexuiz :P
    Mar 04 03:36:35 <div0>	[01:01:11] <@[-z-]> it's no longer nexuiz and the sooner we all accept that, the sooner we can move on
    Mar 04 03:36:39 <div0>	it's not abandoning, but just renaming
    Mar 04 03:36:44 <div0>	we wouldn't have to abandon much
    Mar 04 03:36:55 <div0>	maybe we should abandon the old evil* texture sets if we release under a new name anyway
    Mar 04 03:37:34 <div0>	and half the maps :P
    Mar 04 03:37:45 <div0>	on the other hand, we CAN include quite some public released maps of our taste :P
    Mar 04 03:37:51 <div0>	(but please not ANY greatwall)
    Mar 04 03:38:17 <div0>	So actually... why don't we go for a teamplay focus in the "forked game"?
    Mar 04 03:38:41 <div0>	let's try to include 5 CTF maps, and 5 DM maps that ALSO are suitable for keyhunt and Domination, and 2 or 3 Onslaught maps
    Mar 04 03:58:06 <div0>	[03:24:50] <@Taoki> http://www.alientrap.org/forum/viewtopic.php?p=74456#p74456 Scorp's songs (not tzork sorry), only the on for the tutorial map included.
    Mar 04 03:58:08 <div0>	[03:24:50] <@Taoki> http://forum.alientrap.org/viewtopic.php?p=70446#p70446 3 songs by blkrbt, which haven't been reviewed for many months either
    Mar 04 03:58:18 <div0>	as for songs: I normally like to include them only when they are actually used by the game
    Mar 04 03:58:27 <div0>	but well, this would now be a good point to do it, and remove some songs by elysis :P
    Mar 04 05:11:41 <div0>	okay, I finished the flaw in the player ID system I proposed :P
    Mar 04 05:19:21 <div0>	http://paste.debian.net/62392/
    Mar 04 05:19:31 <div0>	note: the patent for Schnorr identification expired last year :P
    Mar 04 05:20:04 <div0>	so we can actually use it
    Mar 04 05:20:36 <div0>	this prtoocol generates a player ID the generating server cannot trace back...
    Mar 04 05:20:56 <div0>	and the old version had the flaw that an attacker who sniffed the ID of another player can impersonate him by simply providing the same ID
    Mar 04 05:33:54 <div0>	that is then almost the perfect player ID system - nobody has to trust anyone for it to work :P
    Mar 04 05:34:17 <div0>	(well, one has to trust the client application that it actually does perform the protocol... but in open source that can be verified easily)
    Mar 04 06:15:44 <Dokujisan>	<div0> So actually... why don't we go for a teamplay focus in the "forked game"?
    Mar 04 06:15:49 <Dokujisan>	I like that thinking
    Mar 04 06:18:04 <Dokujisan>	<div0> it's not abandoning, but just renaming
    Mar 04 06:18:04 <Dokujisan>	<div0> we wouldn't have to abandon much
    Mar 04 06:18:25 <Dokujisan>	the one thing that I'm hopeful for is the ability to do the things in this fork that weren't done in previous nexuiz
    Mar 04 06:19:07 <div0>	which are?
    Mar 04 06:19:44 <Dokujisan>	If I had my way, I would take these community-driven efforts that I've done in nexuiz and ramp them up, place heavy focus on them
    Mar 04 06:20:06 <div0>	well, which are these?
    Mar 04 06:20:15 <Dokujisan>	ok I'll explain what I've done...
    Mar 04 06:20:28 <div0>	I mean, do you mean stuff game code-wise, or stuff "representation wise"?
    Mar 04 06:20:45 <Dokujisan>	activity-wise
    Mar 04 06:20:48 <Dokujisan>	like creating tournaments
    Mar 04 06:20:49 <div0>	ah, great then
    Mar 04 06:20:55 <div0>	I have ABSOLUTELY no problem with that
    Mar 04 06:20:58 <Dokujisan>	encouraging people to form clans, and helping them form clans
    Mar 04 06:21:04 <div0>	but I do wonder why not much was done in that direction before
    Mar 04 06:21:07 <Dokujisan>	orgnizing training 
    Mar 04 06:21:11 <div0>	but well
    Mar 04 06:21:24 <div0>	what we WILL gain, is a website that does not have to look "professional" like a company site
    Mar 04 06:21:24 <Dokujisan>	setting up a training server and "hiring" some trainers
    Mar 04 06:21:28 <div0>	so we CAN post recent stuff there
    Mar 04 06:21:34 <div0>	and announce events, and like that
    Mar 04 06:22:06 <div0>	also...
    Mar 04 06:22:13 <div0>	when we don't have to act all "professional"...
    Mar 04 06:22:15 <Dokujisan>	and over the past 6-8 months I have formed a group of people who are mappers, or they learned mapping, and I had them working on various map projects
    Mar 04 06:22:19 <div0>	why not put some servers in the default favorites?
    Mar 04 06:22:20 <Dokujisan>	like "fixing" maps
    Mar 04 06:22:23 <div0>	e.g. that training server :P
    Mar 04 06:22:28 <Dokujisan>	and converting maps from DM -> CTF
    Mar 04 06:22:44 <div0>	actually... I would probably ONLY put that training server, and about two beta test servers there
    Mar 04 06:23:04 <div0>	but a training server at the top of the server list WILL help a lot
    Mar 04 06:23:26 <div0>	converting DM -> CTF... not so sure
    Mar 04 06:23:32 <div0>	this never really works out :P
    Mar 04 06:23:47 <div0>	minimanctf is one of the few exceptions
    Mar 04 06:23:51 <Dokujisan>	There were two concepts for training servers. There was mine which was a "bootcamp" server which only had a couple maps on it to allow for a group to be taught by a trainer....and there is the Dojo map concept by -z- and mookow which is like an obstacle course that doesn't require a trainer
    Mar 04 06:24:16 <div0>	not sure if a Dojo server would belong on the top of the server list
    Mar 04 06:24:19 <div0>	bootcamp probably would
    Mar 04 06:24:20 <Dokujisan>	the dojo seems like it would be for getting the "basics" while the bootcamp would be for refining and going from beginner to intermediate or advanced
    Mar 04 06:24:38 <div0>	dojo is interesting for new players? THAT is enw to me
    Mar 04 06:24:45 <Dokujisan>	the bootcamp sessions were like martial arts training that I've done before....lots of drills
    Mar 04 06:24:49 <div0>	IIRC that map was full of very advanced mvoement tricks
    Mar 04 06:25:05 <div0>	but well...
    Mar 04 06:25:07 <Dokujisan>	div0: you should check out the dojo map that mookow is working on. Some very interesting ideas there
    Mar 04 06:25:16 <Dokujisan>	I'll put it up if you want to see
    Mar 04 06:25:22 <div0>	I'd suggest just reserving one or two IPs for use as "newbie training" server
    Mar 04 06:25:26 <div0>	and one more IP for beta tests
    Mar 04 06:26:11 <Dokujisan>	so far, almost everyone that I trained in the bootcamp servers went on to become a nexuiz "regular"
    Mar 04 06:26:11 <div0>	and all these should be by default in the server list (but the beta test server should only be up when actually there is something new to test)
    Mar 04 06:26:20 <Dokujisan>	so it's a great conversion tool
    Mar 04 06:26:33 <div0>	thing is... to me the bootcamp idea sounds way more interesting to a new player
    Mar 04 06:26:34 <Dokujisan>	for building a community and retaining players
    Mar 04 06:26:41 <div0>	obstacle course really isn't everyone's thing
    Mar 04 06:26:43 <Dokujisan>	yeah, but it requires a trainer
    Mar 04 06:26:52 <Dokujisan>	if we can organize trainers properly
    Mar 04 06:26:56 <Dokujisan>	then that will work wonderfully
    Mar 04 06:27:07 <div0>	even if there is no trainer it can work out
    Mar 04 06:27:11 <Dokujisan>	I already know a handful of people who would be willing to do training
    Mar 04 06:27:15 <div0>	with cleverly designed maps for it :P
    Mar 04 06:27:25 <div0>	but, even if there is no trainer, there should be moderators
    Mar 04 06:27:31 <Dokujisan>	well that sounds more like the dojo concept
    Mar 04 06:27:42 <Dokujisan>	where the map is the training tool
    Mar 04 06:27:42 <div0>	and be it just to keep out the Diablo-D3s who join noob servers and then frag everyone there all the time :P
    Mar 04 06:27:48 <div0>	well
    Mar 04 06:27:54 <div0>	I hate putting the focus on obstacle course
    Mar 04 06:27:57 <div0>	THAT is totally boring to me
    Mar 04 06:28:06 <Dokujisan>	you should really see the map. hang on a sec
    Mar 04 06:28:07 <div0>	it should rather be actual gaemplay
    Mar 04 06:28:21 <div0>	it'd be the FIRST obstacle course map that is interesting
    Mar 04 06:28:24 <Dokujisan>	mookow even found a way to play VIDEOS that give an example
    Mar 04 06:28:26 <Dokujisan>	it's amazing
    Mar 04 06:28:29 <div0>	sure
    Mar 04 06:28:33 <div0>	but not for everyone
    Mar 04 06:28:54 <div0>	it's simply for another group of players
    Mar 04 06:29:00 <div0>	while the bootcamp idea should work for everyone
    Mar 04 06:29:05 <div0>	because it focuses on actually PLAYING the game
    Mar 04 06:29:21 <div0>	but yes, it requires a trainer
    Mar 04 06:29:29 <div0>	probably bootcamp server should only be up when a trainer is there
    Mar 04 06:29:41 <div0>	(if we put it on top of the server list, that is)
    Mar 04 06:29:55 <Dokujisan>	the way I did bootcamp before was I created an IRC channel where trainers would idle. Then I created a page with a webchat interface pointing to that channel. The webpage explained bootcamp and said "If you want to train, go into chat and request a trainer"
    Mar 04 06:30:06 <div0>	basically, I don't say the Dojo shouldn't be done...
    Mar 04 06:30:09 <Dokujisan>	and then if a trainer is available, both would go to the bootcamp server for a training session
    Mar 04 06:30:11 <div0>	of course not, it is a good idea
    Mar 04 06:30:20 <div0>	I just don't think it should be announced at the top of the server list all the time
    Mar 04 06:30:27 <div0>	as it may also drive newbies away
    Mar 04 06:30:30 <div0>	it sure would have driven away me
    Mar 04 06:30:43 <Dokujisan>	ok connect nullgaming.com:27005
    Mar 04 06:30:48 <div0>	can't, am at work
    Mar 04 06:30:50 <Dokujisan>	oh ok
    Mar 04 06:31:02 <Dokujisan>	basically, the dojo map has various rooms
    Mar 04 06:31:03 <div0>	basically, the whole obstacle course idea isn't really appealing to me
    Mar 04 06:31:11 <Dokujisan>	and each room has a focus....like movement, weapons, etc
    Mar 04 06:31:18 <Dokujisan>	and within each room, there are doors
    Mar 04 06:31:28 <div0>	well, I am not saying this would be a bad ides
    Mar 04 06:31:30 <div0>	a
    Mar 04 06:31:31 <Dokujisan>	and you enter a door and it walks you through how to do a certain thing....like laser jumping
    Mar 04 06:31:34 <Dokujisan>	wall lasering
    Mar 04 06:31:39 <Dokujisan>	rocket jumping
    Mar 04 06:31:40 <Dokujisan>	etc
    Mar 04 06:31:45 <div0>	as for bootcamp, is there a way to train multiple people at once?
    Mar 04 06:32:07 <Dokujisan>	and before you do the move, you can type "help" and that will start the download of the video. As soon as the video is downloaded, it plays on your screen so you see what you are suppoed to be doing
    Mar 04 06:32:12 <div0>	I'd prefer such a server where players can join and leave at any time
    Mar 04 06:32:22 <Dokujisan>	bootcamp, absolutely. I've trained up to 6 people at a time
    Mar 04 06:32:33 <Dokujisan>	well, actually I've trained more than that a long time ago before bootcamp was started
    Mar 04 06:32:36 <div0>	I just say... ideally it should be working WITHOUT having to go to a chat
    Mar 04 06:32:44 <Dokujisan>	but about 6 people works well
    Mar 04 06:32:47 <div0>	but by joining a public server
    Mar 04 06:33:07 <Dokujisan>	well I would love to see a mechanism for requesting a trainer IN the game. that would be awesome
    Mar 04 06:33:17 <div0>	you can do HTTP requests from QC
    Mar 04 06:33:18 <Dokujisan>	but using webchat was the best I could think of
    Mar 04 06:33:58 <div0>	so basically, you could make a HTTP request to a CGI script that will post the request on IRC
    Mar 04 06:34:34 <Dokujisan>	So what I did with bootcamp was I started to create a teaching plan, a curriculum, with various drills that the trainer would have the students walk through. The reason I started doing this was so I could quickly get a trainer onboard and all they would have to do is follow the curriculum
    Mar 04 06:34:39 <div0>	basically, I envision it this way...
    Mar 04 06:34:44 <div0>	noob joins training server...
    Mar 04 06:34:52 <Dokujisan>	and of course, they would help create the curriculum as well, help refine it, add more drills
    Mar 04 06:34:54 <div0>	and can spectate only
    Mar 04 06:35:00 <div0>	on some button, he can request a trainer
    Mar 04 06:35:10 <div0>	or request the already on the server trainer's attention
    Mar 04 06:35:16 <div0>	trainer can then let him in
    Mar 04 06:35:36 <Dokujisan>	can the trainer request be doing based on geography?
    Mar 04 06:35:36 <div0>	shouldn't be done too much like school though :P
    Mar 04 06:35:46 <div0>	based on geography, no
    Mar 04 06:35:52 <Dokujisan>	no, I ran it like martial arts training
    Mar 04 06:35:55 <div0>	but, we could have multiple training servers
    Mar 04 06:36:01 <div0>	the closer one would be at the top of the list
    Mar 04 06:36:05 <div0>	and be most likely to be joined
    Mar 04 06:36:10 <Dokujisan>	I explained some things, then we did some drills, then I stoped and explained some more and then we did some drills
    Mar 04 06:36:26 <div0>	sure
    Mar 04 06:36:28 <Dokujisan>	usually the sessions lasted about an hour, but sometimes they went for 3-4 hours
    Mar 04 06:36:34 <div0>	I just say... nobody should be "forced" to join at a certain time
    Mar 04 06:36:40 <div0>	and one should easily be able to skip a session too :P
    Mar 04 06:36:54 <div0>	it'd be better if players can just join the training when they feel like it
    Mar 04 06:37:02 <div0>	a curriculum can of course be used to decide what is the focus on what day
    Mar 04 06:37:57 <Dokujisan>	before bootcamp, we tried another approach and that was like running "classes" where we started a nexuiz school server publicly and we went to all of the public severs with people on them and announced "If you want nexuiz training, a class starts in 5 minutes. Go to here"
    Mar 04 06:38:02 <Dokujisan>	but that turned out to be a mess
    Mar 04 06:38:18 <Dokujisan>	we successfully collected a number of players...like as many as 15
    Mar 04 06:38:23 <div0>	well
    Mar 04 06:38:25 <Dokujisan>	and we certainly did train them in some basics
    Mar 04 06:38:26 <div0>	I want something in between
    Mar 04 06:38:30 <Dokujisan>	but it was very very very difficult to moderate
    Mar 04 06:38:35 <Dokujisan>	so that idea didn't work
    Mar 04 06:38:36 <div0>	server should be public, but trainer should decide who he lets in or not
    Mar 04 06:38:42 <Dokujisan>	that is why we came up with bootcamp
    Mar 04 06:38:50 <div0>	it shouldn't look like a closed community
    Mar 04 06:38:59 <div0>	it should be free, and one should be able to join it without commitment
    Mar 04 06:39:17 <div0>	but, moderation should then be done using a whitelist approach
    Mar 04 06:39:25 <div0>	i.e. anyone can join the server and try to talk to the trainer
    Mar 04 06:39:30 <div0>	but the trainer decides who gets to actually play
    Mar 04 06:39:33 <Dokujisan>	the teaching server (the first approach) was public and various people would join it and start shooting because they didn't know any better
    Mar 04 06:39:40 <div0>	EXACTLY :P
    Mar 04 06:39:52 <div0>	a trainer could e.g. let one player join, tell him what to do, and only then let the next one in
    Mar 04 06:39:58 <div0>	to avoid that mess
    Mar 04 06:40:05 <Dokujisan>	so yeah if there are mechanisms built into the game to help moderate the bootcamp server experience, that would be great
    Mar 04 06:40:20 <div0>	basically, I say: the bootcamp should be "really" public
    Mar 04 06:40:29 <div0>	a public server where anyone can join, with bootcamp specific restrictions
    Mar 04 06:40:34 <Dokujisan>	ok
    Mar 04 06:40:39 <Dokujisan>	that's awesome
    Mar 04 06:40:39 <div0>	and a feature to request a trainer when none is available
    Mar 04 06:40:51 <div0>	because: that will get our noobs to actually TRY the bootcamüp
    Mar 04 06:40:58 <div0>	as it'd be at the top of the server list
    Mar 04 06:41:12 <Dokujisan>	that would be a HUGE conversion tool
    Mar 04 06:41:23 <div0>	exactly
    Mar 04 06:41:28 <Dokujisan>	for turning new players into intermediate players quickly
    Mar 04 06:41:45 <div0>	things we need for it: a server should be "spectator only", and someone with master access can let players join the game
    Mar 04 06:42:06 <div0>	and, there should be a way to send a message to IRC (hehe, rcon2irc sort of can already do that, but this would better be more controlled)
    Mar 04 06:42:11 <Dokujisan>	I ran two bootcamp servers
    Mar 04 06:42:49 <div0>	BTW: the spectator-only feature also sounds like a good idea for clan matches
    Mar 04 06:42:52 <Dokujisan>	if a session was already started, someone could start a new session on the other server
    Mar 04 06:44:52 <Dokujisan>	the central user system idea would really help with clan activity as it would allow for a proper stats system and clan tag reservation and perhaps ....team slot reservation?? like for this clan match, only members of [o] can join team blue
    Mar 04 06:45:38 <Dokujisan>	that was a difficulty before with running clan matches where people would join and suddenly jump into the game during warmup and start playing and we'd have to tell them to spectate
    Mar 04 06:46:00 <Dokujisan>	and I had to kick some people and they would get mad because they didn't see my messages before 
    Mar 04 06:46:47 <Dokujisan>	it was just a mess. But if we had a way to enforce rules during clan matches based on usernames or clan names, that would help a lot
    Mar 04 06:47:20 <Dokujisan>	then if someone on team blue dropped their connection, a spectator from that same clan could jump into the game (but the other spectators woudln't be allowed)
    Mar 04 06:47:35 <Dokujisan>	that was another difficulty with clan matches, dropped connections
    Mar 04 06:47:51 <div0>	right
    Mar 04 06:47:58 <div0>	I have described aw working user system
    Mar 04 06:48:03 <div0>	that ensures anonymity AND security :P
    Mar 04 06:48:10 <Dokujisan>	that's awesome!
    Mar 04 06:48:10 <div0>	could sure be used for nick and clan tags too
    Mar 04 06:48:20 <Dokujisan>	I wanna hug you
    Mar 04 06:48:25 <div0>	(of course, by associating a nick, you lose anonymity, but well, then you KNOW it :P)
    Mar 04 06:48:34 <Dokujisan>	right
    Mar 04 06:48:48 <Dokujisan>	so,,another thing that I've done is organize mapping projects
    Mar 04 06:48:52 <div0>	it can still be used to ban trolls, as the anonymous IDs would only be given once per week per email address
    Mar 04 06:49:04 <Dokujisan>	and that also involves mapping training too for those who want to learn
    Mar 04 06:49:04 <div0>	so if you lose your ID, in worst case you have to wait a week to get a new one
    Mar 04 06:49:19 <div0>	a really elaborate troll could of course request a new ID every week but do nothing
    Mar 04 06:49:26 <div0>	and then one year later, he can burn 52 IDs :P
    Mar 04 06:49:34 <div0>	but that is unlikely
    Mar 04 06:49:39 <Dokujisan>	I once created a team of people called NCT = Nexuiz Community Team to help me run some community projects (like organizing bootcamp, organizing clan matches, organizing mapping projects)
    Mar 04 06:50:02 <Dokujisan>	and since I basically gave up on the clan community, the NCT has only been focusing on the mapping projects
    Mar 04 06:50:18 <Dokujisan>	but we made some good progress
    Mar 04 06:51:04 <Dokujisan>	I think Nexuiz should have had an NCT-like group...which is just another way fo saying "you can volunteer to be involved in nexuiz" and then someone would direct and manage those people 
    Mar 04 06:51:17 <Dokujisan>	I mean an NCT sort of group in an official sense
    Mar 04 06:52:17 <Dokujisan>	because it creates more mappers and it allows a lot of new projects to get off the ground quickly because we would already have a group of willing volunteers
    Mar 04 06:52:37 <Dokujisan>	it allows for map testing
    Mar 04 06:52:46 <div0>	speaking of maps... which maps do we want in "notnexuiz"?
    Mar 04 06:52:50 <Dokujisan>	good question
    Mar 04 06:52:53 <div0>	(out of the community maps)
    Mar 04 06:53:19 <Dokujisan>	I would think to start that off with "what maps do we NOT want that are currently in nexuiz" and then figure out how many open slots there are
    Mar 04 06:53:29 <div0>	not really :P
    Mar 04 06:53:35 <div0>	blockscape is e.g. a good candidate, I'd say
    Mar 04 06:53:44 <div0>	maybe needs a better compile though
    Mar 04 06:53:57 <div0>	controlfactor :P
    Mar 04 06:54:01 <div0>	(needs visual remake)
    Mar 04 06:54:22 <div0>	too bad we can't use docpython's maps
    Mar 04 06:54:57 <Dokujisan>	I discussed this with Getty with our other project. What is the major reason for having a lot of maps included with the game? I mean aside from those intended to be played in Campaign mode. It seems like 99% of gameplay happens on non-standard maps that get auto-downloaded to the player by the server.
    Mar 04 06:55:13 <div0>	the included maps represent the game
    Mar 04 06:55:31 <div0>	currently, what you play online is very different from what the game contains
    Mar 04 06:55:34 <div0>	that IMHO is not good
    Mar 04 06:55:40 <Dokujisan>	would we require these included maps to have bot waypoints?
    Mar 04 06:55:59 <div0>	yes
    Mar 04 06:56:08 <Dokujisan>	so someone could feasibly play CTF with some bots
    Mar 04 06:56:09 <div0>	and possibly use them in campaign too
    Mar 04 06:56:14 <div0>	right
    Mar 04 06:56:16 <Dokujisan>	ok
    Mar 04 06:56:19 <div0>	not very well
    Mar 04 06:56:22 <div0>	but they should work
    Mar 04 06:56:29 <Dokujisan>	since mangina improved the bots, they are actually playable in CTF now, I think
    Mar 04 06:56:31 <div0>	this BTW speaks against blockscape...
    Mar 04 06:56:36 <Dokujisan>	er mandinga*
    Mar 04 06:56:36 <div0>	IIRC it cannot be played without laserjumps
    Mar 04 06:56:47 <Dokujisan>	yeah :-/
    Mar 04 06:56:56 <div0>	controlfactor should work with bots
    Mar 04 06:56:56 <Dokujisan>	it would need some jumppads in certain places maybe?
    Mar 04 06:56:58 <div0>	but looks outdated
    Mar 04 06:57:21 <div0>	tznex03, same problem :P
    Mar 04 06:57:35 <div0>	tznex03 is the closest to classic Quake1/2 CTF we ever got
    Mar 04 06:57:42 <Dokujisan>	we couldn't include any of these q3 conversion maps, could we?
    Mar 04 06:57:47 <div0>	we can't
    Mar 04 06:57:49 <Dokujisan>	ok
    Mar 04 06:57:49 <div0>	and should not
    Mar 04 06:58:24 <div0>	hehe, that is already the full list of CTF maps I really would like to add - blockscape (but bots... can't), controlfactor, tznex03
    Mar 04 06:58:37 <Dokujisan>	many people seem to like gasolinepowered, and I'm sure the new version of it is going to be great
    Mar 04 06:58:43 <div0>	oh right
    Mar 04 06:58:44 <Dokujisan>	http://www.nullgaming.com/maps/hoctf/
    Mar 04 06:58:46 <div0>	that one too
    Mar 04 06:58:51 <div0>	I didn't see that one when scrolling :P
    Mar 04 06:58:57 <div0>	gasolinepowered is a clear yes
    Mar 04 06:59:04 <Dokujisan>	those are my CTF maps. Though I should remove the ones that I no longer have in the maplist
    Mar 04 06:59:28 <div0>	all your push are belong to us wtf :P
    Mar 04 06:59:31 <Dokujisan>	and hmm.... I should grab my maplist actually and remove the Q3 conversion maps
    Mar 04 06:59:37 <Dokujisan>	haha that is an april fools joke map
    Mar 04 06:59:54 <div0>	oh right, hydronex is not official either...#
    Mar 04 07:00:01 <Dokujisan>	OH btw.... marketing is another topic. I have a lot of marketing ideas and with some volunteers involved, that can be a good way to attract new players
    Mar 04 07:00:08 <Dokujisan>	like the april fools mapping project
    Mar 04 07:00:14 <Dokujisan>	which is around the corner....this is good timing
    Mar 04 07:00:46 <Dokujisan>	For example.... we would take existing maps and theme them to funny internet memes
    Mar 04 07:00:49 <div0>	lol, you once had bonuscheckers on it
    Mar 04 07:00:56 <Dokujisan>	yeah :-/
    Mar 04 07:01:03 <Dokujisan>	we did a remake of bonuscheckers though
    Mar 04 07:01:08 <div0>	a remake? where
    Mar 04 07:01:13 <Dokujisan>	it's called.....
    Mar 04 07:01:19 <Dokujisan>	courtyard_ctf
    Mar 04 07:01:24 <Dokujisan>	I think
    Mar 04 07:01:31 <div0>	ah, a serious remake :P
    Mar 04 07:01:39 <div0>	original was bonusarenactf, BTW :P
    Mar 04 07:01:44 <div0>	no, bonuscarousel
    Mar 04 07:01:44 <Dokujisan>	grassy has some ideas to improve it further, but the remake was basically successful
    Mar 04 07:02:03 <Dokujisan>	another succesful remake was darkcity_ctf
    Mar 04 07:02:05 <div0>	have screenshot?
    Mar 04 07:02:08 <Dokujisan>	hang on....
    Mar 04 07:02:10 <div0>	darkcity remade? cool
    Mar 04 07:02:13 <div0>	also with keyhunt support?
    Mar 04 07:02:26 <Dokujisan>	hmmm probably didn't include KH support
    Mar 04 07:02:31 <div0>	I like city maps
    Mar 04 07:02:40 <div0>	is it a from scratch remake?
    Mar 04 07:02:58 <div0>	or based on the old one?+
    Mar 04 07:03:04 <Dokujisan>	did you know that mIKEctf2's real name was "Like Spinning Plates"?
    Mar 04 07:03:08 <div0>	yes
    Mar 04 07:03:31 <Dokujisan>	oh, mookow's recent map called Kings and Queens is really really good, but has a FPS drop problem
    Mar 04 07:03:33 <div0>	ah, darkcityctf seems to be based on the roiginal one
    Mar 04 07:03:44 <div0>	bad... cannot use that then for the official game :P
    Mar 04 07:03:52 <Dokujisan>	if the FPS drop could be improved, that could be a good map
    Mar 04 07:03:54 <div0>	(as the original sure is not GPL compatible)
    Mar 04 07:04:07 <div0>	but I would really like a nicely detailed city map for keyhunt
    Mar 04 07:04:14 <Dokujisan>	well he did recreate the whole map from scratch at one point because the brushes were so messed up
    Mar 04 07:04:19 <Dokujisan>	for darkcity_ctf
    Mar 04 07:04:26 <div0>	yes, but he still uses the old textures
    Mar 04 07:04:29 <Dokujisan>	ah I see
    Mar 04 07:04:39 <div0>	if these could get replaced, that'd be great
    Mar 04 07:05:00 <Dokujisan>	I think agressor_ctf could be good but it needs some fixing around the middle point area where the quad is. That's too much of a bottleneck
    Mar 04 07:05:25 <div0>	also... which maps could be warpzonized?
    Mar 04 07:05:32 <div0>	aggressor probbaly cannot
    Mar 04 07:05:41 <div0>	using warpzones there would turn it into a brain twister :P=
    Mar 04 07:05:42 <Dokujisan>	grassy recently recreated onarail to included 2 trains...it's called on2rails. It's an okay map...it's better than the original
    Mar 04 07:05:56 <div0>	need to make stoiber remix of it :P
    Mar 04 07:05:59 <Dokujisan>	oh, warpzones. Man, those are great
    Mar 04 07:06:06 <Dokujisan>	what an awesome idea
    Mar 04 07:06:20 <Dokujisan>	I haven't even begun to think about how those could be used for gameplay
    Mar 04 07:06:24 <div0>	best are used in a way that is compatible to clients that have the extra renders disabled
    Mar 04 07:06:28 <Dokujisan>	like your spiral staircase concept
    Mar 04 07:06:36 <div0>	like, put teleporter brush behind them :P
    Mar 04 07:06:41 <Dokujisan>	I see
    Mar 04 07:07:06 <Dokujisan>	a lot of dublpaws maps are popular on my server
    Mar 04 07:07:08 <Dokujisan>	dance
    Mar 04 07:07:09 <Dokujisan>	go
    Mar 04 07:07:13 <div0>	yes, but these are quite low quality
    Mar 04 07:07:14 <Dokujisan>	fighter_bay
    Mar 04 07:07:18 <div0>	(for inclusion in the game)
    Mar 04 07:07:27 <div0>	good gameplay though
    Mar 04 07:07:29 <Dokujisan>	low quality in terms of textures?
    Mar 04 07:07:34 <div0>	yes, and brush detail
    Mar 04 07:07:36 <Dokujisan>	because I could talk with dublpaws about improving those
    Mar 04 07:07:45 <Dokujisan>	he plays on my server all the time
    Mar 04 07:07:55 <div0>	dance is almost includable though
    Mar 04 07:08:06 <div0>	the other dublpaws maps, not really
    Mar 04 07:08:10 <Dokujisan>	dib and I were working on an dance_enclosed spin-off
    Mar 04 07:08:23 <Dokujisan>	it was about 90% done and then he dropped it
    Mar 04 07:08:28 <div0>	dance is just too one-colored :P
    Mar 04 07:08:39 <div0>	do something better than that wood floor, and it's done
    Mar 04 07:08:40 <Dokujisan>	I happen to like the latest versions of soylent_ctf that makr was working on
    Mar 04 07:08:55 <Dokujisan>	though it needs more testing
    Mar 04 07:09:04 <Dokujisan>	oh....stonecastle
    Mar 04 07:09:08 <Dokujisan>	remake of dm_castle
    Mar 04 07:09:11 <Dokujisan>	everyone loves it
    Mar 04 07:09:18 <Dokujisan>	well except for cortez666 :-P
    Mar 04 07:09:50 <Dokujisan>	I think lavaflag could use a makeover
    Mar 04 07:09:51 <div0>	given that dm_castle was bad
    Mar 04 07:09:54 <div0>	I have to try this one
    Mar 04 07:09:59 <div0>	lavaflag REALLY :P
    Mar 04 07:10:06 <div0>	isn't that the one with the huge bug?
    Mar 04 07:10:08 <div0>	hourglass too
    Mar 04 07:10:31 <div0>	(where you could end up in all black rooms, and hide)
    Mar 04 07:11:03 <Dokujisan>	the gameplay of dm_castle is improved in stonecastle with jumppads in certain places (really helps new players move around the map) and we replaced the machinegun with hagar
    Mar 04 07:11:22 *	Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 04 07:11:31 <Dokujisan>	oh I didn't know about any lavaflag bug :-o
    Mar 04 07:11:46 <Dokujisan>	I like medeivalV2
    Mar 04 07:11:50 <Dokujisan>	but it also needs a makeover
    Mar 04 07:12:21 <div0>	IIRC lavaflag has the sae bug as hourglass, but elsewhere
    Mar 04 07:12:59 <Dokujisan>	ctf_toxic was on our list of maps to improve...mainly in the middle area of the map where the two halves meet
    Mar 04 07:13:55 <div0>	my version? sure
    Mar 04 07:14:03 <div0>	or master's version? :P
    Mar 04 07:14:11 <Dokujisan>	a recent map called Cubical by a new mapper (guy who came from Q2/Q3) is really good. That same guy is working on a Walmart map called NexMart
    Mar 04 07:14:16 <div0>	my version is the one with the "reaction" stuff
    Mar 04 07:14:30 <div0>	oh, but Cubical is by FruitieX
    Mar 04 07:14:34 <div0>	from that mapping contest
    Mar 04 07:14:37 <Dokujisan>	Cubical doesn't look very pretty though. 
    Mar 04 07:14:43 <Dokujisan>	oh he also has a map called cubical??
    Mar 04 07:14:44 <Dokujisan>	oops!
    Mar 04 07:14:55 <Dokujisan>	uh, ok I need to talk with mintox about renaming his then
    Mar 04 07:15:03 <div0>	not sure if this is needed :P
    Mar 04 07:15:08 <div0>	not many play FruitieX's map anyway
    Mar 04 07:15:14 <div0>	actually, it may be mostly forgotten nwo
    Mar 04 07:15:28 <div0>	basically, if the map is good, FruitieX will probably be fine with itr
    Mar 04 07:15:49 <div0>	just talk about it to both of them and find a solution
    Mar 04 07:15:56 <div0>	chances are BTW that the bsp file names do not clash
    Mar 04 07:16:20 <Dokujisan>	Mookow's "Drainage" map had promise, but he never really finished it. 
    Mar 04 07:17:25 <Dokujisan>	Evilspace CTF is popular, but it does have a couple bad gameplay elements. There is a hidden teleporter that leads to the quad and there is that "escape hatch" jump pad right below the flag
    Mar 04 07:17:57 <div0>	yes
    Mar 04 07:18:00 <Dokujisan>	if those things were fixed and if it had a makeover, it could be good.
    Mar 04 07:18:02 <div0>	maybe should be fixed
    Mar 04 07:18:25 <div0>	I do like the idea of the teleporter though, but not of hiding it
    Mar 04 07:18:37 <Dokujisan>	right
    Mar 04 07:18:47 <Dokujisan>	hidden secret stuff in CTF is generally bad for gameplay
    Mar 04 07:18:56 <Dokujisan>	but a teleporter leading to the quad is fine
    Mar 04 07:19:28 <div0>	right
    Mar 04 07:19:30 <Dokujisan>	everyone really likes gforce2. It could still use some refinement. unfortunately cortez took Gforce3 and 4 in a different direction
    Mar 04 07:19:37 <div0>	no, I don't like gforce2 :P
    Mar 04 07:19:45 <div0>	oh wait
    Mar 04 07:19:48 <div0>	version 2, maybe yes
    Mar 04 07:19:57 <Taoki>	Morning everyone :)
    Mar 04 07:19:57 <div0>	but the turrets ended up too annoying
    Mar 04 07:19:59 <Dokujisan>	unfortunately, gforce2 also has that hidden teleporter leaidng to the nex
    Mar 04 07:20:07 <div0>	yes
    Mar 04 07:20:12 <Dokujisan>	yeah the turrets were added in v3
    Mar 04 07:20:24 <Dokujisan>	they were "neat" but they ruined the map
    Mar 04 07:20:53 <Dokujisan>	it's interesting to me that cortez creates interesting maps by accident
    Mar 04 07:21:28 <div0>	and here comes a really controversial question...
    Mar 04 07:21:38 <Dokujisan>	one of the projects was another attempt at remaking dusty to be symmetrical. 
    Mar 04 07:21:41 <div0>	does anyone volunteer to do good item placement for slimepipe (NOT the ctf version)?
    Mar 04 07:21:49 <Dokujisan>	slimepipe was on the list too!
    Mar 04 07:22:00 <Dokujisan>	out of all of mikee's maps, slimepipe was the one that I felt had potential
    Mar 04 07:22:01 <div0>	the only good looking mikeeusa map
    Mar 04 07:22:29 <div0>	even has somewhat okay gameplay
    Mar 04 07:22:33 <div0>	just item placement is bad
    Mar 04 07:22:41 <div0>	and the slime trap... not that way, but has potential
    Mar 04 07:22:44 <Dokujisan>	this hasn't been updated in a month, but here is the projects page we were working from
    Mar 04 07:22:45 <Dokujisan>	http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 04 07:22:49 <Dokujisan>	to fix maps and convert maps
    Mar 04 07:23:11 <div0>	basically, slimepipe probably does not need much work to be includable
    Mar 04 07:23:25 <div0>	of course, mikee later developed it into the wrong direction
    Mar 04 07:23:40 <div0>	by making 4 copies of the map, and confusing corridors
    Mar 04 07:23:50 <div0>	when remaking, watch the license
    Mar 04 07:23:54 <div0>	doc's maps are not GPL
    Mar 04 07:24:43 <div0>	Rustvents - also good idea
    Mar 04 07:25:39 <div0>	for slimepipe, please base on slimepipesmallctf, or even better, slimepipe (not ctf)
    Mar 04 07:25:54 <Dokujisan>	k
    Mar 04 07:28:20 <Dokujisan>	breathium is pretty for a DM map
    Mar 04 07:28:27 <Dokujisan>	I forgot who made it
    Mar 04 07:28:31 <div0>	oh, great, nexdmlc2 got edited
    Mar 04 07:28:35 <div0>	I liked that map
    Mar 04 07:28:49 <div0>	too bad it's nongpl too, it really would have potential
    Mar 04 07:28:58 <Dokujisan>	ahh
    Mar 04 07:29:01 <div0>	maybe original author can be tracked down
    Mar 04 07:29:11 <div0>	or was it rebuilt anyway?
    Mar 04 07:29:21 <Dokujisan>	probably not
    Mar 04 07:29:35 <div0>	because, IIRC it came without .map file
    Mar 04 07:29:35 <Dokujisan>	it was scorpion's first map
    Mar 04 07:29:43 <Dokujisan>	oh? hmmm
    Mar 04 07:29:59 <div0>	oh, no
    Mar 04 07:30:01 <div0>	map was included
    Mar 04 07:32:05 <div0>	basically, many maps in the list have potential, but not many are GPL (or GPL-able)
    Mar 04 07:32:23 <div0>	the others can of course be played on servers anyway
    Mar 04 07:32:49 <Dokujisan>	yeah we certainly weren't tracking licenses. However, we could adjust that for the goal of maps to be included with the game
    Mar 04 07:33:26 <div0>	I just am saying - many of these WOULD have potential for inclusion
    Mar 04 07:33:28 <Dokujisan>	but yeah, this map-project management is another thing that I think should be an official effort put forth by the people who run the game
    Mar 04 07:33:34 <Dokujisan>	because then it could be done better
    Mar 04 07:33:37 <Dokujisan>	and reach more people
    Mar 04 07:33:52 <div0>	and yes, I wouldn't even refuse to include a slimepipe fixed version
    Mar 04 07:33:53 <Dokujisan>	the little effort I've done has created a handful of new mappers
    Mar 04 07:34:18 <div0>	at least the DM version
    Mar 04 07:34:19 <Dokujisan>	...and I don't even make maps! I tried before but gtkradient kept crashing in vista
    Mar 04 07:34:22 <div0>	I am not sure if it can work out as CTF
    Mar 04 07:34:28 <Dokujisan>	I haven't had time to try netradient since
    Mar 04 07:34:58 <div0>	seriously, I'd say slimepipe could become what reslimed has attempted to be but failed
    Mar 04 07:35:05 <div0>	(I still prefer slimepit over reslimed)
    Mar 04 07:35:16 <Dokujisan>	is it slimepit or slimepipe?
    Mar 04 07:35:22 <div0>	mikee's is slimepipe
    Mar 04 07:35:32 <div0>	I now compare to slimepit (the old one in Nexuiz)
    Mar 04 07:35:37 <Dokujisan>	oooooh
    Mar 04 07:35:51 <div0>	reslimed, Strahlemann's successor, does look better than slimepit, but I always hit walls on it
    Mar 04 07:35:54 <div0>	really not fluent
    Mar 04 07:36:02 <div0>	I'd like a "best of both worlds" map :P
    Mar 04 07:36:28 <Dokujisan>	I liked reslimed, mainly because it is larger
    Mar 04 07:36:45 <div0>	yes
    Mar 04 07:36:47 <div0>	that part I like
    Mar 04 07:36:53 <div0>	but not that it lost of slimepit's fluency
    Mar 04 07:37:02 <Dokujisan>	but I always though the shield area down that long hallway was a bit odd
    Mar 04 07:37:09 <div0>	on slimepit I can jump all the time, and never get stuck anywhere
    Mar 04 07:37:18 <div0>	on reslimed, no chance
    Mar 04 07:45:14 <Dokujisan>	if there is any chance of my being put in charge of community development, I'll certainly "sign-up" for that. That is what I've always done for nexuiz and if I can do it on an official basis with the support of those involved in running the game, then these projects can be scaled up to something much bigger.
    Mar 04 07:45:51 <Dokujisan>	that is what I'm planning on doing for the projects I'm working on with Getty
    Mar 04 07:46:08 <Dokujisan>	I'm the community developer or community coordinator for those projects
    Mar 04 07:52:34 <div0>	Nexitus
    Mar 04 07:52:51 <div0>	is that available?
    Mar 04 07:53:00 <div0>	maybe with z at end
    Mar 04 07:55:01 <Dokujisan>	nexitus.com - taken
    Mar 04 07:56:40 <Dokujisan>	nexituz.com available, but that doesn't look as good
    Mar 04 07:57:06 <Dokujisan>	nexidus.com also taken
    Mar 04 07:57:24 <Dokujisan>	nexid.com taken
    Mar 04 07:58:27 <div0>	damn
    Mar 04 07:59:17 <Dokujisan>	another thing, I helped the aussies build up their community and I was planning on starting up a south american community and possibly an asian community at one point
    Mar 04 07:59:58 <Dokujisan>	I talked with mandinga about the south american community idea
    Mar 04 08:01:30 <Dokujisan>	nexidux.com available
    Mar 04 08:01:55 <Dokujisan>	nexidun.com available
    Mar 04 08:02:31 <Dokujisan>	nexidium.com available
    Mar 04 08:04:03 <Dokujisan>	nexiox.com available
    Mar 04 08:10:18 <div0>	nexidium - not so bad
    Mar 04 08:11:36 <Dokujisan>	nexilus.com available
    Mar 04 08:14:35 <div0>	sounds too soft :P
    Mar 04 08:14:46 <Dokujisan>	ya
    Mar 04 08:15:13 <div0>	also, if it differs just by one letter from a traemark, we can get screwed too
    Mar 04 08:15:34 <Dokujisan>	only of that trademark is in the gaming industry
    Mar 04 08:15:43 <div0>	true
    Mar 04 08:15:48 <div0>	maybe in software too
    Mar 04 08:15:52 <Dokujisan>	ya
    Mar 04 08:15:54 <div0>	NEXCARNATE
    Mar 04 08:16:35 <Dokujisan>	nexiton.com available
    Mar 04 08:16:42 <div0>	hm... that could work
    Mar 04 08:16:51 <div0>	the gun could then also be called "The Nexiton"
    Mar 04 08:16:55 <div0>	or maybe Nexitone
    Mar 04 08:17:05 <Dokujisan>	tone your skin with....nexitone!
    Mar 04 08:17:09 <div0>	lol
    Mar 04 08:17:15 <div0>	Nexecution
    Mar 04 08:17:19 <div0>	no, that is too violent :P
    Mar 04 08:17:31 <div0>	Nexcathedra ahahahahah))
    Mar 04 08:17:57 <div0>	NEXHALE
    Mar 04 08:18:18 <div0>	Nexotherm
    Mar 04 08:18:27 <div0>	Nexodium
    Mar 04 08:18:38 <Dokujisan>	nexot.com is available
    Mar 04 08:18:41 <div0>	Nexodus
    Mar 04 08:18:48 <[-z-]>	http://nexuizgpl.com/ << run by bennydacks
    Mar 04 08:18:59 <div0>	Nexogamy - don't even want to know what that would be
    Mar 04 08:19:08 <Dokujisan>	heh, he snatched that domain up quick eh?
    Mar 04 08:19:36 <Dokujisan>	I want to like bennydacks, I really do
    Mar 04 08:19:53 <div0>	Nexotoxic
    Mar 04 08:20:58 <[-z-]>	:-P
    Mar 04 08:21:37 <Dokujisan>	so whenever we pick a name, we need to NOT release it until we make sure we get the appropriate domains that we think we might need
    Mar 04 08:21:40 <div0>	Nextima (but not sure if that is a bad word, just found extima in /usr/share/dict/words)
    Mar 04 08:21:43 <div0>	of course
    Mar 04 08:22:04 <div0>	Nextispex
    Mar 04 08:22:06 <div0>	wtf :P
    Mar 04 08:23:07 <Dokujisan>	and it would be wonderful if all of the things offered by side websites were actually part of the official site
    Mar 04 08:23:44 <Dokujisan>	like news, training videos, etc
    Mar 04 08:23:55 <div0>	that is fine, would even allow me to also accept NN as a part of the official side :P
    Mar 04 08:23:56 <Dokujisan>	clan management 
    Mar 04 08:24:01 <div0>	it just shouldn't be centric to a single community
    Mar 04 08:24:22 <div0>	but [PB] will stay elsewhere
    Mar 04 08:24:28 <div0>	don't want to get forced to use good web design ;)
    Mar 04 08:24:35 <Dokujisan>	haha
    Mar 04 08:24:51 <div0>	but sure - why NOT integrate the various communities
    Mar 04 08:25:35 <[-z-]>	yes, I don't mind building out this new site to act like nexuiz ninjaz was planning to be like
    Mar 04 08:25:41 <Dokujisan>	exactly
    Mar 04 08:25:44 <Dokujisan>	that's what I mean
    Mar 04 08:25:58 <[-z-]>	I already thought about how to integrate a few host and I'm working on builid a map repo into wordpress
    Mar 04 08:26:06 <[-z-]>	I created my first WP plugin yesterday ^_^
    Mar 04 08:26:14 <Dokujisan>	this will give me an excuse to learn wordpress
    Mar 04 08:26:20 <Dokujisan>	I've been avoiding it :-P
    Mar 04 08:26:27 <[-z-]>	it's really a nice CMS
    Mar 04 08:28:55 <[-z-]>	god damn, can't wait until the weekend, I need sleep
    Mar 04 08:29:03 <div0>	I just don't want the ninjaz to dominate it :P
    Mar 04 08:29:10 <div0>	but well, that shouldn't be hard to achieve
    Mar 04 08:29:16 <[-z-]>	I understand and agree
    Mar 04 08:29:16 <div0>	just add enough non-NN content and it's set
    Mar 04 08:29:31 <div0>	a comprehensive portal page WOULD be good
    Mar 04 08:29:50 <div0>	it's just, the different interest group all have different opinions...
    Mar 04 08:29:54 <[-z-]>	part of the reasons ninjaz were started was because I thought it was too hard to get AT to listen on some things
    Mar 04 08:30:00 <div0>	but the main page should have a neutral point of view whereever possible
    Mar 04 08:30:13 <Dokujisan>	IMO, there wouldn't have been a "nexuizninjaz" if there were something like it within the core community.
    Mar 04 08:30:24 <div0>	and how can you be more neutral than by trying to include as many of these special comminities as possible
    Mar 04 08:30:24 <[-z-]>	well put
    Mar 04 08:30:54 <div0>	should probably also include planetnexuiz.de if it still exists :P
    Mar 04 08:33:46 <Dokujisan>	I'm also scanning domain auctions and sales sites because often domains are for sale really cheap...like $15
    Mar 04 08:33:53 <[-z-]>	it's a trap
    Mar 04 08:33:58 <Dokujisan>	?
    Mar 04 08:34:06 <[-z-]>	don't by from squatters
    Mar 04 08:34:17 <Dokujisan>	who says they are squatters?
    Mar 04 08:34:33 <[-z-]>	90% chance
    Mar 04 08:35:05 <[-z-]>	where you chance sedo or something?
    Mar 04 08:35:22 <Dokujisan>	ok I just scanned godaddy auctions for nex*.com
    Mar 04 08:35:25 <Dokujisan>	didn't find much
    Mar 04 08:35:28 <[-z-]>	ahh
    Mar 04 08:35:53 <Dokujisan>	a lot of those godaddy auctions are expired domains that people let lapse
    Mar 04 08:37:43 <div0>	I do think the name SHOULD still start with nex
    Mar 04 08:37:46 <[-z-]>	yeah, godaddy isn't the same as the other sites... but their own brand of evil
    Mar 04 08:37:51 <div0>	but it isn't really easy to find a good name with that
    Mar 04 08:38:02 <Dokujisan>	it would be really convenient if it began with "nex"
    Mar 04 08:38:07 <[-z-]>	nexican
    Mar 04 08:38:08 <[-z-]>	^_^
    Mar 04 08:38:11 <Dokujisan>	haha
    Mar 04 08:38:13 <div0>	Nexotherm only has 2 google hits
    Mar 04 08:38:16 <div0>	it may work :P
    Mar 04 08:38:17 <[-z-]>	nexicola
    Mar 04 08:38:26 <div0>	plus, the word makes sense - explosions are exotherm reactions
    Mar 04 08:38:31 <[-z-]>	nexifz
    Mar 04 08:38:43 *	[-z-] gives channel operator status to Taoki
    Mar 04 08:38:45 <Dokujisan>	here is my list so far...
    Mar 04 08:38:46 <Dokujisan>	http://pastie.org/private/rwg7zyl2a9gwfcdplmqvqa
    Mar 04 08:39:15 <Dokujisan>	I see some repeats
    Mar 04 08:39:15 <div0>	Try: Nexepharis
    Mar 04 08:39:16 <Dokujisan>	oh well
    Mar 04 08:39:25 <Dokujisan>	that's kind of a long name
    Mar 04 08:39:33 <Dokujisan>	I was trying for 8 characters or less
    Mar 04 08:39:33 <div0>	yes, but less weird than Xepharis
    Mar 04 08:39:59 <div0>	Nexiox is not that bad either
    Mar 04 08:40:00 <Dokujisan>	nexepharis.com available
    Mar 04 08:40:12 <[-z-]>	nexephalis
    Mar 04 08:40:19 <div0>	nexenzephalitis?
    Mar 04 08:40:31 <[-z-]>	the logo could be the radar for bleach
    Mar 04 08:40:32 <Dokujisan>	nexameaneggsandwich
    Mar 04 08:40:37 <div0>	that is what your brain gets when you get nexed too much
    Mar 04 08:40:42 <[-z-]>	eabfps
    Mar 04 08:40:48 <[-z-]>	(eggs and bacon FPS)
    Mar 04 08:40:53 <div0>	lol
    Mar 04 08:40:58 <div0>	NEGGS AND BACON
    Mar 04 08:41:03 <[-z-]>	:-P
    Mar 04 08:41:15 <[-z-]>	we can call it nexnex
    Mar 04 08:41:31 <[-z-]>	nexnex.org AVAILABLE
    Mar 04 08:41:44 <Dokujisan>	I really like some of those names that don't have available .coms....so if we get stuck with this name picking thing, we can always consider that as a backup plan
    Mar 04 08:41:47 <[-z-]>	nextnex
    Mar 04 08:42:08 <[-z-]>	nextnex.com 	AVAILABLE
    Mar 04 08:45:56 <Dokujisan>	I need food...brb
    Mar 04 09:05:14 <[-z-]>	alright, see you all from the work place
    Mar 04 09:34:41 *	}-z-{ (z@dojo.nexuizninjaz.com) has joined #notnexuiz
    Mar 04 09:35:03 <Dokujisan>	ok there are some more isuses we need to work out with this transition. We are going to have to recreate a lot of things that exist for nexuiz already...like dev.alientrap.org content and some of the sticky thread information
    Mar 04 09:35:20 <}-z-{>	yeah, I can handle all the web and I'll share access with you Dokujisan 
    Mar 04 09:35:24 <div0>	yes, but that doesn't have to be there from the start
    Mar 04 09:35:28 <Dokujisan>	ok
    Mar 04 09:35:34 <div0>	plus, [-z-] has access to alientrap.org's databases :P
    Mar 04 09:35:37 <}-z-{>	well, getting the web and pm up will help us get organized
    Mar 04 09:35:38 <Dokujisan>	haha
    Mar 04 09:35:53 <div0>	but we can't get it up without a domain name
    Mar 04 09:36:00 <}-z-{>	I was hoping we could come up with a name by the end of today
    Mar 04 09:36:05 <div0>	well... for a start, it'd be nice if it's on nexiuz.org as you now own it anyway :P
    Mar 04 09:36:12 <}-z-{>	but if not, I can just start building on locally
    Mar 04 09:36:24 <}-z-{>	yeah, I'll do that when I get home I guess
    Mar 04 09:36:27 <div0>	it isn't easy to find a good name
    Mar 04 09:36:28 <}-z-{>	start it on nexiuz.org
    Mar 04 09:36:35 <div0>	but we can use nexiuz as "working title", and get a real name later
    Mar 04 09:36:42 <}-z-{>	yeah
    Mar 04 09:36:54 <div0>	just... http://www.nexiuz.org shouldn't contain much info for anyone :P
    Mar 04 09:37:00 <div0>	more like the illfonic announcement was haha :P
    Mar 04 09:37:04 <div0>	it should be in a subdir
    Mar 04 09:37:11 <}-z-{>	what do you mean?
    Mar 04 09:37:18 <div0>	alternatively, it shouldn CLEARLY state EVERYWHERE that nexiuz is unlikely to be the final name
    Mar 04 09:37:26 <}-z-{>	ahh
    Mar 04 09:37:29 <div0>	as using that as final name will be a bad move
    Mar 04 09:37:41 <div0>	(as google will STILL show illfonic's stuff, and assume it's a typo of nexuiz)
    Mar 04 09:38:23 <Dokujisan>	yeah I agree that nexiuz would be a bad choice
    Mar 04 09:39:44 <div0>	nexidium is out
    Mar 04 09:39:48 <div0>	Domains Registered on 2007-07-28_2_77 psroom.com - [ Diese Seite übersetzen ]
    Mar 04 09:39:49 <div0>	nexidium.com
    Mar 04 09:40:02 <}-z-{>	sounds like medicine that makes you fall asleep anyway
    Mar 04 09:40:05 <div0>	even though the domain currently does not exist, it once did
    Mar 04 09:40:07 <div0>	that too
    Mar 04 09:41:04 <div0>	Nuper erat Nexicus nunc est vispillo XSAXius.
    Mar 04 09:41:12 <div0>	Quod vispillo facit, fecerat ed Nexicus.
    Mar 04 09:41:27 <div0>	*et
    Mar 04 09:41:47 <}-z-{>	nexivouz
    Mar 04 09:41:53 <}-z-{>	is that too complicated?
    Mar 04 09:41:54 <div0>	NO PLEASE NOT
    Mar 04 09:41:56 <}-z-{>	haha
    Mar 04 09:42:04 <}-z-{>	nexivu?
    Mar 04 09:42:12 <}-z-{>	like deja vu with nexuiz
    Mar 04 09:42:12 <div0>	also, you meant nexez-vous
    Mar 04 09:43:32 <}-z-{>	nexivu.com AVAILABLE  
    Mar 04 09:43:56 <div0>	and just has 10 google hits
    Mar 04 09:43:58 <div0>	seems usable
    Mar 04 09:44:10 <div0>	but... don't like it much
    Mar 04 09:44:13 <div0>	still put it on the list
    Mar 04 09:44:18 <}-z-{>	nexi.us AVAILABLE  
    Mar 04 09:44:18 <Dokujisan>	added
    Mar 04 09:44:19 <}-z-{>	:-P
    Mar 04 09:44:26 <div0>	also, hard to pronounce
    Mar 04 09:44:30 <div0>	"Nexi vü"
    Mar 04 09:44:45 <}-z-{>	nexii? (like nex 2)
    Mar 04 09:45:06 <}-z-{>	damn, nexit is taken
    Mar 04 09:45:06 <div0>	like the plural of nexius, nexii m.?
    Mar 04 09:45:28 <div0>	(nexii would be nexius's plural in latin grammar)#
    Mar 04 09:45:32 <}-z-{>	:-P
    Mar 04 09:45:47 <div0>	actually... good one
    Mar 04 09:45:51 <div0>	plural form indicates teamplay focus
    Mar 04 09:46:21 <}-z-{>	ironic because we drop the 'us'
    Mar 04 09:46:31 <div0>	HAHA :P
    Mar 04 09:46:35 <Dokujisan>	haha
    Mar 04 09:47:11 <Dokujisan>	nexolus.com is available
    Mar 04 09:47:27 <}-z-{>	sounds complicated
    Mar 04 09:51:51 <Dokujisan>	nexvium.com is available
    Mar 04 09:52:49 <}-z-{>	too hard
    Mar 04 09:55:15 <div0>	nexvium?
    Mar 04 09:55:16 <Dokujisan>	nexona.com available
    Mar 04 09:55:17 <div0>	like valium`?
    Mar 04 09:55:26 <div0>	could write email spam about it :P
    Mar 04 09:56:36 <Dokujisan>	nexori.com available
    Mar 04 09:57:01 <Dokujisan>	nexoric.com available
    Mar 04 09:57:20 <Dokujisan>	nexorin.com available
    Mar 04 09:57:41 <Dokujisan>	nexorn.com available
    Mar 04 09:58:12 <Dokujisan>	nexolic.com available
    Mar 04 09:59:38 <Dokujisan>	nexole.com available
    Mar 04 10:00:19 <Dokujisan>	nexolum.com available
    Mar 04 10:00:48 <Dokujisan>	nexolix.com available
    Mar 04 10:01:26 <Dokujisan>	nexoic.com available
    Mar 04 10:04:51 <Dokujisan>	nexodo.com is not available, but I made a type and noxodo.com is available
    Mar 04 10:05:49 <Dokujisan>	nexorid.com available
    Mar 04 10:06:14 <div0>	nexolix lol
    Mar 04 10:06:18 <div0>	Nex...Oh I see!
    Mar 04 10:07:04 <Dokujisan>	would we consider numbers in the name?
    Mar 04 10:07:29 <div0>	if not too silly, yes
    Mar 04 10:07:30 <Dokujisan>	I don't know what signifigance a number ight have
    Mar 04 10:07:34 <div0>	n3xu1z = silly
    Mar 04 10:07:56 <div0>	nex2go - why not
    Mar 04 10:14:53 <}-z-{>	nex4.us AVAILABLE
    Mar 04 10:16:08 <}-z-{>	zenuis
    Mar 04 10:16:11 <div0>	hm... maybe, not sure
    Mar 04 10:16:13 <}-z-{>	zen u is :-P
    Mar 04 10:18:50 <Dokujisan>	my updated lsit...alphabetized
    Mar 04 10:18:52 <Dokujisan>	http://pastie.org/private/ocjjrj0175nvbbnqycqna
    Mar 04 10:18:53 <div0>	I'd prefer to keep religion out of it :P
    Mar 04 10:19:33 <Dokujisan>	oh... add nexodic.com to the available list
    Mar 04 10:20:10 <div0>	nexodiac
    Mar 04 10:20:13 <div0>	whatever that is
    Mar 04 10:20:15 <div0>	nexomaniac
    Mar 04 10:20:27 <div0>	nexiax
    Mar 04 10:20:46 <div0>	(or nexiacs)
    Mar 04 10:20:52 <div0>	necsiax please not, though
    Mar 04 10:21:23 <div0>	can I invite morphed here btw?
    Mar 04 10:21:29 <Dokujisan>	ok so I would suggest a plan A, B and C... Plan A is to aim for nex????.com, Plan B is to consider a nex???.org that doesn't have an available .com...and Plan C is to consider something not beginning with nex????
    Mar 04 10:21:33 <}-z-{>	yes, you can
    Mar 04 10:21:58 <}-z-{>	and other developers / forces within the community who'd like to help out
    Mar 04 10:22:06 <div0>	Dokujisan: I'd prefer plan AB
    Mar 04 10:22:06 *	morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 04 10:22:10 <morphed>	hi
    Mar 04 10:22:19 <div0>	i.e. both .com and .org should be available if possible
    Mar 04 10:22:29 <div0>	also, google should find less than 100 hits for the name :P
    Mar 04 10:22:30 <Dokujisan>	right now, Plan A isn't turning out too well. Plan B might have some good names in that "taken" list for .coms.... Plan C is wide open
    Mar 04 10:22:47 <div0>	nex does not have to be at the beginning
    Mar 04 10:22:50 <morphed>	what are the plans ?
    Mar 04 10:23:06 <div0>	connexius
    Mar 04 10:23:12 <Dokujisan>	If I were doing this on my own, I would go with Plan C, but I understand the desire to stick with the "nex" prefix
    Mar 04 10:23:21 <div0>	well, let's say
    Mar 04 10:23:26 <div0>	I don't want to rule out C
    Mar 04 10:23:31 <div0>	if you have a really good nex-free name, go ahead :P
    Mar 04 10:23:36 <div0>	we shouldn't be too fixated on it
    Mar 04 10:23:51 <morphed>	open game developers OGD 
    Mar 04 10:23:51 <div0>	but dellum, modiem, please not :P
    Mar 04 10:23:55 <Dokujisan>	morphed: my lastest list of name searching.... http://pastie.org/private/ocjjrj0175nvbbnqycqna
    Mar 04 10:24:00 <div0>	morphed: I mean as game name
    Mar 04 10:24:06 <div0>	OGDFPS isn't too good :P
    Mar 04 10:24:12 <div0>	DaveFPS is better for that, then :P
    Mar 04 10:24:24 <morphed>	i mean team name 
    Mar 04 10:24:27 <div0>	also, OGD sounds like OCD
    Mar 04 10:24:36 <Dokujisan>	we discussed that the team name would be based on the game name
    Mar 04 10:24:41 <Dokujisan>	since the team would only focus on this one game
    Mar 04 10:24:41 <div0>	probably best
    Mar 04 10:24:47 <div0>	if there are spinoffs, they can have their own team name
    Mar 04 10:24:51 <div0>	and team wouldn't be exclusive
    Mar 04 10:24:59 <div0>	so one person can be on multiple teams with no problem :P
    Mar 04 10:25:28 <div0>	basically, I think we should be "open source development team of $GAME", and not "company developing $GAME" :P
    Mar 04 10:25:39 <}-z-{>	div0: what are you going to do about netradiant?
    Mar 04 10:25:47 <div0>	why?
    Mar 04 10:25:49 <div0>	that name can stay
    Mar 04 10:25:55 <div0>	also will stay on icculus
    Mar 04 10:25:56 <}-z-{>	under alientrap as well?
    Mar 04 10:26:00 <div0>	whether on alientrap, not sure
    Mar 04 10:26:03 <div0>	it's just the wiki there anyway
    Mar 04 10:26:09 <div0>	can be copied/moved anyway
    Mar 04 10:26:15 <div0>	development of NR is not alientrap hosted anyway
    Mar 04 10:26:42 <Dokujisan>	that's good
    Mar 04 10:26:43 <div0>	however - if we make a portal with lots of "newnex" related stuff
    Mar 04 10:26:47 <div0>	then NR shall go there too
    Mar 04 10:26:52 <div0>	it'd simply BELONG there
    Mar 04 10:26:58 <div0>	old page on alientrap can become a redirect
    Mar 04 10:27:05 <}-z-{>	which is the point I'm trying to make :-P
    Mar 04 10:27:15 <}-z-{>	just something to consider while we talk out all plans
    Mar 04 10:27:33 <Dokujisan>	we can expect to do redirects on alientrap.org? :-o
    Mar 04 10:27:35 <div0>	just, I doubt redmine wiki can perform a redirect
    Mar 04 10:27:43 <}-z-{>	yes we can
    Mar 04 10:27:46 <div0>	Dokujisan: I really doubt that AT will object to it
    Mar 04 10:27:48 <}-z-{>	div0: meta tag at worst
    Mar 04 10:27:48 <div0>	so yes, we can
    Mar 04 10:27:52 <Dokujisan>	ok
    Mar 04 10:27:52 <div0>	AT simply wouldn't care :P
    Mar 04 10:27:55 <}-z-{>	.htaccess at best
    Mar 04 10:28:05 <div0>	only alientrap.org/nexuiz we maybe can't get :P
    Mar 04 10:28:05 <}-z-{>	nexzen.org AVAILABLE
    Mar 04 10:28:09 <div0>	dev.alientrap.org sure will be ours
    Mar 04 10:28:24 <morphed>	isnt alientrap.org hosted on willis server ?
    Mar 04 10:28:28 <div0>	yes, so?
    Mar 04 10:28:35 <}-z-{>	zennex.org AVAILABLE
    Mar 04 10:28:38 <div0>	basically, I am saying... dev.alientrap.org is not public
    Mar 04 10:28:44 <div0>	if we don't annoy Vermeulen TOO much
    Mar 04 10:28:51 <div0>	we will sure be able to keep a redirect from there
    Mar 04 10:28:57 <div0>	(or even the whole hostname in DNS)
    Mar 04 10:29:07 <div0>	[-z-]: no zen please :P
    Mar 04 10:29:14 <div0>	it's a religious term
    Mar 04 10:29:18 <div0>	keep religion out of the game
    Mar 04 10:29:24 <}-z-{>	spirital maybe, religious?
    Mar 04 10:29:28 <div0>	yes
    Mar 04 10:29:31 <div0>	same thing basically
    Mar 04 10:29:37 <}-z-{>	well it does make me think of zencart
    Mar 04 10:29:41 <}-z-{>	which is anything but ZEN
    Mar 04 10:29:42 <div0>	it is a form of belief
    Mar 04 10:29:52 <}-z-{>	it's more like an abortion of code
    Mar 04 10:29:55 <div0>	one one in a God, but still a belief
    Mar 04 10:29:57 <div0>	so is atheism :P
    Mar 04 10:30:03 <div0>	*not
    Mar 04 10:30:14 <}-z-{>	jesusnexgodbuddha.com
    Mar 04 10:30:17 <div0>	no :P
    Mar 04 10:30:22 <div0>	you forgot the flying spaghetti monster
    Mar 04 10:30:25 <div0>	and xenu
    Mar 04 10:30:26 <}-z-{>	:-P
    Mar 04 10:30:27 <div0>	and and and
    Mar 04 10:30:34 <}-z-{>	of course xenu, how could I forget :-P
    Mar 04 10:30:39 <div0>	but seriously - don't go there
    Mar 04 10:31:02 <}-z-{>	renexia ?
    Mar 04 10:31:09 <div0>	doesn't fit the game
    Mar 04 10:31:12 <div0>	sounds like a MMORPG
    Mar 04 10:31:29 <div0>	renexed?
    Mar 04 10:31:32 <div0>	(like: reslimed)
    Mar 04 10:31:40 <}-z-{>	it's available
    Mar 04 10:31:47 <div0>	but I don't really like it
    Mar 04 10:31:50 <div0>	it's a bit uninspired :P
    Mar 04 10:32:02 <div0>	too generic
    Mar 04 10:33:05 <div0>	NARF ain't a RipofF
    Mar 04 10:33:08 <}-z-{>	nexy.us AVAILABLE
    Mar 04 10:33:28 <div0>	am not a friend of .us, but fine, put in the list
    Mar 04 10:33:39 <}-z-{>	we can just call it nexy in that case :-P
    Mar 04 10:33:40 <div0>	unless the name means we have to take leileilol's models
    Mar 04 10:33:49 <}-z-{>	how's that?
    Mar 04 10:33:54 <div0>	nexy, no, 116000 google hits
    Mar 04 10:34:28 <div0>	still... try brainstorming for non-nex names
    Mar 04 10:34:36 <div0>	these have been under-tried :P
    Mar 04 10:34:51 <div0>	I think we have enough stuff with nex now :P
    Mar 04 10:34:55 <div0>	Crylix
    Mar 04 10:35:04 <div0>	Cryluiz
    Mar 04 10:35:07 <}-z-{>	makes me think of orange things
    Mar 04 10:35:14 <div0>	hm...
    Mar 04 10:35:23 <}-z-{>	sounds like crylink too :-P
    Mar 04 10:35:25 <div0>	Hagrix
    Mar 04 10:35:28 <}-z-{>	ha
    Mar 04 10:35:32 <}-z-{>	I see what you're doing
    Mar 04 10:35:49 <div0>	right :P
    Mar 04 10:35:52 <morphed>	xolaris 
    Mar 04 10:35:55 <div0>	don't have to name it after the Nex
    Mar 04 10:36:11 <div0>	Laseris
    Mar 04 10:36:17 <div0>	no, bad
    Mar 04 10:36:28 <div0>	can we rename the laser gun BTW?
    Mar 04 10:36:34 <div0>	(like, to the new name of the game)
    Mar 04 10:36:43 <div0>	it is the most important part of the game after all
    Mar 04 10:36:49 <div0>	should be named like the game
    Mar 04 10:36:56 <div0>	the sniper gun on the other hand is quite generic :P
    Mar 04 10:37:22 <div0>	morphed: Xolaris... haha
    Mar 04 10:37:34 <div0>	just noticed now that it is not named after Solaris but after a player model :P
    Mar 04 10:37:41 <div0>	Nexitant
    Mar 04 10:37:54 <div0>	"Skadium"
    Mar 04 10:38:02 <div0>	"Spexop"
    Mar 04 10:38:11 <}-z-{>	I'm the skad man! "skiddly diddly bo boop wow"
    Mar 04 10:38:13 <div0>	"The Incredible Marine"
    Mar 04 10:38:21 <}-z-{>	TIM
    Mar 04 10:38:29 <div0>	right
    Mar 04 10:38:35 <}-z-{>	no more dave
    Mar 04 10:38:40 <div0>	I am already using that as "working title" for rube goldberg machines :P
    Mar 04 10:38:50 <}-z-{>	;)
    Mar 04 10:38:51 <div0>	and a possible future TIM-like mod :P
    Mar 04 10:39:01 <}-z-{>	I wish there was a good FOSS version of TIM
    Mar 04 10:39:11 <div0>	I was going to make one based on Nexuiz
    Mar 04 10:39:17 <}-z-{>	>.>
    Mar 04 10:39:18 <div0>	but stopped when finding out how unpredictable ODE is in DP
    Mar 04 10:39:28 <}-z-{>	:-\
    Mar 04 10:39:33 <div0>	I could reset the machine and restart, and it failed in another way
    Mar 04 10:39:47 <morphed>	its realistic that way
    Mar 04 10:39:50 <div0>	morphed: yes
    Mar 04 10:39:52 <div0>	but annoying :P
    Mar 04 10:40:10 <div0>	once that ODE problem is solved
    Mar 04 10:40:15 <div0>	I _will_ make the TIM-like game
    Mar 04 10:40:16 <div0>	except in 3D
    Mar 04 10:40:22 <div0>	so you move in spectator mode around, and move stuff
    Mar 04 10:40:30 <div0>	and then can start the machine
    Mar 04 10:40:31 <Dokujisan>	ok I'm going to start venturing more into the non-nex names
    Mar 04 10:40:34 <div0>	watch it from your view
    Mar 04 10:40:42 <div0>	and at any time, reset and edit further
    Mar 04 10:41:06 <div0>	but, for this the ODE support must become more stable
    Mar 04 10:41:19 <Dokujisan>	keep in mind that I'm tracking these names I'm trying just for ideas, so even if dellum is obviously bad (which I think it is) it could lead to another idea
    Mar 04 10:41:28 <div0>	right
    Mar 04 10:41:35 <div0>	maybe categorize further into bad ideas and possibly okay :P
    Mar 04 10:41:42 <div0>	we don't have anything really good yet, though
    Mar 04 10:41:44 <}-z-{>	Novel Earth Xebec
    Mar 04 10:41:47 <div0>	the "bad ideas" of course can be revived
    Mar 04 10:42:15 <div0>	anyway, have to go
    Mar 04 10:42:19 <div0>	have fun, and  find a good name :P
    Mar 04 10:42:28 <}-z-{>	:-P
    Mar 04 10:42:32 <}-z-{>	laterz
    Mar 04 10:42:35 <Dokujisan>	cya
    Mar 04 10:42:38 <div0>	don't worry, unless you call it nextoris, I won't be likely to reject it
    Mar 04 10:42:51 <div0>	(although, that would go well with Zygotic)
    Mar 04 10:43:46 <}-z-{>	nexfork
    Mar 04 10:43:48 <}-z-{>	^_^
    Mar 04 10:47:51 <Dokujisan>	we're going to be letting go of that japanese kanji for "N"
    Mar 04 10:47:58 <Dokujisan>	well that looks like an "N"
    Mar 04 10:48:03 <Dokujisan>	or "n"
    Mar 04 10:48:08 <Dokujisan>	but
    Mar 04 10:48:12 <}-z-{>	maybe find a new kanji character?
    Mar 04 10:48:23 <Dokujisan>	that is why I was leaning toward something beginning with 'x'
    Mar 04 10:48:54 <morphed>	celerity
    Mar 04 11:22:26 <morphed>	i used company name generator and this is what it generated for us http://img237.imageshack.us/img237/6928/companyname.jpg :)
    Mar 04 11:27:16 <Dokujisan>	haha
    Mar 04 11:36:23 <div0>	yes, that onme we want
    Mar 04 11:39:35 <morphed>	but .com is taken :(
    Mar 04 11:42:06 <morphed>	some other company names with .com free to register http://img535.imageshack.us/img535/476/comanynames.jpg ;]
    Mar 04 11:48:09 <}-z-{>	haha, fucki
    Mar 04 11:50:00 *	morphed has quit (Ping timeout: 364 seconds)
    Mar 04 11:53:55 *	morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 04 12:11:57 <Dokujisan>	}-z-{: you're in florida now?
    Mar 04 12:15:37 <}-z-{>	yes, I am
    Mar 04 12:15:59 <Dokujisan>	which city?
    Mar 04 12:16:10 <Dokujisan>	my dad and brother are in the room and we're discussing possibly moving
    Mar 04 12:16:15 <}-z-{>	Tallahassee
    Mar 04 12:16:19 <}-z-{>	in tha panhandle
    Mar 04 12:16:29 <Dokujisan>	ah, ok. we're talking about the tampa area
    Mar 04 12:16:34 <Dokujisan>	or sarasota
    Mar 04 12:16:35 <}-z-{>	yeah, that's a bit lower :-P
    Mar 04 12:16:38 <}-z-{>	3-4 hours
    Mar 04 12:16:42 <}-z-{>	actually more
    Mar 04 12:16:43 <}-z-{>	4-5
    Mar 04 12:16:45 <}-z-{>	haha :)
    Mar 04 12:16:55 <}-z-{>	I'll be back in a bit, guys are waiting for me to go to lunch
    Mar 04 13:32:58 <Samual>	Umm
    Mar 04 13:33:02 <Samual>	Someone highlighted me above
    Mar 04 13:33:04 <Samual>	But my log cut off
    Mar 04 13:33:10 <Samual>	Could someone post back what it was?
    Mar 04 13:33:31 <Dokujisan>	let me check
    Mar 04 13:34:23 <Samual>	Thanks
    Mar 04 13:37:32 <Dokujisan>	Samual: http://pastie.org/private/wx3tynbiguzpap2zzscvpq
    Mar 04 13:39:27 <Samual>	Hmmm
    Mar 04 13:39:29 <Samual>	That's odd
    Mar 04 13:39:31 <Samual>	It's not in there
    Mar 04 13:39:51 <Samual>	It must be older than that Dokujisan 
    Mar 04 13:40:12 <Samual>	Meh nevermind, i'm sure it wasn't important
    Mar 04 13:40:56 <Dokujisan>	Samual: sorry, it cut off. Div0 quoted what you said right before that
    Mar 04 13:41:04 <Dokujisan>	about verm being lame, but it's hard to leave nexuiz
    Mar 04 13:41:16 <Dokujisan>	or it's hard to abandon
    Mar 04 13:46:35 <Samual>	Ah
    Mar 04 14:00:16 <}-z-{>	10% of my job still requires me to unplug something and plug it back in >_<
    Mar 04 14:08:32 <Samual>	-z-: And what would that be?
    Mar 04 14:08:41 <Samual>	-z-: Get switches :P
    Mar 04 14:48:54 <Samual>	Hey div0
    Mar 04 14:57:56 <morphed>	come on, brainstorm that name goddamnit 
    Mar 04 15:16:34 <}-z-{>	it is a switch
    Mar 04 15:16:48 <}-z-{>	it's a netgear 48 port switch that I need to unplug once a month when it fucks up
    Mar 04 15:18:00 <Dokujisan>	morphed: I'll do more brainstorming in a bit, but I went through a shitton of names already
    Mar 04 15:19:19 <Dokujisan>	go through this list and remove the ones that you are absolutely against (in the top and bottom lists)
    Mar 04 15:19:21 <Dokujisan>	http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 15:19:53 <Dokujisan>	just go through and indent the ones you don't like
    Mar 04 15:19:56 <Dokujisan>	and give me back the list
    Mar 04 15:20:01 <Dokujisan>	Samual: morphed -z-
    Mar 04 15:20:07 <Dokujisan>	Taoki: 
    Mar 04 15:20:11 <Samual>	Hmm?
    Mar 04 15:20:22 <Samual>	Well
    Mar 04 15:20:24 <Taoki>	I'm here for the next minutes
    Mar 04 15:20:30 <Dokujisan>	go through this list and indent the ones that you absolutely don't like and give the list back to me
    Mar 04 15:20:30 <Dokujisan>	http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 15:20:39 <Dokujisan>	in both the top and bottom lists
    Mar 04 15:20:53 <Taoki>	ok
    Mar 04 15:20:57 <morphed>	cant we use 2 words for a name ?
    Mar 04 15:21:04 <Dokujisan>	just start with this first
    Mar 04 15:21:09 <Dokujisan>	smaller name would be better
    Mar 04 15:21:24 <morphed>	why ?
    Mar 04 15:21:34 <Dokujisan>	simplicity
    Mar 04 15:21:38 <Samual>	The easier it is to pronounce the better :P
    Mar 04 15:21:49 <Samual>	:P
    Mar 04 15:21:51 <Dokujisan>	I'm open to two names, but that is more like a Plan D
    Mar 04 15:21:55 <morphed>	i dont have problems with modern warfare, or bad company 
    Mar 04 15:22:04 <Dokujisan>	morphed: can you just start with this first?
    Mar 04 15:22:09 <Dokujisan>	and we can get to that idea after
    Mar 04 15:22:23 <morphed>	Dokujisan: im afraid i dont like any name there :(
    Mar 04 15:22:31 <Dokujisan>	pick the better ones
    Mar 04 15:22:37 <Dokujisan>	they're not all equal
    Mar 04 15:23:26 <morphed>	"nexodicok sa
    Mar 04 15:23:26 <morphed>	" really ? :)
    Mar 04 15:23:43 <Dokujisan>	hu?
    Mar 04 15:23:50 <Dokujisan>	oops
    Mar 04 15:23:56 <Dokujisan>	not sure what happened there
    Mar 04 15:24:10 <morphed>	its sounds like mix of nex, dick and cock ;)
    Mar 04 15:24:14 <Dokujisan>	that is supposed to be "nexodic"
    Mar 04 15:24:26 <Dokujisan>	and I accidentlally typed "ok sa" 
    Mar 04 15:24:29 <Dokujisan>	like I was in IRC
    Mar 04 15:24:47 <Dokujisan>	I didn't realize which window was active :-P
    Mar 04 15:25:45 <Samual>	I said Zenux btw
    Mar 04 15:26:30 <Samual>	iirc -z- liked that one :X
    Mar 04 15:26:31 <morphed>	Zenon :)
    Mar 04 15:26:41 <Samual>	morphed, no :P Common :P
    Mar 04 15:26:52 <morphed>	its redneck name in polish :)
    Mar 04 15:37:17 *	FruitieX (~FruitieX@a83-245-194-105.elisa-laajakaista.fi) has joined #notnexuiz
    Mar 04 15:37:21 <FruitieX>	Evening.
    Mar 04 15:37:53 <Samual>	Ello
    Mar 04 15:38:04 <Taoki>	hi
    Mar 04 15:38:07 <morphed>	hi
    Mar 04 15:38:07 <Samual>	Right now we're still trying to find a name if we do fork
    Mar 04 15:38:15 <morphed>	when we do fork
    Mar 04 15:38:17 <Taoki>	almmost done with the list here
    Mar 04 15:38:28 <FruitieX>	Zymotic
    Mar 04 15:38:31 <FruitieX>	hehe kidding
    Mar 04 15:38:47 <morphed>	old joke ;)
    Mar 04 15:40:24 <Taoki>	I actually considered that at first, but nah
    Mar 04 15:41:36 <morphed>	Citomyz ziuxen
    Mar 04 15:44:08 <Dokujisan>	did  you guys go through that list?
    Mar 04 15:44:58 <morphed>	taoki is working on it right now afaik
    Mar 04 15:45:11 <Taoki>	yes, almost done here, in a minute
    Mar 04 15:46:29 <morphed>	http://norefuge.net/vgng/vgng.html 
    Mar 04 15:47:34 <morphed>	Amish Assault Pinball 
    Mar 04 15:48:19 <FruitieX>	Lol
    Mar 04 15:48:21 <morphed>	Battle Shock 
    Mar 04 15:48:21 <Taoki>	Done here http://pastebin.com/nWkJF7TD
    Mar 04 15:48:31 <Taoki>	Yeah, I left only 4 from the available .coms
    Mar 04 15:48:42 <Dokujisan>	thanks
    Mar 04 15:48:46 <Taoki>	Np
    Mar 04 15:49:05 <Taoki>	After this, we should probably make a tpo 5-6 and do an elimination, or a forum pool with them
    Mar 04 15:49:09 <Taoki>	*top
    Mar 04 15:49:10 <FruitieX>	does not have to be .com :-)
    Mar 04 15:49:20 <Taoki>	thats good
    Mar 04 15:49:34 <Samual>	I personally want Zenux :P
    Mar 04 15:49:48 <Samual>	Or Xenux 
    Mar 04 15:50:31 <Taoki>	Yes, same with the first :)
    Mar 04 15:50:39 <morphed>	its it name of a god of some cult ?
    Mar 04 15:50:39 <Taoki>	Xenux too, but not as much
    Mar 04 15:51:06 <Taoki>	Zenux or Zenuix or even Zeniux were my favorites from the start
    Mar 04 15:51:06 <Samual>	What I would prefer is not having to change the name at all
    Mar 04 15:51:12 <Samual>	But it seems IllFonic doesn't want that.
    Mar 04 15:52:45 <morphed>	everybody have troubles saying nexuiz 
    Mar 04 15:52:53 <Dokujisan>	yep
    Mar 04 15:52:58 <}-z-{>	div suggested we call it 'capsized' :-P
    Mar 04 15:53:01 <Dokujisan>	Nexuiz never was a good name
    Mar 04 15:53:13 <}-z-{>	as a joke of course but I figured I'd spread the humor
    Mar 04 15:53:17 <Dokujisan>	but the symbol was good and the shortened "Nex" and "Nexers" sounded good
    Mar 04 15:53:31 <}-z-{>	nextfps
    Mar 04 15:53:37 <Dokujisan>	so if we can come up with a name that also has good features, but isn't confusing to pronounce, then we'll be doing well
    Mar 04 15:53:55 <}-z-{>	nexfor (what's a nex for?)
    Mar 04 15:54:09 <FruitieX>	22:53:15 < }-z-{> div suggested we call it 'capsized' :-P
    Mar 04 15:54:10 <FruitieX>	:p
    Mar 04 15:54:12 <}-z-{>	there's a dickfore on your face
    Mar 04 15:54:17 <}-z-{>	"what's a dick for?"
    Mar 04 15:54:22 <Dokujisan>	Try to imagine the first time you saw the name "Nexuiz"
    Mar 04 15:54:31 <Dokujisan>	remind yourself that your reaction was "wtf?"
    Mar 04 15:54:46 <Dokujisan>	so that way when we are thinking about this new name, we're letting that name go
    Mar 04 15:55:14 <Dokujisan>	we've been conditioned to be used to "Nexuiz" and we're familiar with it now and associate good things with it
    Mar 04 15:55:18 <Dokujisan>	but it's really not an awesome name
    Mar 04 15:55:36 <}-z-{>	I said, "oh, must be european"
    Mar 04 15:55:44 <Dokujisan>	likewise, we can build up another name that starts off being more clear to pronounce
    Mar 04 15:55:49 <Samual>	I thought it was alien.....
    Mar 04 15:55:52 <Samual>	.... Alientrap
    Mar 04 15:55:52 <morphed>	iirc when nexuiz was showed first time in tv, presenter had troubles to say it 
    Mar 04 15:55:59 <}-z-{>	because we english speaking folk only use language rules that make sense.....
    Mar 04 15:57:28 <Dokujisan>	<CuBe0wL> tbh, me too :D
    Mar 04 15:57:35 <Dokujisan>	<CuBe0wL> I never knew how to spell it, untill the first time I've heard the announcer :D
    Mar 04 15:57:44 <Dokujisan>	I'm talking cubeowl into the fork
    Mar 04 15:57:56 <Dokujisan>	he's kinda heartbroken 
    Mar 04 15:58:08 <Dokujisan>	sorta like Samual  :-P
    Mar 04 15:58:14 <Samual>	Yes >.>
    Mar 04 15:58:18 <Samual>	I liked Nexuiz <.<
    Mar 04 15:58:31 <Samual>	On the other hand, this leaves us open to changes
    Mar 04 15:58:36 <Dokujisan>	exactly!
    Mar 04 15:58:38 <Dokujisan>	good changes!!!
    Mar 04 15:58:39 <Samual>	And it allows us to structure the team better
    Mar 04 15:58:43 <Dokujisan>	yes!!!!!!!
    Mar 04 16:00:25 <}-z-{>	yep
    Mar 04 16:00:31 <}-z-{>	build a stronger smarter foundation
    Mar 04 16:00:36 <}-z-{>	and 'clean out the attic' if you will
    Mar 04 16:01:01 <morphed>	also it will boost motivation and energy 
    Mar 04 16:01:11 <}-z-{>	the hardest part of the transition will be to rebuild the infrastructure for development
    Mar 04 16:01:18 <}-z-{>	which will take a least 3 servers
    Mar 04 16:01:23 <Dokujisan>	samual, -z-, morphed: did you go through the list?
    Mar 04 16:01:35 <}-z-{>	the repository can be handled on icculus git
    Mar 04 16:01:57 <}-z-{>	I have a machine (nn vps) I can donate to be used for test builds and test servers, maybe other things
    Mar 04 16:02:17 <}-z-{>	and shared hosting for the website, mirrors.  dokujisan I believe also has a webserver for such files
    Mar 04 16:02:25 <}-z-{>	I have a mac to do cross platform compiles
    Mar 04 16:02:29 <}-z-{>	Dokujisan: not yet
    Mar 04 16:02:52 <Samual>	Dokujisan, I honestly don't like many at all :P lawl Taoki's list is more than what I would've liked
    Mar 04 16:03:21 <Dokujisan>	Samual: this is to help give a direction on more brainstorming
    Mar 04 16:03:31 <}-z-{>	zeniux is the smoothest out of the list still but not sure if that's the best and div didn't want to use 'zen'
    Mar 04 16:03:37 <Dokujisan>	pick your best, even if they aren't fully good enough for your liking
    Mar 04 16:03:57 <Samual>	Xenuix?
    Mar 04 16:04:02 <Samual>	Er
    Mar 04 16:04:03 <}-z-{>	that's gross
    Mar 04 16:04:04 <Samual>	Xeniux
    Mar 04 16:04:13 <Samual>	stfu fool, I don't see you thinking up anything better
    Mar 04 16:04:25 <}-z-{>	that's because you weren't here earlier when we were thinking
    Mar 04 16:04:29 <}-z-{>	oooooh
    Mar 04 16:04:34 <}-z-{>	gonna need some ice for that burn :-P
    Mar 04 16:04:35 <Samual>	I saw the log
    Mar 04 16:04:46 <Samual>	Dokujisan pastebined it :P
    Mar 04 16:04:47 <}-z-{>	how about notnex?
    Mar 04 16:04:48 <Samual>	I wasn't impressed
    Mar 04 16:05:01 <Dokujisan>	Samual: where?
    Mar 04 16:05:09 <Samual>	From this room?
    Mar 04 16:05:09 <Dokujisan>	oh nvm
    Mar 04 16:05:12 <Dokujisan>	I misread
    Mar 04 16:05:14 <Samual>	lawl
    Mar 04 16:05:26 <}-z-{>	uzinex
    Mar 04 16:05:48 <}-z-{>	zinex.org AVAILABLE
    Mar 04 16:05:56 <}-z-{>	5 letter ones are good if we can get one of derm
    Mar 04 16:06:14 <Dokujisan>	yreah
    Mar 04 16:06:25 <}-z-{>	xudex
    Mar 04 16:06:27 <}-z-{>	ex you decks
    Mar 04 16:06:34 <}-z-{>	welcome to ex you decks
    Mar 04 16:07:01 <Dokujisan>	don't pick each name apart. mainly just skim through and remove the ones that are absolutely horrible
    Mar 04 16:07:03 <morphed>	Dokujisan: my filter http://pastie.org/854491
    Mar 04 16:07:07 <Dokujisan>	k thanks
    Mar 04 16:07:21 <FruitieX>	zinex.org is something to consider :-)
    Mar 04 16:07:22 <}-z-{>	devnex?
    Mar 04 16:07:32 <morphed>	how about we invite tzork here ?
    Mar 04 16:07:37 <}-z-{>	go for it
    Mar 04 16:07:38 <Dokujisan>	absolutely
    Mar 04 16:07:40 <FruitieX>	do it
    Mar 04 16:07:44 <Dokujisan>	I was trying to get cubeowl first
    Mar 04 16:07:47 <}-z-{>	dev[elopers][nex]uiz
    Mar 04 16:07:55 <}-z-{>	err, I did my boxes rong
    Mar 04 16:08:01 <}-z-{>	dev[elopers]nex[uiz]
    Mar 04 16:08:03 <}-z-{>	wrong*
    Mar 04 16:08:04 <}-z-{>	^_^
    Mar 04 16:08:15 <Samual>	dex?
    Mar 04 16:08:17 <Samual>	:P
    Mar 04 16:08:23 *	CuBe0wL (~akion@BKTFW13.usn.hu) has joined #notnexuiz
    Mar 04 16:08:26 <Dokujisan>	yay :-D
    Mar 04 16:08:29 <Samual>	Welcome, CuBe0wL 
    Mar 04 16:08:30 <CuBe0wL>	hey
    Mar 04 16:08:33 <}-z-{>	hey
    Mar 04 16:08:58 <morphed>	hi
    Mar 04 16:09:08 <Dokujisan>	CuBe0wL: go through this list and remove the ones that are absolutely horrible and give the list back to me... http://pastie.org/private/3cxafiq3ogsmnbcileaoog
    Mar 04 16:09:49 <morphed>	or shot some new names 
    Mar 04 16:09:55 <FruitieX>	hai CuBe0wL 
    Mar 04 16:09:57 <Dokujisan>	do that after
    Mar 04 16:10:39 <FruitieX>	night
    Mar 04 16:10:41 <CuBe0wL>	I think I'll have to read the avaible .coms
    Mar 04 16:10:43 <FruitieX>	will read backlog in morning :>
    Mar 04 16:10:57 <Samual>	Dokujisan, can you include .org?
    Mar 04 16:11:01 <Dokujisan>	CuBe0wL: we have a plan A and plan B...so choose also the non-available .coms
    Mar 04 16:11:10 <Samual>	How are you generating that list Dokujisan 
    Mar 04 16:11:12 <Dokujisan>	Samual: we'll get to that after
    Mar 04 16:11:14 <Dokujisan>	by hand
    Mar 04 16:11:28 <Samual>	I bet you can get a script to do that
    Mar 04 16:11:31 <}-z-{>	biznex haha
    Mar 04 16:11:32 *	Samual looks at -z-
    Mar 04 16:11:46 <}-z-{>	was funnier in my head
    Mar 04 16:11:55 <Dokujisan>	Samual: I have a program that will do it actually
    Mar 04 16:11:58 <}-z-{>	because it sounds like 'biznazz'
    Mar 04 16:12:08 <}-z-{>	Samual: I have one, it's called an intern :-P
    Mar 04 16:12:42 <Samual>	Bitch I have one too
    Mar 04 16:12:46 <Samual>	It's called a bash script
    Mar 04 16:12:52 <}-z-{>	more like bitch script
    Mar 04 16:12:54 <Samual>	It just resolves the names :P
    Mar 04 16:12:55 <Samual>	-.-
    Mar 04 16:12:58 <}-z-{>	:-P
    Mar 04 16:13:11 <CuBe0wL>	Quadriux ?
    Mar 04 16:13:29 <}-z-{>	alright, time to hop onto my iron horse and gallop away from the falling sun
    Mar 04 16:13:40 <}-z-{>	I will catch you gentlemen later
    Mar 04 16:13:41 <CuBe0wL>	pronounced as "Kvadrius"
    Mar 04 16:13:49 <}-z-{>	keep me updated on progress
    Mar 04 16:14:03 <}-z-{>	quadraplinex
    Mar 04 16:14:16 <}-z-{>	cleanex (har har)
    Mar 04 16:14:29 <}-z-{>	klennex is a brand of facial tissues
    Mar 04 16:14:31 <CuBe0wL>	xodiox ... this one has pottential imhp
    Mar 04 16:14:32 <Samual>	We'd get sued on that one
    Mar 04 16:14:39 <}-z-{>	k, pz
    Mar 04 16:14:44 <Samual>	kleenex actually :P
    Mar 04 16:14:44 <Samual>	Cya
    Mar 04 16:14:52 <CuBe0wL>	bye }-z-{ 
    Mar 04 16:14:56 <morphed>	CuBe0wL: xanax ;)
    Mar 04 16:15:04 <CuBe0wL>	haha
    Mar 04 16:15:30 *	Dokujisan waits for lists :-)
    Mar 04 16:15:34 <morphed>	exacly
    Mar 04 16:15:34 <CuBe0wL>	Forxiuz
    Mar 04 16:15:37 <CuBe0wL>	:D
    Mar 04 16:15:41 *	Dokujisan looks at Samual 
    Mar 04 16:15:45 <morphed>	CuBe0wL: maybe you know some cool drugs name ? :)
    Mar 04 16:15:54 <Samual>	Oh I didn't actually MAKE the script yet
    Mar 04 16:16:02 <Samual>	Tell -z- to make his interns do shit
    Mar 04 16:16:46 <CuBe0wL>	3-4-phosohoribozile-amino-imidazole-suchsinocarboxamid-snthethase :D
    Mar 04 16:16:49 <FruitieX>	IllNex
    Mar 04 16:16:52 <FruitieX>	NexFonics
    Mar 04 16:16:56 <FruitieX>	-s
    Mar 04 16:16:58 <FruitieX>	k bai :p
    Mar 04 16:17:09 <Dokujisan>	Samual: I don't need the script
    Mar 04 16:17:13 <Dokujisan>	just need input on the names
    Mar 04 16:17:18 <CuBe0wL>	that one is an enzyme name btw :D
    Mar 04 16:17:31 <Samual>	I like mainly what Taoki picked out
    Mar 04 16:17:34 <Dokujisan>	ok
    Mar 04 16:17:47 <Samual>	But mostly Zenux or Zeniux or Xenux and etc
    Mar 04 16:17:51 <CuBe0wL>	wuzzat?
    Mar 04 16:18:54 <CuBe0wL>	zeniux... yeah, then we'll have shaloin monks fighting over what's the best way to place that vase in a map according to latest feng-shui trends
    Mar 04 16:19:31 <Samual>	Haha
    Mar 04 16:19:34 <Samual>	Okay >.>
    Mar 04 16:19:34 <morphed>	zeniux is very silly in polish 
    Mar 04 16:19:47 <Samual>	Yes
    Mar 04 16:20:17 <CuBe0wL>	bbl
    Mar 04 16:20:41 <Samual>	Hey another thing we can change
    Mar 04 16:20:43 <Samual>	NEW FONT.
    Mar 04 16:20:46 <Samual>	..........
    Mar 04 16:20:47 <Samual>	.....................
    Mar 04 16:21:05 <Samual>	amiriteoramirite?
    Mar 04 16:21:09 <morphed>	maybe some cheesy oldschool arcade game name that tells about gameplay ?
    Mar 04 16:21:21 <CuBe0wL>	wingdings at least
    Mar 04 16:23:15 <Samual>	SFIACF?
    Mar 04 16:23:16 <Samual>	:X
    Mar 04 16:23:29 <Samual>	Simple, fast, intense and completely free -.-
    Mar 04 16:23:31 <Samual>	Nah i'm kidding.
    Mar 04 16:24:59 <Dokujisan>	ok here are my picks from the list
    Mar 04 16:25:00 <Dokujisan>	http://pastie.org/private/i9x5ccvczyqjajmngwhzwa
    Mar 04 16:25:44 *	tZork (~blah@c-b42f72d5.31-97-64736c10.cust.bredbandsbolaget.se) has joined #notnexuiz
    Mar 04 16:25:53 <morphed>	hi
    Mar 04 16:25:54 <Samual>	Ello tZork
    Mar 04 16:26:01 <Dokujisan>	I mostly like nexeon, nexion, nexotic, nexilus or nexolus out of the whole list....but I could tolerate the others
    Mar 04 16:26:02 <tZork>	hi
    Mar 04 16:26:27 <Samual>	Well
    Mar 04 16:26:44 <Samual>	I would say we could do a forum post and have a poll.....
    Mar 04 16:26:49 <Dokujisan>	nooooooooo
    Mar 04 16:26:52 <Dokujisan>	can't do this publicly
    Mar 04 16:26:54 <Samual>	But do we want to announce that we're doing this --
    Mar 04 16:26:56 <Samual>	Yeah
    Mar 04 16:27:09 <tZork>	to get the basics outa the way first: im not nessesarely pro-fork
    Mar 04 16:27:21 <Dokujisan>	yeah I cubeowl suggested that
    Mar 04 16:27:44 <Dokujisan>	cubeowl wasn't either, but I think I helped clear up some things about it for him. Now he's likely on the fence or better
    Mar 04 16:28:00 <Dokujisan>	tZork: what are your main reasons for not wanting a fork in this case?
    Mar 04 16:28:08 <Dokujisan>	what are the downsides?
    Mar 04 16:28:32 <tZork>	forking / renaming is sort of admitting defeat, and could possibly mean a lengthy conflict over who's got teh right to what.
    Mar 04 16:29:03 <Dokujisan>	ok first point, we've already discussed a plan for management
    Mar 04 16:29:12 <tZork>	im not saying im nessesarely against it eigther; just that its not a all good option.
    Mar 04 16:29:17 <morphed>	i think that we cant win this
    Mar 04 16:29:25 <Dokujisan>	it needs refinement, but keep in mind that Nexuiz had no outline for how to manage things
    Mar 04 16:29:30 <morphed>	and with GPL cant be any conflict
    Mar 04 16:30:07 <Dokujisan>	but with this new game, we're talking about having it run by a select group (which hasn't been decided yet, just the idea mentioned) for major decisions
    Mar 04 16:30:17 <Dokujisan>	not one single leader
    Mar 04 16:30:22 <Dokujisan>	and that already is a plus
    Mar 04 16:30:34 <tZork>	i would nto count on it morphed, the last few says i experianced things i tought gpl would make impossible.
    Mar 04 16:31:05 <Dokujisan>	we're also only going to be committed to this one game, unlike alientrap
    Mar 04 16:31:36 <Dokujisan>	verm admits that he did this choice primarily because he wants to further alientrap.
    Mar 04 16:32:26 <Dokujisan>	so whatever name is chosen for the game, the development team will be called "the <game-name> team"
    Mar 04 16:33:01 <tZork>	i sugest keeping the name nexuiz in that case. possibly pre or postfix it.
    Mar 04 16:33:03 <Dokujisan>	so far, we've had some great discussions with div0 over the past 24 hours
    Mar 04 16:33:10 <Dokujisan>	we can't keep the name
    Mar 04 16:33:17 <Dokujisan>	we need to let that go
    Mar 04 16:33:38 <morphed>	also its not such a great name 
    Mar 04 16:33:55 <Dokujisan>	here is what I said just a few minutes before you arrived.....
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> Try to imagine the first time you saw the name "Nexuiz"
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> remind yourself that your reaction was "wtf?"
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> so that way when we are thinking about this new name, we're letting that name go
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> we've been conditioned to be used to "Nexuiz" and we're familiar with it now and associate good things with it
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> but it's really not an awesome name
    Mar 04 16:33:57 <Dokujisan>	<}-z-{> I said, "oh, must be european"
    Mar 04 16:33:57 <Dokujisan>	<Dokujisan> likewise, we can build up another name that starts off being more clear to pronounce
    Mar 04 16:34:07 <tZork>	sure we can, noone owns it afaik. so something like Nexuiz::Nextgen is totally ok to use. and as a plus it will draw some media from ill*
    Mar 04 16:34:12 <tZork>	and at
    Mar 04 16:34:57 <Dokujisan>	I would think that alientrap would be able to fight for rights to that trademark....and that means vermeluen
    Mar 04 16:35:07 <tZork>	 <}-z-{> I said, "oh, must be european"
    Mar 04 16:35:13 <tZork>	teh fuck lol?
    Mar 04 16:35:23 <Dokujisan>	and I wouldn't feel right about just stealing that name anyway...not to mention that we don't have the domain
    Mar 04 16:35:32 <Dokujisan>	for whatever name we choose, we should have control over the domain
    Mar 04 16:35:44 <Dokujisan>	so nobody can just sell it or give it someone else
    Mar 04 16:36:34 <Dokujisan>	we also discussed numerous other improvements that we can focus on
    Mar 04 16:36:45 <Dokujisan>	like div0 agreed to a central registration system
    Mar 04 16:36:50 <morphed>	tZork: for me it sounds french 
    Mar 04 16:36:57 <Dokujisan>	with ihs certain preferences for protecting privacy
    Mar 04 16:37:02 <Dokujisan>	his*
    Mar 04 16:37:16 <Dokujisan>	and I talked with him at length about doing official training servers
    Mar 04 16:37:27 <Dokujisan>	and organizing mapping projects
    Mar 04 16:37:42 <Dokujisan>	basically, I hope to become an official community organizer in that regard
    Mar 04 16:38:21 <Dokujisan>	"official" being key here. When things are left to be done by only the community, there is a disadvantage. If things are done from the top down, a lot more momentum can be achieved.
    Mar 04 16:38:39 <Dokujisan>	I can hopefully do what I did for nexuiz but on a larger scale
    Mar 04 16:39:07 <Dokujisan>	this is precisely why I wanted a fork for nexuiz last year....but we didn't have a main developer
    Mar 04 16:39:24 <Dokujisan>	Nexuiz is a semi-successful project by accident
    Mar 04 16:39:54 <Dokujisan>	if it were handled properly, it would have achieved so much more by now
    Mar 04 16:40:18 <tZork>	i allready have two other game projects fightning for my attention, beside my regular work. only reaso i stayed with nexuiz was the legacy and the community.
    Mar 04 16:40:20 <Dokujisan>	but it really didn't have any organization or leadership. Div0 lead out of necessity
    Mar 04 16:40:42 <Dokujisan>	well really the community is likely to come along with us
    Mar 04 16:41:03 <Dokujisan>	we're going along with the new fork....and you like us, right? :-D
    Mar 04 16:41:17 <Dokujisan>	.........right? :-o
    Mar 04 16:41:36 <Dokujisan>	:-(
    Mar 04 16:41:44 <Dokujisan>	anyway, yeah I know you're involved with other games
    Mar 04 16:42:04 <tZork>	im sure not against you, but i dont know if i want to get involved at this point
    Mar 04 16:42:14 <Dokujisan>	like with cubeowl, I know you're busy and I wouldn't be asking you to take some official role that takes up all of your time
    Mar 04 16:42:21 <Dokujisan>	just support this new project in the same way you did nexuiz
    Mar 04 16:42:24 <tZork>	better to state that now then let you doos know it later
    Mar 04 16:42:31 <morphed>	tZork: but legacy will stay, and community will follow us 
    Mar 04 16:43:10 <tZork>	morphed: maybe, but its a chanse for me to make a break with it all. its not like im swamped with free time thise days.
    Mar 04 16:43:32 <tZork>	unlike when i first found nexuiz
    Mar 04 16:43:47 <Dokujisan>	I'm familiar with that
    Mar 04 16:44:41 <tZork>	one of my otehr projects is possibly merge-able with this fork tough. it thats doable; the story is diffrent.
    Mar 04 16:44:57 <morphed>	its like heroin, you cant quit :)
    Mar 04 16:45:18 <Taoki>	back
    Mar 04 16:45:25 <Dokujisan>	tZork: can you tell us more?
    Mar 04 16:45:30 <Dokujisan>	or is it under wraps?
    Mar 04 16:45:34 <Taoki>	Wow, nice to see so many people joined here :)
    Mar 04 16:45:44 <tZork>	not really Dokujisan, theres just not all that much to tell 
    Mar 04 16:46:30 <tZork>	teh idea was to make a game that adress what we tought nexuiz was missing. 
    Mar 04 16:47:15 <Dokujisan>	:-)
    Mar 04 16:47:17 <Dokujisan>	perfect
    Mar 04 16:47:23 <tZork>	and start from a clean codebase
    Mar 04 16:47:28 <Dokujisan>	ah I see
    Mar 04 16:47:39 <Dokujisan>	well that's interesting to me, though I'm not a nexuiz developer
    Mar 04 16:48:28 <tZork>	basicaly just briging along some ideas, both art and code are to be re-built to adress the large issue of legacy bagage nexuiz suffers from.
    Mar 04 16:48:37 <Dokujisan>	I've heard from other developers that there are some things in nexuiz code that need a cleanup
    Mar 04 16:49:39 <tZork>	despite div0's exelent work on it, its sadly still very much a planless design. as sutch adding and chaning and not the least understanding the code takes a massive effort
    Mar 04 16:49:52 <tZork>	at times
    Mar 04 16:49:55 <Dokujisan>	but I think this central user system is a HUGE change that div0 is finally onboard with and he sees the benefits of it
    Mar 04 16:50:30 <Dokujisan>	and that system can allow a lot of other features to be possible
    Mar 04 16:51:19 <tZork>	the second part of l!ft (the oterh project) where to place it in a steam-punk'ish artline. and quite possibly introduce classbased gameplay and PvM gameplay
    Mar 04 16:53:02 <Dokujisan>	I have basically been slowly heading out the door over the past 6 months as far as Nexuiz is concerned. I was too dissatisfied and wanted to focus on something more productive, so I also have other projects that I'm getting involved in
    Mar 04 16:53:13 <Dokujisan>	I gave up on Nexuiz community efforts
    Mar 04 16:53:21 <Dokujisan>	because it was like swimming upstream
    Mar 04 16:53:38 <tZork>	indeed
    Mar 04 16:53:43 <Dokujisan>	and this is why I tried to organize a fork before.... like last August
    Mar 04 16:54:03 <Dokujisan>	but this mistake by vermeleun could turn out to be a wonderful thing
    Mar 04 16:54:05 <Dokujisan>	a clean slate
    Mar 04 16:54:54 <Dokujisan>	and this interests me again
    Mar 04 16:55:08 <Dokujisan>	especially after my conversations with div0 over the past 24 hours
    Mar 04 16:55:35 <Dokujisan>	to be honest, div0 has changed over the past ....I dunno... 8 moths? To me he seems to have changed
    Mar 04 16:56:27 <Dokujisan>	months*
    Mar 04 16:57:27 <Dokujisan>	but it was good conversation, good ideas discussed and if half of them actually happen, the result will be a game a lot better than Nexuiz
    Mar 04 16:57:58 <Dokujisan>	with a bigger and stronger community
    Mar 04 16:58:16 <tZork>	i will air this with the l!ft team and get back
    Mar 04 17:01:11 <Dokujisan>	cool
    Mar 04 17:01:17 <tZork>	i do have a few thing i feel strongly should be done if i are to join this fork, like at the very least trash all current player models and seriosly audit the code. preferably remake it by pulling things over to a new codebase.
    Mar 04 17:01:35 <Dokujisan>	yes we did discuss new player models
    Mar 04 17:01:57 <Dokujisan>	and a new set of default maps
    Mar 04 17:02:13 <tZork>	that too
    Mar 04 17:02:18 <Dokujisan>	I started a list of maps that could use "fixing" and testing before being added
    Mar 04 17:09:11 <Taoki>	http://alientrap.org/forum/viewtopic.php?f=19&t=6054 =P
    Mar 04 17:09:32 <Taoki>	Been crazy enough to work on that all day
    Mar 04 17:10:51 <tZork>	hahaha
    Mar 04 17:10:55 <tZork>	exelent
    Mar 04 17:11:05 <Taoki>	thanks :P
    Mar 04 17:11:18 <Taoki>	http://pics.nexuizninjaz.com/images/zbcmceics6shje6u8wk9.jpg
    Mar 04 17:11:42 <tZork>	however.. make red spawn with tuba only. };P
    Mar 04 17:12:13 <tZork>	yarr i lol @ that pic Taoki =)
    Mar 04 17:12:26 <Dokujisan>	hahaha
    Mar 04 17:12:32 <Taoki>	I can't stop laughing myself... :D
    Mar 04 17:12:57 <Dokujisan>	very clever :-)
    Mar 04 17:13:33 <Taoki>	thx
    Mar 04 17:13:38 <Dokujisan>	Taoki: CTF?
    Mar 04 17:13:42 <tZork>	"where robbing is a way of showing love" omg spot on xD
    Mar 04 17:13:48 <Dokujisan>	I'll put it on HOCTF
    Mar 04 17:13:55 <Taoki>	Yeah, TDM and CTF
    Mar 04 17:14:14 <Taoki>	TDM is not so good, since you spawn at any spawn point of any team (not sure if that should be fixed)
    Mar 04 17:15:56 <Dokujisan>	heh you spelled "Nexiuz" properly :-)
    Mar 04 17:16:03 <Taoki>	yeah :P
    Mar 04 17:20:50 <CuBe0wL>	re for a sentence: back on topic, with the serious talking: what do you do with the servers? Let's say, we fork DCC servers to Nexuiz:NeXtgen. how'd you inform the masses, who don't read the forum?
    Mar 04 17:21:04 <CuBe0wL>	also, I've just had a BRILLIANT idea for fork name:
    Mar 04 17:21:09 <CuBe0wL>	Pheonix
    Mar 04 17:21:22 <CuBe0wL>	pronounced ofc. as Phoenix :D
    Mar 04 17:21:46 <Taoki>	Hmmm... that soulds pretty. Nice idea :)
    Mar 04 17:21:50 <Dokujisan>	I'll be informing the masses from HOCTF and HODM servers in the states
    Mar 04 17:21:52 <CuBe0wL>	homage to Nexuiz typo, and representing the way a killed game is reborn from it's ahes :D
    Mar 04 17:22:12 <Dokujisan>	heh, I made a server once called Phoenix
    Mar 04 17:22:21 <Taoki>	As for informing the masses, I spoke about that with div0 yesterday (we all did on the channel iirc). We can make a new csprogs and put it on servers, that will inform about this
    Mar 04 17:22:24 <Taoki>	Also, another idea
    Mar 04 17:22:31 <Dokujisan>	it was "rising from the ashes: of Fusion CTF" my previous server
    Mar 04 17:22:35 <Dokujisan>	turns out that name is overplayed
    Mar 04 17:22:48 <Dokujisan>	ok Nexiuz Wars loading on HOCTF1
    Mar 04 17:23:00 <Taoki>	Alias a command to chat a message when playing on servers. But not to press it all the time in an annoying spammy way
    Mar 04 17:23:09 <Taoki>	I'll do that once the new name is decided
    Mar 04 17:23:11 <tZork>	<CuBe0wL> Pheonix
    Mar 04 17:23:13 <tZork>	+1
    Mar 04 17:23:16 <Taoki>	And press it every once in a while on the DCC servers
    Mar 04 17:23:20 <Taoki>	yeah
    Mar 04 17:23:53 <CuBe0wL>	though I'm still pro Nexuiz, and no forking
    Mar 04 17:23:59 <CuBe0wL>	I like spoon better ;)
    Mar 04 17:25:35 <Dokujisan>	haha Taoki there are holes in the floor
    Mar 04 17:25:55 <Taoki>	holes?
    Mar 04 17:26:02 <Dokujisan>	yeah I fall through
    Mar 04 17:26:05 <CuBe0wL>	OT again before I leave: ffs, we've printed a final draft of my thesis before binding it, to read through once more
    Mar 04 17:26:17 <Taoki>	weird. Probably some compilation issues...
    Mar 04 17:26:19 <Taoki>	*issues
    Mar 04 17:26:24 <CuBe0wL>	I've already written a full A4 page with errors I've found
    Mar 04 17:26:25 <Dokujisan>	right outside the bases
    Mar 04 17:26:38 <CuBe0wL>	and I'm still at only the 10th page
    Mar 04 17:26:48 <Taoki>	If its on the terrain, might be another issue with patch meshes
    Mar 04 17:31:18 *	DibTop (~chatzilla@c-71-233-23-46.hsd1.ma.comcast.net) has joined #notnexuiz
    Mar 04 17:31:28 <DibTop>	hi notnexuiz :)
    Mar 04 17:31:29 <morphed>	phoenix is great idea but without switched letters 
    Mar 04 17:31:37 <Taoki>	hello
    Mar 04 17:31:46 <morphed>	hi
    Mar 04 17:31:57 <DibTop>	anyone have a pastie of what was already said so no one has to repeat
    Mar 04 17:32:29 <tZork>	i only got a partial
    Mar 04 17:32:29 <Taoki>	I rather like CuBe0wL's version with switched letters. It sounds a bit better for a game like Nexuiz (if we can still call it such until its renamed)
    Mar 04 17:33:08 <DibTop>	one thing im working on right now is rigging oblivion's latest model
    Mar 04 17:33:14 <tZork>	Dokujisan?
    Mar 04 17:33:22 <DibTop>	mostly for practice but if its any good
    Mar 04 17:34:15 DibTop div0 
    Mar 04 17:34:20 <Dokujisan>	DibTop: there has been a ton of conversation
    Mar 04 17:34:25 <Dokujisan>	I'll show you what I have
    Mar 04 17:34:27 <Dokujisan>	hang on
    Mar 04 17:34:30 <DibTop>	thanks
    Mar 04 17:35:52 <tZork>	im interested on what was said before i arrived too Dokujisan
    Mar 04 17:36:37 <Dokujisan>	here is the entire chat since I joine #notnexuiz yesterday
    Mar 04 17:36:39 <Dokujisan>	http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:37:43 <tZork>	heh a bit if bedtime reading ^^
    Mar 04 17:37:48 <Dokujisan>	:-)
    Mar 04 17:39:58 *	soul81 (~soul@a83-163-47-227.adsl.xs4all.nl) has joined #notnexuiz
    Mar 04 17:40:05 <Dokujisan>	soul81: ?
    Mar 04 17:40:18 <Dokujisan>	from netherlands?
    Mar 04 17:40:18 *	soul81 is now known as SoulKeeper_p
    Mar 04 17:40:20 <SoulKeeper_p>	;)
    Mar 04 17:40:20 <Dokujisan>	ahhh
    Mar 04 17:40:33 <Dokujisan>	<Dokujisan> here is the entire chat since I joine #notnexuiz yesterday
    Mar 04 17:40:33 <Dokujisan>	<Dokujisan> http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:40:47 <Dokujisan>	a lot of reading...so I suggest just skimming
    Mar 04 17:40:58 <SoulKeeper_p>	tnx Dokujisan 
    Mar 04 17:41:19 <SoulKeeper_p>	tZork, just poked me, thought join chan
    Mar 04 17:41:26 <DibTop>	Dokujisan: make it the topic
    Mar 04 17:41:30 *	Dokujisan has changed the topic to: here is most of the conversation so far -- http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 04 17:56:51 <Dokujisan>	the interesting part for me starts at Mar 04 06:19:44 
    Mar 04 18:04:58 <tZork>	will have to continiue reading tomorrow, work in 5h, and i better try n get some sleep first.
    Mar 04 18:05:50 <Dokujisan>	k, cya
    Mar 04 18:15:55 *	tZork is now known as tZork|gone
    Mar 04 18:43:19 <CuBe0wL>	what about esteel?
    Mar 04 18:43:31 <CuBe0wL>	he was a major contributor too
    Mar 04 18:43:46 <CuBe0wL>	I think we'd need to invite him here too
    Mar 04 18:44:01 <morphed>	yeah
    Mar 04 18:46:49 <[-z-]>	nexion, nexotic, xenux, zenux are mine out of your last list Dokujisan
    Mar 04 18:47:09 <Dokujisan>	k
    Mar 04 18:48:00 <[-z-]>	Dokujisan: are you in darkplaces?
    Mar 04 18:48:07 <[-z-]>	#darkplaces
    Mar 04 18:48:08 <Dokujisan>	the channel? no
    Mar 04 18:48:11 <[-z-]>	ah
    Mar 04 18:48:12 <[-z-]>	hold
    Mar 04 18:48:21 <Dokujisan>	should I be?
    Mar 04 18:48:59 <[-z-]>	probably
    Mar 04 18:48:59 <Taoki>	Any news about the name? Do we have a top 4-5-6 yet?
    Mar 04 18:49:00 <[-z-]>	on anynet
    Mar 04 18:49:13 <[-z-]>	http://pastie.org/854774
    Mar 04 18:49:28 <Dokujisan>	omg diablo
    Mar 04 18:49:32 <Dokujisan>	I'm not a fan of his
    Mar 04 18:50:02 <[-z-]>	there is more log too if you'd like
    Mar 04 18:50:05 <[-z-]>	some interesting stuff is said
    Mar 04 18:51:34 <Dokujisan>	eh, if it involves diablo, I probably don't want to read it
    Mar 04 18:51:35 <Dokujisan>	heh
    Mar 04 18:51:41 <[-z-]>	http://pastie.org/854777 nope
    Mar 04 18:54:16 <Dokujisan>	[12:59:23 pm] <LordHavoc> div0: I share the theory that it will boost popularity of existing Nexuiz
    Mar 04 18:54:17 <Dokujisan>	yikes!
    Mar 04 18:55:24 <Taoki>	It's not impossible.
    Mar 04 18:56:23 <Dokujisan>	They own that name now. The game we know and play as Nexuiz is an asterisk
    Mar 04 18:56:45 <[-z-]>	omg that's a great name :-P
    Mar 04 18:56:46 <[-z-]>	Nexuiz*
    Mar 04 18:56:52 <Dokujisan>	:-)
    Mar 04 18:57:50 <Taoki>	Apart from the popularity loss, I kinda have the feeling it was after all just a name. It doesn't change anything that we see while we play, so Nexuiz is still Nexuiz to me.
    Mar 04 18:58:06 <Dokujisan>	the name is a lot
    Mar 04 18:58:13 <[-z-]>	yes but that mangled name was ours
    Mar 04 18:58:14 <Dokujisan>	that should not be underestimated
    Mar 04 18:58:25 <[-z-]>	and we all worked together to build what it represents
    Mar 04 18:58:30 <Dokujisan>	We invested our time to build up that name
    Mar 04 18:58:31 <[-z-]>	and this new image does not represent us
    Mar 04 18:58:39 <Taoki>	Well, it does also mean a lot in the sense that... we are used to it so it's like loosing something we cared for
    Mar 04 18:58:49 <[-z-]>	but our rolling stone of a father has tried to tell us this is what we need
    Mar 04 18:59:21 <Dokujisan>	vermeulen certainly did nothing to build up that name. In selling the name (directly or indirectly), he sold our effort and investment in the name
    Mar 04 18:59:29 <morphed>	if we change name, we have milions of players that downloaded nexuiz and didnt liked it back then
    Mar 04 18:59:35 <Dokujisan>	and we now lose that which we helped build up
    Mar 04 19:00:05 <Taoki>	I can't ignore the fact that if it wasn't for Vermeulen, Nexuiz wouldn't have existed, however.
    Mar 04 19:00:10 <morphed>	they might download new game because they dont know its old nexuiz 
    Mar 04 19:00:13 <Dokujisan>	yes, starting over....especially with the backstory of a failed GPL project, can attract a flood of new players ....if we do it properly
    Mar 04 19:00:36 <Dokujisan>	this fork would attract a lot of attention
    Mar 04 19:00:39 <Dokujisan>	or could
    Mar 04 19:00:40 <morphed>	and by millions i mean actual numbers from sourceforge downloads :)
    Mar 04 19:00:40 <[-z-]>	Taoki: but perhaps another game would have
    Mar 04 19:00:47 <Dokujisan>	brb....food
    Mar 04 19:01:49 <Taoki>	I'm confused as to why this is called a fork. Wouldn't it be a fork if we split it into two projects?
    Mar 04 19:02:01 <Taoki>	Im rather seeing it as a renaming
    Mar 04 19:02:14 <[-z-]>	the future of the alientrap AT is unknown
    Mar 04 19:02:20 <[-z-]>	at nexuiz*
    Mar 04 19:03:02 <Taoki>	Oh... there might still be one? I thought it's just this Nexuiz getting renamed. That would be bad... there would be two GPL Nexuizes
    Mar 04 19:03:18 <[-z-]>	well, it would likely die if we fork
    Mar 04 19:03:28 <[-z-]>	unless vermeulen finds a new team
    Mar 04 19:04:12 <Taoki>	yeah. Two GPL Nexuizes would be a horrible idea imo.
    Mar 04 19:04:26 <[-z-]>	well this would be a different game
    Mar 04 19:04:45 <[-z-]>	sounds like a lot of people want to take the opportunity to streamline some things
    Mar 04 19:04:57 <Taoki>	Of course, if Vermeulen may wish to do a fock himself to still maintain a GPL Nexuiz of his own, with a team of his own, that would be his choice. Though it would hurt everything badly.
    Mar 04 19:05:03 <Taoki>	*fork
    Mar 04 19:05:14 <[-z-]>	I doubt he'd have the interest
    Mar 04 19:05:18 <Taoki>	I hope it son't be the case
    Mar 04 19:05:20 <Taoki>	yeah
    Mar 04 19:05:25 <[-z-]>	except only to try and defend his honor
    Mar 04 19:05:31 <[-z-]>	but doing so might even make it worse
    Mar 04 19:05:53 <[-z-]>	There are enough people that feel like the captain abandoned them
    Mar 04 19:06:04 <Taoki>	Yeah, most of us do.
    Mar 04 19:06:18 <[-z-]>	div0: is it true that Vermeulen paid you?
    Mar 04 19:07:27 <[-z-]>	http://alientrap.org/forum/viewtopic.php?f=1&t=6047&start=0#p76262
    Mar 04 19:08:43 <[-z-]>	depending on how vermeulen can spin this PR disaster we might not even have to split
    Mar 04 19:10:09 <Taoki>	I hope he doesnt own the alientrap.com website, or the forum
    Mar 04 19:13:51 <DibTop>	the name should be DiaboliK really  :P
    Mar 04 19:14:28 <DibTop>	did someone suggest Phoenix?
    Mar 04 19:14:48 <Taoki>	Something similar
    Mar 04 19:14:53 <Taoki>	yeah, that too
    Mar 04 19:15:51 <Taoki>	I'm curious about the name. Is there any plan as to when it is decided, or a top with the best names for now?
    Mar 04 19:18:40 <Samual>	DiaboliK as a name wouldn't suck actually :P
    Mar 04 19:18:45 <Samual>	lawl
    Mar 04 19:18:51 <Samual>	It's better than some of the other stuff
    Mar 04 19:23:10 <Dokujisan>	whatever happens with the name, and I was saying this yesterday, we should take some time to pick the proper name
    Mar 04 19:23:12 <Dokujisan>	we have some time
    Mar 04 19:27:02 <Dokujisan>	nexion, nexotic
    Mar 04 19:27:11 <Dokujisan>	nexion is sorta taken already in gaming
    Mar 04 19:27:22 <Dokujisan>	and nexon
    Mar 04 19:27:34 <Dokujisan>	but nexotic doesn't have anything game-related that I can find
    Mar 04 19:28:06 <Dokujisan>	an I found a clan naned team nexotic
    Mar 04 19:28:28 <Dokujisan>	a dance crew named nexotic :-)
    Mar 04 19:29:03 <Taoki>	Not sure on Nexotic here. Would be a good name though
    Mar 04 19:30:18 <Dokujisan>	I like the idea of making a game where we can create a new symbol for it
    Mar 04 19:30:56 <Samual>	I like Nexotic
    Mar 04 19:31:09 <Dokujisan>	what about Nexodic?
    Mar 04 19:31:15 <Dokujisan>	I like the 't' better
    Mar 04 19:31:22 <Dokujisan>	what about Nexilus?
    Mar 04 19:31:23 <Samual>	t is better imo
    Mar 04 19:31:31 <Samual>	Nexilus is too similar :X
    Mar 04 19:31:44 <Samual>	nexotic.org is available
    Mar 04 19:31:46 <Samual>	btw
    Mar 04 19:31:52 <Dokujisan>	yeah... we discussed our planning for this
    Mar 04 19:31:59 <Dokujisan>	Plan A is to aim for an avialable .com
    Mar 04 19:32:06 <Samual>	Yeah
    Mar 04 19:32:07 <Dokujisan>	plan B is to consider .coms that are taken
    Mar 04 19:32:54 <Dokujisan>	I like the look of a lot of the names beginning with "x"
    Mar 04 19:33:02 <Dokujisan>	but the pronunciation is trickier
    Mar 04 19:33:10 <Dokujisan>	like xodius or something
    Mar 04 19:33:15 <Dokujisan>	xenotic
    Mar 04 19:33:40 <Dokujisan>	and it's like a backwards of 'nex'
    Mar 04 19:33:45 <Dokujisan>	'xen'
    Mar 04 19:34:47 <Taoki>	I already picked the ones i support. http://pastebin.com/nWkJF7TD
    Mar 04 19:35:17 <Dokujisan>	ya I have those
    Mar 04 19:35:31 <DibTop>	ziuxen
    Mar 04 19:35:46 <Dokujisan>	you really liked nexvium?
    Mar 04 19:35:47 <Dokujisan>	heh
    Mar 04 19:36:00 <Taoki>	Not a lot, but it sounds acceptable
    Mar 04 19:36:10 <Taoki>	its one of my least favorites from there
    Mar 04 19:36:46 <Dokujisan>	nexolus is too...weak sounding?
    Mar 04 19:37:02 <Dokujisan>	I think that's what div0 said
    Mar 04 19:37:07 <Dokujisan>	using the 'L' sound
    Mar 04 19:37:58 *	mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 04 19:38:05 <Dokujisan>	mand1nga!
    Mar 04 19:38:15 <mand1nga>	Mr Dokujisan !
    Mar 04 19:38:21 <mand1nga>	nice to see you man
    Mar 04 19:38:23 <Dokujisan>	read the link in the topic if you want. It's lengthy
    Mar 04 19:38:26 <Samual>	Ello, mand1nga 
    Mar 04 19:38:32 <mand1nga>	hey Samual 
    Mar 04 19:38:35 <mand1nga>	alright
    Mar 04 19:38:52 <mand1nga>	I've exchanged a few words with Lee today
    Mar 04 19:39:13 <Dokujisan>	heh
    Mar 04 19:40:04 <mand1nga>	nothing relevant, just .. knowing the enemy ;)
    Mar 04 19:40:18 <DibTop>	Phoenix make it Phoinex
    Mar 04 19:40:32 <DibTop>	thats a bit weird though
    Mar 04 19:40:49 <mand1nga>	http://pastebin.com/pjqt20YN
    Mar 04 19:40:51 <Dokujisan>	I'm not keen on phoenix. that name is overplayed by now
    Mar 04 19:41:22 <Dokujisan>	I like it having a name that really has no meaning, a made up word
    Mar 04 19:41:38 <mand1nga>	I have the name
    Mar 04 19:41:45 *	mand1nga <-
    Mar 04 19:41:46 <mand1nga>	:>
    Mar 04 19:43:24 <Dokujisan>	ugh.. I read comments made by vermeulen and the illfonic guy and Lordhavoc and it seems like you can't get through to them
    Mar 04 19:43:30 <Dokujisan>	and it's also too late, imo
    Mar 04 19:43:35 <Dokujisan>	what's done is done
    Mar 04 19:44:11 <Dokujisan>	I mean he can't undo it
    Mar 04 19:44:15 <Dokujisan>	there are contracts
    Mar 04 19:44:34 <mand1nga>	well, that'd be a big problem for them
    Mar 04 19:44:48 <Taoki>	I'm at peace with the idea we'll be continuing under a new name.
    Mar 04 19:44:56 <mand1nga>	imho they can't handle the amount of bad press that is coming
    Mar 04 19:45:05 <Dokujisan>	I'm more than at peace. I'm actually excited for it.
    Mar 04 19:45:06 <Taoki>	The only thing I worry about now is a fork of Nexuiz GPL. That would destroy everything.
    Mar 04 19:45:24 <Dokujisan>	This would be a fork of Nexiuz GPL
    Mar 04 19:45:27 <mand1nga>	I think the commercial version will be dead even before reaching the shelves, like I said before
    Mar 04 19:45:41 <Taoki>	A fork as in, 2 projects continuing fro it
    Mar 04 19:45:49 <[-z-]>	I don't think there is anything to worry about as long as we organize ourselves and our resources properly
    Mar 04 19:46:00 <[-z-]>	improve where the project needs improving and better distribute power
    Mar 04 19:46:32 <mand1nga>	I see those are separated issues 1) the future of GPL nexuiz and 2) do something against LV disrepectful/unlawful actions
    Mar 04 19:46:35 <Dokujisan>	I like everything that's been said so far in this channel since I joined
    Mar 04 19:46:54 <Dokujisan>	LV?
    Mar 04 19:46:58 <[-z-]>	lee vermeulen
    Mar 04 19:47:00 <Dokujisan>	oh
    Mar 04 19:47:16 <mand1nga>	it seems he is the only one to blame
    Mar 04 19:47:27 <Dokujisan>	lordhavoc played a role
    Mar 04 19:47:37 <Dokujisan>	and regardless of what lee says, I still blame illfonic somewhat
    Mar 04 19:47:39 <[-z-]>	different said he never really gave explicity permission to LH
    Mar 04 19:47:39 <mand1nga>	yes, a minor one imho, but still
    Mar 04 19:47:47 <[-z-]>	he said it was more a "I might sell this one day" sort of thing
    Mar 04 19:47:55 <[-z-]>	he definitely didn't know about the name thing
    Mar 04 19:48:39 <mand1nga>	I just can't stand the fact that div0 was kept out of this, I never seen such a lack of respect/manners before
    Mar 04 19:48:41 <Samual>	I didn't know about the name being the same
    Mar 04 19:48:46 <Samual>	However, I knew about the project
    Mar 04 19:49:06 <[-z-]>	how long ago?
    Mar 04 19:49:07 <Samual>	I've known about it for quite a while too :X
    Mar 04 19:49:13 <Samual>	Since I got commit access to Nexuiz
    Mar 04 19:49:13 *	morphed has quit (Read error: Connection timed out)
    Mar 04 19:49:26 <[-z-]>	who told you? LH?
    Mar 04 19:49:27 <Taoki>	To me, Illfonic and Vermeulen are equally guilty
    Mar 04 19:49:35 <Samual>	LordHavoc confronted me about it, -z-
    Mar 04 19:49:41 <[-z-]>	I figured
    Mar 04 19:49:47 <mand1nga>	acces to nexuiz or dp?
    Mar 04 19:49:51 <[-z-]>	and no one told div??
    Mar 04 19:49:52 <Samual>	Nexuiz
    Mar 04 19:49:52 <Dokujisan>	well div0 was told about a console port, but he didn't know that it was not going to be benefitting the current Nexuiz and that it would be a completely different game...and of course the use of the name
    Mar 04 19:49:55 <Samual>	I had DP earlier
    Mar 04 19:50:02 <Samual>	-z-: I thought he knew
    Mar 04 19:50:04 <mand1nga>	wow thats crazy
    Mar 04 19:50:19 <Samual>	If not, he figured it out for the most part
    Mar 04 19:50:29 <Samual>	If you look at the commit log, pay attention to most of the GL changes
    Mar 04 19:50:38 <[-z-]>	anyone ever remember a fund raiser for divVerent sponsored by Lee???
    Mar 04 19:50:38 <mand1nga>	got to go, ttyl
    Mar 04 19:50:50 <mand1nga>	you have all my support guys
    Mar 04 19:50:52 <Samual>	-z-: No, but i've only been here since 2.4.2
    Mar 04 19:50:59 <mand1nga>	(coming from the l!ft team)
    Mar 04 19:51:02 <[-z-]>	that's another thing he claimed in his reply to my ill comment about where the donations were going
    Mar 04 19:51:02 <mand1nga>	later.
    Mar 04 19:51:08 <[-z-]>	bye mand1nga
    Mar 04 19:51:28 <Dokujisan>	thanks mand1nga!
    Mar 04 19:52:53 <Samual>	Anyway I wasn't aware that they were using our game code either
    Mar 04 19:53:03 <Samual>	I just thought they were using the engine and that's it
    Mar 04 19:53:11 <Dokujisan>	that might be true still
    Mar 04 19:53:14 <Samual>	No
    Mar 04 19:53:18 <Dokujisan>	oh?
    Mar 04 19:53:30 <Taoki>	They use parts of the gamecode too. I spotted at least the ghost items, and other users confirmed
    Mar 04 19:53:58 <Samual>	That doesn't necessarily need our gamecode, they could've just taken the feature idea
    Mar 04 19:54:01 <Samual>	Which, i'm fine with
    Mar 04 19:54:09 <Samual>	I'm also upset that they're only doing 2 game modes
    Mar 04 19:54:14 <Samual>	AND THEY'RE REMOVING DEATHMATCH....
    Mar 04 19:54:16 <[-z-]>	I don't trust anyone that makes an all flash website
    Mar 04 19:54:45 <Samual>	Listen, you don't remove deathmatch from a game which was originally designed to BE a deathmatch game
    Mar 04 19:54:58 <[-z-]>	rm deathmatch
    Mar 04 19:55:06 <Samual>	Bitch you forgot permissions
    Mar 04 19:55:06 <[-z-]>	rm -f deathmatch
    Mar 04 19:55:14 <Samual>	-.-
    Mar 04 19:55:24 <[-z-]>	chown z deathmatch && rm -vf deathmatch
    Mar 04 19:55:36 <Taoki>	I agree. Removing deathmatch is something more stupid than concievable. Its the main gametype
    Mar 04 19:55:36 <Samual>	Fine.
    Mar 04 19:55:47 <[-z-]>	I'd play a CTF only game
    Mar 04 19:55:53 <[-z-]>	but I'd want it to be crazy style ZTF :-P
    Mar 04 19:56:02 <[-z-]>	that is multiple flags with multiple values
    Mar 04 19:56:05 <Samual>	That and they won't add Keyhunt or any other game modes which could be very successful
    Mar 04 19:56:20 <[-z-]>	ZTF Fortress is the future! :-P
    Mar 04 19:56:23 <Samual>	I personally would want LMS in there :P
    Mar 04 19:56:38 <Samual>	I bet you LMS could be fun when the server is constantly full :P
    Mar 04 19:56:54 <[-z-]>	the world may never know
    Mar 04 19:57:07 <Samual>	Actually it could be calculated
    Mar 04 19:57:19 <Dokujisan>	ok I need to sleep....but I'm excited for this thing now.
    Mar 04 19:57:30 <Dokujisan>	so please keep the momentum going
    Mar 04 19:57:34 <Samual>	lawl
    Mar 04 19:57:45 <[-z-]>	take care Dokujisan
    Mar 04 19:57:50 <Dokujisan>	cya
    Mar 04 19:57:53 <Samual>	Cya
    Mar 04 19:58:15 <Samual>	But honestly I would be fine with this whole thing if their company did 2 things: 
    Mar 04 19:58:20 <Samual>	Actually.. 3.
    Mar 04 19:58:44 <Samual>	#1: Change the name to something else... We're the ones with the community who built up the name, we're the ones who want to keep it.
    Mar 04 19:59:33 <Samual>	#2: Credit all contributors of code and content that they used in the game. (That does mean in the game credits itself)
    Mar 04 20:00:15 <Samual>	#3: Take heed of the more important things to the community and listen to their opinions about what they want to do with the game.
    Mar 04 20:00:37 <[-z-]>	They already have the "we're better than you, we're saving you, the future is awesome, you don't even know" attitude...
    Mar 04 20:00:39 <Samual>	........... Like me with being upset about only having TDM and CTF :P
    Mar 04 20:00:41 <[-z-]>	so goodluck :-P
    Mar 04 20:01:07 <Samual>	Actually
    Mar 04 20:01:13 <Samual>	All of that................... OR.......................
    Mar 04 20:01:15 <[-z-]>	we are so honored to have old school quake players who might have played nexuiz once or twice buy out game
    Mar 04 20:01:18 <Samual>	They give us all their artwork.
    Mar 04 20:01:19 <[-z-]>	our*
    Mar 04 20:01:20 <Samual>	^_^
    Mar 04 20:01:21 <Samual>	^_^
    Mar 04 20:01:30 <Samual>	I want their fucking artwork damnit
    Mar 04 20:01:31 <Samual>	>.>
    Mar 04 20:01:32 <[-z-]>	yeah, I can't believe they've been such jerks about content too
    Mar 04 20:01:34 <[-z-]>	well
    Mar 04 20:01:38 <[-z-]>	as I said to div in pm
    Mar 04 20:01:46 <[-z-]>	even if they just made us a few new models for our game
    Mar 04 20:01:51 <[-z-]>	it would appease the crowd
    Mar 04 20:02:02 <Samual>	Indeed
    Mar 04 20:02:04 <Samual>	Well
    Mar 04 20:02:08 <Samual>	I want that style :P
    Mar 04 20:02:16 <[-z-]>	severance pk3
    Mar 04 20:02:19 <[-z-]>	harrr
    Mar 04 20:02:25 <Samual>	Listen, the style they went for with the artwork is what i've always wanted from Nexuiz 
    Mar 04 20:02:33 <Samual>	When I dream of Nexuiz, that's what I see
    Mar 04 20:02:34 <Samual>	:P
    Mar 04 20:02:35 <Samual>	:P
    Mar 04 20:02:39 <[-z-]>	samual is in loooooove, samual is in loooooove
    Mar 04 20:02:44 <Samual>	Bullshit
    Mar 04 20:02:46 <Samual>	But well
    Mar 04 20:02:47 <[-z-]>	lol
    Mar 04 20:02:51 <CuBe0wL>	gn
    Mar 04 20:02:55 <Samual>	Seriously, that artwork is awesome.
    Mar 04 20:02:56 <[-z-]>	nice CuBe0wL
    Mar 04 20:03:01 <Samual>	gn CuBe0wL 
    Mar 04 20:03:06 <Samual>	nite*? 
    Mar 04 20:03:33 <[-z-]>	nite*
    Mar 04 20:03:35 <[-z-]>	:)
    Mar 04 20:03:37 <Samual>	^_^
    Mar 04 20:04:43 <Samual>	Anyway, those things happening are what would stop me from leaving Alientrap 
    Mar 04 20:05:09 <[-z-]>	yeah
    Mar 04 20:05:26 <[-z-]>	well Vermeulen said that he cares more about getting the name of alientrap out there than to get the name changed
    Mar 04 20:05:34 <[-z-]>	but he already signed the contract
    Mar 04 20:05:43 <[-z-]>	so... I think it's too late for conditions
    Mar 04 20:05:57 <Samual>	Well
    Mar 04 20:06:03 <Samual>	Can't IllFonic still change the name?
    Mar 04 20:06:08 <[-z-]>	lol
    Mar 04 20:06:14 <[-z-]>	they've already stated they will not
    Mar 04 20:06:17 <[-z-]>	and to basically stfu about it
    Mar 04 20:06:23 <Samual>	So?
    Mar 04 20:06:32 <Dokujisan>	let it go :-P
    Mar 04 20:06:44 <[-z-]>	so do you hit mario blocks when they question mark is already gone?
    Mar 04 20:06:47 <Samual>	Fine... Meh i'm goin out for a bit
    Mar 04 20:06:51 <Samual>	HEY WAIT A SECOND
    Mar 04 20:06:54 <Samual>	DIDN'T YOU GO TO BED?
    Mar 04 20:06:58 <Samual>	^_^
    Mar 04 20:07:07 <Dokujisan>	I was awoken by your heart breaking
    Mar 04 20:07:08 <[-z-]>	he's sleep ircing
    Mar 04 20:07:13 <Dokujisan>	the sound of your heart breaking
    Mar 04 20:07:22 <Samual>	Lies
    Mar 04 20:07:28 <Dokujisan>	and I thought I heard whimpering
    Mar 04 20:07:34 <Dokujisan>	and I didn't realize IRC had sound support
    Mar 04 20:07:49 <[-z-]>	rythmic ascii
    Mar 04 20:08:02 <[-z-]>	beep boop bop beep boop
    Mar 04 20:08:03 <Samual>	Anyway, bbiab
    Mar 04 20:08:04 <Dokujisan>	ok really now....sleep
    Mar 04 20:08:12 <Samual>	gn Doku :P
    Mar 04 20:08:17 <[-z-]>	who wants to play Nexuiz*?
    Mar 04 20:08:31 <Samual>	Hmm
    Mar 04 20:08:40 <Samual>	That may just be enough to keep me here
    Mar 04 20:08:43 <Samual>	:P
    Mar 04 20:08:47 <[-z-]>	I'll be jumping around with a bunch of ho's chasing a flag
    Mar 04 20:08:48 <Samual>	Where?
    Mar 04 20:09:07 <Samual>	Hmm well, maybe i'll join in some time
    Mar 04 20:09:17 <Samual>	^_^
    Mar 04 20:26:41 *	[-z-] gives channel operator status to CuBe0wL DibTop FruitieX
    Mar 04 20:26:42 *	[-z-] gives channel operator status to mand1nga SoulKeeper_p tZork|gone
    Mar 04 20:26:44 *	[-z-] gives channel operator status to }-z-{
    Mar 04 20:47:28 <[-z-]>	nexyes.com AVAILABLE
    Mar 04 20:53:25 *	TVR (~TVR@96.49.107.196) has joined #notnexuiz
    Mar 04 20:55:40 <TVR>	Good to see that this cause is gaining more and more support
    Mar 04 20:56:11 <Taoki>	Hi TVR. Yeah, indeed
    Mar 04 21:10:02 <Taoki>	bed time here. See you all tomorrow
    Mar 04 21:12:36 <TVR>	Later.
    Mar 04 21:13:56 <[-z-]>	goodnight
    Mar 04 21:26:36 *	Taoki has quit (Ping timeout: 364 seconds)
    Mar 04 22:34:22 <[-z-]>	I just need to vent that I have contributed 5 websites to alientrap and managed many web related things under the name and was not informed a single bit about this information.  Not even that the website was getting hiacked, I mean sold.
    Mar 04 22:36:14 <[-z-]>	I really feel like lee could have worked out a better deal on this part
    Mar 04 23:54:39 <TVR>	[-z-]: Economic recession, maybe he needs to money to pay his credit card debt, heh  
    Mar 05 00:09:53 <FruitieX>	23:38:00 <@Dokujisan> basically, I hope to become an official community organizer in that regard
    Mar 05 00:09:57 <FruitieX>	23:38:39 <@Dokujisan> "official" being key here. When things are left to be done by only the community, there is a disadvantage. If things are done from the top down, a lot more momentum can be achieved.
    Mar 05 00:10:01 <FruitieX>	sounds good :)
    Mar 05 00:10:47 <FruitieX>	23:41:01 <@Dokujisan> well really the community is likely to come along with us
    Mar 05 00:10:57 <FruitieX>	their other choice is to stick with 2.5.2 (or svn) :P
    Mar 05 00:12:32 <FruitieX>	23:48:47 < tZork> basicaly just briging along some ideas, both art and code are to be re-built to adress the large issue of legacy bagage nexuiz suffers from.
    Mar 05 00:12:35 <FruitieX>	:)
    Mar 05 00:15:03 <FruitieX>	Also, we need CSQC players. (even though that seems to be impossible/ridiculously hard etc)
    Mar 05 00:15:14 <FruitieX>	00:01:55 <@Dokujisan> yes we did discuss new player models
    Mar 05 00:15:14 <FruitieX>	00:02:16 <@Dokujisan> and a new set of default maps
    Mar 05 00:15:17 <FruitieX>	both: absolutely
    Mar 05 00:15:34 <DibTop>	FruitieX>	Also, we need CSQC players. (even though that seems to be impossible/ridiculously hard etc)
    Mar 05 00:15:44 <DibTop>	lordhavoc said hes gonna work on that when he gets the chance
    Mar 05 00:15:57 <FruitieX>	00:09:30 <@Taoki> http://alientrap.org/forum/viewtopic.php?f=19&t=6054 =P
    Mar 05 00:16:00 <FruitieX>	hahahha
    Mar 05 00:20:02 <FruitieX>	00:22:41 <@Taoki> As for informing the masses, I spoke about that with div0 yesterday (we all did on the channel iirc). We can make a new csprogs and put it on servers, that will inform about this
    Mar 05 00:20:06 <FruitieX>	Good.
    Mar 05 00:20:25 <FruitieX>	As for servers... I have a few
    Mar 05 00:20:37 <FruitieX>	But I'd prefer them to stay Nexrun, which means we need a proper mod system... :P
    Mar 05 00:20:46 <FruitieX>	Or maybe replace the Havoc button ;) ;) ;)
    Mar 05 00:20:58 <FruitieX>	"ChallengeMode"? :P
    Mar 05 00:21:27 <TVR>	We should donate Havoc mode to Illfonic
    Mar 05 00:21:29 <FruitieX>	00:23:31 < tZork> <CuBe0wL> Pheonix
    Mar 05 00:21:37 <FruitieX>	+1, good luck getting a domain for that though
    Mar 05 00:23:38 <TVR>	FruitieX: 2.5.3 isn't coming anytime soon, is the water bug fixed in SVN?
    Mar 05 00:24:06 <TVR>	Otherwise, we'll have to revert back to 2.5...
    Mar 05 00:27:08 <FruitieX>	lol, water bug was fixed maybe a week after releasing 2.5.2 TVR 
    Mar 05 00:27:30 <TVR>	... and the hotfix is taking this long?
    Mar 05 00:29:24 <DibTop>	they dont have a stable engine to release yet
    Mar 05 00:30:58 <FruitieX>	01:59:52 < morphed> if we change name, we have milions of players that downloaded nexuiz and didnt liked it back then
    Mar 05 00:31:04 <FruitieX>	Good point, BTW.
    Mar 05 00:31:20 <FruitieX>	If the name is less confusing, many of these might not be scared off to try it out again :P
    Mar 05 00:32:08 <FruitieX>	IMO we should be removing (or at least make sure about revamping) old maps which use the e* (not eX) textures
    Mar 05 00:32:55 <FruitieX>	Possibly making many new textures from photos (e.g. burningwell is a public domain site for that, or just snap yer own), this is basically what I did for stormkeep2 floor and walls
    Mar 05 00:33:17 <FruitieX>	(still reading backlog btw, cant see what you're posting ;))
    Mar 05 00:34:44 <FruitieX>	02:05:21 <@Taoki> Of course, if Vermeulen may wish to do a fock himself to still maintain a GPL Nexuiz of his own, with a team of his own, that would be his choice. Though it would hurt everything badly.
    Mar 05 00:34:48 <FruitieX>	02:05:26 <@Taoki> *fork
    Mar 05 00:34:51 <FruitieX>	This could sure be bad yes, but I doubt he'd do that
    Mar 05 00:35:02 <FruitieX>	Also, if it's GPL'd, we can take over his changes (and vice versa) :P
    Mar 05 00:36:16 <FruitieX>	No matter what happens... Unless illfonic decides to change name/stop working on console Nexuiz we should change the name IMO
    Mar 05 00:41:08 <FruitieX>	oooh only 3 pages left :P
    Mar 05 00:41:23 <FruitieX>	07:28:05 < TVR> ... and the hotfix is taking this long?
    Mar 05 00:41:28 <FruitieX>	Yeah, it never happened
    Mar 05 00:41:36 <FruitieX>	There was change after change after change
    Mar 05 00:41:50 <FruitieX>	waiting for one change to mature, then there's another change
    Mar 05 00:41:55 <FruitieX>	I guess that's pretty much what happened
    Mar 05 00:42:18 <FruitieX>	and look what we ended up with, warpzones, somewhat fixed black edges on water etc etc
    Mar 05 00:42:26 <FruitieX>	new decal system
    Mar 05 00:42:30 <TVR>	Unfortunately, it killed the player base.
    Mar 05 00:42:46 <TVR>	Used to be 150 players at peak, now it's around 90
    Mar 05 00:42:49 <FruitieX>	yep might as well be
    Mar 05 00:43:19 <TVR>	What are warpzones again? I don't have flash
    Mar 05 00:43:37 <FruitieX>	Wow, you didn't hear about them?
    Mar 05 00:43:48 <FruitieX>	They are like teleporters, except seamless ones
    Mar 05 00:43:53 <TVR>	Are they portal cams, or actual portals from portal?
    Mar 05 00:43:57 <FruitieX>	Just like portals in Valve's portal
    Mar 05 00:44:01 <FruitieX>	actual portals
    Mar 05 00:44:13 <TVR>	How does reorientation work?
    Mar 05 00:44:19 <FruitieX>	Except they can be as big as the mapper wants, as invisible as the mappers want
    Mar 05 00:44:36 <FruitieX>	TVR: There's an entity in the warpzones that set the orientation
    Mar 05 00:44:48 <FruitieX>	the warpzone killtargets this one iirc
    Mar 05 00:45:28 <TVR>	Oh this reminds me of Darkplaces' inability to support vertical model movement
    Mar 05 00:45:38 <FruitieX>	http://www.youtube.com/watch?v=5-8atWDlfhY
    Mar 05 00:45:52 <FruitieX>	yep, in this video you will see
    Mar 05 00:46:12 <FruitieX>	how the player view is always reoriented so the player will stand up straight after jumping into a warpzone
    Mar 05 00:46:46 <TVR>	Remember, I don't have flash...
    Mar 05 00:47:50 <TVR>	btw, does this http://alientrap.org/forum/viewtopic.php?t=6019&p=76283#p76283 demonstrate Darkplaces to the non-English speaking?
    Mar 05 00:50:24 <FruitieX>	Oh, don't have flash?
    Mar 05 00:50:51 <TVR>	Yep, Gnash doesn't work for Youtube
    Mar 05 00:51:18 <FruitieX>	haha nice demonstration x)
    Mar 05 00:51:21 <FruitieX>	that should be fixed BTW
    Mar 05 00:51:32 <FruitieX>	case we get new playermodels, they really need to be able to move their upper body
    Mar 05 00:51:56 <TVR>	I wonder how Illfonic is dealing with that.
    Mar 05 00:52:26 <TVR>	Is this just a Big Rigs style cash grab?
    Mar 05 00:52:29 <FruitieX>	That's done in QC
    Mar 05 00:53:00 <TVR>	Segmented models?
    Mar 05 00:53:09 <FruitieX>	but really, the way it should be fixed is simply, yep, segmented models
    Mar 05 00:53:17 <FruitieX>	that coupled with what we already have, aiming the gun up/down
    Mar 05 00:53:47 <TVR>	You mean, the viewmodel of the gun?
    Mar 05 00:54:12 <DibTop>	i think before we have a new release we should create new playermodels and weapon models
    Mar 05 00:55:46 <TVR>	Let's skip 2.5.3, and head directly to a 3.0 fork
    Mar 05 00:56:07 <FruitieX>	DibTop: Yeah
    Mar 05 00:56:16 <DibTop>	or 2.6 or whatever
    Mar 05 00:56:24 <DibTop>	or just 1.0 with a different name
    Mar 05 00:56:29 <FruitieX>	Some playermodels are really nice, or let's say were really nice before the texture resolution of them was brought down...
    Mar 05 00:56:48 <DibTop>	im working on animating GAK by oblivion
    Mar 05 00:57:33 <TVR>	If all else fails, we can always fall back to pinkbox.
    Mar 05 01:02:36 <FruitieX>	Lol
    Mar 05 01:02:54 <FruitieX>	What really should be considered is high-res textures for everything
    Mar 05 01:03:03 <FruitieX>	Or well, models :P
    Mar 05 01:03:36 <FruitieX>	Players who don't have lots of VRAM have the option of reducing quality, even only for models (default option)
    Mar 05 01:03:48 <FruitieX>	could set gl_picmip 1 default, which I think it already is
    Mar 05 01:04:49 <DibTop>	they dont even need to do that
    Mar 05 01:04:58 <DibTop>	there is a command to reduce the quality of just playermodels
    Mar 05 01:05:04 <DibTop>	but i forget what it was
    Mar 05 01:07:03 <DibTop>	i want to animate obi's newest model too
    Mar 05 01:07:08 <DibTop>	or someone should
    Mar 05 01:07:12 <DibTop>	its really nice
    Mar 05 01:20:29 <FruitieX>	08:05:35 <@DibTop> there is a command to reduce the quality of just playermodels
    Mar 05 01:20:32 <FruitieX>	thats what i meant
    Mar 05 01:20:39 <FruitieX>	it's not only playermodels afaik, it's all models
    Mar 05 01:20:52 <DibTop>	nope there is one to reduce it just for playermodels
    Mar 05 01:20:57 <DibTop>	i forgot i though
    Mar 05 01:24:43 <FruitieX>	cl_playerdetailreduction? (or whatever)
    Mar 05 01:24:45 <FruitieX>	for lod?
    Mar 05 01:24:49 <FruitieX>	that's not what i meant :P
    Mar 05 01:25:18 <DibTop>	maybe
    Mar 05 01:25:20 <DibTop>	i dont know
    Mar 05 01:34:14 *	FruitieX trying to convince Kedhrin to donate some motion caps 8)
    Mar 05 01:35:13 <DibTop>	not gonna happen
    Mar 05 01:43:10 <FruitieX>	TVR: warpzone! http://pics.nexuizninjaz.com/images/adpd7dnuhndv55pqhar.jpg
    Mar 05 01:43:15 <FruitieX>	BTW
    Mar 05 01:43:21 <FruitieX>	would like to have this map included :)
    Mar 05 01:43:26 <FruitieX>	in the possible fork
    Mar 05 01:44:08 <FruitieX>	http://pics.nexuizninjaz.com/images/44samcbugfwbl2swcmyu.jpg
    Mar 05 01:52:42 <div0>	[01:50:43] <@Samual> If not, he figured it out for the most part
    Mar 05 01:52:43 <div0>	[01:50:53] <@Samual> If you look at the commit log, pay attention to most of the GL changes
    Mar 05 01:52:45 <div0>	[01:51:01] <@[-z-]> anyone ever remember a fund raiser for divVerent sponsored by Lee???
    Mar 05 01:52:55 <div0>	no?
    Mar 05 01:53:04 <div0>	as for commit log: this hinted to a PS3 port of the engine
    Mar 05 01:53:11 <div0>	but NOT that nexuiz will be hijacked
    Mar 05 01:53:33 <div0>	[07:43:45] <@FruitieX> TVR: warpzone! http://pics.nexuizninjaz.com/images/adpd7dnuhndv55pqhar.jpg
    Mar 05 01:53:36 <div0>	does this get good fps?
    Mar 05 01:53:40 <div0>	asking, ebcause the map is open
    Mar 05 01:53:55 <div0>	but yes, good use of warpzone
    Mar 05 01:54:09 <div0>	nice idea to put a door threshold in there
    Mar 05 01:54:14 <div0>	makes the warpzone glitch way less visible :P
    Mar 05 01:54:20 <div0>	like, thelighting difference
    Mar 05 01:54:51 <TVR>	It's difficult to recognize when bloom or HDR is enabled
    Mar 05 01:55:38 <TVR>	Heh, do dynamic lights travel through warpzones as well?
    Mar 05 01:55:39 <FruitieX>	indeed div0 that was the point of adding it i'm sure
    Mar 05 01:56:31 <FruitieX>	TVR: dynamic lights don't travel through one, no
    Mar 05 01:56:35 <FruitieX>	neither do sounds
    Mar 05 01:56:40 <TVR>	How about hitscan?
    Mar 05 01:56:47 <FruitieX>	yep does travel through
    Mar 05 01:56:49 <FruitieX>	and projectiles
    Mar 05 01:57:06 <TVR>	Can it be one-way?
    Mar 05 01:57:27 <FruitieX>	not sure, at least before it couldn't
    Mar 05 01:57:50 <FruitieX>	you could of course do stuff like place a trigger_impulse on one side
    Mar 05 01:57:54 <TVR>	Because it wouldn't make sense to be standing on both sides, if it's only one way
    Mar 05 01:57:55 <FruitieX>	that pushes you away from it
    Mar 05 01:58:10 <div0>	TVR: one-way theoretically possible but I didn't support that from QC
    Mar 05 01:58:13 <div0>	do0n't want one-way :P
    Mar 05 01:58:27 <FruitieX>	also div0 it got pretty good fps yes
    Mar 05 01:58:35 <div0>	if you make your own QC code.. you can make it one-way :P
    Mar 05 01:58:36 <FruitieX>	100 average on my laptop iirc
    Mar 05 01:58:45 <FruitieX>	after i removed the water on the middle, which was a real performance killer
    Mar 05 01:58:51 <div0>	ah
    Mar 05 01:58:56 <div0>	so it already HAD extra renders ;)
    Mar 05 01:58:59 <FruitieX>	yep :P
    Mar 05 01:58:59 <div0>	then it indeed doesn't get worse
    Mar 05 01:59:28 <TVR>	gn
    Mar 05 01:59:41 *	TVR has quit ("ChatZilla 0.9.86 [Firefox 3.0.14/2009091913]")
    Mar 05 02:13:54 <FruitieX>	on my desktop i'm getting about 70 fps with reflections set to sharp
    Mar 05 02:14:06 <FruitieX>	other than that pretty much everything disabled (textures full though)
    Mar 05 02:14:18 <FruitieX>	nvidia 6600GT, 2.0GHz old sempron CPU (singlecore)
    Mar 05 02:14:32 <FruitieX>	it's a bit unstable though, which might be cause of having the browser up at the same time
    Mar 05 02:15:51 <FruitieX>	or maybe, it hasn't got enough VRAM and is swapping
    Mar 05 02:16:11 <FruitieX>	now it segfaulted x)
    Mar 05 02:24:57 <div0>	maybe I have to make warpzones and others be able to have different resolution
    Mar 05 02:25:08 <div0>	either that, or warpzone maps shall use r_water_resolutionmultiplier in mapifno
    Mar 05 02:25:41 <div0>	maybe it is good to allow them to have different resolutoion, for weaker hardware
    Mar 05 02:45:59 <div0>	in the new project
    Mar 05 02:46:05 <div0>	can  we become incompatible to existing maps?
    Mar 05 02:46:12 <div0>	I'd like to remove the evil* texture sets
    Mar 05 02:46:30 <div0>	and repack existing custom maps to instead include the textures if they need them
    Mar 05 02:46:42 <div0>	basically, I'd like to only include high quality textures
    Mar 05 02:47:47 <div0>	basically: I think I will make a "nexiuz.git" repository that is like nexuiz.git but with certain parts removed (especially maps and textures)
    Mar 05 02:47:54 <div0>	will keep the models for now though
    Mar 05 02:48:14 <div0>	as for maps, will probbaly only include aggressor for a start, and tutorial
    Mar 05 02:48:26 <div0>	maybe dieselpower too
    Mar 05 02:48:52 <div0>	and then reinclude ONLY the shaders and textures from the evil sets that are missing
    Mar 05 03:38:37 <FruitieX>	09:46:45 <@div0> can  we become incompatible to existing maps?
    Mar 05 03:38:37 <FruitieX>	09:46:52 <@div0> I'd like to remove the evil* texture sets
    Mar 05 03:38:40 <FruitieX>	i sure vote for this
    Mar 05 03:39:46 <FruitieX>	09:48:54 <@div0> as for maps, will probbaly only include aggressor for a start, and tutorial
    Mar 05 03:39:59 <FruitieX>	What about stormkeep2? That one uses mostly my custom made textures and eX textures
    Mar 05 03:40:41 <FruitieX>	I'm ready to retexture a bunch of other favorites (soylent springs to mind immediately :))
    Mar 05 03:41:05 <div0>	oh right
    Mar 05 03:41:08 <div0>	stormkeep2 I forgot
    Mar 05 03:41:14 <div0>	but will first include NO maps, and then reinclude the ones I want
    Mar 05 03:41:22 <div0>	and yes... stormkeep2, maybe even with warpzone
    Mar 05 03:41:28 <FruitieX>	yes :)
    Mar 05 03:41:32 <div0>	even though I am not fully convinced about it yet
    Mar 05 03:41:36 <FruitieX>	hehe
    Mar 05 03:41:37 <div0>	maybe simply should make the warpzone more visible
    Mar 05 03:41:42 <FruitieX>	yes
    Mar 05 03:41:46 <div0>	like, with a Portal-like texture
    Mar 05 03:41:46 <FruitieX>	i have thought about this too
    Mar 05 03:41:59 <FruitieX>	yeah... or simply some shaderwork
    Mar 05 03:42:00 <div0>	not elliptic though, valve may own that :P
    Mar 05 03:42:08 <div0>	sure, thinking of both :P
    Mar 05 03:42:17 <div0>	on the borders, some blue and orange glow
    Mar 05 03:42:22 <div0>	otherwise, wavy transparent
    Mar 05 03:42:23 <FruitieX>	would adding a normalmap to it make it slower?
    Mar 05 03:42:27 <div0>	no
    Mar 05 03:42:28 <FruitieX>	like, need an extra render pass
    Mar 05 03:42:29 <div0>	same code anyway
    Mar 05 03:42:32 <FruitieX>	neat
    Mar 05 03:42:33 <div0>	it already needs the pass
    Mar 05 03:42:37 <FruitieX>	alright
    Mar 05 03:42:42 <div0>	but, it'd prevenmt future optimization :P
    Mar 05 03:42:47 <FruitieX>	oh :P
    Mar 05 03:42:48 <FruitieX>	hmm
    Mar 05 03:42:52 <div0>	if that ever happens anyway
    Mar 05 03:43:05 <div0>	I am not sure if iteven CAN be optimized in DP's renderer design
    Mar 05 03:43:07 <div0>	however...
    Mar 05 03:43:17 <div0>	I think, if it gets optimized, it'll be by a new dp_warpzone shader parametert
    Mar 05 03:43:24 <div0>	which would make a un-modifying warp
    Mar 05 03:43:33 <div0>	and not using dp_refract and dp_camera
    Mar 05 03:43:49 <div0>	this would optimize the common/warpzone shader
    Mar 05 03:43:58 <div0>	but not custom made shaders that you would use if ysou want to style it
    Mar 05 03:44:16 <div0>	so, basically: go ahead, and style it
    Mar 05 03:44:50 <FruitieX>	:P
    Mar 05 03:45:23 <div0>	the warpzones on gasoline don't need styling
    Mar 05 03:45:29 <div0>	they do look clearly like warps anyway :P
    Mar 05 03:45:31 <div0>	which is good
    Mar 05 03:45:53 <div0>	they wouldn't be irritating :P
    Mar 05 03:46:04 <div0>	however - if you style the ones on stormkeep, these could be too
    Mar 05 03:46:30 <FruitieX>	true
    Mar 05 03:49:05 <FruitieX>	could make some "standard" for how warpzones look
    Mar 05 03:49:21 <FruitieX>	would of course need to speak with morphed, tZork etc artists
    Mar 05 03:50:56 <FruitieX>	lol someone has modified wikipedia already: http://en.wikipedia.org/wiki/Nexuiz#Commercialization_and_Death
    Mar 05 03:50:59 <FruitieX>	"and death"
    Mar 05 03:51:00 <FruitieX>	bah :P
    Mar 05 03:51:25 <FruitieX>	mikee? :P
    Mar 05 03:51:43 *	morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:51:54 *	morphed has quit ()
    Mar 05 03:52:05 *	morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:52:05 *	morphed has quit (Client Quit)
    Mar 05 03:52:21 *	morphed (~morphed@095160110118.warszawa.vectranet.pl) has joined #notnexuiz
    Mar 05 03:52:33 *	morphed has quit (Client Quit)
    Mar 05 04:14:52 <FruitieX>	div0: after doing a make, what were the remaining steps to do for a functioning netradiant installation?
    Mar 05 04:15:29 <FruitieX>	i'm currently getting a message "editor binary doesnt match what the latest setup has configured in this directory. Make sure you run the right/latest editor binary you installed"
    Mar 05 04:16:12 <FruitieX>	i'm sure that i ran the download-gamepacks.sh script though
    Mar 05 04:19:08 <div0>	no idea
    Mar 05 04:19:14 <div0>	that message should never come
    Mar 05 04:19:16 <FruitieX>	hmm
    Mar 05 04:19:22 <div0>	can you check for files RADIANT_* in install/?
    Mar 05 04:19:25 <div0>	can you retry make install?
    Mar 05 04:20:13 <FruitieX>	eh, now it works yes
    Mar 05 04:20:23 <FruitieX>	so i'm supposed to get the gamepacks BEFORE make
    Mar 05 04:20:26 <FruitieX>	it seems like...
    Mar 05 04:40:28 <FruitieX>	div0: for the new version of Nexuiz I'd like to see light data on the maps calculated by a raytracer
    Mar 05 04:40:48 <FruitieX>	because in my opinion it manages to look quite a lot better on some maps
    Mar 05 04:40:58 <FruitieX>	at least if done right... :P
    Mar 05 04:41:34 <div0>	will you NEVER want to release it?
    Mar 05 04:44:04 <div0>	or do you happen to have a working raytracer for that?
    Mar 05 04:44:22 <FruitieX>	the DP one WORKS.... but can't save :P
    Mar 05 04:44:27 <div0>	it does not :P
    Mar 05 04:44:40 <div0>	I couldn't get it to light up the floor or ceiling on euclidean fail
    Mar 05 04:44:50 <div0>	if it had worked, it would have motivated me to add loading and saving for it
    Mar 05 04:44:56 <FruitieX>	no? hmm
    Mar 05 04:45:09 <FruitieX>	maybe it has been broken since i tested it
    Mar 05 04:45:12 <FruitieX>	i know it did work for me
    Mar 05 04:45:17 <div0>	can you try on euclidean fail?
    Mar 05 04:45:20 <FruitieX>	sure
    Mar 05 04:45:20 <div0>	maybe the problem is map specific
    Mar 05 04:45:23 <div0>	it lit up the walls
    Mar 05 04:45:25 <FruitieX>	are there rtlights on there already?
    Mar 05 04:45:26 <div0>	but not the floor and ceiling
    Mar 05 04:45:31 <div0>	I made some in the rtlight editor
    Mar 05 04:45:34 <FruitieX>	ok
    Mar 05 04:45:37 <div0>	these properly lit up the floors/ceilings
    Mar 05 04:45:38 <FruitieX>	brb first though
    Mar 05 04:45:40 <div0>	I meanä
    Mar 05 04:45:43 <div0>	the walls :P
    Mar 05 04:59:10 <div0>	one question is left - do we HAVE to rename+
    Mar 05 04:59:16 <div0>	given how hard it seems to be to come out wiht a godo name
    Mar 05 04:59:26 <div0>	[-z-]: if you keep doing SEO as you did for AT, we might not HAVE to rename
    Mar 05 05:00:03 <div0>	it is just that SEO and spreading the word would become WAY more important than now
    Mar 05 05:01:01 <FruitieX>	of course, i got a segfault when turning on rt world lights... :P
    Mar 05 05:01:31 <div0>	BTW, DP's isn't a raytracer :P
    Mar 05 05:01:36 <div0>	it works very similar to q3map2's
    Mar 05 05:01:40 <div0>	just less buggy :P
    Mar 05 05:01:45 <div0>	that is, IF it works
    Mar 05 05:01:49 <FruitieX>	heh
    Mar 05 05:02:03 <div0>	speaking of segfault - also often got segfautls with the lights compile stuff :P
    Mar 05 05:02:09 <FruitieX>	how come i was able to produce some much sweeter looking lightning for aggressor - then? :P
    Mar 05 05:02:17 <div0>	oh? can I see?
    Mar 05 05:02:19 <FruitieX>	even if it doesn't have AO and radiosity
    Mar 05 05:02:23 <FruitieX>	that was a long time ago div0 
    Mar 05 05:02:24 <div0>	not tried it on already finished maps
    Mar 05 05:02:26 <div0>	oh
    Mar 05 05:02:27 <FruitieX>	i have screens though, hold on
    Mar 05 05:02:29 <div0>	maybe he borked it :P
    Mar 05 05:02:40 <FruitieX>	indeed thats what i'm thinking too
    Mar 05 05:02:58 <div0>	but well
    Mar 05 05:03:01 <div0>	once it renders right
    Mar 05 05:03:05 <div0>	I will code loading and saving
    Mar 05 05:03:16 <div0>	will likely use more GPU memory than q3map2 though
    Mar 05 05:03:30 <div0>	(as it doesn't pack the lightmaps together so well)
    Mar 05 05:03:35 <FruitieX>	http://pics.nexuizninjaz.com/images/oq8t3xpshhakub5d0a3.jpg
    Mar 05 05:03:48 <FruitieX>	wtf is that very bright trim light there though? :P
    Mar 05 05:03:49 <FruitieX>	http://pics.nexuizninjaz.com/images/rm2gjazwaoo85rvxgd59.jpg
    Mar 05 05:04:34 <FruitieX>	iirc LH said the lightmaps generated by this are of way smaller resolution than those by q3map2
    Mar 05 05:05:05 <FruitieX>	guess that comes with a cost too - no sharp shadows
    Mar 05 05:05:24 <div0>	but well
    Mar 05 05:05:29 <div0>	I don't think this should be a requirement
    Mar 05 05:05:36 <div0>	rtlights files, however, should be again
    Mar 05 05:05:44 <div0>	even on e&b :P
    Mar 05 05:05:53 <div0>	(but there it really shouldn't be hard)
    Mar 05 05:06:25 <FruitieX>	well, i just think it looks more realistic than what q3map2 generates :)
    Mar 05 05:06:34 <div0>	true :P
    Mar 05 05:06:48 <FruitieX>	q3map2's lightning seems oddly boring in some way
    Mar 05 05:07:01 <FruitieX>	wish we could do this via e.g. blender's internal renderer or so :P
    Mar 05 05:08:39 *	Spaceman (~Spaceman@87.127.156.98) has joined #notnexuiz
    Mar 05 05:09:09 <FruitieX>	also div0, euclidean fail seems to work here :P
    Mar 05 05:09:15 <div0>	oh, cool
    Mar 05 05:09:19 <div0>	maybe thjere has been a fix :P
    Mar 05 05:09:26 <div0>	screenshot?
    Mar 05 05:09:33 <div0>	(of EF with one light :P)
    Mar 05 05:09:42 <div0>	and you did remember to turn off rtlights again after compiling the lights?
    Mar 05 05:10:00 <FruitieX>	i did
    Mar 05 05:10:04 <FruitieX>	i never turned them on in fact :P
    Mar 05 05:10:10 <FruitieX>	as that seems to be almost 100% crash for me
    Mar 05 05:10:15 <FruitieX>	after spawning a light, that is
    Mar 05 05:10:44 <FruitieX>	div0: roof seems oddly dark: http://pics.nexuizninjaz.com/images/rq14ns4laha3scdq2gbz.jpg
    Mar 05 05:11:05 <div0>	oh, you can use rtlight editor without? :P
    Mar 05 05:11:14 <FruitieX>	yes, apparently :P
    Mar 05 05:11:15 <div0>	funny, so floor gets hit, ceiling not
    Mar 05 05:11:41 <FruitieX>	ceiling gets hit a bit
    Mar 05 05:12:04 <FruitieX>	maybe light being so close causes some bugs...
    Mar 05 05:12:27 <div0>	I tried lights in the air too
    Mar 05 05:12:30 <div0>	or make one on  a wall
    Mar 05 05:15:15 <FruitieX>	near wall (to the right): http://pics.nexuizninjaz.com/images/oi7gdi1t7esvv0hjlun.jpg
    Mar 05 05:15:35 <div0>	great, so it actually works for you somewhat
    Mar 05 05:15:35 <FruitieX>	in the air: http://pics.nexuizninjaz.com/images/hqarpb6pmn29nvovsc4w.jpg
    Mar 05 05:15:41 <FruitieX>	100 units from the roof
    Mar 05 05:15:45 <FruitieX>	yep last one looks best
    Mar 05 05:16:04 <FruitieX>	all of them have radius 1000 btw, which is quite much
    Mar 05 05:16:09 <FruitieX>	but as i'm only using one light... :)
    Mar 05 05:16:34 <FruitieX>	the first two pics both have their light pushed only 4 units from the surface (default for r_editlights)
    Mar 05 05:16:58 <div0>	hm... great
    Mar 05 05:17:06 <div0>	when I get this working too, I will make loading/saving :P
    Mar 05 05:18:04 <FruitieX>	aah get it working :P
    Mar 05 05:18:21 <FruitieX>	also need (in order of importance): skybox sun support
    Mar 05 05:18:38 <FruitieX>	surfacelight shader parameter support
    Mar 05 05:18:50 <div0>	surfacelight, not sure if doable
    Mar 05 05:18:54 <FruitieX>	hmm
    Mar 05 05:18:54 <div0>	as it is based on the rtlights
    Mar 05 05:19:00 <div0>	sun. NEEDED, whatever the cost
    Mar 05 05:19:04 <FruitieX>	right well
    Mar 05 05:19:14 <FruitieX>	hacky way of doing surfacelight should work
    Mar 05 05:19:21 <FruitieX>	just spawn some lights above the surface... :P
    Mar 05 05:20:21 <FruitieX>	of course i had to test, even if i knew the outcome: http://pics.nexuizninjaz.com/images/op1ni605okf37c51z62k.jpg
    Mar 05 05:20:28 <FruitieX>	through warpzone: epic fail :)
    Mar 05 05:21:00 <div0>	sure :P
    Mar 05 05:21:03 <div0>	not really avoidable
    Mar 05 05:21:12 <div0>	lights in the "connection space" might be supportable
    Mar 05 05:21:17 <div0>	as they could be transformed to the other side
    Mar 05 05:21:28 <div0>	but other lights, no
    Mar 05 05:21:55 <div0>	hehe, maybe could be done using a warpzone preprocessor, which reads a rtlights file, and adds warpzoned versions of all lights :P
    Mar 05 05:22:21 <FruitieX>	hehe
    Mar 05 05:23:23 <FruitieX>	problem then of course would be, what if there's a room behind the warpzone, and a light near the other warpzone
    Mar 05 05:23:44 <FruitieX>	if that makes any sense...
    Mar 05 05:23:51 <FruitieX>	stormkeep would be a good example here :P
    Mar 05 05:26:39 <div0>	oh :P
    Mar 05 05:26:51 <div0>	it should only project the light to the other side, if it fits into the trigger brush of the zone
    Mar 05 05:27:08 <div0>	that wouldn't cause bugs, but would mean some lights will be missing
    Mar 05 05:31:02 <FruitieX>	ah of course :P
    Mar 05 05:34:14 <FruitieX>	another BTW: this looks terrible on patches :P
    Mar 05 05:34:46 <SoulKeeper_p>	+1 on Pheonix, tho thats already taken.
    Mar 05 05:35:16 <SoulKeeper_p>	hm
    Mar 05 05:35:23 <div0>	FruitieX: patches may be fixable
    Mar 05 05:41:55 *	mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 05:45:38 <SoulKeeper_p>	Here some input according name (random order):(seo tested, and domain name proof.)
    Mar 05 05:45:57 <SoulKeeper_p>	* Nexologic
    Mar 05 05:46:15 <SoulKeeper_p>	* Phanomite (phenomite)
    Mar 05 05:46:22 <SoulKeeper_p>	* JustNex
    Mar 05 06:12:38 *	Morphed (~Morphed@aaqd187.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 05 06:20:55 <div0>	TehRealNexuiz
    Mar 05 06:21:03 <div0>	Nexuiz - the ORIGINAL
    Mar 05 06:32:36 <Morphed>	?
    Mar 05 06:33:12 <Morphed>	so its not pheonix anymore ?
    Mar 05 06:34:20 <Dokujisan>	the name "phoenix" (or the misspelled Pheonix) name is simply overused.
    Mar 05 06:34:54 <Dokujisan>	a unique name would be best
    Mar 05 06:35:06 <Dokujisan>	preferrably something that doesn't already have a meaning
    Mar 05 06:35:13 <Dokujisan>	just like Nexuiz was
    Mar 05 06:36:56 <Morphed>	still its best so far :)
    Mar 05 06:38:54 <SoulKeeper_p>	its pitta on pheonix ye.
    Mar 05 06:39:02 <Dokujisan>	I like nexotic, nexilus, xenotic, nexion (although that one is pretty much taken)
    Mar 05 06:39:07 <SoulKeeper_p>	Morphed, you missed:
    Mar 05 06:39:08 <SoulKeeper_p>	* mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 06:39:08 <SoulKeeper_p>	<SoulKeeper_p> Here some input according name (random order):(seo tested, and domain name proof.)
    Mar 05 06:39:08 <SoulKeeper_p>	<SoulKeeper_p> * Nexologic
    Mar 05 06:39:08 <SoulKeeper_p>	<SoulKeeper_p> * Phanomite (phenomite)
    Mar 05 06:39:08 <SoulKeeper_p>	<SoulKeeper_p> * JustNex
    Mar 05 06:39:10 <SoulKeeper_p>	* Morphed (~Morphed@aaqd187.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 05 06:39:52 <SoulKeeper_p>	+ Nexotic
    Mar 05 06:39:58 <SoulKeeper_p>	1*
    Mar 05 06:40:15 <Dokujisan>	for the 'x' names, xodius is decent too
    Mar 05 06:40:27 <Dokujisan>	the thing is, we can't keep the "n" symbol
    Mar 05 06:40:35 <Dokujisan>	so we're going to have to come up with another symbol
    Mar 05 06:40:58 <Dokujisan>	that's one downside to using the "nex" prefix
    Mar 05 06:41:06 <Dokujisan>	or a name that begins with "n"
    Mar 05 06:41:23 <Morphed>	maybe kanji symbol for reborn or phoenix :)
    Mar 05 06:41:32 <SoulKeeper_p>	yea, kinna..or the design should differ then the orig n"
    Mar 05 06:42:09 <Dokujisan>	Morphed: now that's a good idea
    Mar 05 06:42:21 <Dokujisan>	the previous symbol was kanji for power or something
    Mar 05 06:42:32 <Morphed>	nexologic ?
    Mar 05 06:42:33 <Morphed>	Buy it, use it, break it, fix it,
    Mar 05 06:42:33 <Morphed>	Trash it, change it, mail - upgrade it,
    Mar 05 06:44:50 <Morphed>	http://www.youtube.com/watch?v=YtdWHFwmd2o
    Mar 05 06:46:27 <div0>	could use the katakana for "n" ;)
    Mar 05 06:46:30 <SoulKeeper_p>	strength symbol iirc.
    Mar 05 06:46:33 <SoulKeeper_p>	Morphed, hehe
    Mar 05 06:46:35 <div0>	no, hiragana better
    Mar 05 06:46:53 <div0>	http://images.google.de/imgres?imgurl=http://upload.wikimedia.org/wikipedia/commons/e/e2/N-hiragana.gif&imgrefurl=http://commons.wikimedia.org/wiki/File:N-hiragana.gif&usg=__GBzjYnWOW-oUlc0qBkv0NYa4tNc=&h=100&w=100&sz=3&hl=de&start=1&tbnid=m-p4h4dshSvgOM:&tbnh=82&tbnw=82&prev=/images%3Fq%3Dn%2Bhiragana%26um%3D1%26hl%3Dde%26client%3Dopera%26sa%3DN%26rls%3Den%26tbs%3Disch:1&um=1&itbs=1
    Mar 05 06:47:08 <Morphed>	not that cool
    Mar 05 06:49:15 *	Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 05 06:53:30 <Dokujisan>	ok I got the support of the aussienexers
    Mar 05 06:53:48 <Dokujisan>	so whatever we need them to do for this new-nexuiz fork, they are willing to do
    Mar 05 06:53:50 <FruitieX>	:o
    Mar 05 06:54:05 <div0>	thing is still... shouldn't we keep our name somehow nexuiz-related so it can be done as long as possible?
    Mar 05 06:54:13 <div0>	so basically: maybe a name WITH nexuiz somewhere in it is best
    Mar 05 06:55:02 <div0>	great, so we have the support of Bogan? ;)
    Mar 05 06:55:09 <Dokujisan>	haha
    Mar 05 06:55:21 <Dokujisan>	well he's the most important one..we MUST get him
    Mar 05 06:55:25 <Morphed>	we will have support of willis also 
    Mar 05 06:55:48 <div0>	but basically... we should make one thing clear
    Mar 05 06:55:51 <div0>	this should NOT be a fork
    Mar 05 06:56:00 <div0>	but, we should take over the Alientrap project as a free group
    Mar 05 06:56:15 <div0>	(will happen anyway, if we do what we are going to)
    Mar 05 06:56:40 <div0>	so, we do not HAVE to use an entirely new name
    Mar 05 06:56:43 <Dokujisan>	<div0> this should NOT be a fork
    Mar 05 06:56:44 <Dokujisan>	?
    Mar 05 06:56:48 <div0>	well
    Mar 05 06:56:50 <div0>	assume we fork
    Mar 05 06:57:02 <div0>	do you really think anyone at alientrap will be left and willing to do their own "nexuiz" development?
    Mar 05 06:57:07 <div0>	AT will only care for the console one anyway
    Mar 05 06:57:22 <Dokujisan>	well, that's true, but it's at least verm's decision to do that
    Mar 05 06:57:29 <div0>	sure
    Mar 05 06:57:33 <Dokujisan>	possibly LH would take over
    Mar 05 06:57:38 <div0>	doubt it
    Mar 05 06:58:14 <div0>	he sounded not against the idea of taking Nexuiz out of the hands of Alientrap/Vermeulen, and continuing as an actual FLOSS project, when loosely hinting to that this might happen
    Mar 05 06:58:30 <Dokujisan>	hmm
    Mar 05 06:58:40 <div0>	and actually
    Mar 05 06:58:47 <div0>	if we do a fork, exactly that will effectively happen
    Mar 05 06:58:52 <div0>	LH won't continue with it
    Mar 05 06:59:27 <div0>	so, there will NOT be two competing lines of development
    Mar 05 06:59:45 <div0>	simply because NONE of the currently active Nexuiz developers (apart from LH) are in any way affiliated with Alientrap
    Mar 05 07:00:05 <div0>	so it shouldn't be hard to win them over
    Mar 05 07:00:29 <div0>	and LH on the other hand won't be unhappy to know that he can now work more on Darkwar
    Mar 05 07:01:07 <div0>	basically: we do NOT have to be much different from current Nexuiz
    Mar 05 07:01:20 <Dokujisan>	Now that we have more people in here, I would like to discuss some ideas for structure. You mentioned the idea of 3 (or 5?) key leaders to make final decisions and a committee underneath and a process for deciding things. 
    Mar 05 07:01:27 <div0>	we could, maybe, even use the name (but using JUSt the name Nexuiz would probably be bad, with a variation/suffix would work)
    Mar 05 07:01:39 <div0>	if we do take another name, we should CLEARLY state that the project was once known as Nexuiz
    Mar 05 07:01:44 <SoulKeeper_p>	PureNexuiz
    Mar 05 07:01:47 <SoulKeeper_p>	JustNexuiz
    Mar 05 07:01:57 <div0>	does that work for search engines?
    Mar 05 07:02:01 <div0>	[-z-]: ?
    Mar 05 07:02:08 <Dokujisan>	what's been said a lot so far is that "Nexuiz" was never a good name to begin with
    Mar 05 07:02:12 <div0>	or would we have to spell it "Pure nexuiz"
    Mar 05 07:02:18 <div0>	that is true
    Mar 05 07:02:28 <div0>	yet still, a new name means starting from ground zero, popularity wise
    Mar 05 07:02:34 <SoulKeeper_p>	well div0 its hard to het it up since nexuiz is already there on google rank higher up ;)
    Mar 05 07:02:36 <Dokujisan>	so I don't mind carrying on the use of "nex" in the name
    Mar 05 07:02:38 <div0>	it would be wise to try to figure out how we can at least gain a BIT from illfonic
    Mar 05 07:03:04 <Dokujisan>	I think the buzz from this story, since it is stemming from a failed GPL project, will help us generate a lot of attention
    Mar 05 07:03:07 <Dokujisan>	if we launch this properly
    Mar 05 07:03:32 <Dokujisan>	anytime there is a big story associated with a GPL project, it ends up on digg, reddit, slashdot
    Mar 05 07:03:52 <div0>	yes, but that is short term
    Mar 05 07:04:06 <div0>	but sure
    Mar 05 07:06:52 <div0>	as for organization, I suggest:
    Mar 05 07:06:57 <Dokujisan>	aussienexers asked why this is secret. The main reason I gave was.... " we have a lot of work to do. getting pelted with constant questions would not help that"
    Mar 05 07:07:01 <div0>	- three "leaders" who should come from different backgrounds
    Mar 05 07:07:20 <div0>	- otherwise, freedom should reign among the community
    Mar 05 07:07:39 <div0>	- "big" decisions (like whole new gameplay balance) should be approved by ALL leaders, who stand personally for the community
    Mar 05 07:07:52 <div0>	- small stuff can be decided by the community directly (e.g. by just performing a change and committing)
    Mar 05 07:08:11 <div0>	- nobody will be able AT ALL to sell/relicense the project :P
    Mar 05 07:08:37 <SoulKeeper_p>	PureNexuiz and JustNexuiz both domain wise are avail..
    Mar 05 07:08:50 <Dokujisan>	again, "nexuiz" is deemed a not very good name
    Mar 05 07:09:03 <Dokujisan>	we should let it go
    Mar 05 07:09:04 <SoulKeeper_p>	div0, good simple starting rules
    Mar 05 07:09:24 <Dokujisan>	div0: that sounds good so far
    Mar 05 07:09:35 <SoulKeeper_p>	Dokujisan, one says let it go other wants it, best thing is make up ones mind then act. ;)
    Mar 05 07:09:59 <div0>	different backgrounds: that should ensure no interest group of nexuiz loses too much weight
    Mar 05 07:10:41 <div0>	I'd mention: competitive background (this leader job will most likely go to Dokujisan, or maybe NN), "play for fun" background (e.g. PB)
    Mar 05 07:10:48 <div0>	but there'd be more
    Mar 05 07:11:00 <Dokujisan>	my main interest is that I want to be a community organizer and help with recruiting new talent to the project, marketing efforts, manage volunteers from within the community
    Mar 05 07:11:06 <div0>	sure
    Mar 05 07:11:10 <div0>	that wouldn't be inhibited :P
    Mar 05 07:11:31 <div0>	but regarding game relevant decisions, you probably will represent the competitive side, which is good, as that NEEDS to be represented
    Mar 05 07:11:55 <div0>	and with interest groups, I mean "from the players"
    Mar 05 07:12:10 <div0>	so... let me ask this way
    Mar 05 07:12:13 <div0>	why do you play Nexuiz?
    Mar 05 07:12:25 <Dokujisan>	it's my replacement for martial arts heh
    Mar 05 07:12:51 <Dokujisan>	I used to train in martial arts a lot. I don't as much and nexuiz sorta took that spot.
    Mar 05 07:12:57 <div0>	I mostly play for fun, and therefore like development of new stuff and experimenting... others play competitively, which of course prefers sticking to the roots
    Mar 05 07:13:14 <div0>	(and requires stability in the "core game")
    Mar 05 07:13:26 <SoulKeeper_p>	I can understand why div0 or tZork|gone does not want to necessarily leave the name "nexuiz" ...they are indd some major pro cons to that.
    Mar 05 07:13:36 <Dokujisan>	and I like the organization-side of business and I get to do some of that within nexuiz
    Mar 05 07:13:43 <div0>	but there sure is more interest groups
    Mar 05 07:13:53 <div0>	Dokujisan: well, it should NOT be organized like a business :P
    Mar 05 07:13:57 <div0>	we have seen what happens then ;)
    Mar 05 07:14:05 <Dokujisan>	certainly not like a business, no
    Mar 05 07:14:18 <Dokujisan>	but the 'organization" aspect of running a business is interesting to me
    Mar 05 07:14:21 <div0>	but sure, if you are good at it AND flexible in thought (not time)...
    Mar 05 07:14:24 <div0>	then that is great
    Mar 05 07:14:31 <div0>	and you indeed seem that way
    Mar 05 07:15:15 <div0>	also, I always had an interest in the theory of politics... and how it usually fails :P
    Mar 05 07:15:30 <div0>	which is why I now will try to ensure a structure with a sort of "division of power", but without the bureaucracy
    Mar 05 07:15:42 <div0>	I mean, we sure shouldn't divide into legislative, executive, judicative :P
    Mar 05 07:16:01 <Dokujisan>	I see
    Mar 05 07:16:08 <div0>	but, we should indeed learn some lessons from history of politics :P
    Mar 05 07:16:21 <div0>	like: "much power in one person = FAIL"
    Mar 05 07:16:47 <Dokujisan>	I agree
    Mar 05 07:17:03 <Dokujisan>	a good project needs leadership, but that leadership shouldn't be one single person
    Mar 05 07:17:04 <div0>	and as we have seen now, it's even MORE fail, if nobody knows/realizes that someone has the much power :P
    Mar 05 07:17:14 <Dokujisan>	haha yeah
    Mar 05 07:17:21 <div0>	also, as a free project, leadership should not be exerted by force :P
    Mar 05 07:17:40 <div0>	if someone wants a feature, and the leaders are against it, one should think about a way to get it in in a varied but better fashion
    Mar 05 07:18:15 <div0>	code wise, I'd go so far - if the code is harmless (e.g. if it can be turned off), and mostly bug free, it can go in - even if I don't like what it brings
    Mar 05 07:18:41 <div0>	art wise it's a bit more difficult, as there can be many opinions what is good and what is not
    Mar 05 07:19:28 <div0>	there, I'd only like to avoid bad taste (like, pr0n, or TOO strong displays of violence - after all, the game is meant to be PLAYed, and is not a virtual torture chamber)
    Mar 05 07:19:55 <div0>	of course, the competitive players ALSO do not want overly strong violence, as it blocks the view :P
    Mar 05 07:20:04 <Dokujisan>	yeah... like leaving out "You pussy!!" voice recordings :-)
    Mar 05 07:20:18 <Dokujisan>	or whaever that thing said
    Mar 05 07:20:20 <div0>	as a non-native speaker, I mainly think of a cat when hearing that...
    Mar 05 07:20:23 <div0>	but yes, maybe that should go
    Mar 05 07:20:44 <div0>	there's enough "verbal violence" in chat, we don't need it in sounds too:P
    Mar 05 07:21:47 <div0>	basically... I think regarding that, the game should be in a way so that the Pope wouldn't object to playing it, other than him probably not being interested in video games :P
    Mar 05 07:22:14 <div0>	and there isn't much needed to achieve that... guns are generally accepted as GOOD ;) and the rest is fine, apart from soem voice recordings
    Mar 05 07:22:25 <Dokujisan>	I have to say that I've agreed with 99% of what you've said over the past 48 hours during these chats. The only thing I disagreed with is the privacy concerns with central user system, but we discussed and resolved that now. So I'm very excited and hopefully for where things are going.
    Mar 05 07:22:41 <Dokujisan>	hopeful*
    Mar 05 07:23:18 <div0>	regarding violence for example: I like that our guns are either unrealistic (electro, hlac), or those which do make sense in real life, aren't overly graphic (like shotgun)
    Mar 05 07:23:53 <div0>	shooting someone with a Nex IMHO does not count as graphic violence, as nobody would ever take a scifi weapon for real :P
    Mar 05 07:24:20 <Taoki>	Yeah, that is true as well.
    Mar 05 07:24:20 <Dokujisan>	I really like the futuristic theme that Nexuiz has grown into. I understand it started out more with an industrial/gritty theme like Quake, but changed over time to more futuristic
    Mar 05 07:24:22 <Taoki>	Hi all
    Mar 05 07:24:43 <div0>	this is also BTW why I don't like mikeeusa's "cutting" idea :P
    Mar 05 07:24:50 <div0>	I do not WANT lasers to cut player models into parts
    Mar 05 07:25:00 <Taoki>	Well, I was at some point pondering pain skins. Like a blood layer being stuck to players based on their health
    Mar 05 07:25:05 <div0>	but using it for func_breakable to break a window into parts, sure, yeah
    Mar 05 07:25:20 <div0>	Taoki: I wouldn't care for it violence wise, but it'd eat GPU memory like hell
    Mar 05 07:25:31 <Taoki>	For realism... I don't really like gore and stuff
    Mar 05 07:25:38 <Taoki>	ah, i see
    Mar 05 07:26:12 <div0>	breaking THINGS is not exactly graphic violence after all :P
    Mar 05 07:26:17 <Dokujisan>	yeah
    Mar 05 07:26:27 <div0>	huge explosions, hell yeah
    Mar 05 07:26:30 <Taoki>	Well the old Kingpin - Life of Crime (gang game made over the Quake 1 2 or 3 engine, 10 years old at least) had pain skins, but they were 2 different versions of each player skin
    Mar 05 07:26:54 <div0>	thus I also like the idea that in a fps like Nexuiz, you don't really die
    Mar 05 07:26:57 <div0>	you just respawn :P
    Mar 05 07:27:13 <div0>	you respawn and need to collect items again, but you can continue playing
    Mar 05 07:27:29 <Taoki>	What i'd like to see though is after-damage effects like in UT2004. eg. You shoot someone with the machinegun, they spray a blood trail for a second. Electro, they have lightning coming out of them for a second, etc.
    Mar 05 07:27:39 <div0>	that sure makes you way less immersed to the game - but I like it, I like playing "detached" from the game
    Mar 05 07:28:11 <div0>	Taoki: csqc networked players and we can have it :P
    Mar 05 07:28:16 <div0>	of course with cl_gentle versions of it ;)
    Mar 05 07:28:30 <Taoki>	yeah. It can be enabled only if cl_gentle is
    Mar 05 07:28:38 <Taoki>	I tried implementing it a long time ago
    Mar 05 07:28:42 <div0>	that can be enabled in non-gentle too...
    Mar 05 07:28:45 <div0>	I do not object to it
    Mar 05 07:28:52 <div0>	as it doesn't make the game more violent
    Mar 05 07:28:57 <Taoki>	But couldn't figure hot to put a constant particle generating entity to a player
    Mar 05 07:29:06 <div0>	whether the blood is sprayed on hit, or slowly over time, changes not much
    Mar 05 07:29:07 <Taoki>	Which then dies off after a time
    Mar 05 07:29:13 <div0>	but slowly over time looks better and gives better fps
    Mar 05 07:29:17 <div0>	yes
    Mar 05 07:29:23 <div0>	this is what you need CSQC networked players for
    Mar 05 07:30:06 *	tZork|gone is now known as tZork
    Mar 05 07:30:08 <div0>	do not do it on server qc, although you maybe could
    Mar 05 07:30:12 <div0>	as ti'd be a huge bandwidth hog
    Mar 05 07:30:26 <div0>	in server qc, sure, you could make a particle emitting ent and make it MOVETYPE_FOLLOW the player
    Mar 05 07:30:31 <div0>	but don't, that eats BW like hell
    Mar 05 07:31:08 <div0>	if you want it for your own mod, sure, can code it for you :P
    Mar 05 07:31:15 <div0>	(the server side variant)
    Mar 05 07:31:22 <tZork>	what a day.. hi fokes.
    Mar 05 07:31:27 <div0>	hi
    Mar 05 07:32:18 <FruitieX>	hi
    Mar 05 07:32:27 <tZork>	gebuz the backlog is abt as as logn as Doku's log hehe. will be hard to keep read up on it all. 
    Mar 05 07:32:33 <Dokujisan>	lol
    Mar 05 07:32:45 <Dokujisan>	we just covered ideas on organization
    Mar 05 07:32:52 <Dokujisan>	so scan the recent chat for that
    Mar 05 07:33:27 <Dokujisan>	I'll end up replacing that notnexuiz.log with page giving bullet points
    Mar 05 07:33:36 <Dokujisan>	after some decisions are nailed down
    Mar 05 07:33:55 <Dokujisan>	I need to skim through our discussions about map choices and put those into my notes
    Mar 05 07:35:23 *	Taoki has quit (Ping timeout: 364 seconds)
    Mar 05 07:35:31 <tZork>	a totaly flat organization (as in all votes are equal on all subjects) would be interesting. very likely "to interesting" tough ;)
    Mar 05 07:36:18 <div0>	totally flat would probably not work :P
    Mar 05 07:36:21 <div0>	then you can do nothing
    Mar 05 07:36:42 <div0>	but there should be "enough" leaders, and they should represent various aspects of the game
    Mar 05 07:36:52 <div0>	especially the aspects that tend to cause controversy
    Mar 05 07:37:07 <div0>	the goal is to choose leaders so that any possible controversy is also among the leaders :P
    Mar 05 07:37:27 <Dokujisan>	one thing that is difficult with a committee vote is if not everyone is around to vote
    Mar 05 07:37:33 <Dokujisan>	like on vacation or something
    Mar 05 07:37:34 <div0>	yes
    Mar 05 07:37:51 <div0>	also, not sure if voting by itself actually works
    Mar 05 07:38:09 <div0>	and, big decisions that NEED all leaders to agree (and most of the community) don't happen that often
    Mar 05 07:38:21 <div0>	big gameplay changes can e.g. first be done in a branch, and later applied
    Mar 05 07:38:40 <div0>	most stuff that is being developed is stuff that does not interfere with anyone else
    Mar 05 07:38:46 <Dokujisan>	div0: tZork was asking about (or suggesting, rather) some code cleanup for nexuiz
    Mar 05 07:38:50 <Dokujisan>	tZork: can you go more into that?
    Mar 05 07:38:57 <tZork>	it does work, when the involved parties are somewhat limited in number, and fairly like minded. in that piticular case (in my own experiance) that model is acctualy superior. but its a rather delicate entity.
    Mar 05 07:39:17 <div0>	tZork: in case of Nexuiz community, no
    Mar 05 07:39:20 <div0>	see the CTF scoring case :P
    Mar 05 07:39:24 <Dokujisan>	hehe
    Mar 05 07:39:40 <div0>	everyone convinced that the old was is bad - but also everyone proposing and insisting on his own way to solve it
    Mar 05 07:39:52 <div0>	so whatever decision is taken (even "no change at all"), you have 80% against you
    Mar 05 07:40:08 <Dokujisan>	for CTF scoring, we finally did some proper testing, but unfortunately that testing was done "live" as the default. Everyone on my servers thinks the scoring is strange.
    Mar 05 07:40:19 <tZork>	how to fuck up a good idea - just add ppl ;)
    Mar 05 07:40:27 <Dokujisan>	;-)
    Mar 05 07:41:01 <Dokujisan>	I understand the ideas behind the scoring though. Luckily, scoring isn't a top priority issue. People still love the game even with messed up scoring.
    Mar 05 07:41:03 <tZork>	sure Dokujisan, well my main gippy with nexuiz codebase it its planless. and suffers there of.
    Mar 05 07:41:27 <div0>	tZork: most stuff is quite clean
    Mar 05 07:41:32 <div0>	and I don't think we should overthrow it all
    Mar 05 07:41:37 <div0>	I am rather for slowly reorganizing it
    Mar 05 07:41:51 <div0>	the parts that probably SHOULD be overthrown and replaced: teamplay.qc :P
    Mar 05 07:41:55 <tZork>	quality wize, yes, tnx to you im most cases div0
    Mar 05 07:42:15 <tZork>	but its following much the random structure it happend to evole into
    Mar 05 07:42:17 <div0>	what I fear of a "cleanup" is that 80% of the features will be gone
    Mar 05 07:42:43 <div0>	and THAT I will never approve of
    Mar 05 07:42:52 <tZork>	thus has major unnessesary overhead, and its a bitch to get into for anyone from teh outside.
    Mar 05 07:43:04 <div0>	well, how are you going to fix that?
    Mar 05 07:43:14 <div0>	I am certainly rejecting the idea if it emans that all interesting features are gone
    Mar 05 07:43:23 <tZork>	start clean, copy stuff over. but have a plan for it.
    Mar 05 07:43:34 <div0>	I won't have much time for that, neither much motivation
    Mar 05 07:43:41 <div0>	also, it WILL mean that most features are gone
    Mar 05 07:44:04 <div0>	probably all that I did, as I won't have the motivation to implement it all a second time
    Mar 05 07:44:12 <tZork>	successfull evolution means dropping off dead weight.
    Mar 05 07:44:18 <div0>	depends
    Mar 05 07:44:28 <div0>	I bet you consider Keyhunt dead weight
    Mar 05 07:44:38 <div0>	so YOU would not reimplement it
    Mar 05 07:45:15 <div0>	also, how are you even going to reorganize the bot code? Nobody on earth understands it :P
    Mar 05 07:45:19 <tZork>	not sure, this is a specific case tough, what i want to talk abt it the general idea
    Mar 05 07:45:32 <div0>	general idea may be fine, but it probably won't eb Nexuiz any more then
    Mar 05 07:45:34 <tZork>	if noone cares enougth to port feature X over, its rather likely that noone cares abt afore
    Mar 05 07:45:35 <div0>	but a totally different game
    Mar 05 07:45:38 <Dokujisan>	maybe we can do a code review by a number of people (developers) and start taking notes of areas of the code that they feel needs cleanup. 
    Mar 05 07:45:50 <div0>	tZork: it is not about caring
    Mar 05 07:45:54 <div0>	but also about having the time for it
    Mar 05 07:45:56 <Dokujisan>	and then we can discuss it better after we know what exactly we're talking about (what areas of code)
    Mar 05 07:46:23 <div0>	tZork: if it's some hidden feature nobody ever uses, sure, then that can be "reorganized away"
    Mar 05 07:46:32 <div0>	but what would that be, apart maybe from runematch?
    Mar 05 07:46:40 <Dokujisan>	omg I forgot about runematch
    Mar 05 07:46:42 <div0>	or certain failed balance_teams modes that all suck
    Mar 05 07:47:29 *	Disconnected (Connection reset by peer).
    **** ENDING LOGGING AT Fri Mar 05 07:47:29 2010

    **** BEGIN LOGGING AT Fri Mar 05 07:48:15 2010

    Mar 05 07:48:15 *	Now talking on #notnexuiz
    Mar 05 07:48:15 *	Topic for #notnexuiz is: here is most of the conversation so far -- http://www.nullgaming.com/stuff/notnexuiz.log
    Mar 05 07:48:15 *	Topic for #notnexuiz set by Dokujisan!~doku-lapt@74-132-116-73.dhcp.insightbb.com at Thu Mar 04 17:41:49 2010
    Mar 05 07:48:23 <div0>	plus, keyhunt already has quite a good structure
    Mar 05 07:48:27 <tZork>	keyhunt - sure, but id exspect you to wnt to do taht.
    Mar 05 07:48:42 <div0>	problem is, it is now CLEAR that I will have MUCH less time in the future
    Mar 05 07:48:47 <div0>	I want keyhunt to stay in Nexuiz and be pushed more
    Mar 05 07:48:53 <tZork>	okay
    Mar 05 07:48:57 <div0>	but in about 9 months from now, I will SURE not be able to work on it
    Mar 05 07:49:07 <div0>	(yes, breaking news)
    Mar 05 07:49:38 <Taoki>	I like Assault
    Mar 05 07:49:44 <div0>	so basically, I'd rather think that it should be evolutionary restructured in some way
    Mar 05 07:49:54 <div0>	the goal should be to bring ALL features over
    Mar 05 07:49:58 <div0>	maybe mark in the old code what you have
    Mar 05 07:50:08 <div0>	and continue, keeping only the unimplemented stuff in the old code
    Mar 05 07:50:20 <div0>	so one can easily track what is done and what not
    Mar 05 07:50:42 <div0>	the keyhunt code for example shouldn't be too hard to integrate into a new code base, same goes for race
    Mar 05 07:50:51 <tZork>	right
    Mar 05 07:50:54 <div0>	as the code for it is in its own qc file, and called by callbacks from outside
    Mar 05 07:50:59 <div0>	all game modes should be that way, of course :P
    Mar 05 07:51:16 <tZork>	this is the kinda stuff i want to see more. 
    Mar 05 07:51:27 <div0>	but basically, the goal should NOT be stripping the game to "what I like"
    Mar 05 07:51:31 <div0>	and also NOT reimplementing it
    Mar 05 07:51:36 <div0>	but JUST reorganizing the code
    Mar 05 07:51:42 <div0>	not silently removing stuff
    Mar 05 07:51:44 <Doku-Laptop>	that sounds like a good plan
    Mar 05 07:52:02 <div0>	and an idea to actually do that, is to keep the old code in a subdir of a branched revision tree
    Mar 05 07:52:05 <div0>	or even better.
    Mar 05 07:52:13 <div0>	make a server.new and client.new directory
    Mar 05 07:52:16 <div0>	and develop the new stuff there
    Mar 05 07:52:23 <div0>	it shall have the old code in a subdir
    Mar 05 07:52:32 <div0>	and whenever you have implemented something
    Mar 05 07:52:38 <div0>	you delete it from the copy of the old code before committing
    Mar 05 07:52:56 <div0>	so you see how the old code shrinks and shrinks, and the new one grows
    Mar 05 07:53:01 *	Dokujisan has quit (Ping timeout: 364 seconds)
    Mar 05 07:53:02 <Taoki>	What needs to be reogranized though, and why?
    Mar 05 07:53:04 *	You are now known as Dokujisan
    Mar 05 07:53:05 <div0>	when done, the old code will contain a rotten mess with no features
    Mar 05 07:53:10 <div0>	Taoki: just LOOK at teamplay.qc
    Mar 05 07:53:23 <div0>	the worst file of all that we have
    Mar 05 07:53:32 <tZork>	*brrr*
    Mar 05 07:53:47 <div0>	also, stuff that probably can stay as is, is all in common/
    Mar 05 07:53:55 <div0>	client/ is mostly fine, but stuff needs to be moved into proper files
    Mar 05 07:54:05 <div0>	Main.qc is cluttered, sbar.qc and View.qc separation is unclear
    Mar 05 07:54:17 <tZork>	better file separation is needed in many places iirc
    Mar 05 07:54:21 <div0>	right
    Mar 05 07:54:21 <Taoki>	yeah, some of that is true.
    Mar 05 07:54:34 <div0>	in server, a redesign of some code parts probably needs more work than just shiftign around code between files
    Mar 05 07:54:35 <tZork>	and some new subdir perhaps
    Mar 05 07:54:38 <div0>	although this would likely fix client
    Mar 05 07:54:43 <Taoki>	Does it have to be a code remake specifically, or can each part be optimized and rearranged slowly in time?
    Mar 05 07:54:52 <div0>	Taoki: depends :P
    Mar 05 07:55:05 <div0>	code remake with "copying" much old code
    Mar 05 07:55:09 <tZork>	doxy style commentarys for auto documentation will let ppl get into it fast
    Mar 05 07:55:14 <div0>	e.g. many game modes have a somewhat clean implementation that can be taken over as is
    Mar 05 07:55:20 <div0>	unfortunately that does not include CTF
    Mar 05 07:55:48 <div0>	but Domination, Keyhunt, Race, and of course TDM (not really a mode) would most likely work with exactly their current code
    Mar 05 07:55:55 <FruitieX>	14:54:56 <@div0> Main.qc is cluttered, sbar.qc and View.qc separation is unclear
    Mar 05 07:56:00 <FruitieX>	this should be fixed in the panelhud branch
    Mar 05 07:56:04 <div0>	ah, great
    Mar 05 07:56:09 <FruitieX>	even if the idea of the panelhud is not approved
    Mar 05 07:56:18 <div0>	why would it not be :P
    Mar 05 07:56:21 <FruitieX>	we'll see what it turs out to be :P
    Mar 05 07:56:24 <FruitieX>	turns*
    Mar 05 07:56:29 <div0>	if anything, the idea of configuring this in the menu will not be :P
    Mar 05 07:56:39 <div0>	but then you can still have different HUD "skins" as cfg files
    Mar 05 07:56:46 <FruitieX>	it is done in CSQC to 100% right now :P
    Mar 05 07:57:05 <FruitieX>	yep as cfg files sure
    Mar 05 07:57:05 <div0>	tZork: basically, a start would be identifying what is rotten
    Mar 05 07:57:10 <div0>	then making a new clean code base
    Mar 05 07:57:14 <div0>	and then trying to reintegrate all
    Mar 05 07:57:20 <div0>	the new clean code base should focus on DM and TDM
    Mar 05 07:57:41 <div0>	(yes, immediately with TDM support, as that will be important to have other teamplay modes not too complicated)
    Mar 05 07:57:51 <tZork>	div0: ill dig up my l!ft planning, as i started doing just that before i decided to go scratch intsed. if i can find it.
    Mar 05 07:57:55 <FruitieX>	shouldn't it just be some sort of "interface" for game modes
    Mar 05 07:58:01 <FruitieX>	and have each and every gamemode separate in different files
    Mar 05 07:58:05 <div0>	FruitieX: not possible
    Mar 05 07:58:13 <FruitieX>	oh...
    Mar 05 07:58:13 <div0>	many game modes must interact to very specific events
    Mar 05 07:58:15 <div0>	like player dying
    Mar 05 07:58:23 <Taoki>	Btw, rendomly remembered. Has anyone taken a look at the forgotten contributions I linked yesterday (or 2 daysd ago) here?
    Mar 05 07:58:30 <div0>	not yet
    Mar 05 07:58:30 <tZork>	its possible acctualy
    Mar 05 07:58:42 <div0>	tZork: how do you KNOW all the places that need interaction? :P
    Mar 05 07:58:49 <Taoki>	I should probably make a topic with all of them, so they won't be forgotten
    Mar 05 07:58:54 <div0>	Race also needs quite much interaction (but that oen not with dying, but with spawning)
    Mar 05 07:59:04 <tZork>	the problem is it requiers a re-write
    Mar 05 07:59:16 <div0>	rewrite is bad, as it means only 20% will be taken over
    Mar 05 07:59:19 <tZork>	div0: registerd events
    Mar 05 07:59:24 <div0>	but sure
    Mar 05 07:59:30 <div0>	such a thing wouldn't be a rewrite
    Mar 05 07:59:43 <div0>	I expect to be able to use existing game mode code, and add an init function that registers the callbacks as event handlers
    Mar 05 07:59:54 <div0>	THAT is how it should be possible without rewriting all game modes
    Mar 05 08:00:47 <tZork>	mode X registers what events to recive in some form of initialazation, each event handler has slots, or chains so mutators are effectuvly just non exclusive modes.
    Mar 05 08:00:53 <div0>	basically, I want restructure, not rewrite
    Mar 05 08:01:04 <tZork>	thats roughtly teh idea i had for lift anyway
    Mar 05 08:01:08 <div0>	most existing "feature specific" code should work as is
    Mar 05 08:01:15 <div0>	except for an init function registering handlers
    Mar 05 08:01:24 <div0>	but the generic code base of course need schanging
    Mar 05 08:01:34 <div0>	probably entirely rewriting
    Mar 05 08:02:04 <div0>	also, quite some subsystems probably should stay as is
    Mar 05 08:02:09 <div0>	e.g. waypointsprites and scores subsystem
    Mar 05 08:02:18 <tZork>	also having to stir things up forces a audir of parts one normaly just shun away from. witch is healty.
    Mar 05 08:02:21 <div0>	of course, both are self-contained .qc files already :P
    Mar 05 08:02:30 <div0>	sure
    Mar 05 08:02:43 <div0>	well, MOSTLY self-contained - they use some common "miscfunctions" :P
    Mar 05 08:02:47 <div0>	but otherwise self-contained
    Mar 05 08:02:59 <div0>	such stuff most likely can stay as is, as it does not harm anything or influence anything's structure
    Mar 05 08:03:05 <tZork>	right
    Mar 05 08:03:29 <div0>	what NEEDS cleanup, is teamplay.qc, player death handling, player spawn handling, player think
    Mar 05 08:03:31 <tZork>	no point in rewriting just for teh sake of it.
    Mar 05 08:03:36 <div0>	sure
    Mar 05 08:03:42 <div0>	I just say... try to use existing code if you can
    Mar 05 08:03:50 <div0>	way less debugging work, and better result
    Mar 05 08:04:04 <tZork>	absolutly. 
    Mar 05 08:04:08 <div0>	try not to rewrite feature specific code unless it goes deep into internals
    Mar 05 08:04:11 <div0>	(like ready-restart does)
    Mar 05 08:04:32 <div0>	also one of the messy parts BTW :P
    Mar 05 08:04:48 <div0>	item handling may also need to be improved, althoguh it is mostly good
    Mar 05 08:04:56 <div0>	probably it can stay as is, but needs to be divided up into files
    Mar 05 08:05:19 <div0>	as for the weaponsystem... VERY hard to get THAT right :P
    Mar 05 08:06:04 <tZork>	one thing we have to address asap is how we want to time this. if we want to jank as much as possible of the nexuiz community, we have to be reeeal fast with a release. 
    Mar 05 08:06:20 *	[-z-] gives channel operator status to Dokujisan Morphed Spaceman
    Mar 05 08:06:22 *	[-z-] gives channel operator status to Taoki
    Mar 05 08:06:38 <Taoki>	I agree with more frequent releases
    Mar 05 08:06:57 <[-z-]>	btw, men h8 mike now
    Mar 05 08:06:59 <tZork>	that also influense the under-the-hood dev plan
    Mar 05 08:07:18 <[-z-]>	my /\ /\nd $ key$ /\re bre/\king
    Mar 05 08:08:53 <FruitieX>	1337
    Mar 05 08:09:09 <[-z-]>	not re4lly :(
    Mar 05 08:09:14 <[-z-]>	quite 4nnoying
    Mar 05 08:09:23 <FruitieX>	agree with more frequent releases... we shouldn't need to care THAT much about if the release is stable or not
    Mar 05 08:09:35 <FruitieX>	as we could just patch that up quickly
    Mar 05 08:09:52 <Dokujisan>	we can also organize more people to get involved in a proper testing / feedback loop
    Mar 05 08:10:18 <tZork>	problem: engine bugs. afaik dp has no viable method of self-upgrade
    Mar 05 08:10:33 <Dokujisan>	I would like to have some open dialog with all of the main server admins
    Mar 05 08:10:58 <FruitieX>	BTW :P
    Mar 05 08:11:18 <FruitieX>	next release should be incompatible to old nexuiz releases
    Mar 05 08:11:28 <Taoki>	Hmm, what does everyone think about an auto-update system? One that would popup a menu window saying "update available" when you open Nexuiz while connected to the internet? And that could download everything internally... or if not close Nexuiz and take you to the download page
    Mar 05 08:11:29 <Dokujisan>	so just to be clear, we're forking the nexuiz code and we're NOT forking darkplaces into a new engine, right?
    Mar 05 08:11:31 <FruitieX>	we need to get enough server admins to host servers for that new version...
    Mar 05 08:11:32 <Taoki>	But configurable
    Mar 05 08:11:44 <FruitieX>	and leave the old 2.4.2 minsta servers to rot
    Mar 05 08:11:49 <tZork>	engine bugs issue is the only real reason i for large upgrtades ratehr then frequent.
    Mar 05 08:11:57 <tZork>	i see for*
    Mar 05 08:12:22 <FruitieX>	Dokujisan: right
    Mar 05 08:12:25 <FruitieX>	at least i hope so
    Mar 05 08:12:43 <tZork>	not atm at least. 
    Mar 05 08:13:05 <Dokujisan>	I understand that decision. but it is a disadvantage, right?
    Mar 05 08:13:21 <tZork>	hwo so?
    Mar 05 08:13:23 <Dokujisan>	I mean under "alientrap" we had access to making changes to darkplaces
    Mar 05 08:13:29 <Dokujisan>	are we losing that?
    Mar 05 08:13:42 <tZork>	i dont see why - div0
    Mar 05 08:13:47 <FruitieX>	Samual
    Mar 05 08:13:52 <Dokujisan>	FruitieX: 
    Mar 05 08:13:54 <Dokujisan>	heh
    Mar 05 08:13:56 <FruitieX>	nope
    Mar 05 08:14:02 <FruitieX>	i never had access there :)
    Mar 05 08:14:03 <div0>	anyway, as for rerwrite... shpuld be no goal for next release
    Mar 05 08:14:10 <tZork>	's got repos access and i see no reason for LH ro refuse sane patches / requests
    Mar 05 08:14:13 <FruitieX>	agree with div0 
    Mar 05 08:14:18 <div0>	but kept in mind when making new stuff
    Mar 05 08:14:26 <FruitieX>	we are already so late with our "hotfix"
    Mar 05 08:14:54 <tZork>	haha
    Mar 05 08:15:01 <FruitieX>	right :p
    Mar 05 08:16:13 <tZork>	its friggin hursefix by now xD
    Mar 05 08:16:20 <Dokujisan>	ok I'm skimming through our discussion about which maps to consider as official maps and which maps need cleanup
    Mar 05 08:17:31 <tZork>	@ media i find the size of the current texture pool problematic. theres to much shit.
    Mar 05 08:17:45 <tZork>	and suplicates
    Mar 05 08:17:46 <Taoki>	I was thinking about that. I seen many maps and thought to myself they would be great in SVN
    Mar 05 08:17:57 <tZork>	duplicates*
    Mar 05 08:18:34 <tZork>	otoh removing mean breaking some nex maps. tougth call.
    Mar 05 08:18:35 <Taoki>	Maps I'd like to see removed... only one I know for sure I would is EggAndBacon. I don't hate it, but it's just a big box with several weapons thrown around imo.
    Mar 05 08:19:05 <FruitieX>	tZork: thats what div0 said, remove the evil* packs
    Mar 05 08:19:11 <Spaceman>	I like egg and bacon because of all the weapons
    Mar 05 08:19:19 <Taoki>	Something recent for adding (just updated it myself and posted the update yesterday) is http://www.alientrap.org/forum/viewtopic.php?f=19&t=4945&p=76305#p76305 when vehicvles would be stable. Beautiful map by Sven
    Mar 05 08:19:22 <Spaceman>	and that bots can capture the flag
    Mar 05 08:19:53 <tZork>	official map pool can be super limited imo. noone oterh then the occasional review or sutch will use just it.
    Mar 05 08:20:20 <FruitieX>	Yes
    Mar 05 08:20:28 <FruitieX>	should only consist of really high quality maps
    Mar 05 08:20:29 <Dokujisan>	ok in the log file mentioned in the subject, go to Mar 04 03:36:55
    Mar 05 08:20:30 <tZork>	use  only it i mean
    Mar 05 08:20:36 <Dokujisan>	that is where the map discussion starts
    Mar 05 08:20:41 <div0>	as for maps to keep for a start: aggressor, stormkeep2, e&b
    Mar 05 08:20:55 <div0>	e&b uses an evil texture, but that can be changed :P
    Mar 05 08:21:15 <Taoki>	Would it be illegal to include some wuake converted maps? Some (like kzlegypt, pukka3 / fascinating senseleness) are very good
    Mar 05 08:21:17 <tZork>	reroute textures with shaders is also possible
    Mar 05 08:21:17 <div0>	oh, and that factory map
    Mar 05 08:21:18 <Taoki>	*quake
    Mar 05 08:21:20 <div0>	although just DM
    Mar 05 08:21:20 <Dokujisan>	can we at least give e&b a makeover?
    Mar 05 08:21:21 <div0>	Taoki: yes
    Mar 05 08:21:27 <div0>	Dokujisan: how would you make a makeover on it?
    Mar 05 08:21:29 <Taoki>	oh :(
    Mar 05 08:21:32 <Dokujisan>	make it look interesting... like stormkeep2
    Mar 05 08:21:32 <div0>	I doubt it CAN be done
    Mar 05 08:21:33 <FruitieX>	ah, desertfactory
    Mar 05 08:21:36 <div0>	oh, sure
    Mar 05 08:21:37 <FruitieX>	absolutely keep that one
    Mar 05 08:21:39 <div0>	look I don't care for :P
    Mar 05 08:21:44 <div0>	gameplay, should stay
    Mar 05 08:21:47 <Dokujisan>	the stormkeep2 makeover was just awesome
    Mar 05 08:21:50 <div0>	sure
    Mar 05 08:21:50 <Dokujisan>	imo
    Mar 05 08:21:57 <FruitieX>	even more so with warpzones
    Mar 05 08:21:59 <div0>	also, I'd insist a bit on the wall texture :P
    Mar 05 08:21:59 <FruitieX>	hint hint :)
    Mar 05 08:22:08 <div0>	hehe, idea for e&b: two floor warpzones
    Mar 05 08:22:12 <FruitieX>	oh on stormkeep?
    Mar 05 08:22:14 <div0>	so you jump in, come out of the other hole :P
    Mar 05 08:22:46 <div0>	e&b should retain the wall texture feel (like swimming pool or bathroom walls, sort of)
    Mar 05 08:22:59 <tZork>	soylent maybe
    Mar 05 08:22:59 <div0>	and the obstacle pattern, and that the flags are on a higher ledge
    Mar 05 08:23:05 <div0>	visually, however, doesn't matter much
    Mar 05 08:23:11 <FruitieX>	we should ask sev about cleftvillage
    Mar 05 08:23:12 <div0>	just make it not look generic industrial :P
    Mar 05 08:23:17 <FruitieX>	if anyone remembers
    Mar 05 08:23:22 <div0>	the swimming pool/bathroom look is good
    Mar 05 08:23:25 <FruitieX>	outdoor map
    Mar 05 08:23:28 <tZork>	cleftvillage? ARE YOU SERIOUS?
    Mar 05 08:23:30 <FruitieX>	with sharks in water :P
    Mar 05 08:23:33 <div0>	gameplay wise, bad
    Mar 05 08:23:35 <div0>	look wise, great
    Mar 05 08:23:43 <Taoki>	I'd also make the teleporter doors in Aggressor warpzones :P
    Mar 05 08:23:49 <div0>	cleftvillage is an attempt to clone CTF-LavaGiant a bit
    Mar 05 08:23:51 <div0>	but fails :P
    Mar 05 08:23:56 <div0>	Taoki: please not :P
    Mar 05 08:23:58 <FruitieX>	Taoki: not rly, that's bad
    Mar 05 08:24:01 <div0>	that would be a brain twister
    Mar 05 08:24:01 <FruitieX>	aggressor is too small
    Mar 05 08:24:04 <div0>	do it for a fun map though :P
    Mar 05 08:24:05 <Taoki>	The only issue I find major about warpzones is that they require water rreflections to display.
    Mar 05 08:24:07 <FruitieX>	yep that too haha
    Mar 05 08:24:10 <FruitieX>	fun map indeed
    Mar 05 08:24:17 <div0>	Taoki: sure, simply because they ARE that
    Mar 05 08:24:23 <div0>	you can force it on in mapinfo though
    Mar 05 08:24:36 <Taoki>	Ah, I thought that's temporary. I see
    Mar 05 08:24:42 <Taoki>	Thought they should display either way
    Mar 05 08:24:45 <div0>	well, until a better way is found :P
    Mar 05 08:24:47 <div0>	well
    Mar 05 08:24:49 <tZork>	but are reflections safe on all target hardware?
    Mar 05 08:24:52 <div0>	the reason to not do that, is performance
    Mar 05 08:24:57 <div0>	tZork: no, require glsl
    Mar 05 08:25:00 <div0>	so do warpzones
    Mar 05 08:25:02 <FruitieX>	what about eg. egyptronex
    Mar 05 08:25:09 <div0>	but, mesa software rendering got glsl :P
    Mar 05 08:25:20 <FruitieX>	and clueless newbie's facing worlds
    Mar 05 08:25:21 <div0>	so, warpzones are NOT safe on all plats
    Mar 05 08:25:28 <div0>	so warpzones should have teleport texture behind them
    Mar 05 08:25:30 <Taoki>	Anyway bbl here
    Mar 05 08:25:32 <tZork>	good thing so many gamers use mesa soft thenm eh? xD
    Mar 05 08:25:32 <div0>	to not confuse players too much
    Mar 05 08:25:35 <div0>	tZork: hehe
    Mar 05 08:25:57 <tZork>	the kidna cpu power needed.. i want it.
    Mar 05 08:25:58 <tZork>	:D
    Mar 05 08:26:33 <Dokujisan>	can we consider a soylent_ctf after some tweaks and testing are done?
    Mar 05 08:26:57 <FruitieX>	BTW
    Mar 05 08:27:01 <FruitieX>	what about gasolinepowered?
    Mar 05 08:27:17 <Dokujisan>	I think aggressor_ctf also has some potential but needs to improve the middle area
    Mar 05 08:27:17 <tZork>	you know id be happy with something like 1 or two maps for each major mode (but 1 or two maps MADE for taht mode)
    Mar 05 08:27:48 <Dokujisan>	FruitieX: yes gasolinepowered is one that we all thought needed to ge tin
    Mar 05 08:27:49 <Dokujisan>	get in
    Mar 05 08:27:50 <FruitieX>	runningman/runningmanctf need a retexture IMO
    Mar 05 08:27:59 <Dokujisan>	good call
    Mar 05 08:28:38 <tZork>	the plethora of nexuiz maps shows that the community makes what it wants. i see no reason to maintain a large map-pool in the main release.
    Mar 05 08:28:46 <FruitieX>	am putting a list together
    Mar 05 08:28:54 <Dokujisan>	that's what I'm doing :-P
    Mar 05 08:29:08 <Dokujisan>	along with the other bullet points from these chats
    Mar 05 08:29:41 <[-z-]>	brb, going to try going to gnome
    Mar 05 08:29:53 *	[-z-] has quit (Remote host closed the connection)
    Mar 05 08:30:27 <Dokujisan>	what do we think about treasureisland? I liked the initial one and people love the way it looks. The newer one is a bit strange in gameplay
    Mar 05 08:30:39 <Dokujisan>	it looks great, but needs adjustments, I think
    Mar 05 08:30:46 <tZork>	player models are a preddy urgent tough. if we could make release 1 with even just two good quality models and dump that crap, we definitly would bring soemthing quite real to the table
    Mar 05 08:30:49 *	[-z-] (~detrate@c-98-230-24-23.hsd1.fl.comcast.net) has joined #notnexuiz
    Mar 05 08:31:51 <Dokujisan>	tZork: are there any existing in-progress or dropped player models that people were working on?
    Mar 05 08:31:58 <Dokujisan>	that would be a good candidate
    Mar 05 08:32:07 <FruitieX>	15:29:47 <@Dokujisan> that's what I'm doing :-P
    Mar 05 08:32:09 <FruitieX>	ah darnit :P
    Mar 05 08:32:14 <FruitieX>	currently i got:
    Mar 05 08:32:17 <tZork>	http://www.alientrap.org/forum/viewtopic.php?f=2&t=6051
    Mar 05 08:32:18 <Dokujisan>	or... do we know exactly who can work on a models
    Mar 05 08:32:28 <tZork>	http://www.alientrap.org/forum/viewtopic.php?f=2&t=5997
    Mar 05 08:32:32 <Dokujisan>	FruitieX: PM me your list
    Mar 05 08:33:48 <tZork>	Dokujisan: Oblivion, Morphed, DibTop and me all knows a bit abt assorted sobjects arround it.
    Mar 05 08:34:10 <tZork>	i managed to export animated smd's from blender yesterday
    Mar 05 08:34:22 <tZork>	and turn to dpm
    Mar 05 08:34:23 <Dokujisan>	yeah technical details around player models seem to always been a big problem for nexuiz.
    Mar 05 08:34:27 <Dokujisan>	mainly with animation
    Mar 05 08:34:44 <Dokujisan>	and I understand issues with exporting to md3 or whatever nexuiz needs
    Mar 05 08:34:55 <[-z-]>	on a PS2 keyboard so I can use my A and S keys :roll:
    Mar 05 08:35:20 <[-z-]>	couldn't even dettach a screen without them
    Mar 05 08:35:34 <tZork>	Dokujisan: yes the artist toolchain of darkpalces is bad
    Mar 05 08:35:43 <FruitieX>	tZork: holy crap that model looks ace
    Mar 05 08:35:45 <Dokujisan>	tZork: perhaps we need to generate some documentation on "what we know" about player model technical details
    Mar 05 08:36:07 <Spaceman>	I second that idea
    Mar 05 08:36:13 <tZork>	but with the blender smd thing working, its way more likely ppl can do open models.
    Mar 05 08:36:22 <[-z-]>	have we come up with a name yet?
    Mar 05 08:36:40 <Dokujisan>	[-z-]: we're covering other details at the moment. I think name decision comes last or later
    Mar 05 08:36:47 <Dokujisan>	we should take time with that 
    Mar 05 08:36:59 <tZork>	zpankiuz
    Mar 05 08:37:05 <tZork>	;)
    Mar 05 08:37:09 <Dokujisan>	I'm creating a page to overview the details of our discussions
    Mar 05 08:37:30 <[-z-]>	oky, well I'll work on getting the site ready with a fake name
    Mar 05 08:38:28 <FruitieX>	http://www.alientrap.org/forum/viewtopic.php?f=2&t=5998
    Mar 05 08:38:30 <FruitieX>	hell yes
    Mar 05 08:38:53 <Dokujisan>	ok new menu skin
    Mar 05 08:38:54 <Dokujisan>	good call
    Mar 05 08:39:09 <[-z-]>	as long as it gets finished :)
    Mar 05 08:39:20 <[-z-]>	I'm assuming we can get the source files from sev on this?
    Mar 05 08:39:25 <[-z-]>	I can remix it for the website design
    Mar 05 08:39:43 <FruitieX>	someone should learn how to do fonts and do something close to this: http://pics.nexuizninjaz.com/images/jom5sjku3jvcj7r5ezs.jpg
    Mar 05 08:39:46 <FruitieX>	and of course gpl it :P
    Mar 05 08:39:55 <Dokujisan>	what about stone_castle
    Mar 05 08:40:01 <Dokujisan>	it's much improved over dm_castle
    Mar 05 08:40:03 <FruitieX>	screenshot?
    Mar 05 08:40:04 <FruitieX>	oh
    Mar 05 08:40:04 <[-z-]>	I like stone castle
    Mar 05 08:40:11 <FruitieX>	don't think i've seen it
    Mar 05 08:40:43 <Dokujisan>	http://www.alientrap.org/forum/viewtopic.php?f=19&t=5890
    Mar 05 08:40:58 <Dokujisan>	unfortunately his screenshots are at 150 fov or something crazy
    Mar 05 08:42:20 <Dokujisan>	can you guys help me think of names of all of the decent mappers in nexiuz?
    Mar 05 08:43:37 <[-z-]>	mookow, FruitieX, dublpaws, sev
    Mar 05 08:43:43 <FruitieX>	http://pics.nexuizninjaz.com/images/8vettzmezq8nyp7csw5.jpg
    Mar 05 08:43:48 <FruitieX>	EVIL TEXTURES!!11
    Mar 05 08:43:49 <FruitieX>	:P
    Mar 05 08:43:58 <FruitieX>	or wait...
    Mar 05 08:44:00 <FruitieX>	not at all
    Mar 05 08:44:10 <FruitieX>	still, part of the "low quality packs" i guess
    Mar 05 08:44:18 <[-z-]>	much better flow & he didn't remove the secret jumppads
    Mar 05 08:44:35 <Dokujisan>	Mappers
    Mar 05 08:44:35 <Dokujisan>		FruitieX
    Mar 05 08:44:35 <Dokujisan>		cortez666
    Mar 05 08:44:35 <Dokujisan>		Grasshopper
    Mar 05 08:44:35 <Dokujisan>		Mookow
    Mar 05 08:44:35 <Dokujisan>		Unknown/alphagod
    Mar 05 08:44:35 <Dokujisan>		sev
    Mar 05 08:44:35 <Dokujisan>		dublpaws
    Mar 05 08:44:35 <Dokujisan>		Strahleman
    Mar 05 08:44:35 <Dokujisan>		Diabolik
    Mar 05 08:44:35 <Dokujisan>		djsupport
    Mar 05 08:44:35 <Dokujisan>		lda17h
    Mar 05 08:44:36 <[-z-]>	he added jumppads too
    Mar 05 08:44:48 <FruitieX>	cool
    Mar 05 08:44:58 <Dokujisan>	oh... I thought of a couple more
    Mar 05 08:45:02 <Dokujisan>	cubeowl
    Mar 05 08:45:03 <[-z-]>	fbzor
    Mar 05 08:45:18 <tZork>	!define decent mapper
    Mar 05 08:45:23 <Dokujisan>	your definition
    Mar 05 08:45:24 <[-z-]>	with some guidance, fabzor can produce awesome maps
    Mar 05 08:45:59 <Dokujisan>	yeah I would love to group together mappers and have more interactive dialog about map projects, like I've been doing with the NCT group
    Mar 05 08:46:20 <Dokujisan>	some of the maps in nexuiz are really close to being great, but need adjustments
    Mar 05 08:46:30 <FruitieX>	btw, should we use div0's "strafebot proof" physics set? :)
    Mar 05 08:46:38 <FruitieX>	me likes it somewhat
    Mar 05 08:46:38 <tZork>	dont know Dokujisan, havent kept up 2 date to good. just trying to iluminate theres many things that one can put into that term.
    Mar 05 08:46:48 <FruitieX>	it'd be really easy for newbies
    Mar 05 08:46:52 <Dokujisan>	tZork: you do makes too right?
    Mar 05 08:47:03 <tZork>	uum yes..
    Mar 05 08:47:09 <tZork>	or did
    Mar 05 08:47:10 <Dokujisan>	does clueless newbie make maps?
    Mar 05 08:47:18 <tZork>	>.o
    Mar 05 08:47:26 <tZork>	yep
    Mar 05 08:47:39 <Dokujisan>	sepelio
    Mar 05 08:48:20 <tZork>	i used to map more (the first ctf map in nexuiz was acctualy mine, got removed later tnk god)
    Mar 05 08:49:14 <Dokujisan>	has everyone seen this? This is the sort of thing I want to create for mappers to work from (especially new mappers)
    Mar 05 08:49:16 <Dokujisan>	http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 05 08:49:37 <Dokujisan>	just some ideas for improving or converting maps
    Mar 05 08:49:42 <FruitieX>	div0: don't agree with your latest change in the physics set :P
    Mar 05 08:49:54 <tZork>	cool stuff DibTop
    Mar 05 08:49:57 <tZork>	err Dokujisan
    Mar 05 08:50:01 <FruitieX>	sv_airaccel_sideways_friction -0.3 => 1
    Mar 05 08:50:05 <FruitieX>	instead you should set it at -1 :P
    Mar 05 08:50:12 <tZork>	Heavy would acctualy be a preddy good official map
    Mar 05 08:50:24 <Dokujisan>	this has been very productive among a small group of mappers. If this is done on a larger scale with ALL nexuiz mappers, we could get a lot done
    Mar 05 08:50:35 <FruitieX>	this way i think both nexuiz players and quakers will feel more at home
    Mar 05 08:50:54 <Dokujisan>	even better if -z- could create a little app that allows us to edit these entries easier (I'm doing the HTML by hand at the moment)
    Mar 05 08:51:15 <[-z-]>	which entrie?
    Mar 05 08:51:22 <Dokujisan>	and of course this would be on the official website, not on my personal site
    Mar 05 08:51:29 *	Taoki has quit ("KVIrc Insomnia 4.0.0, revision: 3830, sources date: 20091222, built on: 2010-01-10 23:31:04 UTC http://www.kvirc.net/")
    Mar 05 08:51:32 <Dokujisan>	http://www.nullgaming.com/nexuiz/projects/maps/
    Mar 05 08:51:38 <tZork>	wow by hand? your like a webdesign caveman then Dokujisan ;) mee too, usualy.
    Mar 05 08:51:50 <Dokujisan>	doing a small webapp to handle that -z-
    Mar 05 08:52:00 <[-z-]>	Dokujisan: I'll ee wht I cn whip up tht up
    Mar 05 08:52:06 <[-z-]>	fdjipljkcvzxjklkljd ukeybord
    Mar 05 08:52:07 <Dokujisan>	well I don't mind editing that page. it was simple. but I'd like others to have editing ability
    Mar 05 08:52:16 <tZork>	yar
    Mar 05 08:52:36 *	Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 05 08:52:42 <[-z-]>	Dokujisan: well I'll ee wht I can do about getting some web stuff setup at nexiuz.org from work
    Mar 05 08:52:46 <Dokujisan>	[-z-]: I created some simple classes for different statuses
    Mar 05 08:52:49 <[-z-]>	if it's a slow day
    Mar 05 08:53:15 <Dokujisan>	[-z-]: but we could rethink those classes. I made them up quickly
    Mar 05 08:53:50 <[-z-]>	hey, there i  better remke of bonuchecker tht grhopper mde
    Mar 05 08:53:55 <Taoki>	Ooh... zeonix.com is not taken (another idea for a name)
    Mar 05 08:54:01 <Dokujisan>	yeah I haven't updated that page in a month or so
    Mar 05 08:54:07 <[-z-]>	zeonix sounds cool
    Mar 05 08:54:13 <tZork>	irena, that muse be irena_ctf. the one i made just called iRena it non ctf
    Mar 05 08:54:15 <FruitieX>	15:52:53 < [-z-]> Dokujisan: I'll ee wht I cn whip up tht up
    Mar 05 08:54:15 <FruitieX>	15:52:59 < [-z-]> fdjipljkcvzxjklkljd ukeybord
    Mar 05 08:54:16 <[-z-]>	okay, I put the PS2 keyboard in the other keyboard's place
    Mar 05 08:54:18 <FruitieX>	rofl
    Mar 05 08:54:25 <Taoki>	it came to mind with the Pheonix suggestion
    Mar 05 08:54:25 <[-z-]>	a and s keys dying FruitieX
    Mar 05 08:54:28 <Taoki>	Would be nice
    Mar 05 08:54:30 <[-z-]>	too much gaming on that keyboard
    Mar 05 08:54:31 <FruitieX>	yeah i see
    Mar 05 08:54:33 <FruitieX>	oh lol
    Mar 05 08:54:33 <Dokujisan>	Taoki: added to the list
    Mar 05 08:54:44 <Dokujisan>	Zeonix isn't a bad one at all
    Mar 05 08:54:50 <Dokujisan>	shortened to Zeon
    Mar 05 08:54:55 <Dokujisan>	like we shorten to "Nex"
    Mar 05 08:55:03 <Taoki>	yeah
    Mar 05 08:55:43 <Dokujisan>	ok who are the developers?
    Mar 05 08:55:50 <Dokujisan>	game code 
    Mar 05 08:56:03 <Dokujisan>	div0, tZork, mandinga, diabolik, 
    Mar 05 08:56:06 <Dokujisan>	fruitieX
    Mar 05 08:56:10 <[-z-]>	I believe samual is in
    Mar 05 08:56:12 <[-z-]>	and taoki?
    Mar 05 08:56:15 <FruitieX>	div0: I would also vote for sv_maxspeed 320 and sv_maxairspeed 320
    Mar 05 08:56:32 <Taoki>	I make patches pretty often... I kinda consider myself a half-developer :P
    Mar 05 08:56:37 <Dokujisan>	FruitieX: noted
    Mar 05 08:56:56 <tZork>	what does that do in gameplay terms FruitieX?
    Mar 05 08:57:04 <FruitieX>	so to sum it all up: current physicsNoQWBunny.cfg + sv_airaccel_sideways_friction -1 + sv_maxspeed 320 + sv_maxairspeed 320
    Mar 05 08:57:29 <FruitieX>	tZork: that is a slightly different physics config that div0 has been working on
    Mar 05 08:57:33 <Dokujisan>	blub is a developer, right?
    Mar 05 08:57:36 <Dokujisan>	CSQC guy
    Mar 05 08:57:47 <Dokujisan>	is green marine?
    Mar 05 08:57:54 <FruitieX>	Dokujisan: note that "sum it all up" line ^
    Mar 05 08:58:00 <Dokujisan>	noted
    Mar 05 08:58:29 <FruitieX>	tZork: try it, it feels like a fuse of nexuiz and CPM a bit
    Mar 05 08:58:36 <Dokujisan>	ok who else besides -z- is a web developer?
    Mar 05 08:58:38 <tZork>	Dokujisan: Spaceman, lda17h, FruitieX
    Mar 05 08:58:52 <Dokujisan>	tZork: for web dev?
    Mar 05 08:58:56 <Dokujisan>	oh does spaceman do maps?
    Mar 05 08:59:02 <FruitieX>	for a nexuiz player it should feel pretty much the same
    Mar 05 08:59:04 <tZork>	FruitieX: CPM? Is that liek  C perl module? :P
    Mar 05 08:59:05 *	[-z-] has quit (Ping timeout: 120 seconds)
    Mar 05 08:59:06 <Spaceman>	no, I don't do maps
    Mar 05 08:59:16 <tZork>	Dokujisan: tought you where asking for gamecode devs
    Mar 05 08:59:19 <Spaceman>	I've fixed a few map bugs
    Mar 05 08:59:51 <Dokujisan>	ok so  lda17h does game coding too?
    Mar 05 09:00:19 <Dokujisan>	and what of green marine?
    Mar 05 09:00:44 <tZork>	FruitieX: i know its some special phys config for ..q3? but tahts abt all. so i havent a clue what a merge of it and nexuiz would be.
    Mar 05 09:01:55 <tZork>	Dokujisan: iirc yes, think he made some dodge patch for nexuiz wich looked decent but got lost in the goo
    Mar 05 09:02:04 <Taoki>	Just so I know. Is it alright to talk about the decision to rename Nexuiz outside of this channel yet?
    Mar 05 09:02:17 <tZork>	no
    Mar 05 09:02:25 <tZork>	not in public, imo
    Mar 05 09:02:26 <Dokujisan>	Taoki: no
    Mar 05 09:02:28 <FruitieX>	Dokujisan: more physics stuff to note that's really fun: sv_doublejump 1, sv_jump_speedcap_max 1, sv_jumpspeedcap_max_disable_on_ramps 1
    Mar 05 09:02:30 <Taoki>	ok
    Mar 05 09:02:41 <tZork>	just my opinion tough
    Mar 05 09:02:48 <Dokujisan>	we shouldn't make any of these discussions known outside....except I'm chatting with the aussienexers
    Mar 05 09:02:51 <Dokujisan>	keeping them informed
    Mar 05 09:02:55 <Dokujisan>	certain key people
    Mar 05 09:03:02 <Dokujisan>	and they know not to discuss it publicly too
    Mar 05 09:03:14 <FruitieX>	ok good
    Mar 05 09:05:22 *	Dokujisan has changed the topic to: Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt
    Mar 05 09:05:43 <Dokujisan>	review that, if you would
    Mar 05 09:05:49 <SoulKeeper_p>	<Dokujisan> ok who else besides -z- is a web developer?
    Mar 05 09:05:50 <Dokujisan>	help me fill in the empty spots
    Mar 05 09:05:52 <SoulKeeper_p>	Dokujisan, +1
    Mar 05 09:05:58 <Dokujisan>	you?
    Mar 05 09:07:50 <SoulKeeper_p>	Dokujisan, yes
    Mar 05 09:07:57 <Dokujisan>	k
    Mar 05 09:08:17 <Dokujisan>	ok I added the aussie people now to the ROLES list
    Mar 05 09:10:25 <SoulKeeper_p>	well till when it started to overcrowd and everyone was all sudden a webdev ;)
    Mar 05 09:10:41 <Dokujisan>	I can manage the people. I just need to know who does what
    Mar 05 09:10:50 <Dokujisan>	-z- will likely be the head web dev
    Mar 05 09:10:58 <SoulKeeper_p>	i worked as webdesigner/developer/php coder in past, tho try to avoid those...
    Mar 05 09:11:04 <Dokujisan>	ok
    Mar 05 09:11:10 <Dokujisan>	I'll keep you off that list then :-)
    Mar 05 09:11:16 <SoulKeeper_p>	yea }-z-{ does gooed job imho
    Mar 05 09:11:27 <Dokujisan>	I agree
    Mar 05 09:11:33 <SoulKeeper_p>	Dokujisan, sure i help out np.
    Mar 05 09:13:04 <div0>	FruitieX: please PM me trhat physics info
    Mar 05 09:13:31 <Dokujisan>	ok what about server admins?
    Mar 05 09:13:32 <div0>	[14:50:50] <@FruitieX> sv_airaccel_sideways_friction -0.3 => 1
    Mar 05 09:13:33 <div0>	[14:50:54] <@FruitieX> instead you should set it at -1 :P
    Mar 05 09:13:38 <div0>	why? it gives more control
    Mar 05 09:13:42 <div0>	but I am undecided about it :P
    Mar 05 09:13:51 <tZork>	you could basicaly put me in all fields as i have a bit of professional experiance in all of them :P but i prefer just game devel and maybe models/maps for now.
    Mar 05 09:13:54 <div0>	I just don't like that turning gives no penalty
    Mar 05 09:14:02 <div0>	when turning slowly
    Mar 05 09:14:04 <tZork>	@ Dokujisan
    Mar 05 09:14:05 <div0>	you still accelerate
    Mar 05 09:14:05 <Dokujisan>	ok tZork 
    Mar 05 09:14:12 <div0>	ideal would be if turning does not accelerate :P
    Mar 05 09:14:22 <div0>	but I do not want too much deceleration either
    Mar 05 09:14:35 <div0>	I will probably change the sidefric code to limit to the previous speed before the move
    Mar 05 09:14:42 <div0>	and not to the current speed when applying sidefric
    Mar 05 09:14:57 <div0>	so when turning using CPMA air control, your speed would stay as is (but not increase)
    Mar 05 09:14:59 <div0>	that was my goal
    Mar 05 09:15:24 <div0>	but well, it may need slight code changes :P
    Mar 05 09:17:06 <Dokujisan>	ok, I need a list of the Nexuiz Server Admins
    Mar 05 09:17:17 <div0>	FruitieX: acgtually...
    Mar 05 09:17:20 <FruitieX>	Hmm
    Mar 05 09:17:23 <div0>	from the code, sidefric -1 SHOULD do what I want
    Mar 05 09:17:26 <div0>	maybe it is buggy :P
    Mar 05 09:17:30 <FruitieX>	:P
    Mar 05 09:17:36 <div0>	-1 allows deceleration, but only as much as the backwards key would do
    Mar 05 09:17:40 <div0>	this is actually what I want :P
    Mar 05 09:17:54 <div0>	maybe need to try -9999 ;)
    Mar 05 09:18:04 <div0>	will check that out later
    Mar 05 09:18:07 <div0>	please PM it to me
    Mar 05 09:18:14 <div0>	I wish I could self-PM to make "reminders":P
    Mar 05 09:18:49 <div0>	so yes, if -1 does what I wanted it to do in the code ;) then it is exactly what there should be
    Mar 05 09:19:17 <FruitieX>	heh
    Mar 05 09:20:01 <div0>	basically what the - should do, is "never decelerate more than the backward key could do"
    Mar 05 09:20:06 <div0>	to prevent illogical physics
    Mar 05 09:20:20 <tZork>	/msg yournick blah dont work?
    Mar 05 09:20:30 <tZork>	tahts what i usualy do =)
    Mar 05 09:20:34 <}-z-{>	I would like to share responsbility with Dokujisan and perhaps another person
    Mar 05 09:20:38 <Spaceman>	Dokujisan: cubeowl, esteel run DCC; merlijn runs Simba
    Mar 05 09:20:41 <}-z-{>	but if possible I would like to do the inital setup
    Mar 05 09:20:47 <}-z-{>	cocerning web for this project
    Mar 05 09:20:59 <div0>	tZork: opens a query window :P
    Mar 05 09:21:39 <}-z-{>	I just don't want to be a single point of failure at any point :-P
    Mar 05 09:21:44 <div0>	sure :P
    Mar 05 09:21:59 <}-z-{>	I like the arangement I ad as admin with willis in a way, I would like to keep something like that going
    Mar 05 09:21:59 <Dokujisan>	ok what about SysAdmins? I know that's overlap with web dev and Nexuiz admins, but I'd like a separate list
    Mar 05 09:22:08 <div0>	I would be one, but not the only one
    Mar 05 09:22:11 <}-z-{>	and by the way, it sounded like willis is with us on this
    Mar 05 09:22:14 <tZork>	}-z-{ for Community/Project Organization?
    Mar 05 09:22:21 <div0>	and yes, Willis as sysadmin is good
    Mar 05 09:22:22 <}-z-{>	tZork: ?
    Mar 05 09:22:34 <tZork>	<}-z-{> I would like to share responsbility with Dokujisan and perhaps another person
    Mar 05 09:22:38 <div0>	maybe FruitieX too
    Mar 05 09:22:52 <}-z-{>	ah, tZork for web
    Mar 05 09:22:53 <div0>	just... community/project organization shoudl not mean "global head of all" :P
    Mar 05 09:23:05 <}-z-{>	running the websites, development websites and other web kind of projects
    Mar 05 09:23:10 <div0>	but rather PR, community websites, also autromatically head moderators, etc.
    Mar 05 09:23:11 *	mand1nga (404c1f0e@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 09:23:15 div0 DibTop 
    Mar 05 09:23:30 <tZork>	oh right, well }-z-{ my web stuff is rusty nowdays. im not a good choise i think,
    Mar 05 09:23:31 <div0>	I think general PR belongs into that too
    Mar 05 09:23:37 <div0>	i.e. not just our website, but also other sites :P
    Mar 05 09:23:38 <Dokujisan>	div0: yeah that's what I have in mind. I don't want to boss people around. I consider it more of an organization role than anything
    Mar 05 09:23:52 <}-z-{>	tZork: I think if Dokujisan and willis also share this responsibility we'll be good.
    Mar 05 09:24:05 <}-z-{>	Dokujisan is good at managing, we've seen this
    Mar 05 09:24:07 <Dokujisan>	I want to be able to establish how things are done and then hopefully remove myself from that role over time
    Mar 05 09:24:16 <div0>	as for sysadmin... it'd be nice if these also are responsible for making the builds
    Mar 05 09:24:24 <div0>	as it overlaps quite much :P
    Mar 05 09:24:30 <}-z-{>	makes sense
    Mar 05 09:24:35 <div0>	of course, it'll be mostly automatic
    Mar 05 09:24:41 <div0>	I envision a cronjob for daily builds
    Mar 05 09:24:43 <tZork>	Dokujisan: i think its acctualy needed continiously, nto nessesarely the same person/s tough.
    Mar 05 09:24:53 <div0>	and only making of release builds would be manual
    Mar 05 09:24:58 <div0>	(to put in version number)
    Mar 05 09:25:12 <div0>	on the other hand, website stuff overlaps with sysadmin too
    Mar 05 09:25:18 <}-z-{>	div0: I think we should do that an have an automatic private test server if possible too
    Mar 05 09:25:24 <div0>	sure
    Mar 05 09:25:46 <SoulKeeper_p>	Dokujisan, prolly forgot: Morphed into >Artists section & modeling (afaik), and you can add me aswell for art/gui/texture(2d).
    Mar 05 09:25:58 <div0>	yes
    Mar 05 09:26:08 <div0>	regarding how artwork should LOOK I want no responsibilties...
    Mar 05 09:26:16 <tZork>	hehe
    Mar 05 09:26:18 <div0>	I just request, or demand, general "good taste" principles :P
    Mar 05 09:26:31 <SoulKeeper_p>	haha
    Mar 05 09:26:31 <div0>	I don't care how it looks, as long it's no running around goatse :P
    Mar 05 09:26:43 <div0>	and no, not even a GOOD looking running around goatse please :P
    Mar 05 09:26:53 <tZork>	aww so no leiliololiolioloil? ;)
    Mar 05 09:26:57 <}-z-{>	regarding artwork, I think we should gather a list of wants/needs/likes/dislikes
    Mar 05 09:27:05 <}-z-{>	to give other artists direction when they are looking to contribute
    Mar 05 09:27:23 <}-z-{>	and hopefully that will evolve into some sort of natural style
    Mar 05 09:27:31 <FruitieX>	16:25:35 <@div0> I envision a cronjob for daily builds
    Mar 05 09:27:33 <FruitieX>	yes do want
    Mar 05 09:27:50 <FruitieX>	or one that builds as soon as there's a change in the git master branch
    Mar 05 09:27:53 <Dokujisan>	ok refresh the nexuiz_new_notes.txt
    Mar 05 09:27:53 *	esteel (VDGLpekoeK@planetnexuiz.de) has joined #notnexuiz
    Mar 05 09:27:57 <Dokujisan>	hi esteel :-)
    Mar 05 09:28:00 <}-z-{>	hey esteel 
    Mar 05 09:28:04 <tZork>	hi there esteel
    Mar 05 09:28:06 <esteel>	hola
    Mar 05 09:28:07 <FruitieX>	possibly even one that builds from some select branches
    Mar 05 09:28:10 <Dokujisan>	esteel: glance through the file in the subject
    Mar 05 09:28:19 <FruitieX>	and gives you an older download link with text BULID FAILED if recent builds fail
    Mar 05 09:28:23 <FruitieX>	hello esteel 
    Mar 05 09:29:05 <esteel>	laters when in the train.. right now it would be a pita.. mobilephone only ;)
    Mar 05 09:29:16 <FruitieX>	btw Dokujisan, i also admin a couple of nexuiz servers :P
    Mar 05 09:29:17 <Dokujisan>	ok
    Mar 05 09:29:25 <}-z-{>	yeah, actually there is a plugin for redmine concerning builds... you can have it automatically report certain things as bugs, sorry for the vague description :-P
    Mar 05 09:29:30 <FruitieX>	or well actually, they all run the nexrun mod >_>
    Mar 05 09:29:45 <tZork>	meh if build fail it should send horrid viroidz! taht'd keep yall motivated not to write bugz! xD
    Mar 05 09:29:57 <FruitieX>	ye tZork :P
    Mar 05 09:31:38 <Dokujisan>	ok one question regarding websites.... I want to invite the aussienexers to have their community join the core website instead of operating a separate website
    Mar 05 09:31:52 <}-z-{>	Dokujisan: I was thinking we could wrap in it wordpress MU
    Mar 05 09:32:00 <Dokujisan>	ok
    Mar 05 09:32:22 <}-z-{>	I'm not sure what this means for the mybb bridge however
    Mar 05 09:32:50 <}-z-{>	they may need an account on the main nexuiz* site for that
    Mar 05 09:32:59 <}-z-{>	I have to look into it
    Mar 05 09:38:25 <}-z-{>	okay, temporary domains to get setup on: theworthless.net, beertitties.com, cankill.us, withfoss.org
    Mar 05 09:38:36 <Dokujisan>	ok I think I have the aussies onboard with a central website
    Mar 05 09:39:21 <}-z-{>	just to setup something external we can all start using as a way to organize information until we better define ourselves
    Mar 05 09:39:59 <}-z-{>	I like cankill.us
    Mar 05 09:40:19 <}-z-{>	or withfoss.org
    Mar 05 09:41:07 <tZork>	i like both b33f and titties.. so i guess i like beertitties.com ;)
    Mar 05 09:41:14 <}-z-{>	:-P
    Mar 05 09:42:23 <}-z-{>	Dokujisan: any opinion?
    Mar 05 09:42:23 <Dokujisan>	hey... can we do an official mumble server?
    Mar 05 09:42:33 <}-z-{>	most definitely
    Mar 05 09:42:36 <}-z-{>	very good idea
    Mar 05 09:42:36 <Dokujisan>	I run a mumble server. I think there is one in Au
    Mar 05 09:42:46 <Dokujisan>	I think my mumble server is very low on resources
    Mar 05 09:42:56 <}-z-{>	we can probably integrate that into the website and probably the forums
    Mar 05 09:43:01 <}-z-{>	"user is on mumble now" w00t
    Mar 05 09:43:13 <}-z-{>	optionally displayed by choice of the user of course
    Mar 05 09:43:23 <}-z-{>	they'd have to associate their mumble account as well
    Mar 05 09:43:23 <Dokujisan>	and the lagtime between regions isn't a problem either. I've had people from australia on my mumble server and the chatting is fine
    Mar 05 09:43:34 <}-z-{>	Dokujisan: beertitties.com?
    Mar 05 09:43:45 <Dokujisan>	for some reason, the .25 seconds delay doesn't hurt the mumble experience
    Mar 05 09:43:48 <Dokujisan>	:-o
    Mar 05 09:43:53 <Dokujisan>	ya lost me
    Mar 05 09:44:05 <Dokujisan>	oh a temp website domain?
    Mar 05 09:44:08 <}-z-{>	I want to setup a temp site we can all collaborate on until we think about the name
    Mar 05 09:44:10 <Dokujisan>	ok
    Mar 05 09:44:11 <}-z-{>	yes
    Mar 05 09:44:11 <Dokujisan>	yeah
    Mar 05 09:44:12 <Dokujisan>	good idea
    Mar 05 09:44:38 <Dokujisan>	um it really can be anything
    Mar 05 09:44:44 <Dokujisan>	fukillfonic.com
    Mar 05 09:44:45 <}-z-{>	well I already have that registered
    Mar 05 09:44:46 <Dokujisan>	heh 
    Mar 05 09:44:52 <Dokujisan>	haha seriously???
    Mar 05 09:44:54 <}-z-{>	yes lol
    Mar 05 09:45:00 <Dokujisan>	wow....I'm not gonna ask
    Mar 05 09:45:05 <}-z-{>	haha
    Mar 05 09:45:17 <Dokujisan>	that must have been one drunk domain searching night
    Mar 05 09:45:24 <Dokujisan>	like drunk phone calls
    Mar 05 09:45:31 <}-z-{>	drunk in college, "OMG WOULDN'T IT BE GREAT IF WE HAD A WEBSITE THAT INVOLVED BEER AND BOOBIES AND GIRLS SHOWING US BOOBIES WHILE DRINKING BEERS?"
    Mar 05 09:45:54 <Dokujisan>	"You know what's awesome?? Beer is awesome. But you know what else is really awesome???"
    Mar 05 09:46:05 <Dokujisan>	haha
    Mar 05 09:46:37 <Dokujisan>	well I dunno if anyone would be offended by that name
    Mar 05 09:46:42 <Dokujisan>	but it doesn't bother me for a temp site
    Mar 05 09:46:47 <Dokujisan>	well...
    Mar 05 09:46:49 <}-z-{>	okey dokey
    Mar 05 09:46:54 <Dokujisan>	ok maybe pick a less offenseive domain if you have one
    Mar 05 09:47:02 <}-z-{>	cankill.us ?
    Mar 05 09:47:05 <Dokujisan>	sure
    Mar 05 09:47:07 <}-z-{>	withfoss.org ?
    Mar 05 09:47:12 <Dokujisan>	cankill.us
    Mar 05 09:47:15 <}-z-{>	okay
    Mar 05 09:49:26 <}-z-{>	might take me all day to get setup, I have work work to do as well
    Mar 05 09:51:36 <}-z-{>	btw, is redmine's textile based wiki good enough for everyone or should I be considering alternatives?
    Mar 05 09:52:21 <tZork>	beer and boodies is mroe offensive then able to commit murder? =( ;)
    Mar 05 09:52:58 <}-z-{>	lol
    Mar 05 09:53:02 <tZork>	the cankill one will be fine for temp id say
    Mar 05 09:58:12 <Dokujisan>	question... do we have to use quakenet? >.<
    Mar 05 09:58:35 <Dokujisan>	other games use other networks like gameradius
    Mar 05 09:58:59 <}-z-{>	what is the advantage of other networks?
    Mar 05 09:59:02 <Dokujisan>	for my other project I'm involved with, Getty was showing me a way to have #nexuiz on multiple networks and have them all connect to each other through a bot
    Mar 05 09:59:10 <Dokujisan>	so we would have our own IRC network
    Mar 05 09:59:21 <tZork>	for devchannel, freenode maybe?
    Mar 05 09:59:43 <}-z-{>	I'm not sure I understand what you mean Dokujisan 
    Mar 05 09:59:44 <Dokujisan>	and #battlecube channels on quakenet and other networks and they would all echo to/from our network
    Mar 05 09:59:50 <}-z-{>	oh I see
    Mar 05 09:59:53 <Dokujisan>	there would be a bot that echos what is typed
    Mar 05 09:59:56 <Dokujisan>	between the various networks
    Mar 05 10:00:01 <}-z-{>	well, we can have a poll when we put up the website
    Mar 05 10:00:15 <}-z-{>	There are nice survey and poll scripts for wordpress
    Mar 05 10:00:31 <}-z-{>	s/scripts/plugins/
    Mar 05 10:06:56 <Dokujisan>	ah forgot about mrBougo
    Mar 05 10:06:59 <Dokujisan>	he's a developer, right?
    Mar 05 10:07:03 <}-z-{>	yes
    Mar 05 10:07:07 <}-z-{>	and more than that
    Mar 05 10:07:13 <Dokujisan>	give me the list
    Mar 05 10:07:14 <}-z-{>	positive energy within the community
    Mar 05 10:07:17 <Dokujisan>	heh
    Mar 05 10:07:19 <Dokujisan>	well...
    Mar 05 10:07:27 <Dokujisan>	in our breakdown of roles
    Mar 05 10:07:31 <Dokujisan>	and skillsets
    Mar 05 10:07:40 <Dokujisan>	game dev and web dev?
    Mar 05 10:07:45 <Dokujisan>	server admin?
    Mar 05 10:07:48 <Dokujisan>	moderator?
    Mar 05 10:08:00 <}-z-{>	game dev, server admin, moderator
    Mar 05 10:08:03 <}-z-{>	don't know about web dev
    Mar 05 10:08:08 <}-z-{>	that'd be up to him
    Mar 05 10:08:29 <}-z-{>	by the way, I don't mind repurposing the nexuiz ninjaz game server as a build / test machine
    Mar 05 10:08:40 <Dokujisan>	awesome
    Mar 05 10:08:41 <}-z-{>	I'll run a few other services on it but won't be a big deal
    Mar 05 10:08:49 <}-z-{>	maybe 1 nexuiz ninjaz server... though we might be 'the ninjaz' by then
    Mar 05 10:09:01 <}-z-{>	and I'll use it for irsii, like I'm doing now :-P
    Mar 05 10:09:02 <Dokujisan>	div0 and I had a long discussion about the bootcamp and dojo servers
    Mar 05 10:09:12 <}-z-{>	oh yeah?
    Mar 05 10:10:16 <Dokujisan>	I'm updating the notes with it. just a sec
    Mar 05 10:10:23 <}-z-{>	okay
    Mar 05 10:10:28 <}-z-{>	where are the notes? sorry I don't have the url
    Mar 05 10:11:02 <Dokujisan>	in the subject
    Mar 05 10:11:06 <Dokujisan>	can you see it?
    Mar 05 10:11:09 <}-z-{>	hurr durr
    Mar 05 10:11:10 <}-z-{>	yes
    Mar 05 10:11:13 <}-z-{>	what a great place
    Mar 05 10:11:16 <}-z-{>	I feel 'tarded
    Mar 05 10:11:37 <}-z-{>	btw Dokujisan there was a documentation generation tool I mentioned in #alientrap-dev ~a month ago
    Mar 05 10:11:45 <}-z-{>	I know this may be a little forward thinking
    Mar 05 10:11:54 <tZork>	this is quite interesting 
    Mar 05 10:11:54 <}-z-{>	but your style in the notes there just jogged my memory
    Mar 05 10:12:10 <}-z-{>	because writing documentation in their psuedo-wiki format would generate HTML and manpages
    Mar 05 10:12:17 <tZork>	wrt to the NDA's afore blamed:
    Mar 05 10:12:18 <tZork>	10-03-05 15:59] <tZork> Chris: out of curiosity, are you somehow involved in the deal? 
    Mar 05 10:12:18 <tZork>	[10-03-05 16:00] <Chris> no but this has been in the making for some time now
    Mar 05 10:12:18 <tZork>	[10-03-05 16:00] <Chris> since last year
    Mar 05 10:12:18 <tZork>	[10-03-05 16:00] <Chris> well this concept
    Mar 05 10:12:18 <tZork>	[10-03-05 16:00] <Chris> and honestly, I would like to be in contribution to it, and make a good game, and something not fully for this reason but a good reason none the less: something the community would be proud of
    Mar 05 10:12:19 <}-z-{>	and I think that could really benefit the project
    Mar 05 10:12:19 <tZork>	[10-03-05 16:01] <Chris> I honestly though have a bit of venom to spew to those who feel aggravated by the decision though
    Mar 05 10:12:51 <Dokujisan>	ok refresh the notes again }-z-{ I added the details about training
    Mar 05 10:13:02 <}-z-{>	wait chris is upset about people being upset about this?
    Mar 05 10:13:12 <tZork>	taht too , but read agaiun
    Mar 05 10:13:14 <tZork>	again*
    Mar 05 10:13:28 <}-z-{>	Dokujisan: I think there should be a board or committee larger than 3 leaders, just for the record
    Mar 05 10:13:35 <Dokujisan>	I was thinking 5
    Mar 05 10:13:39 <}-z-{>	3 I believe to still have weak point
    Mar 05 10:13:42 <Dokujisan>	I was gonna suggest that to div0
    Mar 05 10:13:45 <}-z-{>	yeah
    Mar 05 10:14:06 <tZork>	he knows abt it since more then a year, hes not involved in it and yet at and ill refer to NDA not to comment.
    Mar 05 10:14:30 <tZork>	thats the interesting part
    Mar 05 10:14:53 <Dokujisan>	I dunno who Chris is
    Mar 05 10:14:54 <FruitieX>	oow whenever i said to want cleftwillage i meant
    Mar 05 10:14:57 <FruitieX>	TREASURE ISLAND :P
    Mar 05 10:15:05 <Dokujisan>	:-) ok
    Mar 05 10:15:08 <tZork>	oh forgot a few lines, thise go atop of the otehr ones:
    Mar 05 10:15:08 <tZork>	10-03-05 15:54] <Chris> <@div0> the use of the NAME Nexuiz in that way, NOPE
    Mar 05 10:15:08 <tZork>	[10-03-05 15:54] <Chris> I've known about this for months
    Mar 05 10:15:08 <tZork>	[10-03-05 15:54] <Chris> and it has been hinted to nexuiz entering a new platform
    Mar 05 10:15:15 <FruitieX>	cleftvillage is crap :P
    Mar 05 10:15:18 <tZork>	lmao FruitieX
    Mar 05 10:15:40 <Dokujisan>	clefvillage has some very interesting elements
    Mar 05 10:15:44 <Dokujisan>	I like the beach
    Mar 05 10:15:56 <Dokujisan>	but bad gameplay, as it turns out
    Mar 05 10:16:07 <tZork>	it looks good fore sure, but gameplay is.. well its not.
    Mar 05 10:16:28 <}-z-{>	Dokujisan: I know div is against hierarchies but I think to a degree perhaps a "committee" of liasions would be beneficial
    Mar 05 10:16:32 <tZork>	maybe for keyhunt =)
    Mar 05 10:16:33 <Dokujisan>	tZork and FruitieX can you think of more to add to the maps section? 
    Mar 05 10:16:48 <}-z-{>	the players that can speak between developers and players and grease the wheels, help diffuse tension, etc.
    Mar 05 10:16:56 <tZork>	tbh id keep the maplist as short as possible Dokujisan
    Mar 05 10:17:00 <Dokujisan>	}-z-{: I thought he aggreed to that.... 3 leaders (or 5 perhaps) for major decisions with a committee under it for "most" decisions
    Mar 05 10:17:00 <FruitieX>	also what about strength?
    Mar 05 10:17:03 <}-z-{>	make sure everyone is in touch as they need to be sort of thing
    Mar 05 10:17:10 <Dokujisan>	tZork: yeah but we need a list to start discussion
    Mar 05 10:17:12 <CuBe0wL>	re
    Mar 05 10:17:16 <CuBe0wL>	what's new?
    Mar 05 10:17:18 <FruitieX>	it afaik uses mostly eX textures
    Mar 05 10:17:24 <FruitieX>	CuBe0wL: read topic
    Mar 05 10:17:34 <tZork>	strength is proformance murder, and i cant say i totaly love the gameplay
    Mar 05 10:17:37 <Dokujisan>	tZork: I personally agree with making the game less bloated, only having a few included maps
    Mar 05 10:17:54 <Dokujisan>	ooooh I do like strength. I think it could be redone maybe?
    Mar 05 10:17:58 <}-z-{>	bbiab, I have to manually edit a database because an ajax callback seems to be failing due to a fileupload error, yay
    Mar 05 10:18:22 <FruitieX>	Dokujisan: why redone, i think it is pretty much fine as it is
    Mar 05 10:18:32 <FruitieX>	maybe redone lightning if we ever get a working raytracer solution
    Mar 05 10:18:48 <FruitieX>	other than that it has excellent textures, excellent detail, excellent gameplay IMO :)
    Mar 05 10:18:49 <Dokujisan>	eh.... it could be better on FPS and it has some holes in it. I would like to see it a little more cleaner .... like Stormkeep2 :-)
    Mar 05 10:18:59 <CuBe0wL>	so we fork, it's official?
    Mar 05 10:19:06 <Dokujisan>	:-D \o/
    Mar 05 10:19:18 <tZork>	nothing official afaik CuBe0wL
    Mar 05 10:19:22 <CuBe0wL>	ok
    Mar 05 10:19:23 <Dokujisan>	aww :-(
    Mar 05 10:19:30 <CuBe0wL>	but things are bloody serious?
    Mar 05 10:19:41 <Dokujisan>	it seems like this is as official as a fork gets, isn't it?
    Mar 05 10:19:47 <tZork>	brainlack created this mess. lets not give it anotehr chanse.
    Mar 05 10:19:58 <FruitieX>	agreed Dokujisan it has bad fps, this should be worked on
    Mar 05 10:20:01 <Dokujisan>	we still have a lot of work to do, of course
    Mar 05 10:20:04 <FruitieX>	but texture/detail wise i have nothing to add
    Mar 05 10:20:18 <FruitieX>	of course i'd want warpzones again, but they will just halve the fps again :)
    Mar 05 10:20:19 <}-z-{>	nevermind, I'm back 1and1 is failing
    Mar 05 10:20:29 <tZork>	i do, eX is booooring
    Mar 05 10:20:32 <tZork>	;)
    Mar 05 10:20:45 <Dokujisan>	FruitieX: you know how the edges on stormkeep2 look really smooth now? I dunno what it is that changed, but the edge detail is impressive. I would like to see more of that in maps
    Mar 05 10:20:46 <FruitieX>	lol but we cant have all maps using trak5/4 :P
    Mar 05 10:20:56 <FruitieX>	edge? :P
    Mar 05 10:21:06 <Dokujisan>	hmm let me grab some screenshots
    Mar 05 10:22:03 <CuBe0wL>	woah, that maplist is very slim
    Mar 05 10:22:21 <Dokujisan>	yesh help me add more just for our discussion
    Mar 05 10:22:42 <FruitieX>	CuBe0wL: yes
    Mar 05 10:22:48 <Dokujisan>	wow I can't find any stormkeep2 screenshots :-(
    Mar 05 10:22:54 <CuBe0wL>	well, do we eant to keep the Nexuiz athmospere ?
    Mar 05 10:22:59 <FruitieX>	only supply very high detail maps is the goal apparently...
    Mar 05 10:23:09 <Dokujisan>	CuBe0wL: not sure what you mean. You mean style?
    Mar 05 10:23:12 <FruitieX>	which i find good
    Mar 05 10:23:18 <tZork>	irena (not ctf) its playes well in dm/isg games IMO
    Mar 05 10:23:21 <CuBe0wL>	yes, and feel im general
    Mar 05 10:23:28 <FruitieX>	also another goal is to remove the low resolution texture packs (evil* eg)
    Mar 05 10:23:38 <Dokujisan>	tZork: I have irena on my list of map projects to be fixed. Nobody has taken it up yet though
    Mar 05 10:23:39 <CuBe0wL>	noooo! I like evil a lot :(
    Mar 05 10:23:48 <FruitieX>	irena would need a major rehaul imo :P
    Mar 05 10:23:52 <CuBe0wL>	or, remake it high res :P
    Mar 05 10:23:54 <tZork>	Dokujisan: tahts the ctf
    Mar 05 10:23:54 <FruitieX>	looks like warsow without cel-shading :P
    Mar 05 10:23:59 <tZork>	as you mention bases
    Mar 05 10:24:01 <Dokujisan>	tZork: oh there is a non-CTF one?
    Mar 05 10:24:12 <FruitieX>	CuBe0wL: good luck with that
    Mar 05 10:24:19 <}-z-{>	fyi, dance is still a giant warsow logo
    Mar 05 10:24:20 <FruitieX>	of course, if someone does it is possible to add later
    Mar 05 10:24:29 <CuBe0wL>	well, if high quality is a goal, why reslimed is missing from the list?
    Mar 05 10:24:30 <tZork>	yes i made it as non ctf Dokujisan... then it was turned to ctf by someoneo else. its totaly bad for ctf.
    Mar 05 10:24:35 <FruitieX>	dance needs a remake for sure
    Mar 05 10:24:38 <FruitieX>	at least retexture
    Mar 05 10:24:46 <FruitieX>	right reslimed!
    Mar 05 10:24:50 <FruitieX>	add that Dokujisan, reslimed
    Mar 05 10:24:50 <CuBe0wL>	or silvercity , tZork version
    Mar 05 10:24:56 <tZork>	nah
    Mar 05 10:25:06 <Dokujisan>	I really like the silvercity remake, but it's low FPS
    Mar 05 10:25:11 <CuBe0wL>	oh
    Mar 05 10:25:13 <FruitieX>	needs remake, yep fix fps too
    Mar 05 10:25:19 <CuBe0wL>	Hot Grounds? :D
    Mar 05 10:25:25 <FruitieX>	:d
    Mar 05 10:25:28 <}-z-{>	hahaha, one of the features of Wordpress MU, "Ambiguity about how to pronounce its name"
    Mar 05 10:25:30 <FruitieX>	cant remember which that is
    Mar 05 10:25:37 <CuBe0wL>	cbdm1 :D
    Mar 05 10:25:37 <FruitieX>	oh a dm map by you
    Mar 05 10:25:40 <FruitieX>	i dont think i ever played it
    Mar 05 10:25:45 <CuBe0wL>	you should
    Mar 05 10:25:53 <Dokujisan>	I think killall_organic has potential, but needs some adjustments for gameplay
    Mar 05 10:25:57 <tZork>	did a few times, bit to hardcore i think. 
    Mar 05 10:26:15 <tZork>	as in you gotta be on your toes ont to get lava all over your cahones
    Mar 05 10:26:23 <CuBe0wL>	Dokujisan, no, killall organic needs a MAJOR overhaul
    Mar 05 10:26:29 <Dokujisan>	it does?
    Mar 05 10:26:32 <CuBe0wL>	yes
    Mar 05 10:26:39 <Dokujisan>	ok well I'm putting it on the list anyway :-)
    Mar 05 10:26:48 <Dokujisan>	just for discussion
    Mar 05 10:26:55 <CuBe0wL>	and I have plans, but I haven't find time yet to execute it
    Mar 05 10:27:00 <Dokujisan>	and I barely played hotgrounds. It's DM, right?
    Mar 05 10:27:05 <CuBe0wL>	yes
    Mar 05 10:27:16 <Dokujisan>	I remember it looks good
    Mar 05 10:27:21 <CuBe0wL>	thx
    Mar 05 10:27:38 <CuBe0wL>	I plan to revisit greatwall too
    Mar 05 10:27:45 <CuBe0wL>	fixing some stuff
    Mar 05 10:27:47 <Dokujisan>	oh no
    Mar 05 10:27:59 <CuBe0wL>	like laser fence over the bases
    Mar 05 10:28:09 <CuBe0wL>	so it's not a hopin hop out anymore
    Mar 05 10:28:13 <tZork>	personaly i like brokenworlds and irena the best of my maps i think.. well tznex03 too but you get good enougth teams on that map abt once every 100 tries.. and it comes arround in teh rot abt once every month so.. xD
    Mar 05 10:28:26 <Dokujisan>	the main thing I never liked about greatwall is the main feature that is liked it (by those who like it) and that is the jump pads that throw you across the whole map
    Mar 05 10:28:34 <Dokujisan>	is liked about it*
    Mar 05 10:29:07 <CuBe0wL>	I planned to make it a bit more difficult
    Mar 05 10:29:12 <Dokujisan>	tZork: brokenworlds 2 looks awesome, but almost everyone I speak with about it prefers brokenworlds 1
    Mar 05 10:29:12 <CuBe0wL>	a bit assault like
    Mar 05 10:29:14 <Dokujisan>	for gameplay
    Mar 05 10:29:28 <CuBe0wL>	and I mean turrets
    Mar 05 10:29:36 <tZork>	well the gw_overloaded experiment show you cant make gw to difficult ot ppl will hate on it
    Mar 05 10:29:42 <Dokujisan>	I never liked turrets + CTF
    Mar 05 10:29:55 <CuBe0wL>	MG turrets looking the air, and killing those who try to just use them
    Mar 05 10:30:15 <FruitieX>	problem with reslimed is that it uses lots of evil textures
    Mar 05 10:30:36 <CuBe0wL>	I want something like you need to active the turrets/destroy them to be able to use the midair route
    Mar 05 10:30:39 <tZork>	frankly original slimepit play better
    Mar 05 10:30:46 <CuBe0wL>	Fortress resurrection?
    Mar 05 10:30:52 <CuBe0wL>	tZork, I somehow like both
    Mar 05 10:30:55 <Dokujisan>	I feel like the turrets are just an annoyance or distraction to CTF
    Mar 05 10:30:56 <FruitieX>	i would vote yes on including brokenworlds
    Mar 05 10:31:07 <FruitieX>	agree with turrets being a distraction
    Mar 05 10:31:18 <CuBe0wL>	mannable turrets?
    Mar 05 10:31:29 <CuBe0wL>	now that tZorks vehicle code is usable
    Mar 05 10:31:30 <tZork>	me too CuBe0wL, but on a avarage game, slimepit is the better map, gameplay wize. imo.
    Mar 05 10:31:53 <Taoki>	http://pastebin.com/PpDSFi4c Is it ok to post this topic on the forum at this current stage?
    Mar 05 10:31:55 <CuBe0wL>	ppl on DCC like both, that's my impression
    Mar 05 10:32:01 <tZork>	Dokujisan: if the map wasent designed for it, yeh.
    Mar 05 10:32:07 <Taoki>	Or recommended
    Mar 05 10:32:16 <Dokujisan>	manually playable turrets is a whole other discission
    Mar 05 10:32:21 <Dokujisan>	I would love to test that out more
    Mar 05 10:32:35 <tZork>	its horribly boring Dokujisan
    Mar 05 10:32:35 <Dokujisan>	but I haven't been keeping up with the vehicle code stuff in a while
    Mar 05 10:33:13 <Dokujisan>	I remember seeing the spider walker video
    Mar 05 10:33:34 <FruitieX>	Dokujisan: definitely add reslimed as a map we should consider if we get replacement textures...
    Mar 05 10:33:45 <Dokujisan>	ok
    Mar 05 10:33:46 <tZork>	its like a wheeless tank. you just sit there confined by a rot/pitch speed limuted gun with sub-par damage. (manable turrets)
    Mar 05 10:33:51 <FruitieX>	eg. retexture or someone remaking the textures in higher res
    Mar 05 10:34:11 <Dokujisan>	FruitieX: also div0 mentioned that reslimed isn't as easy to run around as slimepit. It's easier to get stuck on thigns
    Mar 05 10:34:26 <FruitieX>	that should be somewhat easy to fix
    Mar 05 10:34:29 <FruitieX>	add that to the notes
    Mar 05 10:35:27 <CuBe0wL>	btw... what about that community petition?
    Mar 05 10:35:34 <Dokujisan>	what petition?
    Mar 05 10:35:43 <Taoki>	Anyway, posting that topic, if no one thinks it could get in the way right now or anything
    Mar 05 10:35:45 <CuBe0wL>	if we officially fork, there's no real need for that
    Mar 05 10:35:48 <tZork>	relimed is a bit to big for its layout style imo. unless the server's crowded you end up searching more then fighting,
    Mar 05 10:35:50 <Dokujisan>	Taoki: what topic?? :-o
    Mar 05 10:35:50 <CuBe0wL>	Taoki, not yet pls
    Mar 05 10:35:57 <Taoki>	http://pastebin.com/PpDSFi4c
    Mar 05 10:35:59 <CuBe0wL>	I disapprove
    Mar 05 10:36:04 <Taoki>	ok, I'll just save it then
    Mar 05 10:36:14 <FruitieX>	Dokujisan: maybe same thing about final_rage
    Mar 05 10:36:29 <FruitieX>	also, add desertfactory (div0 mentioned that earlier)
    Mar 05 10:36:40 <Taoki>	I was hoping that with the name change, we could apear with some new content and something surprising
    Mar 05 10:37:16 <CuBe0wL>	I'd like to stick as much Nexuizish as we can
    Mar 05 10:37:47 <FruitieX>	I hope this too Taoki 
    Mar 05 10:37:52 <CuBe0wL>	eg. I'd keep all models, btu remake them. with the same name. eg. Replace original Nexus with that new one
    Mar 05 10:38:17 <CuBe0wL>	who's made that? my brain is fried again, I can't remember the nick
    Mar 05 10:38:34 <tZork>	Dokujisan: manable gun platforms should be designed for that, the current auto turrets use good prediction and targetselect ratehr then firepower. thus maning them makes little sense. manable guns should make up for the lack of movemenbt with firepower, imo.
    Mar 05 10:38:47 <Taoki>	Someone should really consider this http://alientrap.org/forum/viewtopic.php?p=69763#p69763 Best forgotten contribution i know of
    Mar 05 10:39:01 Taoki tZork 
    Mar 05 10:39:04 <Dokujisan>	Taoki: I have it added
    Mar 05 10:39:06 <CuBe0wL>	Dokujisan, I was talking about this petition: http://alientrap.org/forum/viewtopic.php?f=4&t=6050&start=0
    Mar 05 10:39:30 <Dokujisan>	wow that is a lot of color
    Mar 05 10:39:39 <FruitieX>	:o indeed
    Mar 05 10:39:44 <FruitieX>	color is fine :D
    Mar 05 10:39:46 <Dokujisan>	"this post is sponsored by Crayola Crayons"
    Mar 05 10:39:57 <CuBe0wL>	:)
    Mar 05 10:40:02 <CuBe0wL>	anyway, read up
    Mar 05 10:41:07 <Dokujisan>	I am not in support of any petitions
    Mar 05 10:41:19 <Dokujisan>	contracts have already been signed. Things are already decided.
    Mar 05 10:41:24 <Dokujisan>	and trust is already lost
    Mar 05 10:41:39 <Dokujisan>	and everything that has been said in this channel is....awesome
    Mar 05 10:41:58 <Dokujisan>	what we have been discussing over the past 2 days in here is exactly what nexuiz should have been
    Mar 05 10:42:49 <Dokujisan>	in just having these conversations and doing this planning that we're doing, we'll be getting more done in a month than nexuiz had previously done in a year (imo)
    Mar 05 10:43:16 <FruitieX>	Indeed.
    Mar 05 10:43:27 <}-z-{>	mmm hmm
    Mar 05 10:43:28 <Dokujisan>	we need to start informing more key people
    Mar 05 10:43:59 <Dokujisan>	so they can drop the public outcry and start preparing for the future
    Mar 05 10:44:04 <CuBe0wL>	one question remains on my side
    Mar 05 10:44:11 <CuBe0wL>	a very achy one
    Mar 05 10:44:17 <CuBe0wL>	what about DCC server?
    Mar 05 10:44:27 <Dokujisan>	doesn't esteel run it?
    Mar 05 10:44:31 <CuBe0wL>	it's not our own with esteel
    Mar 05 10:44:39 <CuBe0wL>	it's not his property I think
    Mar 05 10:44:40 <Dokujisan>	esteel is in this channel
    Mar 05 10:44:46 <CuBe0wL>	yes, I see him
    Mar 05 10:44:54 <FruitieX>	CuBe0wL: sxen?
    Mar 05 10:45:00 <CuBe0wL>	yes, he's the guy
    Mar 05 10:45:03 <FruitieX>	:)
    Mar 05 10:45:04 <CuBe0wL>	ollipapa
    Mar 05 10:45:12 <}-z-{>	esteel is on this side of the fence
    Mar 05 10:45:16 <tZork>	hrm maybe Procyon2 for the maplist (dm or insta)
    Mar 05 10:45:16 <}-z-{>	is he not?
    Mar 05 10:45:37 <CuBe0wL>	dunno, I haven't seen him talking, I haven't read the backlogs
    Mar 05 10:45:38 <FruitieX>	Dokujisan: desertfactory as sure thing on maplist :)
    Mar 05 10:45:41 <Dokujisan>	he hasn't said exactly, but it appears that he is onboard
    Mar 05 10:45:48 <FruitieX>	that should be the last official map, rest can be supplied as pk3
    Mar 05 10:45:55 <CuBe0wL>	what about Kadaverjack?
    Mar 05 10:46:11 <CuBe0wL>	he still owns planetnexuiz.de iirc
    Mar 05 10:46:20 <CuBe0wL>	and he was a major developer once too
    Mar 05 10:46:34 <Dokujisan>	is he still active in the nexuiz community?
    Mar 05 10:46:41 <}-z-{>	active enough
    Mar 05 10:46:49 <CuBe0wL>	not so much, but he posts his thoughts now and then
    Mar 05 10:47:29 <Taoki>	Ok, here's another question onto the development. I haven't hard anything about ODE support ever since the first tests were done and videos of it working were put on Youtube. Everything went silent after... what is the status of ODE support in DP? Why aren't physical brushes already in entities.def?
    Mar 05 10:48:14 <Dokujisan>	what is ODE?
    Mar 05 10:48:41 <tZork>	physics engine
    Mar 05 10:48:43 <Taoki>	Open Dynamics Engine. Physics engine, for realistic physics like moving crates, stuff rolling around etc
    Mar 05 10:48:44 <Dokujisan>	ahh
    Mar 05 10:49:15 <FruitieX>	indeed what happened to that...
    Mar 05 10:49:20 <Taoki>	Was pretty excited about that at first :) But at some point it went silent
    Mar 05 10:50:13 <div0>	[16:36:20] <@CuBe0wL> btw... what about that community petition?
    Mar 05 10:50:19 <div0>	why? AT would LET us take over, I am sure
    Mar 05 10:50:55 <}-z-{>	to vermeulen's credit?
    Mar 05 10:51:21 <Dokujisan>	is paperclips a developer?
    Mar 05 10:51:34 <Dokujisan>	or contributor of some sort
    Mar 05 10:51:35 <FruitieX>	no i dont think so
    Mar 05 10:51:37 <}-z-{>	I didn't think he was, maybe mapper?
    Mar 05 10:52:19 <tZork>	ode sorta clashes with the 'normal' game iirc eg interaction between old quake objects and ode is shitty. 
    Mar 05 10:52:21 <Dokujisan>	}-z-{: can you query the unique usernames of people who created topics under "Map Releases">
    Mar 05 10:52:23 <Dokujisan>	?
    Mar 05 10:52:43 <tZork>	id imagine thats one of the things that stopped the ode use sofar
    Mar 05 10:52:48 <}-z-{>	not easily and not right now
    Mar 05 10:52:52 <Dokujisan>	ok
    Mar 05 10:52:58 <}-z-{>	apparently redmin can't accept a database password starting with #
    Mar 05 10:53:09 <}-z-{>	because it's telling me this on rake: Access denied for user 'db_cankill'@'silversurfer.dreamhost.com' (using password: NO)
    Mar 05 10:54:04 <Dokujisan>	Who is "Chris"? a developer?
    Mar 05 10:54:18 <}-z-{>	isn't he a qc guy? from i3d land?
    Mar 05 10:54:20 <CuBe0wL>	nexuiz_new_notes : vcall rename text "Pheonix notes"
    Mar 05 10:54:51 <Dokujisan>	no
    Mar 05 10:54:59 <CuBe0wL>	:(
    Mar 05 10:55:00 <Dokujisan>	I think we already shot down pheonix as a name
    Mar 05 10:55:04 <CuBe0wL>	when?
    Mar 05 10:55:08 <Samual>	Ello
    Mar 05 10:55:13 <tZork>	Dokujisan: some dood lurkign arround #darkplaces. developer of some sort iirc.
    Mar 05 10:55:23 <Spaceman>	nexitron?
    Mar 05 10:55:25 <Dokujisan>	the name Phoenix is overused a lot, a misspelling of it is even worse.
    Mar 05 10:55:32 <Samual>	Chris is a developer making his own game with Darkplaces
    Mar 05 10:55:35 <Samual>	Ignore him
    Mar 05 10:55:45 <Dokujisan>	I think we really want a name that doesn't have an existing meaning, just like nexuiz
    Mar 05 10:55:48 <Samual>	iirc he's making a realistic game
    Mar 05 10:56:09 <Dokujisan>	CuBe0wL: but.... someone did suggest we use a symbol that means phoenix or something like it
    Mar 05 10:56:20 <Dokujisan>	for the game symbol, since we can't use the 'n' kanji anymore
    Mar 05 10:56:22 <CuBe0wL>	Dokujisan, imho what was so awesome in the name of Nexuiz, that it really made ppl say "wtf"
    Mar 05 10:56:38 <Dokujisan>	CuBe0wL: well... not awesome. It's not a good name
    Mar 05 10:56:45 <Dokujisan>	so "wtf" was more like.... who came up with that?
    Mar 05 10:56:46 <CuBe0wL>	playfull
    Mar 05 10:56:50 <tZork>	Samual: well dont always ignore him. read backlog on him here for a interresting part.
    Mar 05 10:56:54 <CuBe0wL>	I always liked it
    Mar 05 10:57:07 <Dokujisan>	CuBe0wL: you already admitted that you thought it was strange :-)
    Mar 05 10:57:10 <Dokujisan>	at first
    Mar 05 10:57:28 <Dokujisan>	really any name that we come up with is going to grow to have meaning to us, just like nexuiz
    Mar 05 10:57:32 <CuBe0wL>	yes, but I never said I didn't like it from the first read
    Mar 05 10:57:37 <Dokujisan>	but I thikn we should still take some time with the choice
    Mar 05 10:57:44 <CuBe0wL>	k
    Mar 05 10:57:46 <Samual>	[10:57:14am] <tZork> Samual: well dont always ignore him. read backlog on him here for a interresting part.
    Mar 05 10:57:50 <Dokujisan>	well I never "hated" it. I just thought it was odd
    Mar 05 10:57:52 <Samual>	I don't have time to read the whole #darkplaces log
    Mar 05 10:58:08 <tZork>	_backlog on him here_
    Mar 05 10:58:11 <Dokujisan>	I would really like a name that people can pronounce
    Mar 05 10:58:17 <FruitieX>	+1
    Mar 05 10:58:17 <tZork>	use search you lazy toad
    Mar 05 10:58:20 <FruitieX>	+1000 :P
    Mar 05 10:58:26 <Dokujisan>	haha
    Mar 05 10:58:37 <Samual>	I can't, my logs fail :P
    Mar 05 10:58:42 <Taoki>	Hmm... I have an idea for the symbol. Hold on
    Mar 05 10:58:50 <tZork>	.|.. 
    Mar 05 10:58:52 <CuBe0wL>	I still stand by my suggestion, it should be considered as a name. (also, Pheonix is pronouncabel, and we can still pronounce it as phoenix)
    Mar 05 10:58:55 <tZork>	taht one? };P
    Mar 05 10:59:01 <Dokujisan>	CuBe0wL: but yeah we can find some kanji that has the same meaning as "phoenix"
    Mar 05 10:59:13 <CuBe0wL>	hey, not a bad idea
    Mar 05 10:59:42 <CuBe0wL>	btw. what I always liked in Nexuiz are the in community jokes
    Mar 05 11:00:06 <Taoki>	http://img46.imageshack.us/img46/1096/kojndragonstrength.png }-z-{ gave me this an year ago (it was to make a ninja player model... I'm sorry I haven't made it even today :( ) Anyway, something like that could be pretty.
    Mar 05 11:00:32 <CuBe0wL>	"epic", "AGY))", "Nexuiz", the fact that Specop (not SPACE COP) is a woman...
    Mar 05 11:00:39 <Taoki>	Not -that- one, but something similar
    Mar 05 11:01:21 <CuBe0wL>	Pheonix would be a similar ingame joke, that roots back to Nexuiz. Playfull, and still brings back good memories for those, who knew it
    Mar 05 11:01:55 <CuBe0wL>	for those who will join later, it might be a wtf, but it'll be still funny when it get's explained
    Mar 05 11:02:16 <CuBe0wL>	community building, on the remains of the old one
    Mar 05 11:02:53 <Taoki>	Pheonix could be a good name for a default character
    Mar 05 11:03:07 <Dokujisan>	another good idea
    Mar 05 11:03:27 <Dokujisan>	or they could have a phoenix symbol on their chest
    Mar 05 11:03:33 <Taoki>	yeah
    Mar 05 11:03:49 <CuBe0wL>	hmm... Nexus renamed to Pheonix ?
    Mar 05 11:04:06 <CuBe0wL>	feels a bit too distant
    Mar 05 11:04:08 <Dokujisan>	is that the main character name? Nexus?
    Mar 05 11:04:35 <CuBe0wL>	well, I always thought about Nexus and Xolar as their race is the main one
    Mar 05 11:04:48 <Dokujisan>	I like using the symbolism of "phoenix" but I can't say I like the name. I once tried to use it for a server name "Phoenix CTF" as it was rising from the ashes of my previous server "Fusion CTF"....but it turned out to be a bad name
    Mar 05 11:04:52 <CuBe0wL>	their description says: "Nexuiz's soldier"
    Mar 05 11:04:57 <Taoki>	We could add a new character. I believe that with this name change we should also add something new
    Mar 05 11:06:02 <FruitieX>	pheonix sounds good
    Mar 05 11:06:08 <CuBe0wL>	I kinda like the style of Nexuiz's player models
    Mar 05 11:06:14 <FruitieX>	phoenix would be bad simply because it'd be near impossible to get google hits :)
    Mar 05 11:06:34 <tZork>	pnehoix?
    Mar 05 11:06:57 <Samual>	tZork, easier to pronounce than Nexuiz for sure
    Mar 05 11:06:59 <CuBe0wL>	that's sounds like a diseas, not a game
    Mar 05 11:07:09 <tZork>	soz gettin a bit silly.. 
    Mar 05 11:07:58 <CuBe0wL>	also, a phoenix is a bird
    Mar 05 11:08:06 <CuBe0wL>	birds are always the symbol to be free
    Mar 05 11:08:16 <FruitieX>	Hmm
    Mar 05 11:08:17 <CuBe0wL>	Pheonix is free as a bird
    Mar 05 11:08:43 <CuBe0wL>	haha
    Mar 05 11:08:45 <FruitieX>	good luck getting a domain for either though...
    Mar 05 11:09:11 <CuBe0wL>	we could implement the game mode: catch the chicken... just with phoenix :D
    Mar 05 11:09:36 <CuBe0wL>	pheonixgame.org ?
    Mar 05 11:09:57 <tZork>	hehe
    Mar 05 11:10:02 <tZork>	freeonix
    Mar 05 11:10:19 <tZork>	sounds like a oddball os tough
    Mar 05 11:10:28 <CuBe0wL>	+1 :D
    Mar 05 11:10:36 <FruitieX>	pheonixgame.org is available
    Mar 05 11:10:46 <FruitieX>	.com is taken :O
    Mar 05 11:11:09 <tZork>	or juz 1337 speak it. ph3onix.com
    Mar 05 11:11:21 <Dokujisan>	ew
    Mar 05 11:11:53 <Dokujisan>	can we establish a rule that we aren't allowed to use 1337 speak in anything? :-)
    Mar 05 11:12:29 <tZork>	sure, just as long as its allowed to break it ;)
    Mar 05 11:12:50 <Dokujisan>	rules are made to be br0k3n
    Mar 05 11:12:56 <CuBe0wL>	lol :D http://pheonixgame.com/default.aspx
    Mar 05 11:13:09 <FruitieX>	yes wtf
    Mar 05 11:13:13 <FruitieX>	awesome web design
    Mar 05 11:13:18 <tZork>	email based game
    Mar 05 11:13:27 <tZork>	epic colors ate my eyes
    Mar 05 11:13:34 <CuBe0wL>	yep, email based RPG
    Mar 05 11:13:37 <FruitieX>	>_<
    Mar 05 11:13:49 <Dokujisan>	btw did you see this parody map? http://alientrap.org/forum/viewtopic.php?f=19&t=6054
    Mar 05 11:13:58 <FruitieX>	by Taoki? yes :D
    Mar 05 11:14:09 <CuBe0wL>	freepheonix.com is available!
    Mar 05 11:14:19 <Taoki>	:P
    Mar 05 11:14:22 <tZork>	HERE ARE THE RULES:
    Mar 05 11:14:23 <tZork>	CLICK HERE TO DONATE TO CREATION AND MAINTENANCE
    Mar 05 11:14:40 <tZork>	roflamao
    Mar 05 11:15:10 <Dokujisan>	rolling on the floor laughing and maiming an orphan?
    Mar 05 11:15:36 <Dokujisan>	ok... I have no idea about our timeline with this fork
    Mar 05 11:15:37 <Dokujisan>	however
    Mar 05 11:15:46 <CuBe0wL>	pheonixgame.org is available!
    Mar 05 11:15:57 <Dokujisan>	I was already starting to plan the April Fools day mapping project
    Mar 05 11:16:14 <Dokujisan>	the halloween mapping thing failed, but last year's april fool's mapping project was a success
    Mar 05 11:16:21 <CuBe0wL>	hey
    Mar 05 11:16:29 <CuBe0wL>	I contributed to halloween :P
    Mar 05 11:16:39 <Dokujisan>	I know, but it was a failed project overall
    Mar 05 11:16:44 <CuBe0wL>	true
    Mar 05 11:18:35 <CuBe0wL>	btw... I'be just realised yesterday I could reopen the locked Illfonic's thread :D
    Mar 05 11:18:41 <CuBe0wL>	should I? >:D
    Mar 05 11:18:49 <Dokujisan>	oh they locked it?
    Mar 05 11:19:04 <Dokujisan>	that was quite a pointless thread
    Mar 05 11:19:38 <CuBe0wL>	lol Dokujisan are you reading the forum nowadays at all? :D
    Mar 05 11:19:43 <Dokujisan>	"I'd like to get feedback from you guys" ... "Ok, I hear your feedback, but it's going to change absolutely nothing. Do you have any other feedback?"
    Mar 05 11:20:00 <Dokujisan>	yeah I do a bit. not as much as I used to though
    Mar 05 11:20:15 <Dokujisan>	I usually scan just the map releases forum
    Mar 05 11:20:18 <Dokujisan>	which is...not active lately
    Mar 05 11:20:27 <CuBe0wL>	I'd like to get feedback abour OUR game, OUR, NOT YOURS, I DON'T GIVE A FLYING FUCK FOR THAT. :D
    Mar 05 11:21:13 <CuBe0wL>	oh, about maps, I think "Vociferous" is starting to get in shape...
    Mar 05 11:22:08 <Dokujisan>	this? http://www.alientrap.org/forum/viewtopic.php?f=19&t=4807
    Mar 05 11:23:18 <CuBe0wL>	yes
    Mar 05 11:23:20 <CuBe0wL>	http://alientrap.org/forum/viewtopic.php?p=75629#p75629
    Mar 05 11:23:20 <FruitieX>	BTW had this idea: http://en.wikipedia.org/wiki/Nu_(letter)
    Mar 05 11:23:26 <FruitieX>	what about NuNex? :P
    Mar 05 11:23:35 <FruitieX>	would be pronounced like "New Nex" wouldnt it
    Mar 05 11:23:49 <FruitieX>	well almost
    Mar 05 11:23:59 <Dokujisan>	hmm, I would really like to see a name that is it's own
    Mar 05 11:24:12 <Dokujisan>	a year from now, we're not going to be thinking "Nexuiz" anymore
    Mar 05 11:24:20 <Spaceman>	http://en.wikipedia.org/wiki/Phoenix_(mythology) 
    Mar 05 11:24:42 <Spaceman>	mentions "simurgh"
    Mar 05 11:25:02 <CuBe0wL>	I instantly associated with Nu with Elfen lied
    Mar 05 11:25:07 <CuBe0wL>	Elven Lied, sorry
    Mar 05 11:25:58 <mand1nga>	Nex Juice?
    Mar 05 11:26:04 <mand1nga>	:P
    Mar 05 11:26:08 <Spaceman>	NuNex -> nun ex
    Mar 05 11:26:17 <Dokujisan>	hey mand1nga :-) 
    Mar 05 11:26:19 <mand1nga>	Nü Nex
    Mar 05 11:26:23 <Dokujisan>	did you read the text file in the subject?
    Mar 05 11:26:24 <CuBe0wL>	http://bluejaunte.files.wordpress.com/2009/11/tactical_facepalm.jpg
    Mar 05 11:26:26 <mand1nga>	hey Doku
    Mar 05 11:26:42 <mand1nga>	most of it, but haven't finished yet
    Mar 05 11:26:59 <CuBe0wL>	I think I've had
    Mar 05 11:27:08 <CuBe0wL>	ooops
    Mar 05 11:27:10 <mand1nga>	and I agree on everything I read, I suppose we'd be on the same page
    Mar 05 11:27:19 <CuBe0wL>	sorry, I thikn I've edited the topic
    Mar 05 11:27:37 <CuBe0wL>	lemme check that link in my history
    Mar 05 11:27:51 *	CuBe0wL has changed the topic to: Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt
    Mar 05 11:27:54 <tZork>	tactical facepalm?
    Mar 05 11:28:03 <CuBe0wL>	for those idiot ideas
    Mar 05 11:28:05 <tZork>	thats...
    Mar 05 11:28:41 <CuBe0wL>	oh, one thing for models, if there be any... TAUNT ANIMATIONS!
    Mar 05 11:28:42 <Samual>	I've seen that before
    Mar 05 11:28:47 <CuBe0wL>	we need facepalm
    Mar 05 11:29:23 <mand1nga>	only when Samual talks
    Mar 05 11:29:27 <CuBe0wL>	some kind of a dance
    Mar 05 11:29:33 <mand1nga>	:>
    Mar 05 11:29:40 <Samual>	[11:29:48am] <mand1nga> only when Samual talks
    Mar 05 11:29:43 <Samual>	...
    Mar 05 11:29:57 <mand1nga>	I'm kidding you fool :P
    Mar 05 11:30:00 <CuBe0wL>	imagine pyria doing a sexy dance when you get fragged by her ;)
    Mar 05 11:30:03 <Samual>	>.>
    Mar 05 11:31:25 <Spaceman>	pyria has a sexy animation
    Mar 05 11:31:58 <Spaceman>	but I can't remember how to use it
    Mar 05 11:32:04 <CuBe0wL>	oO
    Mar 05 11:32:13 <CuBe0wL>	look at the codes pls
    Mar 05 11:32:19 <CuBe0wL>	I wanna see it :D
    Mar 05 11:32:22 <Spaceman>	ask MrBougo
    Mar 05 11:32:31 <mand1nga>	I like the idea of having three leaders
    Mar 05 11:32:37 <Spaceman>	F?nix
    Mar 05 11:33:09 <mand1nga>	I don't know who these leaders will be
    Mar 05 11:33:31 <Spaceman>	In Japan, the phoenix is called h?-? (kanji:"??") or fushich? (????), literally "Immortal Bird".
    Mar 05 11:33:50 <tZork>	stop putting in the same sentance. they to not belong.
    Mar 05 11:34:10 <tZork>	err stop puttin oyria and sexy *
    Mar 05 11:35:50 <Dokujisan>	ok guys... let's resume our name discussions.... please read this and PICK FROM THE LIST YOUR TOP CHOICES and send me your list. Keep in mind that you're picking the ones that don't completely suck. They dont have to be perfect, but they can give us a direction.
    Mar 05 11:35:52 <Dokujisan>	http://www.nullgaming.com/stuff/nexuiz_new_name.txt
    Mar 05 11:35:52 <mand1nga>	I'd like to have a strict anti-mikee policy on this project
    Mar 05 11:36:05 <tZork>	think this kbd is giving in. i usualy fark up words, but some go missing
    Mar 05 11:36:13 <tZork>	but now* 
    Mar 05 11:36:24 <mand1nga>	Dokujisan: I suggest to make a poll somewhere so we decide the name
    Mar 05 11:36:33 <Dokujisan>	mand1nga: we can get to that after you dwindle down
    Mar 05 11:36:35 <mand1nga>	unless it has been decided already
    Mar 05 11:36:45 <mand1nga>	dwindle?
    Mar 05 11:36:57 <Dokujisan>	we need to start with a bulk list. We still hve more brainstorming for names to do. This isn't the final list
    Mar 05 11:37:14 <Dokujisan>	but you guys picking from this list will help with future brainstorming
    Mar 05 11:37:58 <mand1nga>	Dokujisan: what do you mean by dwindle down?
    Mar 05 11:37:59 <Spaceman>	sexy pyria http://www.flickr.com/photos/23986967@N05/2506000688/in/set-72157605143265605/
    Mar 05 11:38:09 <Dokujisan>	mand1nga: reduce in number
    Mar 05 11:38:52 <mand1nga>	I still don't get it, can you rephrase please?
    Mar 05 11:39:05 <mand1nga>	Spaceman: come on she has no legs there :o
    Mar 05 11:39:18 <Dokujisan>	theree are 50 or so on that list. we need to reduce that to 10 or so
    Mar 05 11:39:53 <Spaceman>	I wasn't looking at her legs :p
    Mar 05 11:40:53 <mand1nga>	wow those names are crazy
    Mar 05 11:41:16 <Samual>	Honestly
    Mar 05 11:41:17 <mand1nga>	lol how about nexodus
    Mar 05 11:41:20 <Samual>	I think we could do Sexuiz
    Mar 05 11:41:30 <Samual>	I bet it would be the best opensource game of all time
    Mar 05 11:41:48 <Samual>	Open Arena already has the scene right now, but they're doing it wrong
    Mar 05 11:41:54 <Samual>	Needs moar graphix :X
    Mar 05 11:41:58 <mand1nga>	lol nexzilla wtf I can't take this list seriously
    Mar 05 11:42:30 <Dokujisan>	these are just for picking a direction and I included everything mentioned
    Mar 05 11:45:04 <Dokujisan>	ok CuBe0wL I looked at vociferous. I used to have this map on my HODM server. It has some flaws in this beta version, but you probably know that
    Mar 05 11:46:06 <Dokujisan>	like big long hallways with no place to evade, and teleporter exists look like teleporter entrances and that's a little confusing
    Mar 05 11:46:25 <CuBe0wL>	MY PICKS: nexetic, nexira, nexonic, xenotic. I gotta puke for all avaible ones, most of them sounds like medicine names. Also, some suggestions: Reborn, NeXT, Pheonix
    Mar 05 11:46:39 <Dokujisan>	noted
    Mar 05 11:46:58 <}-z-{>	http://dev.xonotic.org we can start getting organized here
    Mar 05 11:47:18 <mand1nga>	I think a word in japanese might fit as a new name
    Mar 05 11:47:39 <Samual>	Xenotic
    Mar 05 11:47:41 <mand1nga>	I'd like to try other things apart of random names including z and x
    Mar 05 11:47:41 <Samual>	I like that
    Mar 05 11:47:53 <Samual>	>.>
    Mar 05 11:47:58 <Dokujisan>	sure, we can get to foreign/non-english names. Right now, we're aiming for made-up words that have no meaning (like nexuiz was)
    Mar 05 11:48:00 <Samual>	lawl well I still like Xenotic.
    Mar 05 11:48:00 <FruitieX>	:P
    Mar 05 11:48:18 <mand1nga>	something like ryūshutsu :)
    Mar 05 11:48:29 <mand1nga>	(exodus in japanese)
    Mar 05 11:48:33 <Dokujisan>	"- We should have a name that people can pronounce"
    Mar 05 11:48:46 <mand1nga>	I know, that was a sample
    Mar 05 11:48:48 <Dokujisan>	otherwise, I'm not against using a japanese word
    Mar 05 11:49:05 <FruitieX>	I like Xenotic too somewhat :P
    Mar 05 11:49:12 <Dokujisan>	but let's start with one thing at a time. We can do another phase of searching for foreign names
    Mar 05 11:49:24 <Dokujisan>	after this step
    Mar 05 11:50:10 <FruitieX>	also remember we can postfix with "game"
    Mar 05 11:50:16 <FruitieX>	eg. xenoticgame.com is available
    Mar 05 11:50:29 <Dokujisan>	read the top of my names file
    Mar 05 11:50:29 <}-z-{>	too long
    Mar 05 11:50:34 <Dokujisan>	it says that is a plan B
    Mar 05 11:50:40 <FruitieX>	oh okay
    Mar 05 11:51:04 <Dokujisan>	FruitieX: is xenotic the only one on your list?
    Mar 05 11:51:07 <}-z-{>	Dokujisan: want to start moving that file to the wiki in dev.xonotic.org?
    Mar 05 11:51:13 <}-z-{>	that text file
    Mar 05 11:51:14 <Dokujisan>	absolutely
    Mar 05 11:51:19 <Dokujisan>	I want to move both of these
    Mar 05 11:51:29 <}-z-{>	I'll need more time with wordpress mu
    Mar 05 11:51:32 <Dokujisan>	k
    Mar 05 11:51:35 <}-z-{>	still trying to do my real work too :-P
    Mar 05 11:51:35 <mand1nga>	I'd rather sex.cankill.us :P
    Mar 05 11:51:38 <FruitieX>	nah i'll take a look at the others Dokujisan 
    Mar 05 11:51:44 <}-z-{>	mand1nga: it's just temporary :-P
    Mar 05 11:51:48 <CuBe0wL>	Zymotic
    Mar 05 11:51:50 <CuBe0wL>	:D
    Mar 05 11:51:51 <}-z-{>	was a short domain name I had already
    Mar 05 11:51:56 <mand1nga>	I vote for divox
    Mar 05 11:51:58 <FruitieX>	CuBe0wL: oold
    Mar 05 11:52:05 <}-z-{>	divx? :-P
    Mar 05 11:52:07 <mand1nga>	(totally kidding :P)
    Mar 05 11:52:08 <CuBe0wL>	divox eh?
    Mar 05 11:52:30 <CuBe0wL>	why not kinky, or diva
    Mar 05 11:52:40 <CuBe0wL>	tactical facepalm in....
    Mar 05 11:52:41 <CuBe0wL>	3
    Mar 05 11:52:42 <CuBe0wL>	2
    Mar 05 11:52:43 <CuBe0wL>	1
    Mar 05 11:52:44 <Dokujisan>	mand1nga: consider how strange the word "nexuiz" is and we found a way to appreciate it anyway over time
    Mar 05 11:52:48 *	CuBe0wL FACEPALM!
    Mar 05 11:53:17 <Dokujisan>	mand1nga: likewise, the new name we end up using might also have a name that grows on you (but is not spelled oddly and can be pronounced easily)
    Mar 05 11:53:19 <mand1nga>	Dokujisan: sure, but I say lets try other approaches too
    Mar 05 11:53:26 <mand1nga>	in an organized way of course
    Mar 05 11:53:29 <Dokujisan>	mand1nga: yep, as I said, we'll do that after this step
    Mar 05 11:53:42 <}-z-{>	superhappyfun game
    Mar 05 11:53:54 <Dokujisan>	greek, japanese and latin words are usually good for picking names
    Mar 05 11:54:24 <Dokujisan>	and as part of that, we can do a variation of a greek/japanese/latin word.... 
    Mar 05 11:54:29 <CuBe0wL>	Itoma?
    Mar 05 11:54:43 <FruitieX>	18:54:41 <@}-z-{> superhappyfun game
    Mar 05 11:54:45 <FruitieX>	dot com
    Mar 05 11:54:49 <CuBe0wL>	means "free" in Japan, and also a wave goodbye
    Mar 05 11:55:07 <FruitieX>	:o that sounds good CuBe0wL 
    Mar 05 11:55:20 <CuBe0wL>	also, it means free time too :D
    Mar 05 11:55:27 <FruitieX>	haha
    Mar 05 11:55:33 <Dokujisan>	that's better than pheonix :-)
    Mar 05 11:55:51 <CuBe0wL>	or spare time :)
    Mar 05 11:56:59 <mand1nga>	well I kinda like one name on the list: zeonix but I'm sure I'd like more a random japanese word
    Mar 05 11:57:02 <CuBe0wL>	but itoma domain is taken
    Mar 05 11:57:19 <SoulKeeper_p>	ItomaFPS is free, domain seo wise.
    Mar 05 11:57:27 <FruitieX>	itomagame :P
    Mar 05 11:57:35 <FruitieX>	is free both com and org
    Mar 05 11:59:20 <CuBe0wL>	Itoma feels... both odd and cool at the same time
    Mar 05 11:59:36 <FruitieX>	yeh
    Mar 05 11:59:43 <CuBe0wL>	Toritoma? :D
    Mar 05 11:59:49 <mand1nga>	it feels odd at one time for me :P
    Mar 05 11:59:49 <CuBe0wL>	sounds like tomato
    Mar 05 12:00:03 <FruitieX>	Nexitoma? :P
    Mar 05 12:00:10 <mand1nga>	kontesuto = contest
    Mar 05 12:00:17 <CuBe0wL>	too long
    Mar 05 12:00:28 <mand1nga>	sokudo = speed
    Mar 05 12:00:37 <esteel>	meh, connection on the train is really bad atm..
    Mar 05 12:00:39 <CuBe0wL>	or simply... Tori?
    Mar 05 12:00:44 <CuBe0wL>	hi esteel 
    Mar 05 12:00:49 <esteel>	hi CuBe0wL 
    Mar 05 12:00:54 <CuBe0wL>	Tori means "bird" if I'm not mostaken
    Mar 05 12:00:56 <tZork>	sudoku? :S
    Mar 05 12:01:01 <FruitieX>	CuBe0wL: that makes me think of the game Toribash
    Mar 05 12:01:01 <FruitieX>	:P
    Mar 05 12:01:10 <CuBe0wL>	me too, but that's cool :D
    Mar 05 12:01:30 *	pavlvs (pavlvs@75.39.134.107) has joined #notnexuiz
    Mar 05 12:01:58 <pavlvs>	yo
    Mar 05 12:02:04 <tZork>	hi pavlvs
    Mar 05 12:02:12 <pavlvs>	hi tZork 
    Mar 05 12:02:44 <CuBe0wL>	Saikai? it means resumption
    Mar 05 12:02:45 <mand1nga>	hi pavlvs 
    Mar 05 12:02:59 <pavlvs>	hm looks like almost everyone necessary is in here
    Mar 05 12:03:31 <Dokujisan>	:-)
    Mar 05 12:03:34 <CuBe0wL>	I was just going to tell ask :D
    Mar 05 12:03:38 <CuBe0wL>	afk I mean
    Mar 05 12:03:43 <CuBe0wL>	I'm starving :(
    Mar 05 12:04:02 <CuBe0wL>	I'll go check and see what can I find in the deep freezer
    Mar 05 12:04:04 <FruitieX>	Really though, Itoma sounded nice :-)
    Mar 05 12:04:48 <FruitieX>	dunno
    Mar 05 12:04:59 <Dokujisan>	it's up there
    Mar 05 12:05:06 <Dokujisan>	in quality, I mean
    Mar 05 12:05:10 <Dokujisan>	I haven't added it yet
    Mar 05 12:05:34 <}-z-{>	erosdon't see anyone registered yet
    Mar 05 12:05:38 <}-z-{>	don't*
    Mar 05 12:05:42 <Dokujisan>	I just did
    Mar 05 12:05:49 <Dokujisan>	but does it sent a confirmation email?
    Mar 05 12:05:54 <}-z-{>	it should
    Mar 05 12:06:07 <FruitieX>	registering domains already? :o
    Mar 05 12:06:12 <}-z-{>	no
    Mar 05 12:06:17 <}-z-{>	just using a temp one to get organized
    Mar 05 12:06:38 <FruitieX>	right
    Mar 05 12:06:39 <}-z-{>	Dokujisan: I activiated you
    Mar 05 12:06:41 <Dokujisan>	ok
    Mar 05 12:06:52 <}-z-{>	and made you admin
    Mar 05 12:07:01 <}-z-{>	did you set a password, do you need a password?
    Mar 05 12:07:08 <esteel>	tori? saikai? loking for new names?  Superiuz.. similar to superior :P
    Mar 05 12:07:10 <Dokujisan>	I'm in
    Mar 05 12:07:33 <CuBe0wL>	too bad there's Toribash
    Mar 05 12:07:44 <CuBe0wL>	Tori would be a nice pick
    Mar 05 12:08:56 <CuBe0wL>	esteel, what kind of irc client do you use? mirggi?
    Mar 05 12:09:19 <}-z-{>	Dokujisan: I hit a bump in the road
    Mar 05 12:09:20 <}-z-{>	NOTICE
    Mar 05 12:09:25 <}-z-{>	"WordPress MU is not allowed to be run on our shared hosting servers. If you intend on running this under your account, you are required to be on a Private Server"
    Mar 05 12:09:41 <Dokujisan>	:-o
    Mar 05 12:09:45 <Dokujisan>	hmmm
    Mar 05 12:09:51 <Dokujisan>	so do I need to host it?
    Mar 05 12:10:09 <Dokujisan>	and give you access
    Mar 05 12:10:16 <CuBe0wL>	brb
    Mar 05 12:10:26 <}-z-{>	can you give me SSH and PHPMyAdmin?
    Mar 05 12:11:14 <Dokujisan>	hmm... well is this going to end up as a permanent solution?
    Mar 05 12:11:18 <Dokujisan>	or just a temporary thing
    Mar 05 12:11:22 <}-z-{>	perm
    Mar 05 12:11:30 <Dokujisan>	ok let me think about that.....
    Mar 05 12:11:50 <}-z-{>	okay, I'm looking into Dreamhost PS
    Mar 05 12:11:58 <}-z-{>	I don't want to put mu on the would be build server
    Mar 05 12:12:15 <esteel>	CuBe0wL: weechat
    Mar 05 12:12:39 <}-z-{>	man dh ps is 'spensive
    Mar 05 12:12:45 <}-z-{>	might as well buy another VPS at that price lol
    Mar 05 12:12:54 <}-z-{>	minimum is $15/mo for 150mb
    Mar 05 12:13:04 <CuBe0wL>	}-z-{, what will you do with nexuiz ninjaz btw ?
    Mar 05 12:13:20 <}-z-{>	I can fork that 'the ninjaz'
    Mar 05 12:13:32 <}-z-{>	and be more general but put most of my efforts towards this project
    Mar 05 12:13:40 <Spaceman>	ItomaNinjaz?
    Mar 05 12:13:49 <}-z-{>	maybe illfonic will offer money for the domain and we can pay for the build server for a year :-P
    Mar 05 12:14:05 <CuBe0wL>	{X}ItomaNinjaz ? :D
    Mar 05 12:14:35 <esteel>	hey, where are all those names coming from? :P
    Mar 05 12:15:04 <}-z-{>	Dokujisan: it's probably best if we do a separate VPS or dedicated anyway, it's better to have full control over apache for this
    Mar 05 12:15:15 <pavlvs>	i can consider something
    Mar 05 12:15:24 <Samual>	Well
    Mar 05 12:15:28 <Samual>	I have a VPS too
    Mar 05 12:15:31 <Samual>	Actually I have two
    Mar 05 12:15:48 <Samual>	Although I don't personally own them :P
    Mar 05 12:15:50 <Dokujisan>	}-z-{: yes I would think that is best
    Mar 05 12:15:54 <}-z-{>	probably need 512mb RAM, multicore processor prefered, 5gb MINIMUM but want ~20 to be comfortable
    Mar 05 12:15:56 <Samual>	I'd have to ask the owner if we could use them if needed.
    Mar 05 12:16:01 <}-z-{>	gb space
    Mar 05 12:16:27 <Samual>	My server has 728mb memory, 20GB hard drive, and it's a quad core (They fucked up, it was supposed to be dual core)
    Mar 05 12:16:31 <Samual>	Er
    Mar 05 12:16:35 <Samual>	768*
    Mar 05 12:16:37 <}-z-{>	yes but it's not dedicated to this, correct?
    Mar 05 12:16:50 <Samual>	Well, right now it just runs my Nexuiz server :P
    Mar 05 12:16:53 <pavlvs>	hm
    Mar 05 12:16:59 <Samual>	Which takes up all of 100mb of the ram :P
    Mar 05 12:17:06 <pavlvs>	wthis is neede for something processing intensive?
    Mar 05 12:17:07 <CuBe0wL>	brb, I need to boild my veegtable dish I've found in the fridge
    Mar 05 12:17:08 *	merlijn (merlijn@84.245.21.196) has joined #notnexuiz
    Mar 05 12:17:56 <}-z-{>	pavlvs: just apache and mysql
    Mar 05 12:18:01 <}-z-{>	which _can_ be processor intensive
    Mar 05 12:18:05 <}-z-{>	but not necessarily
    Mar 05 12:18:15 <}-z-{>	I propose we keep the development site on another server
    Mar 05 12:18:27 <}-z-{>	because running rails on top of apache will kill our resources a bit
    Mar 05 12:18:27 <Dokujisan>	ok I just chatted with dublpaws and he is willing to give Dance a makeover to have it considered for inclusion in the game
    Mar 05 12:18:45 <}-z-{>	also, if one site goes down, we can still communicate to users via the other
    Mar 05 12:18:46 <Dokujisan>	and if anyone wants to help him with that, collaborate, he is open to that
    Mar 05 12:18:57 <pavlvs>	}-z-{: [prae] has a dual quad with 8gb ram, soon to be 12gb
    Mar 05 12:19:04 <tZork>	728 megs on a quad? wth=
    Mar 05 12:19:08 <}-z-{>	wow yeah, that'd be very helpful :-P
    Mar 05 12:19:16 <}-z-{>	that's fully dedicated I assume?
    Mar 05 12:19:21 <Samual>	tZork, it was supposed to be a dual core :P
    Mar 05 12:19:22 <pavlvs>	yes colo'd
    Mar 05 12:19:26 <}-z-{>	very nice
    Mar 05 12:19:28 <}-z-{>	what OS?
    Mar 05 12:19:34 <pavlvs>	}-z-{: i run xen so i could spin up a VM sometime
    Mar 05 12:19:36 <tZork>	its still ftw Samual
    Mar 05 12:19:38 <pavlvs>	debian
    Mar 05 12:19:51 <}-z-{>	okay
    Mar 05 12:20:02 <}-z-{>	debian or ubuntu should be good
    Mar 05 12:20:13 <}-z-{>	can you give me ssh and possbily sudo?
    Mar 05 12:20:17 <tZork>	Samual: rented, virtual? tahtäd explain it..
    Mar 05 12:20:24 <pavlvs>	of course
    Mar 05 12:20:28 <}-z-{>	awesome
    Mar 05 12:20:31 <pavlvs>	such is the beauty of vm's
    Mar 05 12:20:33 <Dokujisan>	perfect :-)
    Mar 05 12:20:35 <}-z-{>	:)
    Mar 05 12:20:40 <Samual>	Virtual and rented
    Mar 05 12:20:44 <Dokujisan>	pavlvs: if you host that, then I think I can continue hosting HOCTF/HODM
    Mar 05 12:20:45 <pavlvs>	but yeah ill have to see if we have resources available
    Mar 05 12:21:03 <}-z-{>	what they hell else can you be using all those resources for? :-P
    Mar 05 12:21:04 <Dokujisan>	actually, I would prefer to now with this fork
    Mar 05 12:21:22 <Dokujisan>	I was planning on transitioning my servers over to pavlvs
    Mar 05 12:21:30 <Dokujisan>	HOCTF/HODM
    Mar 05 12:21:38 <pavlvs>	need about $30-40 more in my ram fund to get to that 12gb
    Mar 05 12:21:52 <}-z-{>	you're really using 8gb already?
    Mar 05 12:22:20 <}-z-{>	you gotta be running at least 18 nexuiz servers for that :-P
    Mar 05 12:22:26 <pavlvs>	well, if i were to run all the nexuiz servers i was planning on running
    Mar 05 12:22:33 <pavlvs>	which is 15
    Mar 05 12:22:37 <pavlvs>	;p
    Mar 05 12:22:39 <}-z-{>	I can run 10 servers under 2gb
    Mar 05 12:22:54 <pavlvs>	i also have 3 tf2 servers and a l4d2 server
    Mar 05 12:22:58 <}-z-{>	ah well
    Mar 05 12:23:02 <}-z-{>	that's another story :-P
    Mar 05 12:23:02 <pavlvs>	and email and various apaches
    Mar 05 12:23:07 <Dokujisan>	oh...this is perfect, because pavlvs also runs a mumble server
    Mar 05 12:23:12 <pavlvs>	the zimbra takes ridiculous ram
    Mar 05 12:23:13 <}-z-{>	ah nice
    Mar 05 12:23:15 <pavlvs>	yes
    Mar 05 12:23:19 <pavlvs>	praeclan.com
    Mar 05 12:23:19 <}-z-{>	yeah, I've heard zimbra is a hog
    Mar 05 12:23:20 <tZork>	Samual: less of a prob then since its likely not 728 total mem. the thing is a modern cpu (onr core) easly chug tough a gig of ram proccessing its stuff. less then one g per code oin a didecated is just stupid. 
    Mar 05 12:23:27 <merlijn>	hiya, I'm just trying to read up on the stuff that happened, any other stuff besides topic I should read?
    Mar 05 12:23:39 <Dokujisan>	pavlvs: we talked about having an official mumble server for the game
    Mar 05 12:23:42 <}-z-{>	pavlvs: how soon can this be ready for our use?
    Mar 05 12:23:50 <tZork>	hi merlijn
    Mar 05 12:23:54 <Dokujisan>	but I dont' think mumble uses much in terms of resources
    Mar 05 12:23:56 <pavlvs>	i guess i dont have plans tonight...
    Mar 05 12:23:57 <CuBe0wL>	re
    Mar 05 12:24:05 <merlijn>	also I can provide any server stuff you're needing
    Mar 05 12:24:17 <Dokujisan>	hey merlijn :-D
    Mar 05 12:24:38 *	}-z-{ has changed the topic to:  Details so far -- http://www.nullgaming.com/stuff/nexuiz_new_notes.txt  -- http://dev.xonotic.org -- temporary development site to get organized
    Mar 05 12:24:40 <Dokujisan>	merlijn: that file in the topic is a pretty good overview
    Mar 05 12:24:50 <}-z-{>	Dokujisan: should I make dev.xonotic.org register only for now?
    Mar 05 12:24:59 <Dokujisan>	yes
    Mar 05 12:25:06 <Dokujisan>	good call
    Mar 05 12:25:09 <merlijn>	I still don't get what the main reason for forking is, just getting rid of vermeulen/alientrap?
    Mar 05 12:25:21 <}-z-{>	that's a large part
    Mar 05 12:25:21 <Dokujisan>	merlijn: well there are a lot of reasons actually
    Mar 05 12:25:31 <Dokujisan>	to me, this is actually a chance for a clean slate
    Mar 05 12:25:31 <}-z-{>	but we're already streamlining a lot of things
    Mar 05 12:25:53 <FruitieX>	BTW maps, what about race maps?
    Mar 05 12:26:00 <Dokujisan>	if you read through those notes, you'll see a lot of ideas have been put forth, including a structure for how the game is managed
    Mar 05 12:26:03 <Dokujisan>	which nexuiz never had
    Mar 05 12:26:04 <FruitieX>	we should probably skip the piece-o-cake map
    Mar 05 12:26:05 <CuBe0wL>	+1 for race
    Mar 05 12:26:09 <FruitieX>	in fact, probably no nexrun maps at all
    Mar 05 12:26:13 <FruitieX>	in the official release
    Mar 05 12:26:22 <Dokujisan>	FruitieX: I know nothing about race maps, so let me know what you guys come up with
    Mar 05 12:26:30 <CuBe0wL>	why, they are good, and GPL'ed
    Mar 05 12:26:34 <FruitieX>	or depends, if anyone's interested in having nexrun as a "havoc mode" replacement :P
    Mar 05 12:26:35 <merlijn>	we've had multiple attempts at streamlining and better organisation - why is this one going to work?
    Mar 05 12:26:56 <}-z-{>	Dokujisan: I've started the wiki for the plan here: http://dev.xonotic.org/projects/notnexuiz/wiki/Plan
    Mar 05 12:27:08 <}-z-{>	just a dump of your text file right now
    Mar 05 12:27:09 <merlijn>	btw, I'm not being negative just some healthy scepticism :)
    Mar 05 12:27:19 <FruitieX>	development can kill us
    Mar 05 12:27:21 <FruitieX>	:P
    Mar 05 12:27:23 <}-z-{>	:-P
    Mar 05 12:27:44 <Dokujisan>	thanks }-z-{ 
    Mar 05 12:27:57 <}-z-{>	I'll help you clean it up a bit
    Mar 05 12:28:10 <}-z-{>	pavlvs: do you have an IP I can set an A record for?
    Mar 05 12:28:13 <CuBe0wL>	one thing I really suggest we should inform the community on the forum of our forking plan ASAP
    Mar 05 12:28:18 <}-z-{>	for the temporary domain name
    Mar 05 12:28:27 <}-z-{>	CuBe0wL: I'd like to get more organized first
    Mar 05 12:28:38 <pavlvs>	}-z-{: we'll have to figure out ip/domain stuff 
    Mar 05 12:28:40 <}-z-{>	so we don't come off as a bunch of idiots
    Mar 05 12:28:43 <}-z-{>	okay pavlvs 
    Mar 05 12:28:44 <Dokujisan>	merlijn: I think it's because we're starting from scratch with organization. I lost interest in Nexuiz 8-9 months ago, but this gives me a surge of interest again, and I think that is probably the same for others
    Mar 05 12:28:44 <pavlvs>	its a bid weird with my xen config
    Mar 05 12:28:58 <}-z-{>	I should be able to add an A record and you can do a virtual host on apache
    Mar 05 12:29:03 <pavlvs>	}-z-{: i need to do some homework and go to class, i'll be back at 5 EST
    Mar 05 12:29:08 <}-z-{>	okay pavlvs 
    Mar 05 12:29:16 <pavlvs>	}-z-{: also i have a bind server if that helps
    Mar 05 12:29:34 <Dokujisan>	merlijn: I've always wanted a nexuiz fork because of this very problem of lack-of-management and leadership for the game. But now it appears that everyone is onboard with plans to do everything Nexuiz should have had.
    Mar 05 12:29:46 <}-z-{>	yes pavlvs it will for wordpress mu
    Mar 05 12:29:55 <merlijn>	Dokujisan: new ideas usually generate a lot of energy at first, question is whether that will stay
    Mar 05 12:29:56 <pavlvs>	wight
    Mar 05 12:29:59 <}-z-{>	so we can setup subdomains
    Mar 05 12:30:01 <}-z-{>	and such
    Mar 05 12:30:18 <pavlvs>	well then the nameserver is 208.94.245.226
    Mar 05 12:30:21 <}-z-{>	Dokujisan: give me 5 minutes to clean up this wiki page, then have it
    Mar 05 12:30:27 <pavlvs>	praeclan.com
    Mar 05 12:30:34 <Dokujisan>	merlijn: well the goal with my ideas is to establish methods for how things will work....so that will carry the momentum
    Mar 05 12:30:42 <}-z-{>	pavlvs: I'd prefer if I can use use an arecord to you machines IP
    Mar 05 12:30:54 <}-z-{>	so I can leave DNS on dreamhost which is currently serving dev.xonotic.org
    Mar 05 12:31:01 <pavlvs>	okie
    Mar 05 12:31:03 <}-z-{>	A record*
    Mar 05 12:31:13 <Dokujisan>	merlijn: I'm going to be doing a lot of the community organization and part of that involves delegating and recruiting. As we recruit, those new people add even more energy to the project
    Mar 05 12:31:17 <}-z-{>	do you know how to handle apache virtual hosts?
    Mar 05 12:31:46 <merlijn>	Dokujisan: and what about the nexuiz name? wouldn't it at least me a good idea to benefit from the promotion on the IllFonic side of things?
    Mar 05 12:32:10 <Dokujisan>	merlijn: the promotion of "Nexuiz" by illfonic will only benefit Illfonic's name.
    Mar 05 12:32:24 <tZork>	got b33r? - http://tzork.dvrdns.org/tmp/gotbeer.jpg :D
    Mar 05 12:32:27 <Dokujisan>	a year from now, when googling for "Nexuiz", people will start to find the game by Illfonic
    Mar 05 12:32:30 <merlijn>	Dokujisan: why are you so sure about that?
    Mar 05 12:32:34 <Dokujisan>	and it will be harder to find "our" game
    Mar 05 12:32:57 <merlijn>	maybe, but a new game will be hard to find anyway
    Mar 05 12:33:41 <Dokujisan>	the fact that they have nexuiz.com alone is bad enough. When people try to find our Nexuiz game (assuming they hear about it) they will end up on Nexuiz.com and that will be all console stuff.
    Mar 05 12:33:46 <CuBe0wL>	I don't think so
    Mar 05 12:34:09 <CuBe0wL>	I was repying to merlijn 
    Mar 05 12:34:18 <esteel>	i do.. or at least that tiiiiiny 'pc nexuiz' link currently on is a bad sign..
    Mar 05 12:34:53 <Morphed>	tiny and gray 
    Mar 05 12:35:06 <mand1nga>	aww tZork 
    Mar 05 12:35:07 <CuBe0wL>	unimportant
    Mar 05 12:35:18 <Morphed>	very importand 
    Mar 05 12:35:25 <}-z-{>	really hate that redmin crosses out my name
    Mar 05 12:35:32 <Morphed>	also bottom right corner is worst place on website 
    Mar 05 12:35:39 <}-z-{>	anyway, Dokujisan http://dev.xonotic.org/projects/notnexuiz/wiki/Plan updated
    Mar 05 12:35:44 <}-z-{>	now wiki styled
    Mar 05 12:35:53 <Dokujisan>	awesome
    Mar 05 12:36:05 *	CuBe0wL requests login
    Mar 05 12:36:10 <}-z-{>	CuBe0wL: register ;)
    Mar 05 12:36:16 <}-z-{>	I will approve you
    Mar 05 12:36:27 <}-z-{>	that goes for everyone
    Mar 05 12:36:33 <merlijn>	hmm, I see some people in that list that I didn't even know were part of the nexuiz community
    Mar 05 12:36:39 <}-z-{>	this site will migrate to the official one when we determine a name and register a domain
    Mar 05 12:36:40 <merlijn>	like jayvee
    Mar 05 12:36:43 <Dokujisan>	so basically "our nexuiz" is left to be an asterisk next to the big "Nexiuz" that now has a marketing budget with a for-profit company behind it
    Mar 05 12:36:59 <Dokujisan>	we would be competing for attention
    Mar 05 12:37:02 <Dokujisan>	without the nexuiz.com domain
    Mar 05 12:37:03 <tZork>	mand1nga: messy still, but i still havent built it all yet. when its done it will be a compleat pub with beer pump and all. and homemade beer, wich is what im testing now =)
    Mar 05 12:37:06 <}-z-{>	"a link back to the gpl nexuiz will remain on our website FOR MARKETING PURPOSES"
    Mar 05 12:37:12 <}-z-{>	is what illfonic said
    Mar 05 12:37:26 <}-z-{>	I think that summarizes their view of our game
    Mar 05 12:37:34 <pavlvs>	maybe they meant for marketing of gpl nexuiz?
    Mar 05 12:37:40 <}-z-{>	;o) maybe
    Mar 05 12:37:47 <Morphed>	im sure they did :P
    Mar 05 12:38:02 <esteel>	still, i think vermeulen screwed up pretty hard by his overscretcy..
    Mar 05 12:38:09 <esteel>	too much bad blood already
    Mar 05 12:38:20 <Dokujisan>	with this new fork, we'll NEVER be in a position like this again
    Mar 05 12:38:25 <Dokujisan>	ever
    Mar 05 12:38:27 <mand1nga>	tZork: that's amazing :)
    Mar 05 12:38:27 <}-z-{>	yes and hasn't worked hard enough to fix it
    Mar 05 12:38:40 <}-z-{>	he seems to be spreading lies about some things too
    Mar 05 12:38:50 <}-z-{>	claimed to have run a fundraiser for div0???
    Mar 05 12:38:55 <}-z-{>	wtf, I never heard of that and neither did div0
    Mar 05 12:39:34 <tZork>	agreed esteel, if this had been done with.. hell even just a polite tone it would never got this offensive.
    Mar 05 12:39:34 <esteel>	}-z-{: well to be fair i can imagine he is pretty busy atm.. still, it should have been better
    Mar 05 12:40:02 <Morphed>	who cares if he is busy ? he got paid to do it
    Mar 05 12:40:22 <mand1nga>	its a bloody vampire
    Mar 05 12:40:35 <}-z-{>	alright, I need to grab some lunch
    Mar 05 12:40:36 <tZork>	"to bzy to stand in line; shot the otehrs before me" 
    Mar 05 12:40:37 <}-z-{>	bbl
    Mar 05 12:40:45 <tZork>	dont think the law will accept that
    Mar 05 12:40:51 <}-z-{>	vermeulen doesn't seem like the type to fall on his sword
    Mar 05 12:40:59 <esteel>	tZork: hehe
    Mar 05 12:41:01 <}-z-{>	but rather throw his team under the bus
    Mar 05 12:41:49 <esteel>	btw, have registered..
    Mar 05 12:42:06 <CuBe0wL>	tZork, once you have something edible, tell me :) I'll pay for the shipment price, but I want to taste your b33r :D
    Mar 05 12:42:16 <merlijn>	but speaking of legal matters - the fork has to be GPL and nobody is stopping anyone from merging our code into the old nexuiz
    Mar 05 12:42:31 <CuBe0wL>	I just hope it's not made the way the sweet lemanode is made in shut up woman, get on my horse ;)
    Mar 05 12:42:49 <tZork>	CuBe0wL: its quite ok acctualy, but a bti thin this time. still learning =)
    Mar 05 12:42:51 <CuBe0wL>	merlijn, so?
    Mar 05 12:42:52 <Dokujisan>	merlijn: they are supposedly dealing with that. I think they are only using DP code and not Nexuiz code, or not very much Nexuiz game code? Something like that.
    Mar 05 12:43:22 <merlijn>	what if Vermeulen wants to keep "his" nexuiz alive and imports our changes?
    Mar 05 12:43:22 <Dokujisan>	and LH made it seem like they were dealing with the permission aspect of relicensing contributed code
    Mar 05 12:43:23 <tZork>	no Dokujisan
    Mar 05 12:43:39 <Dokujisan>	tZork: they are using game code?
    Mar 05 12:43:39 <tZork>	if we want to release fast we basicaly have to use nexuiz gamecode
    Mar 05 12:43:48 <tZork>	oh they
    Mar 05 12:43:49 <Dokujisan>	oh I don't mean us. I meant illfonic
    Mar 05 12:43:52 <tZork>	as in ill*
    Mar 05 12:44:01 <tZork>	tehy use nexuiz gamecode too
    Mar 05 12:44:05 <tZork>	afaik
    Mar 05 12:44:05 <Dokujisan>	I see
    Mar 05 12:44:16 <tZork>	or well tehy do
    Mar 05 12:44:19 <tZork>	lh said so
    Mar 05 12:44:58 <Morphed>	merlijn, then we will let ppl know about it on slashdot and gain free marketing 
    Mar 05 12:45:11 <tZork>	with some unusual elements ripped out, liek my turrets.
    Mar 05 12:45:17 <merlijn>	also, since we're reorganizing stuff - can we PLEASE have mailing lists?
    Mar 05 12:45:27 <Dokujisan>	Does anyone here want to collaborate with Dublpaws to give "dance" a makeover?
    Mar 05 12:45:34 <Dokujisan>	FruitieX: ?
    Mar 05 12:45:40 <CuBe0wL>	to be back ontopic with the name: I think the best would be to let the original Nexuiz community (or at least the part that follwos us) to decide about the name of the new project. this would mean it's truly "ours", it's the community's project. The best would be to make a list we put together, and let the masses decide about the name
    Mar 05 12:45:57 <Dokujisan>	we can't make the name choice public
    Mar 05 12:46:04 <CuBe0wL>	why?
    Mar 05 12:46:04 <Dokujisan>	people will grab domains faster than we can blink
    Mar 05 12:46:11 <Spaceman>	merlijn: that is an interesting idea
    Mar 05 12:46:13 <CuBe0wL>	I see
    Mar 05 12:46:19 <tZork>	unfortunatly Dokujisan is right
    Mar 05 12:46:32 <CuBe0wL>	technical aspect, I understand
    Mar 05 12:46:33 <Dokujisan>	we need to make sure we solidify our decision AND make sure we have the domains we need (and IRC channels or whatever) before announcing
    Mar 05 12:46:36 <FruitieX>	Dokujisan: I could
    Mar 05 12:46:43 <FruitieX>	never really played the map much though
    Mar 05 12:46:52 <tZork>	n00b!
    Mar 05 12:46:52 <Dokujisan>	FruitieX: it's pretty popular on my HOCTF server
    Mar 05 12:46:55 <tZork>	;)
    Mar 05 12:47:07 <FruitieX>	yep i know
    Mar 05 12:47:11 <FruitieX>	what, n00b? :P
    Mar 05 12:47:15 <FruitieX>	only played pickup duels ;)
    Mar 05 12:47:16 <tZork>	its a decent map
    Mar 05 12:47:18 <FruitieX>	and tdm/ctf
    Mar 05 12:47:26 <tZork>	see? noob! :D
    Mar 05 12:47:30 *	merlijn votes for kicking FruitieX for not knowing every square qu of dance by heart
    Mar 05 12:47:31 <CuBe0wL>	:D
    Mar 05 12:47:39 <Spaceman>	:)
    Mar 05 12:47:42 <tZork>	haha
    Mar 05 12:47:49 <CuBe0wL>	umm... I don't know the map either :D
    Mar 05 12:47:53 <CuBe0wL>	at least not by name
    Mar 05 12:48:10 <CuBe0wL>	sure I'd recognise it form a screenshot
    Mar 05 12:48:17 <tZork>	http://rm.endoftheinternet.org/~nexuiz/maps/mapshots/dance.jpg
    Mar 05 12:48:22 <FruitieX>	but in pickup ctf, they only play runningmanctf, castle, mikectf2/3, facing, greatwall
    Mar 05 12:48:25 <FruitieX>	:P
    Mar 05 12:48:29 <CuBe0wL>	oh yes
    Mar 05 12:48:33 <}-z-{>	esteel and Morphed, you've been approved on teh dev system
    Mar 05 12:48:34 <CuBe0wL>	how do I hate it :D
    Mar 05 12:48:38 <tZork>	FruitieX: sadly yes
    Mar 05 12:48:41 <mand1nga>	dance is fun :)
    Mar 05 12:48:48 <mand1nga>	}-z-{: you can add me too if you want
    Mar 05 12:48:53 <}-z-{>	mand1nga: you have to sign up
    Mar 05 12:48:56 <}-z-{>	I activate the accounts
    Mar 05 12:48:58 <FruitieX>	seems like a fun project to remake
    Mar 05 12:48:58 <tZork>	FruitieX: not bad maps, but its so limited
    Mar 05 12:49:00 <mand1nga>	okay
    Mar 05 12:49:03 <Dokujisan>	FruitieX: can you join #nexuiz.nct on quakenet? I'm inviting dublpaws there
    Mar 05 12:49:05 <FruitieX>	indeed tZork 
    Mar 05 12:49:22 <}-z-{>	Dokujisan: I will give you ssh to the redmine server after we decide on the name and go forward for real
    Mar 05 12:49:26 <FruitieX>	can you invite him to #nexuiz.editing instead? :P
    Mar 05 12:49:36 *	CuBe0wL registered too
    Mar 05 12:49:42 <}-z-{>	I don't imagine you'll need it for much but it's a "just in case" sort of thing
    Mar 05 12:49:49 <}-z-{>	I should be able to handle maintainence and backups
    Mar 05 12:50:16 *	CuBe0wL gives channel operator status to esteel mand1nga merlijn pavlvs
    Mar 05 12:50:16 *	CuBe0wL gives channel operator status to Taoki
    Mar 05 12:50:22 <}-z-{>	mand1nga: CuBe0wL, you'd been activated
    Mar 05 12:50:29 <merlijn>	again if you need server capacity, I can easily plug in a bunch of servers at work
    Mar 05 12:50:34 <CuBe0wL>	is this btw. the full "developer" group ?
    Mar 05 12:50:36 *	FruitieX registered three
    Mar 05 12:50:41 <}-z-{>	CuBe0wL: not yet I don't think
    Mar 05 12:50:44 <mand1nga>	ty zee
    Mar 05 12:50:45 <}-z-{>	please check the wiki page
    Mar 05 12:50:46 <FruitieX>	not yet
    Mar 05 12:50:50 <FruitieX>	e.g. MrBougo missing
    Mar 05 12:50:56 <}-z-{>	merlijn: that's good to know, we will keep that in mind
    Mar 05 12:51:02 <FruitieX>	well i think :p
    Mar 05 12:51:03 <esteel>	hmm, ill need new domain too.. planetXYZ.de :P
    Mar 05 12:51:16 <tZork>	hm reg where? 
    Mar 05 12:51:30 <}-z-{>	http://dev.xonotic.org is the temp development site for us to get organized at
    Mar 05 12:51:34 <CuBe0wL>	Application error
    Mar 05 12:51:34 <CuBe0wL>	Rails application failed to start properly :D
    Mar 05 12:51:38 <merlijn>	we'd actually have to hijack lots of nexuiz domains and forward that to the new game :P
    Mar 05 12:51:41 <}-z-{>	where? CuBe0wL ?
    Mar 05 12:51:48 <CuBe0wL>	http://dev.xonotic.org/my/page
    Mar 05 12:51:56 <}-z-{>	works for me
    Mar 05 12:51:57 <}-z-{>	refresh
    Mar 05 12:52:01 <tZork>	urlcatch totaly faild that. freeky.
    Mar 05 12:52:26 <FruitieX>	Invalid user or password
    Mar 05 12:52:27 <FruitieX>	gah
    Mar 05 12:52:31 <FruitieX>	just registered
    Mar 05 12:52:36 <FruitieX>	do you have to approve it?
    Mar 05 12:52:40 <esteel>	merlijn: like which domains?
    Mar 05 12:53:01 <merlijn>	esteel: well your planetnexuiz.de for example :P
    Mar 05 12:53:45 <merlijn>	there needs to be a way for people that search for nexuiz to find the forked game
    Mar 05 12:54:20 <FruitieX>	indeed
    Mar 05 12:54:31 <FruitieX>	DCC delight are luckers :]
    Mar 05 12:54:41 <FruitieX>	Nexrun might need to change name too
    Mar 05 12:54:56 <Spaceman>	and the Nex weapon
    Mar 05 12:55:02 <FruitieX>	:p
    Mar 05 12:55:06 <merlijn>	just delete the nex
    Mar 05 12:55:08 <merlijn>	:P
    Mar 05 12:55:11 <Spaceman>	+1
    Mar 05 12:55:15 <esteel>	FruitieX: do you mean the mod? maybe a general mode-name like "runners" would be good?
    Mar 05 12:55:41 <CuBe0wL>	}-z-{, Nexuiz Admins wuzzat ?
    Mar 05 12:55:49 <CuBe0wL>	you mean server admins ?
    Mar 05 12:55:55 <Spaceman>	some flag textures will need to change
    Mar 05 12:55:57 <}-z-{>	Dokujisan: will have to clarify
    Mar 05 12:56:11 <}-z-{>	Dokujisan: I just aded some server resources if you want to expand on them
    Mar 05 12:56:14 <}-z-{>	I'm going to lunch for real now
    Mar 05 12:56:15 <}-z-{>	bbiab
    Mar 05 12:56:41 <CuBe0wL>	NEx = Tiuffgun
    Mar 05 12:56:45 <esteel>	:PP
    Mar 05 12:56:57 <esteel>	i see you want your sounds mods to be default..
    Mar 05 12:57:03 <CuBe0wL>	haha
    Mar 05 12:57:04 <tZork>	harr
    Mar 05 12:57:31 <esteel>	merlijn: well i can change that domain easily
    Mar 05 12:57:33 <CuBe0wL>	well, it could be an option to use roflsounds and roflgfx :D
    Mar 05 12:57:58 <Dokujisan>	yes nexuiz admins meant nexuiz server admins
    Mar 05 12:58:02 <esteel>	in fact hyvin.de also points to it :P  i just learned to late that it was badly translated.. FruitieX woulud be able to tell :P
    Mar 05 12:58:22 <CuBe0wL>	Dokujisan, I'd like to keep my mod status too pls :D
    Mar 05 12:58:27 <FruitieX>	wtf is that
    Mar 05 12:58:28 <FruitieX>	:P
    Mar 05 12:58:49 <esteel>	FruitieX: should be 'good'  in english? no?
    Mar 05 12:58:50 <Dokujisan>	CuBe0wL: ok
    Mar 05 12:58:54 <esteel>	or rather goodly..
    Mar 05 12:58:54 <CuBe0wL>	esteel, so can I keep my ftp too? :D
    Mar 05 12:59:00 <FruitieX>	yes or well
    Mar 05 12:59:07 <FruitieX>	good = hyvä
    Mar 05 12:59:20 <CuBe0wL>	haha
    Mar 05 12:59:21 <CuBe0wL>	epic
    Mar 05 12:59:25 <esteel>	CuBe0wL: yeah.. just not sure how long the old pn.de will be there then :P
    Mar 05 12:59:46 <CuBe0wL>	but I'll still be able to use it under a diffrent name?
    Mar 05 13:00:05 <esteel>	FruitieX: yeah, that what i found out too late.. i just asked google for 'good' in finnish.. said hyvin :P
    Mar 05 13:00:12 <esteel>	CuBe0wL: sure, why not?
    Mar 05 13:00:38 <CuBe0wL>	(just to mention, if you have ssh access to my home @ pn.de, you can read my thesis :D)
    Mar 05 13:00:51 <CuBe0wL>	but pls, don't steal or sell it :D
    Mar 05 13:00:57 <mand1nga>	is there any git support for redmine?
    Mar 05 13:01:15 <Dokujisan>	<FruitieX> can you invite him to #nexuiz.editing instead? :P
    Mar 05 13:01:21 <merlijn>	CuBe0wL: is your thesis about which medicine can easily be turned into drugs?
    Mar 05 13:01:25 <Dokujisan>	I don't think we want any discussion of a fork leaked by accident
    Mar 05 13:01:29 <merlijn>	otherwise I'm probably not interested :P
    Mar 05 13:01:33 <tZork>	haha
    Mar 05 13:01:35 <CuBe0wL>	chances I'll be able to write an article, and it might published in  a medical journal
    Mar 05 13:01:39 <Dokujisan>	I know #nexuiz.nct is a safe plcae to discuss mapping
    Mar 05 13:02:07 <Dokujisan>	eh I just make sure he knows not to mention the fork
    Mar 05 13:02:08 <Dokujisan>	ok
    Mar 05 13:02:10 <CuBe0wL>	merlijn, no, I've written my thesis in "Image analyzis in medicine technology"
    Mar 05 13:02:27 <esteel>	CuBe0wL: i'll offer your thesis to vermeulen :PPP harhar
    Mar 05 13:02:32 <CuBe0wL>	:D
    Mar 05 13:02:33 <tZork>	interesting subejct
    Mar 05 13:02:34 <CuBe0wL>	haha
    Mar 05 13:02:52 <CuBe0wL>	tZork, indeed
    Mar 05 13:03:43 <CuBe0wL>	in case we publish an abstract or the full article in english too, I'll handle you guys it to read if you want :)
    Mar 05 13:03:52 <esteel>	meh, tunnels and mobile internet to not like each other..
    Mar 05 13:04:00 <tZork>	im definitly interested =)
    Mar 05 13:04:19 <tZork>	bbiab, better get me some food 
    Mar 05 13:04:26 <CuBe0wL>	have a good one
    Mar 05 13:04:34 <FruitieX>	Dokujisan: oh okay
    Mar 05 13:04:36 <FruitieX>	coming
    Mar 05 13:04:37 <esteel>	enjoy tZork 
    Mar 05 13:04:43 <CuBe0wL>	where's MrBougo anyway?
    Mar 05 13:07:05 <merlijn>	MrB usually isn't online all that much
    Mar 05 13:07:18 <mand1nga>	afaik he didn't like the idea of forking
    Mar 05 13:07:23 <mand1nga>	I told him about this channel yesterday
    Mar 05 13:07:23 <merlijn>	Spaceman: you can probably run stats on when MrB is likely to appear :P
    Mar 05 13:08:21 <merlijn>	to be fair, I don't fully like the idea of forking either
    Mar 05 13:08:51 <pavlvs>	yer
    Mar 05 13:08:58 <Dokujisan>	I love it
    Mar 05 13:09:00 <CuBe0wL>	hmm?
    Mar 05 13:09:04 <Dokujisan>	it's healthy medicine
    Mar 05 13:09:10 <merlijn>	Vermeulen has now actually made some money on Nexuiz now, maybe he'd just let us take over and we can rename it anyway
    Mar 05 13:09:17 <CuBe0wL>	MrBougo is always online in #pb.nexuiz
    Mar 05 13:09:42 <Dokujisan>	merlijn: what benefit does that give?
    Mar 05 13:10:12 <merlijn>	Dokujisan: less troublesome than forking, plus I think that for now we can at least benefit from all the fuzz about nexuiz
    Mar 05 13:10:26 <merlijn>	forking implies that BOTH projects move forward
    Mar 05 13:10:37 <merlijn>	I don't think that is a good idea
    Mar 05 13:10:46 <pavlvs>	++
    Mar 05 13:10:59 <merlijn>	and even if they don't both move forward, the old nexuiz will still exist
    Mar 05 13:11:00 <Dokujisan>	well the "troublesome" part, to me, is the good part, because that means overhauling and resetting, which will really help this project greatly.
    Mar 05 13:11:14 <merlijn>	I'm not at all against that
    Mar 05 13:11:32 <FruitieX>	got to say I'm support doku here :)
    Mar 05 13:11:33 <CuBe0wL>	merlijn, well, all the major brainpower will move on this project
    Mar 05 13:11:36 <FruitieX>	I*
    Mar 05 13:11:40 <Dokujisan>	and the buzz around this drama can benefit a fork, because problems in GPL projects always gain attention on digg/reddit/slashdot, etc
    Mar 05 13:11:48 <merlijn>	CuBe0wL: is LH in on this?
    Mar 05 13:12:00 <CuBe0wL>	proly not
    Mar 05 13:12:05 <FruitieX>	afaik he is at least not against it
    Mar 05 13:12:05 <CuBe0wL>	at least not tha I know of
    Mar 05 13:12:27 <CuBe0wL>	what I was trying to say
    Mar 05 13:12:34 <merlijn>	I think LH is the only one who can do certain things as he knows everything about the engine
    Mar 05 13:12:35 <CuBe0wL>	wo developers, Nexuiz will die
    Mar 05 13:12:46 <CuBe0wL>	but it's only the title
    Mar 05 13:13:02 <CuBe0wL>	it's not the name that makes Nexuiz to be Nexuiz
    Mar 05 13:13:13 <CuBe0wL>	it's the people who play and develope it
    Mar 05 13:13:19 <merlijn>	I think we should only fork if we can't get what we want in the original nexuiz project - but from what I understand nobody has investigated that option
    Mar 05 13:13:20 <Spaceman>	merlijn: MrBougo's join time on a Friday is fairy random
    Mar 05 13:13:43 <Dokujisan>	I think what we're doing with this fork is taking ALL of the good things about nexuiz and improving ALL of the bad things
    Mar 05 13:13:57 <Dokujisan>	All of the good things about nexuiz is.. you guys
    Mar 05 13:14:03 <Dokujisan>	and some others
    Mar 05 13:14:14 <CuBe0wL>	honored
    Mar 05 13:14:22 <Spaceman>	it would be nice to keep the nexuiz name
    Mar 05 13:14:42 <CuBe0wL>	it would be nice if fukcfonic would rename it's game
    Mar 05 13:14:54 <Spaceman>	that would be a lot better
    Mar 05 13:15:23 <CuBe0wL>	if that'd happen, I probably won't think the fork as a very good idea
    Mar 05 13:15:28 <Dokujisan>	I still say I never really like the name "nexuiz" but I just grew to accept it :-)
    Mar 05 13:15:46 <Spaceman>	it's just a group of letters
    Mar 05 13:15:46 <merlijn>	anyway, I'm going to do some other stuff now - just a small word of wisdom before I go: carefully evaluate your options before making hasty decisions
    Mar 05 13:15:53 <CuBe0wL>	but kehdrin or what's the guy's name said, they won't change it, period.
    Mar 05 13:15:59 <Dokujisan>	I did like the 'n' symbol though. That was good.
    Mar 05 13:16:10 <CuBe0wL>	merlijn, we won't rush anything
    Mar 05 13:17:03 <Dokujisan>	I mean, put simply, nexuiz was a sinking ship to me. I was on my way out
    Mar 05 13:17:11 <Dokujisan>	but this changes everything
    Mar 05 13:17:36 <Dokujisan>	I mean I was on my way out well before this illfonic mess
    Mar 05 13:23:26 <FruitieX>	by the way, this idea will be useful in our fork i think: http://www.youtube.com/watch?v=NotqttdZUoQ
    Mar 05 13:23:33 <FruitieX>	I'm very open for ideas now concerning that :)
    Mar 05 13:36:09 <esteel>	bbl, switching trains :P
    Mar 05 13:41:32 <}-z-{>	Dokujisan: we need another community/project manager
    Mar 05 13:41:54 <Samual>	Hmm
    Mar 05 13:42:10 <}-z-{>	is that a task you're interested in Samual?
    Mar 05 13:42:38 <Samual>	Meh
    Mar 05 13:42:41 <Samual>	People don't like me
    Mar 05 13:42:43 <Samual>	And i'm too lazy
    Mar 05 13:42:55 <CuBe0wL>	oh, one thing came to my mind, while I'm mapping right now: PLEASE GIVE THE RAILGUN IT'S OWN AMMO!!!
    Mar 05 13:43:04 <}-z-{>	okay lol
    Mar 05 13:43:11 <Samual>	No :P I still don't like that idea CuBe0wL 
    Mar 05 13:43:11 <}-z-{>	CuBe0wL: well that can be discuess for sure
    Mar 05 13:43:22 <Samual>	I'll still be doing the balance I think :P
    Mar 05 13:43:32 <}-z-{>	okay
    Mar 05 13:43:39 <CuBe0wL>	RAGEQUIT!
    Mar 05 13:43:42 *	CuBe0wL (~akion@BKTFW13.usn.hu) has left #notnexuiz (Távozom)
    Mar 05 13:43:43 <Samual>	-.-
    Mar 05 13:43:47 *	CuBe0wL (~akion@BKTFW13.usn.hu) has joined #notnexuiz
    Mar 05 13:43:52 <CuBe0wL>	jsut kidding :D
    Mar 05 13:44:10 <CuBe0wL>	aww, I've lost me op :(
    Mar 05 13:44:28 *	}-z-{ gives channel operator status to CuBe0wL
    Mar 05 13:45:20 *	ProjektGhost (~raygalina@64.107.218.2) has joined #notnexuiz
    Mar 05 13:45:29 <ProjektGhost>	that's better
    Mar 05 13:45:31 <Samual>	Ghost: Keep quiet :P
    Mar 05 13:45:36 <ProjektGhost>	okay, fine
    Mar 05 13:45:39 <Samual>	He wants to suggest names
    Mar 05 13:45:40 <ProjektGhost>	anyway, new name
    Mar 05 13:45:49 <ProjektGhost>	Nexius
    Mar 05 13:45:52 <Samual>	-.-
    Mar 05 13:45:55 <ProjektGhost>	you get to correct the name now
    Mar 05 13:45:58 <ProjektGhost>	no, seriously
    Mar 05 13:46:06 <ProjektGhost>	it's close enough to be familiar, but still different
    Mar 05 13:46:09 <ProjektGhost>	it's perfect, IMO
    Mar 05 13:46:23 <Samual>	.com name is taken
    Mar 05 13:46:35 <Samual>	Plan A: .com name
    Mar 05 13:46:50 <Samual>	Plan B: Consider already taken .com names
    Mar 05 13:47:08 <Samual>	Plan C: multiple words in the name
    Mar 05 13:47:12 <Samual>	Plan D: .org name
    Mar 05 13:47:14 <Samual>	^_^
    Mar 05 13:47:23 <CuBe0wL>	he?
    Mar 05 13:47:30 <Samual>	At least I think that's how Doku put it 
    Mar 05 13:47:41 <CuBe0wL>	what about the names we tried out from Japan?
    Mar 05 13:48:14 <ProjektGhost>	are they going to use the Nexuiz logo?
    Mar 05 13:48:21 <ProjektGhost>	the Chinese character for Strength?
    Mar 05 13:48:24 <CuBe0wL>	Illfonic?
    Mar 05 13:48:24 <Samual>	Probably not
    Mar 05 13:48:28 <Samual>	Oh
    Mar 05 13:48:30 <Samual>	IllFonic will
    Mar 05 13:48:35 <CuBe0wL>	they already do
    Mar 05 13:48:42 <ProjektGhost>	then call is Strenght, or a synonym
    Mar 05 13:50:47 <ProjektGhost>	"Kings of Valor" or something
    Mar 05 13:51:21 <ProjektGhost>	sounds too RPG-ish, though
    Mar 05 13:52:25 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-big-large-great.html http://www.tribalshapes.com/categories/kanji/kanji-blood.html http://www.tribalshapes.com/categories/kanji/kanji-chaos.html
    Mar 05 13:53:56 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-conquer-overcome.html http://www.tribalshapes.com/categories/kanji/kanji-fast.html
    Mar 05 13:54:48 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-friend.html
    Mar 05 13:55:28 <Samual>	strength ftw
    Mar 05 13:55:36 <ProjektGhost>	what about Zen
    Mar 05 13:55:40 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-good-luck.html http://www.tribalshapes.com/categories/kanji/kanji-group.html
    Mar 05 13:55:42 <ProjektGhost>	get the symbol for that
    Mar 05 13:55:43 <ProjektGhost>	=p
    Mar 05 13:55:44 <}-z-{>	div didn't want to use zen
    Mar 05 13:55:49 <ProjektGhost>	lame
    Mar 05 13:58:00 <Samual>	http://www.tribalshapes.com/categories/kanji/kanji-ability-talent.html
    Mar 05 13:58:10 <Samual>	>.>
    Mar 05 13:58:20 <}-z-{>	too complicated
    Mar 05 13:58:22 <}-z-{>	it's 2 symbols
    Mar 05 13:58:26 <}-z-{>	we only want 1
    Mar 05 13:58:29 <Samual>	lawl I know
    Mar 05 13:58:35 <Samual>	I was just pointing at the bottom one
    Mar 05 13:58:35 <}-z-{>	group might be the best yet
    Mar 05 13:58:38 <Samual>	Because it's epic
    Mar 05 13:59:43 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-learning-studies-science.html
    Mar 05 13:59:47 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-loyalty-faithfulness.html
    Mar 05 14:00:11 <Dokujisan>	good resource
    Mar 05 14:01:07 <Dokujisan>	ok if that kanji for ability/talent is two characters, what does the first character by itself mean?
    Mar 05 14:01:36 <Dokujisan>	that would be a good symbol for a name beginning with a T
    Mar 05 14:03:16 <}-z-{>	I posted a t looking one
    Mar 05 14:03:47 <Dokujisan>	for group
    Mar 05 14:03:49 <ProjektGhost>	tabellion, tabefaction 
    Mar 05 14:03:51 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-now-the-present.html
    Mar 05 14:04:07 <CuBe0wL>	http://www.tribalshapes.com/img/tattoos/friend.gif
    Mar 05 14:04:10 <CuBe0wL>	this is the best
    Mar 05 14:04:14 <CuBe0wL>	easy to write
    Mar 05 14:04:24 <}-z-{>	http://www.tribalshapes.com/categories/kanji/kanji-people-nation.html
    Mar 05 14:04:35 <CuBe0wL>	and has a little resamblence to the original strenght logo
    Mar 05 14:04:55 <}-z-{>	group is one of my favorites so far
    Mar 05 14:05:05 <CuBe0wL>	I like that kanji symbol of friend very much
    Mar 05 14:05:25 <CuBe0wL>	why group?
    Mar 05 14:05:39 <}-z-{>	I has a nice feel to it and represens us being a group or community
    Mar 05 14:05:46 <CuBe0wL>	ok
    Mar 05 14:05:50 <}-z-{>	easy to draw too
    Mar 05 14:06:09 <}-z-{>	but friend is nice too
    Mar 05 14:06:16 <FruitieX>	btw, should we focus on a better singleplayer campaign too?
    Mar 05 14:06:23 <}-z-{>	sure FruitieX 
    Mar 05 14:06:39 <FruitieX>	needs better story, possibly against monsters instead of bots
    Mar 05 14:06:45 <FruitieX>	hopefully at least :P
    Mar 05 14:07:46 <}-z-{>	good K one > http://www.tribalshapes.com/categories/kanji/kanji-water.html
    Mar 05 14:08:24 <}-z-{>	can you guys be sure to annotate wiki edits?
    Mar 05 14:10:51 <Dokujisan>	k, I did for one
    Mar 05 14:10:54 <Dokujisan>	I'll do it more
    Mar 05 14:12:34 <Dokujisan>	}-z-{: there is a mumble server listing (php script) that I use on http://nullgaming.com/batcaves/
    Mar 05 14:12:53 <}-z-{>	yes, remind me when we have wordpress mu running
    Mar 05 14:12:57 <Dokujisan>	k
    Mar 05 14:13:05 <}-z-{>	what are your feelings on buddy press?
    Mar 05 14:13:15 <}-z-{>	do you prefer to use buddypress or mybb for forums?
    Mar 05 14:13:30 <Dokujisan>	I've never looked at buddypress
    Mar 05 14:13:41 <}-z-{>	buddy press might be too confusing for some
    Mar 05 14:13:53 <}-z-{>	it's a wordpress mu wrapper
    Mar 05 14:13:57 <}-z-{>	www.nexuizclans.com uses it
    Mar 05 14:16:21 <DibTop>	tZork: what were you saying cool stuff about?
    Mar 05 14:16:33 <CuBe0wL>	}-z-{, do you have an nvidia card?
    Mar 05 14:16:41 <}-z-{>	yes
    Mar 05 14:16:48 <CuBe0wL>	and you use two monitors, don't you?
    Mar 05 14:16:52 <}-z-{>	correct
    Mar 05 14:17:03 <CuBe0wL>	ok, how do you start nexuiz on only one monitor?
    Mar 05 14:17:10 <CuBe0wL>	it auto streches for me to both
    Mar 05 14:17:22 <}-z-{>	fullscreen 0
    Mar 05 14:17:23 <}-z-{>	:-P
    Mar 05 14:17:28 <CuBe0wL>	bah
    Mar 05 14:17:33 <CuBe0wL>	no other way ?
    Mar 05 14:17:35 <}-z-{>	I play in windowed mode
    Mar 05 14:17:35 <}-z-{>	well
    Mar 05 14:17:40 <}-z-{>	are you using twinview?
    Mar 05 14:17:43 <CuBe0wL>	yep
    Mar 05 14:18:15 <}-z-{>	when I used to play fullscreen, I just defined my resolution and twinview handled it as I expected
    Mar 05 14:18:26 <}-z-{>	it was like a psuedo fullscreen though
    Mar 05 14:18:35 <}-z-{>	if you click off it, your panels will rise above it type thing
    Mar 05 14:18:51 <}-z-{>	I couldn't specify my dimensions in the gui
    Mar 05 14:18:55 <}-z-{>	had to do it in my autoexec
    Mar 05 14:18:57 <CuBe0wL>	well, it streches me to noth monitors, and I can't set the resolution to anything
    Mar 05 14:19:08 <}-z-{>	autoexec :-P
    Mar 05 14:19:16 <CuBe0wL>	I have that in my autoexec
    Mar 05 14:19:25 <DibTop>	FruitieX: im working on rigging obi's newest model :)
    Mar 05 14:19:29 <CuBe0wL>	but once I set the res, it's not accepted
    Mar 05 14:19:38 <}-z-{>	did you do the cod_vid_width and height too?
    Mar 05 14:19:41 <}-z-{>	con*
    Mar 05 14:20:00 <CuBe0wL>	umm.. wtf, con has it's own resolution? oO
    Mar 05 14:20:04 <CuBe0wL>	no btw :D
    Mar 05 14:20:05 <FruitieX>	DibTop: good :)
    Mar 05 14:20:15 <CuBe0wL>	k, that could have been the problem :D
    Mar 05 14:20:59 *	ProjektGhost (~raygalina@64.107.218.2) has left #notnexuiz
    Mar 05 14:21:05 <}-z-{>	CuBe0wL: yeah it defines text size/shape too :-P
    Mar 05 14:25:37 <}-z-{>	I wish flash didn't crash all the time
    Mar 05 14:26:00 <Dokujisan>	<DibTop> FruitieX: im working on rigging obi's newest model :)
    Mar 05 14:26:01 <Dokujisan>	:-o
    Mar 05 14:26:06 <}-z-{>	nice
    Mar 05 14:26:21 DibTop div0 
    Mar 05 14:33:06 <Spaceman>	DibTop: earlier in #nexuiz lda17h wanted some info about nexuiz animations, he wants to modify some of nexuiz anims
    Mar 05 14:33:26 <Spaceman>	FruitieX: can you remove the border from the HUD elements?
    Mar 05 14:34:39 <FruitieX>	yes you can
    Mar 05 14:34:50 <FruitieX>	you can also make it look just the way you want with skins ala menu :)
    Mar 05 14:34:58 <Samual>	[14:19:26pm] <CuBe0wL> well, it streches me to noth monitors, and I can't set the resolution to anything
    Mar 05 14:34:59 <Samual>	lawl
    Mar 05 14:35:00 <FruitieX>	make the border as thick you want even (per-panel setting)
    Mar 05 14:35:05 <Samual>	Mine stretches to all three monitors
    Mar 05 14:35:10 <Samual>	5760x1200
    Mar 05 14:35:13 <Samual>	I just have to deal with it
    Mar 05 14:35:16 <Samual>	-.-
    Mar 05 14:35:18 <}-z-{>	http://ie6funeral.com/
    Mar 05 14:35:35 <Dokujisan>	on a side note, can someone help me test a website? Go here and scroll to the bottom and post a few symbols like... euro and pound sterling and maybe some other common characters used in europe. User name= testuser1  password=9999
    Mar 05 14:35:59 <Dokujisan>	or any other characters you want to try
    Mar 05 14:36:12 <}-z-{>	do we guess the url? :-P
    Mar 05 14:36:17 <Spaceman>	go where?
    Mar 05 14:36:24 <Dokujisan>	hang on...
    Mar 05 14:36:33 <Dokujisan>	http://message.axkickboxing.com/newdesign/index.phtml?action=dispthread&topic=29479
    Mar 05 14:36:45 <}-z-{>	ahh, still having issues with that
    Mar 05 14:36:56 <Dokujisan>	well I converted the database to UTF-8 yesterday. 
    Mar 05 14:37:00 <}-z-{>	ahh
    Mar 05 14:37:03 <Dokujisan>	made a copy and converted that, rather
    Mar 05 14:37:05 <}-z-{>	damn, how long did that take?
    Mar 05 14:37:13 <Dokujisan>	but I am still learning about character encoding
    Mar 05 14:37:46 <Dokujisan>	I need to make sure someone from europe, with whatever keyboard layout they might use, can enter characters and it will show up properly
    Mar 05 14:37:56 <Dokujisan>	the only thing I can do is copy/paste
    Mar 05 14:38:17 <}-z-{>	I can type chinese
    Mar 05 14:38:19 <}-z-{>	:-P
    Mar 05 14:38:31 <Dokujisan>	ah yeah I can type japanese if i install the keyboard utility
    Mar 05 14:38:33 <Dokujisan>	forgot about that
    Mar 05 14:38:57 <Dokujisan>	the database dump file is 1.2GB or so
    Mar 05 14:39:28 <Dokujisan>	and it took just a few minutes to do each step... export / conversion / import
    Mar 05 14:39:30 <}-z-{>	打开哦开发似的卡0
    Mar 05 14:39:43 <}-z-{>	yeah, I'd imagine it'd be big
    Mar 05 14:40:07 <}-z-{>	Your message could not be posted because the password you submitted was wrong.
    Mar 05 14:40:13 <Dokujisan>	ok hang on
    Mar 05 14:40:27 <Dokujisan>	testuser1
    Mar 05 14:40:29 <Dokujisan>	9999
    Mar 05 14:40:42 <}-z-{>	yep, still getting that error
    Mar 05 14:40:44 <Dokujisan>	case sensitive names
    Mar 05 14:41:31 <Dokujisan>	hmmm ok it failed for me too. Let me get that figured out
    Mar 05 14:41:43 <}-z-{>	:
    Mar 05 14:41:46 <}-z-{>	oooh noes
    Mar 05 14:41:57 <}-z-{>	the chinese messed up my irsii lol
    Mar 05 14:42:04 <}-z-{>	okay, all better
    Mar 05 14:42:07 <}-z-{>	that was whacky
    Mar 05 14:42:45 <}-z-{>	oh hey, do we have any reviews of other projects workflows?
    Mar 05 14:42:54 <}-z-{>	such as warsow and tremulous?
    Mar 05 14:43:13 <}-z-{>	is warsow development even open?
    Mar 05 14:45:04 <Dokujisan>	}-z-{: ok try login:testuser1 pw:4781
    Mar 05 14:45:07 <Dokujisan>	er testuser2
    Mar 05 14:45:27 <}-z-{>	posted chinese okay
    Mar 05 14:45:58 <Dokujisan>	can someone here from Europe post some euro characters?
    Mar 05 14:46:10 <Spaceman>	i'm trying
    Mar 05 14:46:42 <}-z-{>	I don't see how warsow's development is public
    Mar 05 14:47:41 <Spaceman>	the euro's look good ?
    Mar 05 14:48:38 <Dokujisan>	haha what the hell
    Mar 05 14:48:45 <CuBe0wL>	and Z҉A҉L҉G҉O̚̕̚ too
    Mar 05 14:48:50 <Dokujisan>	lol
    Mar 05 14:48:53 <}-z-{>	lol
    Mar 05 14:48:55 <Dokujisan>	who posted that?
    Mar 05 14:48:58 <}-z-{>	CuBe0wL: 
    Mar 05 14:49:01 <}-z-{>	I'm guessing :-P
    Mar 05 14:49:06 <}-z-{>	cryllic millions
    Mar 05 14:49:13 <Dokujisan>	crazy :-)
    Mar 05 14:49:16 <Dokujisan>	ok just a second guys
    Mar 05 14:49:21 <Dokujisan>	we're gonna do a comparison
    Mar 05 14:49:22 <CuBe0wL>	Z҉A҉L҉G҉O̚̕̚ !!!
    Mar 05 14:49:38 <Dokujisan>	http://message.axkickboxing.com/index.phtml?action=dispthread&topic=29479
    Mar 05 14:49:39 <CuBe0wL>	H̡́͝E ̨W̢̛H̡̧O͟͏ W̧A̵̡͘I̷̢͜TS͘͟ ̢́BE̛͝H̡͜I͏̨N͡D҉̨ ̀T̵H̸́E ̨W͏͢AL̴͠L͜!̸͟͞!̶!́
    Mar 05 14:49:41 <Dokujisan>	do the same on that address
    Mar 05 14:49:57 <Dokujisan>	it's the same topic on another set of PHP and another database
    Mar 05 14:49:58 <}-z-{>	ಠ_ಠ
    Mar 05 14:50:02 <}-z-{>	http://en.wikipedia.org/wiki/Combining_Cyrillic_Millions
    Mar 05 14:50:09 <Dokujisan>	same username + password
    Mar 05 14:50:29 <Dokujisan>	and I fugured it why testuser1 didn't work. It's a different database >.<
    Mar 05 14:50:54 <}-z-{>	:-P
    Mar 05 14:51:18 <}-z-{>	for the wiki, are we good with the dev wiki or do we want one that is part of the user site as well?
    Mar 05 14:52:16 <Dokujisan>	we could use both, probably
    Mar 05 14:52:30 <Dokujisan>	dev wiki might have some notes related to...development
    Mar 05 14:52:46 <Dokujisan>	the other wiki would be more like OUNS was
    Mar 05 14:53:29 <Dokujisan>	CuBe0wL: so zalgo didn't work that time?
    Mar 05 14:53:59 <CuBe0wL>	sure it Z҉A҉L҉G҉O̚̕
    Mar 05 14:54:27 <Dokujisan>	oh I see the issue. When the encoding is switched to utf8 in the HTML, that is when that breaks
    Mar 05 14:54:29 <Dokujisan>	ok
    Mar 05 14:54:30 <}-z-{>	okay, so the next question is, how intense of a wiki do we need, do you think we can get away with a wp plugin for starters?
    Mar 05 14:54:31 <CuBe0wL>	Z̵̴̡̬͚̘̗̯͓A͏͇L͇̜̩͜G̙̳͚̹̰̣̖͢͝O̭̦͢ ̲̗̗̀Z̮̬̹A̢̨͖̱͙͔L͖̖͙̘̣̤͘G̴̢͖̲̭O̖͈̺̻̻̖͎̻͟ ͚͓̯͙̱Z̘̯̗̖̩A͏͎̣͡L̢̬̭̀G̗̞̼͔O̫̺̯̖̹͠ ̦̟̜͉̟͉̀I̗̫̪L̞̯͖̫͢͝L̴̙̮͉͔͟͠F̪̗̱̩͓̻͕̞̘̀̕͡O͇̺̗̤̘̘̳͍N̡͔̖̻̰͙I̹̦͕͇̖͢Ç̩̘̺̜͉ ̪̦̭̻̤̻Z̥̹̝͔Ą̵͍̰L̷̻̥̗̮̳̫̟̞G̢̨̯͓͠O͏̸̹̳̤̣̼͉͉̪̟̠Z̵̴̡̬͚̘̗̯͓A͏͇L͇̜̩͜G̙̳͚͢͝
    Mar 05 14:54:31 <CuBe0wL>	̹̰̣̖O̭̦͢ ̲̗̗̀s. ̕҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉Z ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉ ̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̚̕̕̚̕̚͡ ALGO ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̚̕̚҉ ̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̚̕̕̚̕̚͡ ͡҉҉grows. ҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓
    Mar 05 14:54:32 <CuBe0wL>	̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̕̚̕̚͡ ̒̓̔̕̚ZAL҉̵̞̟̠̖̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑̒̓̔̿̿̿̕̚̕̚͡ ̒̓̔̕̚GO commeth.
    Mar 05 14:54:45 <Dokujisan>	then the test passed! The new site with the new database seems to work 
    Mar 05 14:55:32 <CuBe0wL>	Dokujisan, well, I can see   Z҉A҉L҉G҉O̚̕ on both pages (he is still H҉̵̞̟̠̖̗̘Ȅ̐̑̒̚̕̚ IS C̒̓̔̿̿̿̕̚̚̕̚̕̚̕̚̕̚̕̚OMI҉̵̞̟̠̖̗̘NG > ͡҉҉ ̵̡̢̛̗̘̙̜̝̞̟̠͇̊̋̌̍̎̏̿̿̿̚ ҉ ҉҉̡̢̡̢̛̛̖̗̘̙̜̝̞̟̠̖̗̘̙̜̝̞̟̠̊̋̌̍̎̏̐̑̒̓̔̊̋̌̍̎̏̐̑ ͡҉҉ )
    Mar 05 14:55:49 <Dokujisan>	CuBe0wL: yes but change the character encoding of the second one to UTF8
    Mar 05 14:55:49 <}-z-{>	I'd like to propose we use this for future documentation of the project: http://www.methods.co.nz/asciidoc/
    Mar 05 14:55:52 <Dokujisan>	in your browser
    Mar 05 14:55:58 <Samual>	CuBe0wL, O.o
    Mar 05 14:56:04 <Dokujisan>	CuBe0wL: it should break after that
    Mar 05 14:56:08 <CuBe0wL>	Samual?
    Mar 05 14:57:27 <Samual>	Font is fun ^_^
    Mar 05 14:59:08 <CuBe0wL>	http://www.zalgo.org/wp-content/gallery/zalgo/1237835262258.jpg
    Mar 05 14:59:19 <}-z-{>	this is used: http://www.methods.co.nz/asciidoc/asciidoc.txt
    Mar 05 14:59:25 <}-z-{>	to generate this: http://www.methods.co.nz/asciidoc/asciidoc.css-embedded.html
    Mar 05 15:00:01 <Dokujisan>	and the other thing that works is the search. I can search for '£'
    Mar 05 15:00:03 <Dokujisan>	on the new site
    Mar 05 15:00:16 <}-z-{>	Dokujisan: have we thought of anyone who can help with documentation?
    Mar 05 15:00:23 <}-z-{>	shaggy maybe still interested?
    Mar 05 15:00:30 <Dokujisan>	}-z-{: we need a serious discussion for that topic, certainly
    Mar 05 15:00:36 <Dokujisan>	it will be hard to recruit for that
    Mar 05 15:00:39 <Dokujisan>	but I think it's possible
    Mar 05 15:00:43 <}-z-{>	yeah
    Mar 05 15:01:01 <}-z-{>	I think this is something we can streamline with the build system too
    Mar 05 15:01:12 <Dokujisan>	anyway thanks for helpign to test that, CuBe0wL, Spaceman and -z-
    Mar 05 15:01:38 <}-z-{>	so even the nightly builds on the test server, we can provide up-to-date documentation in HTML form if needed (for example)
    Mar 05 15:01:47 <Dokujisan>	wow -z-
    Mar 05 15:01:49 <}-z-{>	obviously the other thing I want to get going is a nightly cvar/cmd list searcher
    Mar 05 15:01:50 <Dokujisan>	how does that work?
    Mar 05 15:02:04 <}-z-{>	with the asciidoc tool
    Mar 05 15:02:05 <}-z-{>	http://www.methods.co.nz/asciidoc/asciidoc.txt
    Mar 05 15:02:08 <}-z-{>	http://www.methods.co.nz/asciidoc/
    Mar 05 15:04:11 <CuBe0wL>	it seems LH is online
    Mar 05 15:04:20 <CuBe0wL>	does he know about this palce?
    Mar 05 15:05:12 <Samual>	Probably not
    Mar 05 15:05:24 <Samual>	Do we WANT him to know?
    Mar 05 15:05:27 <}-z-{>	no
    Mar 05 15:05:29 <}-z-{>	at least not yet
    Mar 05 15:05:32 <}-z-{>	he was in on the deal
    Mar 05 15:05:39 <Samual>	Indeed
    Mar 05 15:05:57 <}-z-{>	he more or less let the community get hurt for his own good.
    Mar 05 15:07:28 <CuBe0wL>	I still think he should know about it... just for the reason, he's the only DP coder
    Mar 05 15:07:56 <CuBe0wL>	what will we do with the engine, if we can't solve a problem, and he's not interested in forked Nexuiz at all?
    Mar 05 15:08:18 <}-z-{>	will that really be the case though?
    Mar 05 15:08:42 <}-z-{>	I just think at this point telling him might do more harm than good
    Mar 05 15:09:44 <CuBe0wL>	I certainly won't tell, I don't think it's my job
    Mar 05 15:09:55 <CuBe0wL>	I was just wondering, ya know
    Mar 05 15:10:02 <}-z-{>	I think div0 really has the voice on this decision
    Mar 05 15:10:11 <CuBe0wL>	div0, 
    Mar 05 15:10:14 <CuBe0wL>	we summon you
    Mar 05 15:10:26 <}-z-{>	btw, willis has informed me that for the past month or so nexuiz.com was a 301 redirect so alientrap.org/nexuiz
    Mar 05 15:10:29 <CuBe0wL>	man, this will take ages like this :(
    Mar 05 15:11:11 <}-z-{>	ages like what?
    Mar 05 15:11:29 <CuBe0wL>	btw. it's interesting to note, that Vermeulen still hasn't sold nexuiz.com
    Mar 05 15:11:36 <CuBe0wL>	he just let Illfonic to use it
    Mar 05 15:11:41 <CuBe0wL>	but he still owns it
    Mar 05 15:11:43 <CuBe0wL>	what for?
    Mar 05 15:11:47 <}-z-{>	yeah but he made a shitty deal with them
    Mar 05 15:12:05 <}-z-{>	could have gotten our project more space on the homepage as part of the deal
    Mar 05 15:12:23 <CuBe0wL>	and a difference in name of Illfonics side
    Mar 05 15:12:24 <}-z-{>	301 means that search engines have been indexing alientra.org/nexuiz for the past month, not nexuiz.com
    Mar 05 15:13:09 <CuBe0wL>	lol, I've just realised what kedhrin said by "But, I am not going to put my team in here to defend themselves and our company decisions."
    Mar 05 15:13:31 <CuBe0wL>	he took it a total insult that I've invited his men to join our conversation
    Mar 05 15:14:08 <CuBe0wL>	what an elitist fucktard... how do people sink that low?
    Mar 05 15:14:45 <}-z-{>	"The GPL Nexuiz is still linked on this web-site. This is necessary for the commercial marketing of the project."
    Mar 05 15:15:01 <}-z-{>	that one still gets me the most
    Mar 05 15:16:47 <CuBe0wL>	I still don't know if I should write the whole scandal to hup.hu or not
    Mar 05 15:16:52 <}-z-{>	zeniux still sticks out in my head
    Mar 05 15:17:07 <}-z-{>	Dokujisan: can you put that names list on the wiki?
    Mar 05 15:17:34 <Dokujisan>	yeah
    Mar 05 15:18:11 <CuBe0wL>	don't forget Pheonix and Itoma
    Mar 05 15:18:21 <}-z-{>	don't really like either of those to be honest
    Mar 05 15:18:58 <CuBe0wL>	hmmm
    Mar 05 15:19:15 <CuBe0wL>	I've just realised zeniux has the same letters as Nexuiz
    Mar 05 15:19:20 <CuBe0wL>	just scrambled
    Mar 05 15:19:23 <}-z-{>	yes
    Mar 05 15:19:32 <CuBe0wL>	but I don't like the sound of it
    Mar 05 15:19:33 <Dokujisan>	}-z-{: how do you add a new page to this wiki o_O
    Mar 05 15:19:43 <CuBe0wL>	create new page link? :P
    Mar 05 15:19:53 <Dokujisan>	I don't see it
    Mar 05 15:20:17 <Dokujisan>	I see "new file" where I can attach a file
    Mar 05 15:21:41 <}-z-{>	just go to the url
    Mar 05 15:21:45 <}-z-{>	or create a link in an existing page
    Mar 05 15:21:54 <}-z-{>	[my_new_page](click me for new page)
    Mar 05 15:23:02 <CuBe0wL>	shouldn't we hide this channel? 
    Mar 05 15:23:14 <}-z-{>	isn't it p?
    Mar 05 15:23:16 <}-z-{>	omg it was
    Mar 05 15:23:18 <CuBe0wL>	iirc alientrap-dev was hidden too for  a time
    Mar 05 15:23:27 *	}-z-{ sets mode +p #notnexuiz
    Mar 05 15:23:33 <CuBe0wL>	well, I can see the channel if I whois myself
    Mar 05 15:23:34 <}-z-{>	or did I want +s?
    Mar 05 15:23:42 <}-z-{>	oh it is s
    Mar 05 15:24:14 *	}-z-{ sets mode -p #notnexuiz
    Mar 05 15:24:23 <Dokujisan>	it seems to still be +s
    Mar 05 15:24:29 <}-z-{>	yes, +p is deprecated
    Mar 05 15:24:33 <}-z-{>	+s is what we want
    Mar 05 15:26:39 <Dokujisan>	testing dance_beta1 on bc1
    Mar 05 15:28:58 <CuBe0wL>	heh... Fri Mar 05, 2010 9:14 am last visit from Kedhrin on the AT forum
    Mar 05 15:30:44 <}-z-{>	maybe we should consider setting up an etherpad for the project as well
    Mar 05 15:36:02 <}-z-{>	just as a little tool we can offer on the site
    Mar 05 15:37:51 <Dokujisan>	CuBe0wL: can you check out dance on bc1?
    Mar 05 15:45:07 <CuBe0wL>	Dokujisan, umm... sure
    Mar 05 15:45:23 <Dokujisan>	nullgaming.com:26001
    Mar 05 15:45:49 <CuBe0wL>	}-z-{, how'd you say in english that .. hmm... somebody tells you good news without hiding the real intention behind it, but that's actually the opposite?
    Mar 05 15:46:08 <CuBe0wL>	or by telling you that it'll be good for you, but in the end you'll recieve nothing?
    Mar 05 15:46:08 <}-z-{>	vested interest?
    Mar 05 15:47:03 <CuBe0wL>	I'm trying to tell LordHavoc what Illfonic tries to do with us by dropping half truths, and giving promises full of "maybe"'s
    Mar 05 15:47:16 <CuBe0wL>	but in the end, I'm certain we won't gain anything
    Mar 05 15:47:37 <}-z-{>	I mean, I can see their point... but it also defeats the purpose of what I thought our project was
    Mar 05 15:48:30 <}-z-{>	'hustle' is another word you might be looking for
    Mar 05 15:48:44 <}-z-{>	Hustle may mean: work a scam, intentionally "mis-direct" someone to achieve a personal gain from that person being mis-directed. The hustle, or scam, is usually performed in a fast paced environment as does not allow time to reflect on all options available to the victim, and usually plays on the greed or kindness of people and has an element of chance, although tipped overly into the favor of the "hustler", which is in proportion to how the hustlee views
    Mar 05 15:49:29 <CuBe0wL>	holding out a carrot with sy
    Mar 05 15:49:35 <CuBe0wL>	that was what I searched for
    Mar 05 15:50:34 <}-z-{>	ah
    Mar 05 15:51:01 <Morphed>	they behave as some mega corporation or some important politician
    Mar 05 15:53:33 <}-z-{>	CuBe0wL: the reason you can see the channel if your own whois is because you are joined in the channel
    Mar 05 15:53:38 <}-z-{>	if you leave and whois me, you will not see it
    Mar 05 15:53:40 <CuBe0wL>	I see
    Mar 05 15:54:10 <CuBe0wL>	I've gone into an open conversation with LH on the topic of the Future of the two games
    Mar 05 15:54:18 <CuBe0wL>	I wonder how he'll respond
    Mar 05 15:54:54 <CuBe0wL>	one zillion nexuiz credits he'll start referring to NDA's and other papers ha had to sign, so he can't tell anything
    Mar 05 15:55:25 <}-z-{>	:-P
    Mar 05 15:56:50 <Samual>	One billion internets
    Mar 05 16:09:23 <CuBe0wL>	omfg, I still can't believe how devoted some guys are towards Nexuiz :)
    Mar 05 16:09:41 <CuBe0wL>	after all this hassle, I thougt everybody will stop developing for just a few days
    Mar 05 16:09:47 <CuBe0wL>	FruitieX, you're a hero :D
    Mar 05 16:10:26 <CuBe0wL>	gotta check the commit logs for others too
    Mar 05 16:11:33 <FruitieX>	wohoo an hero
    Mar 05 16:11:43 <Samual>	an hero?
    Mar 05 16:11:52 <Samual>	No "an hero" is committing suicide
    Mar 05 16:11:52 <FruitieX>	yes
    Mar 05 16:11:54 <Samual>	Don't an hero
    Mar 05 16:12:02 <Samual>	^_^
    Mar 05 16:12:20 <Samual>	Go to urban dictionary if you don't believe me
    Mar 05 16:12:40 <FruitieX>	I do believe you.
    Mar 05 16:14:40 <mand1nga>	why is he aN hero?
    Mar 05 16:15:33 <FruitieX>	nvm :)
    Mar 05 16:16:25 <FruitieX>	maybe i'm a NaN hero :)
    Mar 05 16:16:43 <CuBe0wL>	you're gathering another tactical facepalm :D
    Mar 05 16:18:30 <FruitieX>	darn, didn't quite manage to get a tactical DOUBLE facepalm :D
    Mar 05 16:26:04 <}-z-{>	lol a NaN hero
    Mar 05 16:36:53 <}-z-{>	Dokujisan: names list?
    Mar 05 16:38:46 DibTop div0 
    Mar 05 16:38:47 <Dokujisan>	wow...  DibTop 
    Mar 05 16:38:58 <Dokujisan>	I just threw the last version of dance_enclosed on hoctf to test
    Mar 05 16:39:00 <Dokujisan>	and people liked it
    Mar 05 16:39:20 <Dokujisan>	they bitched immediately of course, but after about 3 mintues of gameplay, people started liking it
    Mar 05 16:39:45 <CuBe0wL>	as always :)
    Mar 05 16:40:04 <Dokujisan>	after the match, I asked players to rate it, most rated it 7
    Mar 05 16:40:07 <Dokujisan>	out of 10
    Mar 05 16:40:07 <CuBe0wL>	huh... I've just looked back at the 4 years I've had with Nexuiz
    Mar 05 16:40:12 <CuBe0wL>	4...
    Mar 05 16:40:17 <Dokujisan>	:-)
    Mar 05 16:40:18 <CuBe0wL>	that can't be correct
    Mar 05 16:40:29 <Dokujisan>	i thikn I've been here more than 3
    Mar 05 16:40:29 <CuBe0wL>	it's my 6th year at the uni
    Mar 05 16:40:57 <CuBe0wL>	and I remember I was playing Nexuiz when I started it
    Mar 05 16:41:12 <CuBe0wL>	and I was away too for a half year or so
    Mar 05 16:41:33 <CuBe0wL>	because I was pissed that they've changed to push force of the laser :D
    Mar 05 16:41:37 <}-z-{>	Dokujisan: names list?
    Mar 05 16:42:20 <CuBe0wL>	looking back this far, I feel far more heartbroken we need to fork, or just generally stop playing at all
    Mar 05 16:42:43 *	mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 16:42:52 <}-z-{>	21:31:11 < motorsep> now I am wondering if guys will suck it up and continue with Nexuiz or start new project
    Mar 05 16:42:55 <}-z-{>	21:34:43 < }-z-{> I guess a lot of that depends on how Vermeulen goes about fixing this mess and earning back respect of some of the most influential contributors
    Mar 05 16:42:59 <}-z-{>	21:42:18 < Vermeulen> like i said before, there are certain developers I do need to discuss with and basically apologize for mishandling a number of things
    Mar 05 16:43:02 <}-z-{>	21:42:30 < Vermeulen> but when it comes to the name and the issue community members are having with the change, that was a decision i made that i am fine with taking the wrath for
    Mar 05 16:43:07 <}-z-{>	42:49 < Vermeulen> I should have been more open with the plans but it was always the intention to fund further nexuiz development with these funds. I didn't plan before about promising to be open with the exact royalty split but I  think that'll be the best way to make up for the mishandlings on my part with developers
    Mar 05 16:43:47 <CuBe0wL>	it seems he has quite hard days too
    Mar 05 16:44:07 <CuBe0wL>	he changes his opinion on the topic day by day
    Mar 05 16:44:34 <merlijn>	he is in the middle of a crossfire and wants to keep both parties happy
    Mar 05 16:44:55 <}-z-{>	he created the crossfire
    Mar 05 16:45:22 <merlijn>	sure, but we all make mistakes
    Mar 05 16:45:27 <Dokujisan>	<}-z-{> Dokujisan: names list?
    Mar 05 16:45:32 <Dokujisan>	I don't know how to create a page on that wiki
    Mar 05 16:45:37 <Dokujisan>	I don't see the option
    Mar 05 16:45:54 <}-z-{>	I told you two ways
    Mar 05 16:46:02 <}-z-{>	extend the url ...wiki/my_new_page
    Mar 05 16:46:07 <}-z-{>	or create a link on an existing page
    Mar 05 16:46:18 <}-z-{>	[my_new_page](linking text)
    Mar 05 16:46:19 <Dokujisan>	ok
    Mar 05 16:52:37 <Dokujisan>	http://dev.xonotic.org/projects/notnexuiz/wiki/Names
    Mar 05 16:52:47 <}-z-{>	noice
    Mar 05 16:54:18 <merlijn>	}-z-{: I just signed up for the redmine thing, can you approve?
    Mar 05 16:54:25 <}-z-{>	certainly
    Mar 05 16:54:45 <}-z-{>	pavlvs too
    Mar 05 16:55:03 <pavlvs>	ty
    Mar 05 16:56:41 <}-z-{>	added names list to the main wiki page
    Mar 05 16:59:25 <}-z-{>	I'm leaving work now, ttyl
    Mar 05 17:13:50 <esteel>	evening..
    Mar 05 17:14:14 <Spaceman>	evening
    Mar 05 17:17:38 <esteel>	hi Spaceman ;)
    Mar 05 17:34:53 *	mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 17:35:12 <mand1nga>	man, we should set like a deadline
    Mar 05 17:35:16 <mand1nga>	once we get everything ready
    Mar 05 17:35:31 <mand1nga>	and leave every alientrap-related thing, like irc, forum, etc
    Mar 05 17:35:41 <mand1nga>	everyone at once
    Mar 05 17:35:55 <Dokujisan>	hey guys... grasshoppers new map is looking really nice
    Mar 05 17:35:56 <Dokujisan>	http://pics.nexuizninjaz.com/viewer.php?file=3336oqc2tvlt8p6tsna1.jpg
    Mar 05 17:35:56 <mand1nga>	it'd be fun :P
    Mar 05 17:36:13 <Dokujisan>	he's putting a lot of emphasis on details with it
    Mar 05 17:36:53 <Dokujisan>	 haha yeah  mand1nga that would be interesting :-)
    Mar 05 17:39:45 *	[-z-] (~detrate@c-98-230-24-23.hsd1.fl.comcast.net) has joined #notnexuiz
    Mar 05 17:39:48 <mand1nga>	well there is no easy way of just leaving the forum, but maybe we all change our signatures the very same day, telling something about the cause
    Mar 05 17:40:36 <mand1nga>	it'd have a message and would be fun
    Mar 05 17:42:45 <}-z-{>	I'm not usually malicious but it would be possible to add something to the theme, like a banner about vermeulen that says, "all your work are belong to me. I sell it for the $$$" and make it very hard to remove
    Mar 05 17:43:04 <}-z-{>	but then again, it's probably just not worth it
    Mar 05 17:43:19 <}-z-{>	he just doesn't seem to get how he's hurt people
    Mar 05 17:43:34 <}-z-{>	he seems to act like it's all just going to blow over without him greasing the wheels at all
    Mar 05 17:43:58 <Spaceman>	its best to leave on amicable terms
    Mar 05 17:44:06 <mand1nga>	yes I perceive the same
    Mar 05 17:44:26 <[-z-]>	yeah
    Mar 05 17:44:41 <Spaceman>	just because verm* has been underhanded doesn't mean anybody else has to be
    Mar 05 17:44:44 <mand1nga>	Spaceman: well, sure, leaving without saying a single word will have a really strong effect too imho
    Mar 05 17:45:04 <Spaceman>	that's a better method
    Mar 05 17:45:15 <[-z-]>	there is still the power of the pen beyond that
    Mar 05 17:45:25 <[-z-]>	it'd be better to let a 3rd party write about the situation
    Mar 05 17:45:30 <[-z-]>	after it's all gone down
    Mar 05 17:45:32 <Spaceman>	can new nex copy the forum from alientrap?
    Mar 05 17:45:40 <[-z-]>	I'd rather not
    Mar 05 17:45:53 <[-z-]>	1) it's huge, 2) it's phpbb, 3) then we'd just be stealing right back
    Mar 05 17:46:00 <Spaceman>	there is a lot of information there
    Mar 05 17:46:03 <mand1nga>	[-z-]: sure
    Mar 05 17:46:14 <Samual>	You don't like phpbb?
    Mar 05 17:46:17 <[-z-]>	Spaceman: and we can port it all to the wiki
    Mar 05 17:46:27 <mand1nga>	I'm surprised this thing didn't reach /. yet
    Mar 05 17:46:30 <[-z-]>	Samual: they don't even have function hooks
    Mar 05 17:46:36 <[-z-]>	you have to hard mod your files
    Mar 05 17:46:42 <Spaceman>	maybe if individuals ask to transfer their posts
    Mar 05 17:46:52 <Spaceman>	but there would be lots of holes
    Mar 05 17:46:58 <Samual>	[17:46:02pm] <mand1nga> I'm surprised this thing didn't reach /. yet
    Mar 05 17:47:01 <Spaceman>	and it would look crap
    Mar 05 17:47:03 <Samual>	It will soon most likely
    Mar 05 17:47:05 <[-z-]>	Spaceman: I think it's better to just reorganize on the new website
    Mar 05 17:47:08 <mand1nga>	talking about phpbb, please I'd like to have a strict no mikee-like trolls allowed under any circumpstance
    Mar 05 17:47:13 <[-z-]>	we'll have an official picture, video and map repository
    Mar 05 17:47:30 <[-z-]>	mand1nga: there is a friend and foe list in mybb
    Mar 05 17:48:03 <mand1nga>	amazing
    Mar 05 17:48:28 <[-z-]>	I learned that mybb isn't the greatest for mass bans, hopefully that won't come into play soon though :-P
    Mar 05 17:48:57 <[-z-]>	because in a well moderated forum, you shouldn't need to do a mass ban / deletion of the banee's posts
    Mar 05 17:49:18 <mand1nga>	how then?
    Mar 05 17:49:26 <[-z-]>	how what?
    Mar 05 17:49:34 <mand1nga>	I mean if a mikee guy fills the forum with crap
    Mar 05 17:49:59 <mand1nga>	the only thing you can do is a mass deletion, etc
    Mar 05 17:50:19 <[-z-]>	well I don't think we'll need to use it
    Mar 05 17:50:26 <[-z-]>	there is also a warning system in mybb
    Mar 05 17:50:44 <[-z-]>	http://wiki.mybboard.net/index.php/Warning_System
    Mar 05 17:51:04 <mand1nga>	you say the the problem will solve itself with a reputation system and/or an ignore feature, more or less?
    Mar 05 17:51:22 <[-z-]>	yes they should and we should be able to ban users on a per user basis
    Mar 05 17:51:33 <[-z-]>	if we were trying to ban say 30 people at once, it wouldn't be so simple
    Mar 05 17:51:48 <[-z-]>	but you really shouldn't be trying to ban 30 users at once unless you have a poorly moderated forum
    Mar 05 17:52:06 <[-z-]>	this will likely solve itself as the frontend of the admin backend continues in development
    Mar 05 17:52:13 <[-z-]>	they did a major rewrite ~a year ago
    Mar 05 17:52:26 <[-z-]>	but the code is really well organized and the plugin system is well made
    Mar 05 17:52:32 <[-z-]>	there is also a bridge available to wordpress
    Mar 05 17:52:35 <mand1nga>	sure, or beign under attack, 30 ppl sounds quite massive to me
    Mar 05 17:52:36 <[-z-]>	so it seems like a good choice
    Mar 05 17:52:50 <[-z-]>	yes but being under attack, we disable user registration
    Mar 05 17:52:58 <[-z-]>	possible the forums, depending on the degree of the attack
    Mar 05 17:53:00 <mand1nga>	sure
    Mar 05 17:53:02 <[-z-]>	and then deal with ip tables from there
    Mar 05 17:53:24 <mand1nga>	I like those systems were one can report users doing funky things
    Mar 05 17:53:47 <[-z-]>	yes, you can do that with mybb too
    Mar 05 17:54:29 <mand1nga>	well .. unfortunately I think we should get ready on that, more than likely mikee will try to spread his crap again whenever we start a new forum
    Mar 05 17:54:45 <[-z-]>	yeah, shouldn't be a problem
    Mar 05 17:54:52 <[-z-]>	he was contained on the NN forums
    Mar 05 17:54:57 <Spaceman>	how many people have registered for the AT forums and how many are active?
    Mar 05 17:55:07 <[-z-]>	probably 1/8 or less are active
    Mar 05 17:55:10 <mand1nga>	cool
    Mar 05 17:55:17 <[-z-]>	Total members 2993
    Mar 05 17:55:22 <[-z-]>	yeah, I'd say ~100-300 active
    Mar 05 17:56:04 <[-z-]>	phpbb admitted does a few moderation controls better on the front-end but the foundation of the system is not as agile
    Mar 05 17:56:41 <[-z-]>	Users per day:  	2.04
    Mar 05 17:56:46 <[-z-]>	 	Topics per day:  	3.86
    Mar 05 17:56:51 <[-z-]>	Posts per day:  	50.45
    Mar 05 17:57:34 <mand1nga>	small but interesting forum
    Mar 05 17:57:46 <[-z-]>	~450 inactive accounts... not sure what classifies them as 'inactive' though
    Mar 05 17:58:31 <mand1nga>	I thought there were way more registered users, like 10k
    Mar 05 17:58:39 <[-z-]>	nahaha
    Mar 05 17:58:46 <[-z-]>	we're a small community
    Mar 05 17:58:58 <mand1nga>	indeed
    Mar 05 17:59:06 <[-z-]>	especially compared to urban terror
    Mar 05 17:59:56 <Samual>	Urban Terror can suck my dick
    Mar 05 18:00:10 <[-z-]>	yeah well, they capped a lot of CS kids
    Mar 05 18:00:15 <Samual>	Actually
    Mar 05 18:00:20 <[-z-]>	I can't seem to get a number on their forums
    Mar 05 18:00:21 <mand1nga>	I'm creator/moderator of a Nexuiz forum here in my country, we're mostly argentinians and chileans
    Mar 05 18:00:22 <Samual>	I wouldn't even let that filth do that
    Mar 05 18:00:25 <mand1nga>	about 10 active users :P
    Mar 05 18:00:25 <[-z-]>	but their servers were quite popular
    Mar 05 18:00:45 <[-z-]>	mand1nga: :)
    Mar 05 18:00:55 <[-z-]>	Nexuiz Diplomat of Chile
    Mar 05 18:00:56 <Samual>	Urban Terror has 27 major problems with it
    Mar 05 18:01:05 <Samual>	1-26: It's a rip off of CS
    Mar 05 18:01:05 <[-z-]>	27? lol
    Mar 05 18:01:11 <mand1nga>	connectivity with other countries like peru, colombia, ecuador, etc its pretty bad for playing, not sure why
    Mar 05 18:01:26 <Samual>	27: It's a rip off of CS and it also takes the CS community
    Mar 05 18:01:33 <mand1nga>	makes me thing maybe we should consider opening sections for specific languages
    Mar 05 18:01:36 <[-z-]>	Samual: those are weak reasons
    Mar 05 18:01:43 <mand1nga>	for non english writers/readers :P
    Mar 05 18:01:43 <Samual>	Oh you want actual reasons?
    Mar 05 18:01:48 <Samual>	It's easy to hack/cheat,
    Mar 05 18:01:56 <Samual>	The serverlist takes a longass time to populate
    Mar 05 18:01:59 <[-z-]>	do they distribute the source?
    Mar 05 18:01:59 <Samual>	The engine is ugly as hell
    Mar 05 18:02:14 <Samual>	Yes?
    Mar 05 18:02:14 <[-z-]>	I thought the engine was decent
    Mar 05 18:02:17 <[-z-]>	I haven't looked at the code
    Mar 05 18:02:26 <Samual>	I see so many aimbots on that game
    Mar 05 18:02:27 <[-z-]>	I wouldn't even know what to think if I did :-P
    Mar 05 18:02:28 <Samual>	You have no idea
    Mar 05 18:02:34 <mand1nga>	they have some sort of ragdoll support it seems
    Mar 05 18:02:41 <Samual>	That's hacked together :P
    Mar 05 18:02:41 <mand1nga>	but gfx are ugly imho
    Mar 05 18:02:45 <[-z-]>	no, I haven't logged into your brain in a while, so I have no idea :-P
    Mar 05 18:03:12 <Samual>	Good
    Mar 05 18:03:24 <Samual>	imo you aren't worthy
    Mar 05 18:03:27 <mand1nga>	maybe ppl enjoy more to shoot ppl like models
    Mar 05 18:03:38 <mand1nga>	I'm the opposite
    Mar 05 18:03:57 <mand1nga>	I'd rather to shoot an alien like thing :P
    Mar 05 18:04:22 <Samual>	I'd rather shoot people
    Mar 05 18:04:30 <Samual>	Not models, but people
    Mar 05 18:04:33 <Samual>	But well
    Mar 05 18:04:40 <[-z-]>	ls ~/samuals_brain
    Mar 05 18:04:44 <[-z-]>	microsoft.doc
    Mar 05 18:04:48 <Samual>	..............
    Mar 05 18:04:52 <mand1nga>	lmao
    Mar 05 18:04:52 <Samual>	......................................
    Mar 05 18:04:52 <[-z-]>	porn/
    Mar 05 18:04:52 <tZork>	lol
    Mar 05 18:05:05 <[-z-]>	stupid_things_z_says.txt
    Mar 05 18:05:08 <mand1nga>	"ls command not found"
    Mar 05 18:05:12 <tZork>	microsoft_porn/
    Mar 05 18:05:16 <[-z-]>	haha :-P
    Mar 05 18:05:56 <mand1nga>	tZork: cheers mate, having a b33r here :)
    Mar 05 18:06:14 <tZork>	balmer in pink latex dress. disturbing dont wuite cut it as description.. :D
    Mar 05 18:06:30 <tZork>	cheers mand1nga =) 
    Mar 05 18:06:34 <mand1nga>	lol
    Mar 05 18:06:53 <Samual>	ls ~/tylers_brain           ls: cannot access tylers_brain: No such file or directory
    Mar 05 18:07:12 <Samual>	Bitch.
    Mar 05 18:07:18 <[-z-]>	2 minutes and 13 seconds... new record time for a good comeback
    Mar 05 18:07:20 <[-z-]>	impressive
    Mar 05 18:07:26 <Samual>	stfu
    Mar 05 18:07:29 <[-z-]>	"that was awesome"
    Mar 05 18:07:30 <Samual>	Also: The game
    Mar 05 18:07:31 <mand1nga>	this thing I'm drinking, called "barley wine" beer has about 10% of alcohol 
    Mar 05 18:07:40 <[-z-]>	nice mand1nga, what brand?
    Mar 05 18:07:41 <mand1nga>	quite strong and tasty :)
    Mar 05 18:07:46 <[-z-]>	I like me a good barley wine
    Mar 05 18:07:51 <mand1nga>	Antares, a local brand
    Mar 05 18:07:55 <[-z-]>	ahh
    Mar 05 18:07:55 <mand1nga>	nice :)
    Mar 05 18:08:04 <mand1nga>	its quite good I must say
    Mar 05 18:08:05 <[-z-]>	do you get american imports?
    Mar 05 18:08:18 <mand1nga>	not really .... mostly from europe
    Mar 05 18:08:23 <[-z-]>	yeah, I figured :-P
    Mar 05 18:08:24 <mand1nga>	belgium, germany, etc
    Mar 05 18:08:35 <[-z-]>	you got some good cabranets, eh?
    Mar 05 18:08:39 <tZork>	hmm interesting. teh rather strong stuff (7+) usualy arent that great in my experiance. but the exceptions can be quite amazing
    Mar 05 18:08:42 <[-z-]>	in your region
    Mar 05 18:08:46 <mand1nga>	I don't know a single really good american beer .. sadly
    Mar 05 18:08:53 <[-z-]>	haha :-P
    Mar 05 18:09:05 <mand1nga>	cabranets? whats that?
    Mar 05 18:09:11 <[-z-]>	wine
    Mar 05 18:09:12 <[-z-]>	red wine
    Mar 05 18:09:14 <mand1nga>	cabernets? :P wine?
    Mar 05 18:09:19 <mand1nga>	oh sure :)
    Mar 05 18:09:23 <[-z-]>	my bad :-P
    Mar 05 18:09:36 <[-z-]>	not my wine of choice but when I have ones from chile, they are always good and cheap
    Mar 05 18:09:39 <mand1nga>	yes we have quite good wine
    Mar 05 18:09:59 <[-z-]>	malbec is native to your region?
    Mar 05 18:09:59 <mand1nga>	yes, price/quality is fine
    Mar 05 18:10:12 <mand1nga>	not sure .. I don't know really
    Mar 05 18:10:13 <[-z-]>	http://www.greatdivide.com/ << good american beer
    Mar 05 18:10:16 <tZork>	i have good experianc of wine from chile too
    Mar 05 18:10:23 <mand1nga>	but its my favourite type :)
    Mar 05 18:10:39 <[-z-]>	seriously mand1nga, I've had $5 dollar wines from chile they kicked the crap out of a $40 bottle
    Mar 05 18:10:42 <mand1nga>	new zealand and france will always have better wines
    Mar 05 18:10:55 <[-z-]>	because of their long fertile soil?
    Mar 05 18:11:05 <[-z-]>	possibly their latitude
    Mar 05 18:11:19 <mand1nga>	I know, I think we're trying hard to get better on that
    Mar 05 18:11:31 <[-z-]>	I'm very please so far :-P
    Mar 05 18:11:33 <mand1nga>	probably the soil, not sure
    Mar 05 18:11:36 <[-z-]>	you guys are the google of redwine
    Mar 05 18:11:39 <tZork>	heh i think i tasted old ruffian at some pont.. but i cant remerb if it was good. just the name stuck :P
    Mar 05 18:11:49 <[-z-]>	tZork: that's a goodie
    Mar 05 18:11:50 <mand1nga>	hahaha
    Mar 05 18:12:02 <tZork>	(wrt to greatdivide)
    Mar 05 18:12:12 <[-z-]>	yeah, I got that ;)
    Mar 05 18:12:53 <tZork>	hm ale
    Mar 05 18:13:01 <[-z-]>	that's in a great place in the united states for beer and skiing/snowboarding
    Mar 05 18:13:04 <[-z-]>	Colorado
    Mar 05 18:13:10 <mand1nga>	nice
    Mar 05 18:13:25 <mand1nga>	[-z-]: tell me a nice beer brand from there
    Mar 05 18:13:49 <[-z-]>	from colorado? great divide
    Mar 05 18:14:03 <[-z-]>	dogfish head I think is in New Hampsire, which is east coast
    Mar 05 18:14:10 <[-z-]>	that's another good american brewery
    Mar 05 18:14:30 <mand1nga>	in fact I had a few nice beers while I was in ny but I don't remember the names at all :>
    Mar 05 18:14:43 <[-z-]>	I read an article about the owner in entrepreneur magazine and he seems like a really cool guy that knows what he's doing and loves beer
    Mar 05 18:15:18 <[-z-]>	hmm delaware
    Mar 05 18:15:20 <[-z-]>	http://www.dogfish.com/
    Mar 05 18:15:25 <mand1nga>	at the mc gees and .. the blue note jazz club
    Mar 05 18:16:12 <esteel>	nighty
    Mar 05 18:16:19 <mand1nga>	nn esteel 
    Mar 05 18:16:20 <[-z-]>	night
    Mar 05 18:16:24 <[-z-]>	mand1nga: I haven't been to either
    Mar 05 18:16:28 <[-z-]>	NYC is huge :)
    Mar 05 18:18:30 <mand1nga>	no doubt :P
    Mar 05 18:18:30 <mand1nga>	well sadly this was the last one
    Mar 05 18:18:31 <mand1nga>	but I have fernet, probably you never heard about that 
    Mar 05 18:19:41 <mand1nga>	http://en.wikipedia.org/wiki/Fernet
    Mar 05 18:19:48 <[-z-]>	nope :-P
    Mar 05 18:20:03 <[-z-]>	sounds nice
    Mar 05 18:20:04 <DibTop>	cool Dokujisan 
    Mar 05 18:20:06 <mand1nga>	this must be my 3rd favorite beverage
    Mar 05 18:20:12 <DibTop>	i guess ill work on it again 
    Mar 05 18:20:18 <[-z-]>	I wonder if they carry it around here
    Mar 05 18:20:25 <mand1nga>	beer, wine, fernet .. wishkey might do .. but I'm not that old yet :P
    Mar 05 18:20:26 <[-z-]>	do you usually mix it?
    Mar 05 18:20:37 <mand1nga>	whisky*
    Mar 05 18:20:54 <mand1nga>	yes, with coca cola/pepsi/tonic
    Mar 05 18:20:55 DibTop div0 
    Mar 05 18:21:09 <Dokujisan>	DibTop: we played a second match on it and again it played well. It was a little tiny bit campy
    Mar 05 18:21:14 <Dokujisan>	but generally not bad
    Mar 05 18:21:17 DibTop div0 
    Mar 05 18:21:20 <DibTop>	cool stuff
    Mar 05 18:21:21 <mand1nga>	its really popular here, seems to be a thing from Italy though
    Mar 05 18:21:22 <DibTop>	that map is old
    Mar 05 18:21:28 <Dokujisan>	DibTop: also dublpaws is giving dance a makeover
    Mar 05 18:21:36 <DibTop>	cool
    Mar 05 18:21:41 <Dokujisan>	dunno if you want to try to mimic the new style or not
    Mar 05 18:22:02 <Dokujisan>	it's on bc1 as dance_beta1
    Mar 05 18:22:21 <[-z-]>	Dokujisan: are you aware that have have a revision of zion?
    Mar 05 18:22:28 <Dokujisan>	no
    Mar 05 18:22:33 <[-z-]>	it's not quite finished
    Mar 05 18:22:41 <[-z-]>	I need to work on the bases and maybe textures
    Mar 05 18:22:46 <[-z-]>	but it's a lot more in depth
    Mar 05 18:22:48 <Dokujisan>	ok
    Mar 05 18:23:16 <[-z-]>	now my mouse cursor disappears over my channel list...
    Mar 05 18:23:37 <[-z-]>	I hate computers sometimes
    Mar 05 18:23:56 <Dokujisan>	:-)
    Mar 05 18:24:35 <Samual>	lawl
    Mar 05 18:24:39 <Samual>	I see three mouse pointers
    Mar 05 18:24:49 <Samual>	xinerama draws one for every x screen
    Mar 05 18:24:49 <[-z-]>	I have the stupid kde-cursor now too
    Mar 05 18:24:59 <Samual>	Yes I do too for firefox
    Mar 05 18:25:02 <[-z-]>	Samual: ever see xdmx?
    Mar 05 18:25:07 <Samual>	No?
    Mar 05 18:25:08 <[-z-]>	http://dmx.sourceforge.net
    Mar 05 18:25:08 <Samual>	What is it?
    Mar 05 18:25:18 <[-z-]>	distributed multihead x
    Mar 05 18:25:27 <[-z-]>	probably slow as hell but 1337!
    Mar 05 18:25:41 <Samual>	Hmm
    Mar 05 18:25:48 <Samual>	xserver-xgl is fast at least
    Mar 05 18:25:56 <Samual>	I'll check it out later though
    Mar 05 18:26:11 <[-z-]>	xserver-xgl?
    Mar 05 18:26:18 <DibTop>	btw i think we should stop changing physics
    Mar 05 18:26:31 <DibTop>	for nexuiz i mean 2.6 or whatever
    Mar 05 18:26:36 <[-z-]>	after we implement moonjumping ability for 10 seconds after a headshot
    Mar 05 18:29:43 *	mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 18:32:07 <Samual>	xserver-xgl = old shit which isn't being developed anymore
    Mar 05 18:32:13 <Samual>	It allows my 3 monitors to work with compiz
    Mar 05 18:32:42 <[-z-]>	ah
    Mar 05 18:46:00 *	mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 05 19:12:13 <CuBe0wL>	gn all
    Mar 05 19:12:27 <Taoki>	night
    Mar 05 20:59:53 *	tZork is now known as tZork|gone
    Mar 05 21:16:27 *	Dokujisan has changed the topic to:  Details are posted on the Wiki -- http://dev.xonotic.org -- temporary development site to get organized
    Mar 05 21:20:41 *	Samual gives channel operator status to mand1nga
    Mar 05 21:20:46 *	Samual gives channel operator status to [-z-]
    Mar 05 21:50:33 *	johngalt (~mshade@ip98-169-164-171.dc.dc.cox.net) has joined #notnexuiz
    Mar 05 21:50:56 <johngalt>	hi guys
    Mar 05 21:51:22 <Dokujisan>	:-)
    Mar 05 21:51:33 <Dokujisan>	johngalt: go here and register
    Mar 05 21:51:34 <Dokujisan>	http://dev.xonotic.org
    Mar 05 21:51:41 <Dokujisan>	and i'll activate you
    Mar 05 21:51:45 <Dokujisan>	so you can read the Wiki
    Mar 05 21:52:03 <johngalt>	reg'd
    Mar 05 21:52:10 <johngalt>	can I let Deiz in on this?
    Mar 05 21:52:20 <Dokujisan>	activated
    Mar 05 21:52:24 <Dokujisan>	who is Deiz?
    Mar 05 21:52:39 <Samual>	Hey John
    Mar 05 21:52:43 <johngalt>	old school player, good friend of mine.  
    Mar 05 21:52:50 <johngalt>	if you want it admin only, thats definitely cool
    Mar 05 21:53:02 <johngalt>	understand the need for keeping close to the vest
    Mar 05 21:53:06 <Dokujisan>	I mean... sure there will be lots of people who get involved, but not everyone is in this channel
    Mar 05 21:53:11 <Dokujisan>	yeah
    Mar 05 21:53:25 <Dokujisan>	for example, I'm keeping the Aussies updated, but they are in another channel
    Mar 05 21:54:03 <Dokujisan>	we'll get more people in on the discussions after some of this initial stuff is covered
    Mar 05 21:55:12 <johngalt>	k
    Mar 05 21:55:43 <DibTop>	hi johngalt :)
    Mar 05 21:55:47 <johngalt>	hiya
    Mar 05 21:56:01 <DibTop>	howve you been?
    Mar 05 21:56:09 *	Deiz_ (~swh@69-196-147-186.dsl.teksavvy.com) has joined #notnexuiz
    Mar 05 21:57:02 <johngalt>	good
    Mar 05 21:57:14 <johngalt>	busy as hell
    Mar 05 21:57:33 <DibTop>	hah i bet, i havent seen you in a very long time
    Mar 05 21:57:36 *	mand1nga has quit ("http://www.mibbit.com ajax IRC Client")
    Mar 05 21:57:41 <johngalt>	i had server up again for a short while
    Mar 05 21:57:50 <Dokujisan>	yeah I saw that. Was that with softlayer?
    Mar 05 21:58:12 <johngalt>	it was on peer1
    Mar 05 21:58:17 <johngalt>	serverbeach reseller
    Mar 05 21:58:26 <johngalt>	damn good price i got on that actually
    Mar 05 21:58:36 <DibTop>	yup so that
    Mar 05 21:58:41 <johngalt>	but the community had changed so much i couldn't get into it much.  then this
    Mar 05 21:58:54 <johngalt>	took it down a day or two before this whole illfonic thing came to light
    Mar 05 21:59:27 <DibTop>	ya
    Mar 05 21:59:33 <DibTop>	im just mad at lee
    Mar 05 21:59:39 <DibTop>	not even mad at illfonic atm
    Mar 05 21:59:45 <johngalt>	i think we all are.  a no show for the last however long
    Mar 05 22:00:00 <DibTop>	seems a lot of people are lashing out illfonic
    Mar 05 22:00:01 <johngalt>	and then... "Oh, yes, it's all about the community.  This is good for you.  Take your medicine."
    Mar 05 22:00:15 <DibTop>	i honestly hold lee responsible for it
    Mar 05 22:00:17 <johngalt>	illfonic are just the opportunists, not the root.
    Mar 05 22:00:20 <johngalt>	anyway
    Mar 05 22:00:27 <johngalt>	we know what happened, that's why we're here.
    Mar 05 22:00:31 *	johngalt reads wiki
    Mar 05 22:00:32 <DibTop>	johngalt>	illfonic are just the opportunists, not the root.
    Mar 05 22:00:33 <DibTop>	exactly
    Mar 05 22:00:42 <Dokujisan>	http://pics.nexuizninjaz.com/viewer.php?file=rogou3t1yz0f4qpo9x.jpg
    Mar 05 22:00:52 <Deiz_>	It was a good opportunity, potentially.
    Mar 05 22:01:02 <Deiz_>	The name licensing and attempted rebranding squandered it.
    Mar 05 22:01:32 <Deiz_>	The disingenuous babble from the Illfonic rep didn't help, though.
    Mar 05 22:02:03 <Deiz_>	How's (license) mobility to be combined with safety from a future incident?
    Mar 05 22:02:41 <Dokujisan>	nice to meet ya Deiz_ 
    Mar 05 22:02:56 <Deiz_>	Hello.
    Mar 05 22:03:19 <Deiz_>	We've met, I think, but I've been out for ages.
    Mar 05 22:04:00 <DibTop>	i think im gonna work on modeling mostly
    Mar 05 22:04:18 <DibTop>	thats where we seriously lack
    Mar 05 22:04:24 <Dokujisan>	yes!
    Mar 05 22:04:27 <Dokujisan>	definitely
    Mar 05 22:04:30 <DibTop>	and i dont think we should release until we have new models
    Mar 05 22:04:35 DibTop div0 
    Mar 05 22:04:40 <johngalt>	DibTop: do you have modeling experience?
    Mar 05 22:04:41 <DibTop>	i think we can show up the console nexuiz
    Mar 05 22:04:43 <johngalt>	rigging?
    Mar 05 22:04:44 <Dokujisan>	DibTop: how are you learning about rigging models?
    Mar 05 22:04:48 <DibTop>	johngalt: not modeling but some animating
    Mar 05 22:04:54 <DibTop>	already know how to rig Dokujisan 
    Mar 05 22:04:59 <Dokujisan>	how did you learn
    Mar 05 22:05:02 <johngalt>	Rigging Dokujisan is easy.
    Mar 05 22:05:06 <DibTop>	blender tut
    Mar 05 22:05:09 <DibTop>	need it?
    Mar 05 22:05:09 <johngalt>	Just get him excited, he rigs himself.
    Mar 05 22:05:42 <Dokujisan>	well, so anyone can follow a blender animation tutorial and they can animate models for nexuiz? or is there more information needed about nexuiz to finalize it?
    Mar 05 22:05:52 <DibTop>	more info needed
    Mar 05 22:05:59 <DibTop>	and im still working on documenting that
    Mar 05 22:06:01 <Dokujisan>	ok where did you get info?
    Mar 05 22:06:05 <Dokujisan>	yeah that's what I'm getting at
    Mar 05 22:06:10 <DibTop>	it needs to be documented
    Mar 05 22:06:24 <Dokujisan>	Who in Nexuiz has that information though, currently?
    Mar 05 22:06:25 <DibTop>	ill write something up after i get it in nexuiz and working
    Mar 05 22:06:33 <DibTop>	i think Morphed does
    Mar 05 22:06:35 <johngalt>	is there anything we need to look at legally for a fork?
    Mar 05 22:06:36 <Dokujisan>	ok
    Mar 05 22:06:37 <DibTop>	but only for 3ds max
    Mar 05 22:06:43 <DibTop>	he dosent use blender
    Mar 05 22:06:51 <DibTop>	tzork has some knowledge as well
    Mar 05 22:06:55 <DibTop>	more with 3ds though
    Mar 05 22:07:01 <DibTop>	obi = 3ds too
    Mar 05 22:07:15 <Dokujisan>	johngalt: I don't think so. Everything in Nexuiz content wise was GPL compatible, and unlike illfonic, we're forking into another GPL game
    Mar 05 22:07:28 <Dokujisan>	we may need to strip out references to "nexuiz"
    Mar 05 22:07:35 <johngalt>	i think that's correct.
    Mar 05 22:07:40 <johngalt>	just putting the question out there.
    Mar 05 22:09:47 <Deiz_>	Licensing hurts my brain.
    Mar 05 22:09:50 <Dokujisan>	heh
    Mar 05 22:10:05 <johngalt>	so much of GPL is untested
    Mar 05 22:10:12 <johngalt>	and most of it misunderstood :)
    Mar 05 22:10:38 <johngalt>	so as far as naming goes, are we trying to keep to something similar, or is anything fair game?
    Mar 05 22:10:44 <Deiz_>	It gets extended.
    Mar 05 22:11:02 <Dokujisan>	there are ideas started for names in the wiki
    Mar 05 22:11:08 <johngalt>	yeah, I'm looking at that now
    Mar 05 22:11:08 <Dokujisan>	that's just a step 1 though
    Mar 05 22:11:12 <Deiz_>	You can't close my code, it's GPLed... You can't remove that load-bearing wall, it's GPLed.
    Mar 05 22:11:52 <Deiz_>	I'm assuming the game code  license will be set in stone, as changing it'd require all past contributors to be in agreement.
    Mar 05 22:12:03 <Deiz_>	The Nexuiz repo never had copyright assignment like Darkplaces, did it?
    Mar 05 22:12:04 <Dokujisan>	each time I mention the fork, that's an immediate question about the name, understandably. I think it's wise to take proper time to figure out the name.
    Mar 05 22:12:43 <Deiz_>	It's hard to do worse than "Neck-see-us" which is spelled "Neck-shoe-is".
    Mar 05 22:12:48 <Dokujisan>	yep :-)
    Mar 05 22:12:52 <johngalt>	Dokujisan: absolutely. name is least important aspect. 
    Mar 05 22:12:52 <Dokujisan>	that's the point i keep making
    Mar 05 22:13:00 <Dokujisan>	that "nexuiz" is actually a pretty bad name
    Mar 05 22:13:03 <johngalt>	at least immediately
    Mar 05 22:13:21 <Dokujisan>	"Nexiuz" wouldn't have been a bad name though
    Mar 05 22:13:38 <Dokujisan>	and then kanji "n" symbol looked good
    Mar 05 22:14:08 <Deiz_>	Heh
    Mar 05 22:14:16 <Deiz_>	On that map screenshot, the texture on the right side is backwards.
    Mar 05 22:14:42 <johngalt>	which screenshot?
    Mar 05 22:14:48 <Deiz_>	http://pics.nexuizninjaz.com/viewer.php?file=rogou3t1yz0f4qpo9x.jpg
    Mar 05 22:14:56 <johngalt>	ah
    Mar 05 22:17:02 <Dokujisan>	http://pics.nexuizninjaz.com/viewer.php?file=zbcmceics6shje6u8wk9.jpg
    Mar 05 22:17:06 <Dokujisan>	that one is funny :-)
    Mar 05 22:17:33 <johngalt>	hahah
    Mar 05 22:17:52 <Deiz_>	Was he incommunicado for that entire time, or just making very minor contributions?
    Mar 05 22:20:48 <johngalt>	Deiz_: http://dev.alientrap.org/repositories/stats/nexuiz
    Mar 05 22:21:22 <Deiz_>	Heh. Insufficient resolution to make out whether it's non-zero.
    Mar 05 22:21:32 <johngalt>	well he's on there twice
    Mar 05 22:21:40 <johngalt>	vermeulen and vermeulenl
    Mar 05 22:21:43 <Deiz_>	Ah, yes.
    Mar 05 22:23:20 <Deiz_>	http://www.ohloh.net/p/nexuiz/contributors/1595580376992
    Mar 05 22:24:27 <Deiz_>	So, no major commit flurries since mid-2005.
    Mar 05 22:24:30 <Dokujisan>	alright I gotta crash. Cya later...
    Mar 05 22:24:40 <johngalt>	seeya doku
    Mar 05 22:29:32 <Samual>	http://www.ohloh.net/p/nexuiz/contributors/1595580541087
    Mar 05 22:29:33 <Samual>	Yay
    Mar 05 22:29:38 <Samual>	I feel important
    Mar 05 22:30:03 <Samual>	http://www.ohloh.net/p/nexuiz/contributors/1595580541086
    Mar 05 22:30:04 <Samual>	ohshi
    Mar 05 22:30:09 <Samual>	FruitieX > Me
    Mar 05 22:30:27 <pavlvs>	oh hello Deiz_ 
    Mar 05 22:33:33 <DibTop>	hrm i wonder if someone can retexture the marine model
    Mar 05 22:33:39 <DibTop>	cause its really not that bad
    Mar 05 22:33:57 <DibTop>	just needs new art
    Mar 05 22:37:43 <johngalt>	hiya pavlvs 
    Mar 05 22:37:56 <pavlvs>	hi johngalt 
    Mar 05 22:37:58 *	Taoki has quit (Ping timeout: 120 seconds)
    Mar 05 22:41:46 <Samual>	BTW, div0's work: This developer has been contributing to this project since March 2006, with a total of 43 person-months of code development. He or she made a total of 4652 commits and the main programming language used was C.
    Mar 05 22:42:01 *	pavlvs327 (pavlvs@adsl-75-39-134-107.dsl.tpkaks.sbcglobal.net) has joined #notnexuiz
    Mar 05 22:42:03 <Samual>	4652 commits :P
    Mar 05 22:42:17 <johngalt>	yep.  div0 *is* nexuiz.
    Mar 05 22:42:22 <johngalt>	or isnot nexuiz
    Mar 05 22:42:35 *	esteel1 (OQBFtg94ui@planetnexuiz.de) has joined #notnexuiz
    Mar 05 22:42:35 <Samual>	That's more than half damnit :P
    Mar 05 22:42:58 *	Spaceman_1 (~Spaceman@87.127.156.98) has joined #notnexuiz
    Mar 05 22:43:04 *	esteel has quit (Ping timeout: 120 seconds)
    Mar 05 22:43:04 *	Spaceman has quit (Ping timeout: 120 seconds)
    Mar 05 22:43:04 *	pavlvs has quit (Ping timeout: 120 seconds)
    Mar 06 01:22:04 <[-z-]>	wasn't the marine just retextured?
    Mar 06 01:31:13 <DibTop>	-z- not really
    Mar 06 01:31:26 <[-z-]>	o rly?
    Mar 06 01:31:27 <DibTop>	well it was kind of but maybe 6 months ago
    Mar 06 01:31:34 <DibTop>	it could use gloss, bump etc
    Mar 06 01:31:39 <DibTop>	to make it look better
    Mar 06 01:35:25 <[-z-]>	http://image.com.com/gamespot/images/2010/060/990996_20100302_790screen006.jpg
    Mar 06 01:35:36 <[-z-]>	am I wrong or is that shot not coming out of the gun?
    Mar 06 01:36:38 <pavlvs327>	persistent trails?
    Mar 06 01:36:58 *	pavlvs327 is now known as pavlvs
    Mar 06 01:36:59 <[-z-]>	so it was shot and that's the trail fading?
    Mar 06 01:37:10 <pavlvs>	tahts my assumption
    Mar 06 01:38:07 <DibTop>	similar to the nex affect probably
    Mar 06 01:38:58 <pavlvs>	althoguh if they're using nexuiz gamecode... ;p
    Mar 06 01:39:11 <[-z-]>	HLAC seems suspicious
    Mar 06 01:39:13 <pavlvs>	shot origins have been pretty messed up :)
    Mar 06 01:39:58 <[-z-]>	where did I jus tread the weapons list about their game?
    Mar 06 01:41:17 <[-z-]>	LOL, this page comes up in a google search for Nexuiz weapons http://dev.alientrap.org/wiki/1/Weapons
    Mar 06 01:41:28 <pavlvs>	[-z-]: the first post of the original illfonic thread, 2nnd para of GDC header
    Mar 06 01:41:28 <pavlvs>	iirc
    Mar 06 01:41:36 <[-z-]>	ah
    Mar 06 01:41:45 <[-z-]>	yeah is the hlac from another game?
    Mar 06 01:42:26 <DibTop>	no its from this one
    Mar 06 01:42:37 <DibTop>	tzork was pretty pissed about that :S
    Mar 06 01:42:39 <pavlvs>	no
    Mar 06 01:42:39 <pavlvs>	tZork|gone invented it
    Mar 06 01:42:45 <[-z-]>	yeah, I'd be pissed too
    Mar 06 01:42:50 <DibTop>	me too
    Mar 06 01:42:52 <pavlvs>	i was using it as an example of where Lee didnt get appropriate permission
    Mar 06 01:42:56 <[-z-]>	vermeulen really screwed up this time
    Mar 06 01:43:05 <DibTop>	this time?
    Mar 06 01:43:10 <DibTop>	hes screwed up before?
    Mar 06 01:43:26 <[-z-]>	he's made some odd moves in the past
    Mar 06 01:43:53 <[-z-]>	I have some personal discoveries with him
    Mar 06 01:43:54 <DibTop>	this was a good move in all honesty just horrendous outcome/planning
    Mar 06 01:44:10 <[-z-]>	yeah the screwed the pooch on execution
    Mar 06 01:44:42 <[-z-]>	I don't think it would have been hard to get the community on board
    Mar 06 01:44:58 <[-z-]>	but instead of asking "for permission", he's asking "for forgiveness"
    Mar 06 01:45:05 <[-z-]>	but he's really not even asking for forgiveness
    Mar 06 01:45:12 <[-z-]>	which pisses me off even more
    Mar 06 01:45:14 <pavlvs>	yup
    Mar 06 01:45:58 <[-z-]>	I tried to bring this up to him, saying maybe he should hunt down the contributors it's affected the most
    Mar 06 01:46:28 <[-z-]>	and he seemed to think that without royalities, the contributors wouldn't care... but I don't think anyone is really concerned about the money
    Mar 06 01:47:28 <[-z-]>	more so a better explanation, an apology and a plan of action
    Mar 06 01:57:06 <DibTop>	i should sue if they use accuracy stats :P
    Mar 06 01:57:42 <pavlvs>	well the problem is
    Mar 06 01:57:56 <pavlvs>	its closed source, so you dont know if they reused your code or not
    Mar 06 01:58:06 <pavlvs>	so you have to sue for the code
    Mar 06 01:58:43 <DibTop>	haha true true
    Mar 06 03:09:35 <FruitieX>	01:02:46 < mand1nga> they have some sort of ragdoll support it seems
    Mar 06 03:09:44 <FruitieX>	UrbanTerror? Ragdoll? errrrrr. NO. :P
    Mar 06 03:11:26 <FruitieX>	o, maybe new release
    Mar 06 03:35:26 <Morphed>	i wonder if that console nexuiz will have ragdolls 
    Mar 06 04:06:42 <CuBe0wL>	morning
    Mar 06 04:08:03 <Morphed>	hi
    Mar 06 04:27:32 <CuBe0wL>	google Agents for Games and Simulations: Trends in Techniques, Concepts and Design (Frank Dignum) :D
    Mar 06 05:01:21 *	mand1nga (ba88357b@webchat.mibbit.com) has joined #notnexuiz
    Mar 06 05:11:43 *	Spaceman_1 is now known as Spaceman
    Mar 06 05:46:02 *	Morphed_ (Morphed@aapi142.neoplus.adsl.tpnet.pl) has joined #notnexuiz
    Mar 06 05:47:47 *	esteel1 is now known as esteel
    Mar 06 05:49:17 *	Morphed has quit (Ping timeout: 364 seconds)
    Mar 06 06:16:48 *	MrBougo (~MrBougo@ip-213-49-242-191.dsl.scarlet.be) has joined #notnexuiz
    Mar 06 06:16:55 <MrBougo>	welp.
    Mar 06 06:17:14 <Spaceman>	hello MrBougo
    Mar 06 06:17:29 <MrBougo>	I'm interested in the motives of this, why do you guys think it is beneficial to fork?
    Mar 06 06:18:50 <pavlvs>	looks like new name
    Mar 06 06:19:27 <pavlvs>	and the obvious reason to get out of alientrap so an absentee "owner" cant sell it out
    Mar 06 06:19:47 <pavlvs>	not sure if that part requires a fork really
    Mar 06 06:20:12 <MrBougo>	so you're planning to "move out", taking the community as a whole away from alientrap
    Mar 06 06:20:18 <MrBougo>	how would this work out?
    Mar 06 06:20:30 <MrBougo>	would lee give up his project?
    Mar 06 06:21:39 <Spaceman>	there would still be the possibility of a GPL Nexuiz
    Mar 06 06:22:03 <MrBougo>	how so?
    Mar 06 06:22:08 <MrBougo>	it still is possible
    Mar 06 06:22:09 <Spaceman>	a gpl nexuiz could use the code from the fork version
    Mar 06 06:22:16 <Spaceman>	forked*
    Mar 06 06:22:27 <MrBougo>	nexuiz is still gpl
    Mar 06 06:22:33 <MrBougo>	I mean, nexuiz pc
    Mar 06 06:23:23 <merlijn>	the part I still don't like is that if there is a fork, both projects would coexist for a while at least
    Mar 06 06:23:38 <MrBougo>	this^
    Mar 06 06:23:38 <pavlvs>	yeah same
    Mar 06 06:23:55 <Spaceman>	sorry, I meant that there would be the possibility of new version of gpl nexuix being published in th e future
    Mar 06 06:24:01 <MrBougo>	that's why this seems risky to me
    Mar 06 06:24:05 <MrBougo>	how do you move a whole community
    Mar 06 06:24:20 <MrBougo>	granted, it isn't that big, and the main elements will surely change if they see the others do
    Mar 06 06:24:35 <MrBougo>	one question
    Mar 06 06:24:37 <merlijn>	I'd want alientrap.org/nexuiz to say something along the lines of "Nexuiz is discontinued, however it is revamped by project XXX"
    Mar 06 06:24:42 <pavlvs>	div0 still hasnt said anyhting in here
    Mar 06 06:24:47 <MrBougo>	will all the developers move too?
    Mar 06 06:24:48 <pavlvs>	i am kinda waiting on his thoughts
    Mar 06 06:25:22 <MrBougo>	and what prevents nexuiz from importing notnexuiz's changes as they come
    Mar 06 06:26:04 <MrBougo>	of course they can't sell it anymore then :p
    Mar 06 06:26:15 <Spaceman>	who will publish the gpl nexuiz version?
    Mar 06 06:26:24 <MrBougo>	bbl
    Mar 06 06:26:39 <Spaceman>	I'm assuming the developers will abandon alientrap for the new project#
    Mar 06 06:27:04 <Spaceman>	pavlvs: div0 has said lots
    Mar 06 06:27:11 <Morphed_>	all devs that have some self respect :)
    Mar 06 06:34:35 <Spaceman>	Dokujisan: can you add log from http://www.nullgaming.com/stuff/notnexuiz.log to the wiki
    Mar 06 07:09:39 *	Taoki (kvirc@93.113.162.42) has joined #notnexuiz
    Mar 06 07:32:09 <MrBougo>	Spaceman, 404
    Mar 06 07:32:21 <MrBougo>	who logs this channel?
    Mar 06 07:32:52 <Spaceman>	the url was working yesterday
    Mar 06 07:33:21 <Spaceman>	the wiki was added last night and some of the log has been added to the wike
    Mar 06 07:33:24 <Spaceman>	wiki
    Mar 06 07:34:46 <Spaceman>	MrBougo: I can add my log but it only started 10:00 yesterday
    Mar 06 07:35:58 <MrBougo>	put "this channel is logged" in the topic at least :p
    Mar 06 07:37:22 <MrBougo>	Morphed, that was off-topic and uncalled for
    Mar 06 07:37:43 <Dokujisan>	Spaceman: sure
    Mar 06 07:38:02 <Spaceman>	how do you add a page to the wiki?
    Mar 06 07:38:08 <MrBougo>	you guys should get some info page up
    Mar 06 07:38:53 <MrBougo>	explaining your motives, why you believe it's a good thing, and where you think this is going
    Mar 06 07:38:58 <Dokujisan>	Spaceman: the easiest way is to add a name to end of the URL
    Mar 06 07:39:20 <Dokujisan>	MrBougo: have you registered wtih the site and looked through the wiki?
    Mar 06 07:39:25 <MrBougo>	no
    Mar 06 07:39:32 <MrBougo>	and I mean a public page
    Mar 06 07:39:32 <Dokujisan>	http://dev.xonotic.org
    Mar 06 07:39:39 <Dokujisan>	we'll do that eventually
    Mar 06 07:39:42 <MrBougo>	unless this is a secret project
    Mar 06 07:39:55 <Dokujisan>	it is somewhat secret at the moment, only to help us focus
    Mar 06 07:39:59 <MrBougo>	are you going to get this started when things settle down?
    Mar 06 07:40:03 <Spaceman>	I tried http://dev.xonotic.org/projects/notnexuiz/wiki/test
    Mar 06 07:40:17 <Spaceman>	404 The page you were trying to access doesn't exist or has been removed.
    Mar 06 07:40:29 <Dokujisan>	Spaceman: you might not have page creation rights
    Mar 06 07:40:33 <Spaceman>	maybe I need to be an admin
    Mar 06 07:40:42 <Dokujisan>	that URL opens a blank edit screen for me
    Mar 06 07:40:46 *	Spaceman prods [-z-]
    Mar 06 07:40:55 <Dokujisan>	Spaceman: what did you want to add?
    Mar 06 07:41:01 <Dokujisan>	I can change your permissions
    Mar 06 07:41:03 <MrBougo>	Spaceman, meanwhule ask somebody whocan :p
    Mar 06 07:41:04 <MrBougo>	woops
    Mar 06 07:41:07 <MrBougo>	typos
    Mar 06 07:41:08 <Spaceman>	my irc log
    Mar 06 07:41:23 <Dokujisan>	Spaceman: I'm gonna add my entire IRC log from when I first entered this channel
    Mar 06 07:41:34 <Spaceman>	that is even better
    Mar 06 07:41:34 <Dokujisan>	so that should include your log
    Mar 06 07:41:36 <Dokujisan>	k
    Mar 06 07:41:47 <Spaceman>	mine is only 26 hours
    Mar 06 07:41:57 <Spaceman>	thanks

