import numpy as np 

def function(x):

	g8 = x
	h7 = x
	paths = []
	try:
		if h7 > 6:
			g8 = g8*4
			g8 = 8-x
			paths.append(1)
		else:
			h7 = 1*2
			paths.append(2)
		if x >= 3:
			g8 = g8-9
			x = 5*h7
			paths.append(3)
		else:
			h7 = 0*h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))