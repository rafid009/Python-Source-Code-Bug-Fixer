import numpy as np 

def function(x):

	g1 = 6
	z0 = 4
	paths = []
	try:
		if x >= 6:
			g1 = g1-g1
			g1 = g1*6
			paths.append(1)
		else:
			g1 = 2+g1
			g1 = g1-2
			paths.append(2)
		if x < 1:
			g1 = x+g1
			paths.append(3)
		else:
			g1 = x*8
			g1 = g1-6
			x = x/x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))