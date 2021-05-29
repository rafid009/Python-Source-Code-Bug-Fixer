import numpy as np 

def function(x):

	g8 = 7
	h2 = x
	paths = []
	try:
		if g8 >= 1:
			x = 0-x
			h2 = 2*h2
			paths.append(1)
		else:
			h2 = h2+5
			h2 = h2+6
			paths.append(2)
		if g8 >= 6:
			h2 = 3+5
			h2 = g8*1
			paths.append(3)
		else:
			h2 = 6/h2
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