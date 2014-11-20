There are 3 weapons systems coded in Xonotic

1. simple animated model, muzzl flash handling on `h_` model:

  * `h_tuba.dpm`, `h_tuba.dpm.animinfo` - invisible model controlling the animation  
    tags:  
    shot = muzzle end (shot origin, also used for muzzle flashes)  
    shell = casings ejection point (must be on the right hand side of the gun)  
    weapon = attachment for `v_tuba.md3`  
  * `v_tuba.md3` - first and third person model  
  * `g_tuba.md3` - pickup model  

2. fully animated model, muzzle flash handling on `h_` model:

  * `h_tuba.dpm`, `h_tuba.dpm.animinfo` - animated first person model  
    tags:  
    shot = muzzle end (shot origin, also used for muzzle flashes)  
    shell = casings ejection point (must be on the right hand side of the gun)  
    handle = corresponding to the origin of `v_tuba.md3` (used for muzzle flashes)  
  * `v_tuba.md3` - third person model  
  * `g_tuba.md3` - pickup model  

3. fully animated model, muzzle flash handling on `v_` model:

  * `h_tuba.dpm`, `h_tuba.dpm.animinfo` - animated first person model  
    tags:  
    shot = muzzle end (shot origin)  
    shell = casings ejection point (must be on the right hand side of the gun)  
  * `v_tuba.md3` - third person model  
    tags:  
    shot = muzzle end (for muzzle flashes)  
  * `g_tuba.md3` - pickup model  