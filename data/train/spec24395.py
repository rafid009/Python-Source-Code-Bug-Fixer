import numpy as np 

def function(x):

	g8 = 1
	x9 = 4
	paths = []
	try:
		if g8 >= 9:
			x = 0+x
			paths.append(1)
		else:
			x9 = g8-5
			x = 9/x
			paths.append(2)
		if x < 2:
			x = x/x9
			paths.append(3)
		else:
			g8 = g8-7
			x = x-g8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		g8 = x9**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))