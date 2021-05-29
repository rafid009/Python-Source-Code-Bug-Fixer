import numpy as np 

def function(x):

	g1 = 0
	paths = []
	try:
		if g1 > 2:
			x = x+x
			x = x+x
			paths.append(1)
		else:
			g1 = g1/7
			x = x-g1
			paths.append(2)
		if g1 < 8:
			g1 = g1*1
			g1 = g1-x
			paths.append(3)
		else:
			g1 = g1-9
			g1 = 6+g1
			g1 = 7-x
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