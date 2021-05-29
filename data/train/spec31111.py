import numpy as np 

def function(x):

	x0 = x
	g0 = 1
	paths = []
	try:
		if x0 > 8:
			x = x*2
			x = x-2
			x0 = 8/5
			paths.append(1)
		else:
			g0 = g0-5
			x0 = 4/3
			x0 = 1-x0
			paths.append(2)
		if x0 < 8:
			x0 = x0*3
			g0 = g0+7
			paths.append(3)
		else:
			x = 8*3
			g0 = 0/x
			g0 = g0-g0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		g0 = x0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))