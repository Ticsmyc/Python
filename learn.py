from random import randint

class Die():

	def __init__(self,sides=6):
		self.side=sides

	def roll_die(self):
		x=randint(1,self.side)
		print(x)

my_die=Die(10)
for i in range(0,10):
	my_die.roll_die()



