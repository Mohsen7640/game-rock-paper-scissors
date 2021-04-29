"""
rock --> r
paper --> p
scissors --> s
"""

GAME_CHOICES = ('r', 'p', 's')

"""
0 --> Draw
1 --> Win user, Lose system
2 --> Win system, Lose user
"""
RULES = {
	'rr': 0,
	'rp': 2,
	'rs': 1,

	'pr': 1,
	'pp': 0,
	'ps': 2,

	'sr': 2,
	'sp': 1,
	'ss': 0
}

scoreboard = {
	'user': 0,
	'system': 0
}
