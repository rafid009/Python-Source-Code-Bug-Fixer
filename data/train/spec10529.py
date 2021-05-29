import numpy as np 

def function(x):

	g0 = 1
	x7 = 4
	paths = []
	try:
		if g0 > 5:
			g0 = g0/g0
			paths.append(1)
		else:
			x7 = g0+x
			g0 = 7+x
			paths.append(2)
		if x7 > 7:
			g0 = g0*g0
			g0 = 2/g0
			paths.append(3)
		else:
			x = g0+g0
			x7 = x7/8
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		g0 = x7**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))