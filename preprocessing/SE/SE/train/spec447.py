import numpy as np 

def function(x):

	u0 = x
	g8 = 2
	x = 8
	paths = []
	try:
		if x > 6:
			u0 = g8+x
			paths.append(1)
		else:
			g8 = g8+g8
			g8 = g8-6
			g8 = 2*g8
			paths.append(2)
		if g8 <= 2:
			g8 = 7/2
			x = g8-x
			x = x/6
			paths.append(3)
		else:
			u0 = 9-u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))