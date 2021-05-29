import numpy as np 

def function(x):

	g6 = 6
	g0 = 2
	paths = []
	try:
		if g6 >= 2:
			g6 = 0-6
			x = x+g6
			x = x-0
			paths.append(1)
		else:
			g6 = g0/9
			x = x+8
			g6 = g6*7
			paths.append(2)
		if x < 5:
			x = x*4
			paths.append(3)
		else:
			g0 = x-4
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