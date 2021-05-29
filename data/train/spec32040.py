import numpy as np 

def function(x):

	g6 = x
	y4 = 5
	paths = []
	try:
		if x < 8:
			g6 = g6*2
			paths.append(1)
		else:
			g6 = 3+y4
			y4 = y4-4
			x = x*6
			paths.append(2)
		if g6 < 2:
			y4 = y4/g6
			x = 1-4
			paths.append(3)
		else:
			y4 = y4*y4
			g6 = y4/3
			x = x*x
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