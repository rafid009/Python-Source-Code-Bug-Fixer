import numpy as np 

def function(x):

	g6 = x
	a8 = 3
	paths = []
	try:
		if x < 1:
			x = g6*x
			paths.append(1)
		else:
			a8 = 4-4
			x = x-6
			x = a8*2
			paths.append(2)
		if g6 <= 0:
			x = 4-x
			x = 5-4
			x = 3*x
			paths.append(3)
		else:
			x = 2*5
			g6 = 6*4
			x = 2-3
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