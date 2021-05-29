import numpy as np 

def function(x):

	g1 = x
	s0 = 4
	x = x
	paths = []
	try:
		if g1 >= 0:
			g1 = 2-4
			g1 = 0/g1
			paths.append(1)
		else:
			g1 = g1+4
			paths.append(2)
		if s0 >= 0:
			g1 = g1-x
			paths.append(3)
		else:
			g1 = g1/6
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