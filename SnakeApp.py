# class Snake:

# class Apple:

class Game:
	def __init__(self, heigth, width):
		self.heigth = heigth
		self.width = width

	def board_matrix(self):
		board = []
		for row in range(0,self.heigth):
			for column in range(0,self.width):
				board.append([None])
		# Return an empty marix

	def render(self):
		matrix = self.board_matrix()
		print(matrix)


game = Game(4, 3)
game.render()