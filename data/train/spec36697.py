import numpy as np 

def function(x):

	v9 = x
	g6 = x
	paths = []
	try:
		if g6 >= 2:
			g6 = g6-2
			paths.append(1)
		else:
			g6 = g6/6
			paths.append(2)
		if v9 >= 7:
			v9 = v9/8
			paths.append(3)
		else:
			x = 9*x
			x = 7*g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))