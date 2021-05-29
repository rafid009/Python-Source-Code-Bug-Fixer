import numpy as np 

def function(x):

	a0 = x
	g6 = x
	paths = []
	try:
		if a0 > 1:
			x = x/2
			a0 = 3*a0
			paths.append(1)
		else:
			x = 6-x
			a0 = a0+g6
			paths.append(2)
		if a0 > 6:
			g6 = 7/g6
			a0 = x*6
			a0 = 2*x
			paths.append(3)
		else:
			a0 = 8-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		g6 = a0**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))