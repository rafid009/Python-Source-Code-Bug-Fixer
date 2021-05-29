import numpy as np 

def function(x):

	g0 = x
	x7 = 6
	paths = []
	try:
		if x7 <= 8:
			x = 0*x7
			paths.append(1)
		else:
			x = 8+x7
			x7 = 4/x7
			paths.append(2)
		if g0 > 7:
			g0 = 0+g0
			x = x7*x
			paths.append(3)
		else:
			x7 = g0*x7
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