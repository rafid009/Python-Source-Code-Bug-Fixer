import numpy as np 

def function(x):

	i7 = x
	g6 = x
	paths = []
	try:
		if i7 > 5:
			x = x-6
			paths.append(1)
		else:
			g6 = 1-g6
			g6 = 2-0
			paths.append(2)
		if x <= 8:
			x = x*x
			g6 = g6+6
			i7 = i7-8
			paths.append(3)
		else:
			x = x+1
			x = 4-x
			g6 = g6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))