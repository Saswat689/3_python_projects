import random
import math

#guessing game with a human
# def guess(x):
# 	random_number = random.randint(1,x)
# 	guess = 0

# 	while guess != random_number:
# 		guess = int(input(f"Guess a number between 1 and {x}"))
# 		print(guess)
# 		if guess < random_number:
# 			print("Sorry guess too low")
# 		elif guess > random_number:
# 			print("Sorry guess too high.")
# 	print(f"Yay,congrats. You have guessed the right number {random_number}")			


# guessing game with a computer
# def computer_guess(x):
# 	low = 1
# 	high = x
# 	feedback = ''
# 	while feedback != 'c':
# 		if low != high:
# 			guess = random.randint(low,high)
# 		else:
# 			guess = low	

# 		feedback = input(f"Is {guess} too high(H), too Low (L) or correct (C)").lower()	
# 		if feedback == 'h':
# 			high = guess - 1
# 		elif feedback == 'l':
# 			low = guess + 1

# 	print("Yay! The computer guessed it correctly.")


# guess(5)	
# computer_guess(10)


# Rock paper scissors

# def play():
# 	user = input("What's your choice? \n r' for rock, 'p' for paper, 's' for scissors ")
# 	computer = random.choice(['r','p','s'])	
# 	if user == computer:
# 		return 'Its a Tie'

# 	if is_win(user,computer):
# 		return 'You won'

# 	return 'You lost!'		

# def is_win(player,opponent):
# 	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
# 		return True

# print(play())




# TIC TAC TOE
# class Player:
# 	def __init__(self,letter):
# 		#letter is x or 0
# 		self.letter = letter


# 	# we want all players to get their next move
# 	def get_move(self,game):
# 		pass # continue


# class RandomComputerPlayer(Player):
# 	def __init__(self,letter):
# 		super().__init__(letter)

# 	def get_move(self,game):
# 		square = random.choice(game.available_moves())
# 		return square			

# class HumanPlayer(Player):
# 	def __init__(self,letter):
# 		super().__init__(letter)

# 	def get_move(self,game):
# 		valid_square = False
# 		val = None
# 		while not valid_square:
# 			square = input(self.letter + '\'s turn, input move (0-8)')
# 			try:
# 				val = int(square)
# 				if val not in game.available_moves():
# 					raise ValueError
# 				valid_square = True
# 			except ValueError:
# 				print('Invalid square. Try again')

# 		return val				


# class TicTacToe:
# 	def __init__(self):
# 		self.board = [' ' for _ in range(9)]
# 		self.current_winner = None

# 	def print_board(self):
# 		for row in [self.board[(i*3):(i+1)*3] for i in range(3)]:
# 			print('| '+' | '.join(row) +' |')

# 	@staticmethod
# 	def print_board_nums():
# 		number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
# 		for row in number_board:
# 			print('| '+' | '.join(row) +' |')


# 	def available_moves(self):
# 		moves = []
# 		for (i,spot) in enumerate(self.board):
# 			if spot == ' ':
# 				moves.append(i)

# 		return moves	

# 	def empty_squares(self):
# 		return ' ' in self.board

# 	def num_empty_squares(self):
# 		return self.board.count(' ')

# 	def make_move(self,square,letter):
# 		if self.board[square] == ' ':
# 			self.board[square] = letter
# 			if self.winner(square,letter):
# 				self.current_winner = letter
# 			return True
# 		return False

# 	def winner(self,square,letter):
# 		#check row
# 		row_ind = square // 3
# 		row = self.board[row_ind*3 : (row_ind + 1) * 3]
# 		if all([spot == letter for spot in row]):
# 			return True

# 		#check row
# 		col_ind = square % 3
# 		column = [self.board[col_ind+i*3] for i in range(3)]
# 		if all([spot == letter for spot in column]):
# 			return True						


# 		if square % 2 == 0:
# 			diagonal = [self.board[i] for i in [0,4,8]]
# 			if all([spot == letter for spot in diagonal]):
# 				return True	
# 			diagonal2 = [self.board[i] for i in [2,4,6]]
# 			if all([spot == letter for spot in diagonal2]):
# 				return True	

# 		return False		

# def play(game,x_player,o_player,print_game=True):
# 	if print_game:
# 		game.print_board_nums()

# 	letter = 'X'
# 	while game.empty_squares():
# 		if letter == 'O':
# 			square = o_player.get_move(game)
# 		else:
# 			square = x_player.get_move(game)

# 		if game.make_move(square,letter):
# 			if print_game:
# 				print(letter + f" makes a move to square {square}")
# 				game.print_board()
# 				print('')

# 			if game.current_winner:
# 				if print_game:
# 					print(letter + ' wins!')
# 				return letter					

# 			letter = 'O' if letter == 'X' else 'X'

# 	if print_game:
# 		print("It's a tie")	

# x_player = HumanPlayer('X')
# o_player = RandomComputerPlayer('O')
# t = TicTacToe()
# play(t,x_player,o_player,print_game=True)





# Implementation of binary search agorithm

# We will prove that binary search is faster than naive search

# naive search: scan entire list and ask if its equal to target
# if yes, return the index
# if no, return -1

def naive_search(l,target):
	for i in range(len(l)):
		if l[i] == target:
			return i

	return -1


# binary search uses divide and conquer
# we will leverage the fact that our list is sorted

def binary_search(l,target,low=None,high=None):
	if low is None:
		low = 0
	if high is None:
		high = len(l) - 1

	if high < low:
		return -1	

	# average(mid)
	midpoint = (low + high) // 2

	if l[midpoint] == target:
		return midpoint

	elif target < l[midpoint]:
		return binary_search(l,target,low,midpoint-1)
	else:
		return binary_search(l,target,midpoint+1,high)		


l = [1,3,5,10,12]
target = 10
print(naive_search(l,target))
print(binary_search(l,target))		

