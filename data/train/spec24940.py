import numpy as np 

def function(x):

	l1 = 2
	g0 = 3
	paths = []
	try:
		if x >= 7:
			g0 = 0/g0
			paths.append(1)
		else:
			x = g0-8
			g0 = l1-g0
			paths.append(2)
		if l1 > 4:
			g0 = l1-7
			paths.append(3)
		else:
			x = l1*x
			g0 = l1-g0
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