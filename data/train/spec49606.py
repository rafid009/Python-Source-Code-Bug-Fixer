import numpy as np 

def function(x):

	y7 = x
	g1 = 5
	x = 4
	paths = []
	try:
		if y7 >= 0:
			y7 = 9/y7
			x = x-y7
			y7 = 7+g1
			paths.append(1)
		else:
			g1 = 1/x
			paths.append(2)
		if y7 <= 0:
			y7 = 3*g1
			y7 = 9*1
			paths.append(3)
		else:
			g1 = 2*g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))