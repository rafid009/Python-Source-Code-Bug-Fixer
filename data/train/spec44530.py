import numpy as np 

def function(x):

	y5 = 9
	g8 = x
	paths = []
	try:
		if y5 < 4:
			g8 = 7*7
			g8 = x+8
			paths.append(1)
		else:
			x = x/y5
			x = g8-x
			x = x*y5
			paths.append(2)
		if g8 < 4:
			y5 = 1+g8
			y5 = 1-y5
			paths.append(3)
		else:
			y5 = 3*y5
			g8 = g8*7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		g8 = y5**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))