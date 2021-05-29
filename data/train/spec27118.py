import numpy as np 

def function(x):

	a8 = x
	g7 = 1
	paths = []
	try:
		if g7 >= 7:
			x = 3*x
			g7 = 8-g7
			paths.append(1)
		else:
			a8 = a8-a8
			paths.append(2)
		if g7 > 6:
			g7 = 7*2
			x = 9*x
			g7 = g7*a8
			paths.append(3)
		else:
			a8 = g7*2
			a8 = 5+2
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