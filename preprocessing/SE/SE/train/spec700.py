import numpy as np 

def function(x):

	g1 = 7
	y3 = 1
	paths = []
	try:
		if x > 6:
			x = g1+3
			paths.append(1)
		else:
			x = x-4
			x = 3+x
			g1 = 2-g1
			paths.append(2)
		if g1 > 5:
			x = x+1
			paths.append(3)
		else:
			y3 = y3+g1
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