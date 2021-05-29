import numpy as np 

def function(x):

	g5 = 4
	h8 = 3
	paths = []
	try:
		if g5 > 0:
			h8 = 9*h8
			g5 = 5-g5
			x = 6/x
			paths.append(1)
		else:
			g5 = 1+6
			paths.append(2)
		if x > 9:
			h8 = 0-h8
			paths.append(3)
		else:
			h8 = 9/h8
			h8 = 2/x
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