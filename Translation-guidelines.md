-   First create an account on Transifex using a proper nickname and a real email address (it will be used to give you credit for your contributions, and so that we're able to contact you later if we need further translation help).

-   Always match newlines and white space with translation strings: if a string has 4 spaces in the beginning of it in English, do the same thing for the translation. If a string has 2 newlines at the end of it, or one in the middle and another at the end, repeat the same thing in the translated string.

-   Always match variables in the strings properly, as explained here: http://docs.translatehouse.org/projects/localization-guide/en/latest/guide/translation/variables.html

-   Keep color codes the same, like ^BG or ^TC or ^F4 or ^2, these are special color codes and are handled by the HUD/text rendering code. See the [List of color codes](List of color codes).

-   Normally do not translate proper nouns, like most weapon names (excluding Machinegun, Shotgun, etc), or game mode names, unless they make sense in your language to be translated. Mutators CAN be translated, but not mutators which have proper names, like "MinstaGib", or "NIX" which is an acronym.

-   Pay attention to capitalization... scoreboard columns for example are intended to be lowercase. In general, it's always a good idea to follow the context of the English writing, and make sure the capitalization matches in English (Unless your language has some other grammatical rule that makes more sense here.)

-   Strings that have **no English words** do not need to be translated, like "%s %s (%s%s)" should not be translated: if you see these, please report them on https://gitlab.com/xonotic/xonotic-data.pk3dir, as they should not have been added in the first place.

-   If you are even slightly unsure of the context or meaning of a string, read the code or ask someone on IRC, if you're still unable to be 100% sure, then mark your string as a "suggestion" on Transifex and MOVE ON, do not risk adding an improper translation.

-   Some strings have prefixes which help you know the context of the string... For example, say there is a listbox in the menu which controls effects settings, we can add a prefix into the translatable string for each item in the list like this: "PREFIX^translatable text". In the case of effects, we can do: "EFFECTS^Low", "EFFECTS^Medium", and "EFFECTS^High", and you can then know the context of the Low/Medium/High translation easily. When forming the final translated string, REMOVE THE PREFIX AND THE ^ SYMBOL. However, be careful not to confuse these with color codes or intentional placements of ^. If in doubt, read the code, context sensitive lines of code which use this prefix idea will have a ZCTX() or CTX() wrapper around the whole string, giving you a good clarification as to how to proceed. Please refer to the [List of prefixes](List of prefixes).

-   NEVER pervert, profane, or mock a string that is not normally written as such in English. If there is no joke or gore in the English writing, do not add one in the translation. We must adhere to supporting cl_gentle (a non-swearing, "E rated" version of the texts) even in translations.

-   Users who abuse the translation system (i.e. putting inappropriate language in places it should not be, advertisements, spam, or other such problems) will be banned from the translation system.

-   Overall, just try and write the translation in a way which fits your language best... If something is silly in English and it's okay to do it silly in your language, then go ahead: just try and make it match the English meaning as closely as possible.

-   After you have completed translations, please test them both in the menu and in game to make sure there aren't any mistakes. WARNING: If you make a mistake while translating a notification system string, it CAN crash the game upon loading, as the notification system analyzes all strings and ensures they are written correctly! ( See here, an earlier problem that have been noticed on the old German translations: http://i.imgur.com/mePBYvO.jpg ). [How to test translations locally](How to test translations locally).