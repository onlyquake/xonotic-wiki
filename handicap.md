Handicap is used to make the game even for players with different skill levels. Currently, handicap affects only damage. A handicap value of 1 means that there is no handicap. Handicap values more than 1 means the game is harder. For example, if your handicap is 2, you will deal 50% damage to opponents while they will deal 200% damage to you. Handicap values less than 1 do the opposite.

There are 2 types of handicap: voluntary and forced. Voluntary handicap can be set by client via `cl_handicap` variable.
```
cl_handicap 1
sendcvar cl_handicap 1
```
For obvious reasons, you can't set it to be less than 1.

Forced handicap can be set by the server and can be less than 1. For example, by [dynamic handicap](dynamic-handicap) mutator.