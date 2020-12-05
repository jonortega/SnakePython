# class Snake:

# class Apple:

class Game:
	def __init__(self, heigth, width):
		self.heigth = heigth
		self.width = width

	def render(self):
		print("Heigth: " + str(self.heigth))
		print("Width: " + str(self.width))

game = Game(10, 20)
game.render()