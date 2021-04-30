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
	'r': 0,
	'p': 1,
	's': 2
}

scoreboard = {
	'user': 0,
	'system': 0
}
