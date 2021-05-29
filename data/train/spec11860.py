import numpy as np 

def function(x):

	g1 = 8
	w4 = x
	paths = []
	try:
		if x > 3:
			w4 = 1-w4
			g1 = g1+w4
			paths.append(1)
		else:
			g1 = 6/w4
			g1 = 8-6
			paths.append(2)
		if x >= 2:
			g1 = x+0
			x = 6-x
			g1 = g1/w4
			paths.append(3)
		else:
			g1 = 9/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))