import numpy as np 

def function(x):

	q3 = x
	g1 = 9
	paths = []
	try:
		if g1 > 2:
			x = 9-x
			paths.append(1)
		else:
			q3 = 5+q3
			paths.append(2)
		if x < 1:
			x = 9+x
			g1 = 3/8
			paths.append(3)
		else:
			x = x-7
			g1 = g1-g1
			x = x*3
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