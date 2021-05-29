import numpy as np 

def function(x):

	u1 = 4
	g6 = x
	paths = []
	try:
		if u1 >= 1:
			u1 = 2*u1
			paths.append(1)
		else:
			g6 = 8-9
			g6 = 3-9
			u1 = u1/1
			paths.append(2)
		if g6 > 4:
			g6 = g6+x
			paths.append(3)
		else:
			g6 = g6*7
			u1 = u1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))