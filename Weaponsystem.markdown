There are 3 weapons systems coded in Xonotic

\* 1. simple animated model, muzzlr flash handling on h\_ model:
 **\* h\_tuba.dpm, h\_tuba.dpm.animinfo - invisible model controlling the animation
 tags:
 shot = muzzle end
 shell = casings ejection point
 weapon = attachment for v\_tuba.md3
**\* v\_tuba.md3 - first and third person model
 **\* g\_tuba.md3 - pickup model
** 2. fully animated model, muzzle flash handling on h\_ model:
 **\* h\_tuba.dpm, h\_tuba.dpm.animinfo - animated first person model
 tags:
 shot = muzzle end
 shell = casings ejection point
 handle = corresponding to the origin of v\_tuba.md3
**\* v\_tuba.md3 - third person model
 **\* g\_tuba.md3 - pickup model
** 3. fully animated model, muzzle flash handling on v\_ model:
 **\* h\_tuba.dpm, h\_tuba.dpm.animinfo - animated first person model
 tags:
 shot = muzzle end
 shell = casings ejection point
**\* v\_tuba.md3 - third person model
 tags:
 shot = muzzle end (for muzzle flashes)
 \*\* g\_tuba.md3 - pickup model
