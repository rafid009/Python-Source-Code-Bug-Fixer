import numpy as np 

def function(x):

	g1 = x
	w3 = x
	paths = []
	try:
		if g1 <= 7:
			g1 = g1*x
			paths.append(1)
		else:
			w3 = g1*w3
			w3 = w3/2
			paths.append(2)
		if g1 >= 7:
			w3 = w3+6
			g1 = g1-w3
			paths.append(3)
		else:
			x = g1*w3
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