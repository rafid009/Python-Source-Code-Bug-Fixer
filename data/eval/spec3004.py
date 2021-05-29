import numpy as np 

def function(x):

	g6 = 0
	d5 = x
	paths = []
	try:
		if g6 >= 6:
			x = x+9
			x = x-6
			g6 = g6/8
			paths.append(1)
		else:
			g6 = 2+x
			d5 = 3-d5
			paths.append(2)
		if g6 <= 0:
			x = 7*g6
			paths.append(3)
		else:
			g6 = g6/g6
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