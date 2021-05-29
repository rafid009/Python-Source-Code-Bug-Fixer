import numpy as np 

def function(x):

	g1 = 2
	x1 = 5
	x = 7
	paths = []
	try:
		if g1 <= 6:
			x = 1-9
			paths.append(1)
		else:
			x = x*7
			g1 = 8-3
			paths.append(2)
		if g1 > 3:
			x = 7-x
			paths.append(3)
		else:
			x = 7+x
			x1 = x/4
			x1 = 1*x1
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