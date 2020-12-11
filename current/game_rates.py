#!/usr/bin/env python3

Infinite = 1000000

RATE_DEATH = 100

# Dangers
DANGER_RATE_ZOMBIE      = RATE_DEATH #death
DANGER_RATE_NEAR_ZOMBIE_FACE = RATE_DEATH #int(RATE_DEATH*0.9)
DANGER_RATE_NEAR_ZOMBIE_BACK = (RATE_DEATH*2)//3
DANGER_RATE_ZOMBIE_EXIT = RATE_DEATH//2

DANGER_RATE_NEAR_PLAYER_BACK = (RATE_DEATH*2)//3 #can fire - high risk
DANGER_RATE_NEAR_PLAYER_FACE = (RATE_DEATH*8)//10 #can fire - high risk
DANGER_RATE_NEAR_PLAYER_DIAG = RATE_DEATH//2
DANGER_RATE_PLAYER           = RATE_DEATH//2 #mrisky to jump - can move and fire

DANGER_DIST_RADIUS = 5
DANGER_DIST_DECAY  = 10

DANGERZ_DIST_RADIUS = 3
DANGERZ_DIST_DECAY  = 3

RATE_MOVE_STEP      = [0, 1, 2.1]
RATE_MOVE_GOLD_DEFAULT  = -5
#RATE_MOVE_GOLD          = RATE_MOVE_GOLD_DEFAULT
RATE_MOVE_PERK      = -5
RATE_MOVE_TARGET    = -10

MOVE_RATE_RISKY = (RATE_DEATH*2)//3

RATE_FIRE_100 = 100
RATE_FIRE_0   = 0

RATE_FIRE_NEIGHBOUR = RATE_FIRE_100
RATE_FIRE_DUELER    = 50

RATE_FIRE_PLAYER  = 10
RATE_FIRE_PLAYERN = 6
RATE_FIRE_ZOMBIE  = 10
RATE_FIRE_ZOMBIEN = 8
RATE_FIRE_STARTS  = 1

RATE_FIRE_MAKE_SHOT = 5


RATE_FIRE_SCALES = [1, 1, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]


CUBE_HISTORY_LEN = 5
CUBE_LONG_HISTORY_LEN = 10

ATTACK_STARTS_RANGE_MIN = 2
ATTACK_STARTS_RANGE_MAX = 2

# BERSERK_STARTS_RANGE_MIN =  1
# BERSERK_STARTS_RANGE_MAX =  2

BERSERK_STARTS_RANGE_MIN =  1
BERSERK_STARTS_RANGE_MAX =  1
BERSERK_ALLOW_DUEL = True

#BERSERRK_AUTOSTART_NO_EXITS = 10
VISIBILITY_DURATION = 100

