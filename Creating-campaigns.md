## Creating campaigns

This page explains how to create campaigns for Xonotic.

## Basics

Xonotic uses text files to store campaigns.

Campaigns are text files with the name “`campaign<name>.txt`”, where `<name>` can be any alphanumeric identifier which is used to uniquely identify the campaign.

Example: `campaignxonoticbeta.txt`

## File syntax

It's basically like CSV (Comma-Separated Values), but with comments.

The following lines are possible

* Campaign title: Must be always the first line and has the form `//campaign:<Name>`, where `<Name>` is the human-readable campaign title.
* Empty lines: Are ignored
* Comments: These lines start with `//` and are ignored (except the 1st line which is a special case)
* Level definitions: This is a comma-separated list. Each value must be delimeted by quotation marks (e.g. `"value"`). You can omit the quotation marks for empty values, *except* for the last item in the list

### Level definition

A comma-separated list (see above). Each level is exactly one line. The meaning of the values in a line must follow this order:

* Game mode: The short codename for the game mode (e.g. `dm` for deathmatch, `kh` for Key Hunt, etc.)
* Technical map name (e.g. `boil`)
* Bots: Number of bots
* Skill: Bot skill level. Minimum 2, maximum 11.
* Fraglimit: Frag/score limit (meaning depends on game mode) or empty if none
* Time limit: Time limit in minutes or empty if infinite time
* Mutator sets: A list of mutators/[CVars](CVars) to activate in this level, separated by semicolons. Can be empty.
* Level title. Can be empty.
* Level description. Can be empty.

## Minimal example

This is a minimal example campaign with 1 level:

`campaignminimal.txt`:

```
//campaign:Minimal Example Campaign
"dm","boil","5","8","30",,"g_instagib 1; sv_gravity 200","InstaGib Fun on Boil","To win this level, you must insta-gib against 5 bots until you have 30 frags. Good luck!"
```

The campaign's only level is a Deathmatch on Boil with 5 bots at skill level 8. Frag limit of 30. [InstaGib](InstaGib) mutator is active and [gravity](Gravity) is set to 25% (`sv_gravity` is 800 by default).

## Where to put the campaign file?

* In the source code: `<YOUR_XONOTIC_SOURCE_DIRECTORY>/data/xonotic-maps.pk3dir/maps/`
* In your user directory: `<YOUR_HOME_DIRECTORY>/.xonotic/data/maps/`
