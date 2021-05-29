import numpy as np 

def function(x):

	g1 = 0
	t1 = x
	paths = []
	try:
		if x > 7:
			x = 2*6
			x = x-g1
			g1 = g1/x
			paths.append(1)
		else:
			g1 = 1-g1
			paths.append(2)
		if x > 7:
			g1 = g1-x
			x = 7/x
			paths.append(3)
		else:
			x = x/g1
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