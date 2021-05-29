import numpy as np 

def function(x):

	w3 = 6
	g1 = x
	paths = []
	try:
		if x >= 2:
			w3 = w3*g1
			g1 = x+3
			g1 = g1/w3
			paths.append(1)
		else:
			w3 = w3-6
			paths.append(2)
		if g1 < 1:
			w3 = 8*g1
			g1 = g1-g1
			paths.append(3)
		else:
			g1 = g1-6
			g1 = 0/x
			w3 = 8*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))