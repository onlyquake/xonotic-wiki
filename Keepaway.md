Keepaway
========

Object of the Game
------------------

In Keepaway, a ball will spawn randomly on the map. The goal is to take the ball and—when you have it—kill as many people as possible and protect yourself.

Scoring
-------

The following actions can score you points (scores as of 0.8.2):

| Name | Action | Default score |
|:-:|:-:|:-:|
| Kill As Carrier | Kill an opponent while you carry the ball | +1 |
| Ball Carrier Kill | Kill the ball carrier | +1 |
| Time Points | Carry the ball for a short amount of time | 0 |

In 0.8.2, there are no Time Points by default, but they can be enabled by the server (see below).

The first player to reach the score limit (usually 30) will win the match.

### Custom scoring

Servers can change the score you get for each action above with [CVars](CVars) (`g_keepway_score_*`). This means they can also enable Time Points.

Detailed rules
--------------

* If nobody collects the ball for a while, it will teleport to a random place

Helpful Hints and Tips
----------------------

-   _(Insert Hints Here)_