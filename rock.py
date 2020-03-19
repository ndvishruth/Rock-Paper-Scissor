import random

def play_again():
	option=input('To continue type [Y/Yes]\n').lower()
	if option=='yes' or option=='y':
		perform_operation()
	else:
		pass

def perform_operation():
	choice=['rock','paper','scissor']
	computer=choice[random.randint(0,2)]
	print('Rock Paper Scissor')
	player=input('Your choice: ').lower()
	while player not in choice:
		print('Choose rock, paper or scissor')
		player=input('Your choice: ').lower()
	print('Computer choice: ',computer)

	if player==computer:
		print('Draw')
	elif player=='rock' and computer=='paper':
		print('Computer wins')
	elif player=='rock' and computer=='scissor':
		print('You win')
	elif player=='paper' and computer=='rock':
		print('You win')
	elif player=='paper' and computer=='scissor':
		print('Computer wins')
	elif player=='scissor' and computer=='paper':
		print('You win')
	elif player=='scissor' and computer=='rock':
		print('Computer wins')	

	play_again()

if __name__ == '__main__':
	perform_operation()