import numpy as np 

def function(x):

	n2 = x
	g6 = x
	paths = []
	try:
		if x <= 8:
			g6 = g6+9
			g6 = 4*g6
			paths.append(1)
		else:
			g6 = 2/g6
			g6 = n2+g6
			g6 = g6-x
			paths.append(2)
		if n2 > 8:
			x = x-5
			paths.append(3)
		else:
			x = x/x
			g6 = 4-x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		g6 = n2**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))