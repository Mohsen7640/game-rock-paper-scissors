from config import GAME_CHOICES, RULES, scoreboard
import random


def get_user_choice():
	user_input = input('Enter your choice please (r, p, s): ')
	if user_input not in GAME_CHOICES:
		print("Oops!!, wrong choice, try again please...")
		return get_user_choice()

	return user_input


def get_system_choice():
	return random.choice(GAME_CHOICES)


def find_winner(user, system):
	choice = user + system
	return RULES[choice]


def update_scoreboard(result):
	if result['user'] == 3:
		scoreboard['user'] += 1
		msg = 'You win'
	else:
		scoreboard['system'] += 1
		msg = 'You lose'

	print("#" * 30)
	print("##", f'user: {scoreboard["user"]}'.ljust(24), "##")
	print("##", f'system: {scoreboard["system"]}'.ljust(24), "##")
	print("##", f'last game: {msg}'.ljust(24), "##")
	print("#" * 30)


def play_again():
	user_input = input('Do you want to play again? (y/n)')
	if user_input.lower() == 'y':
		play()


def play():
	result = {'user': 0, 'system': 0}

	while result['user'] < 3 and result['system'] < 3:
		user_choice = get_user_choice()
		system_choice = get_system_choice()
		winner = find_winner(user_choice, system_choice)

		if winner == 1:
			msg = 'You win'
			result['user'] += 1
		elif winner == 2:
			msg = 'You lose'
			result['system'] += 1
		else:
			msg = 'Draw'

		print(f"user: {user_choice}\t "
			  f"system: {system_choice}\t result: {msg}")

	update_scoreboard(result)
	play_again()


if __name__ == '__main__':
	play()
