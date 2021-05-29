import numpy as np 

def function(x):

	q8 = 1
	g0 = 3
	paths = []
	try:
		if x < 8:
			q8 = 1-4
			paths.append(1)
		else:
			q8 = q8+6
			g0 = g0*3
			g0 = 2-1
			paths.append(2)
		if q8 >= 2:
			g0 = g0-8
			paths.append(3)
		else:
			x = x/g0
			q8 = 8/q8
			g0 = 3/7
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))