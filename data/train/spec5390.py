import numpy as np 

def function(x):

	r9 = x
	g6 = 4
	paths = []
	try:
		if r9 <= 0:
			g6 = g6/5
			paths.append(1)
		else:
			g6 = g6*x
			paths.append(2)
		if x >= 3:
			x = 7-x
			r9 = r9+5
			paths.append(3)
		else:
			g6 = 0+6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		g6 = r9**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))