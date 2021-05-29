import numpy as np 

def function(x):

	g0 = x
	g3 = 6
	paths = []
	try:
		if g3 > 4:
			x = x+4
			x = x-7
			x = x-3
			paths.append(1)
		else:
			g3 = g3/3
			g3 = g3+1
			g0 = 5+g0
			paths.append(2)
		if g0 > 2:
			g0 = g0-0
			g3 = g0/g3
			x = 9*x
			paths.append(3)
		else:
			g3 = g0/9
			g3 = x+2
			g3 = g3/g0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))