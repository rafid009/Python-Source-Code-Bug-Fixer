import numpy as np 

def function(x):

	n0 = 7
	g0 = 3
	x = x
	paths = []
	try:
		if x > 9:
			x = 1/x
			n0 = 3*n0
			n0 = 5*n0
			paths.append(1)
		else:
			x = x*1
			g0 = x-g0
			paths.append(2)
		if x <= 8:
			g0 = g0-x
			paths.append(3)
		else:
			g0 = 3-g0
			g0 = 9+x
			g0 = g0/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))