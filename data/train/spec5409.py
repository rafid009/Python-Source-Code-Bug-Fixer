import numpy as np 

def function(x):

	g6 = 1
	w9 = x
	paths = []
	try:
		if w9 <= 9:
			x = x*g6
			x = 0-x
			paths.append(1)
		else:
			w9 = 7+5
			w9 = w9/x
			paths.append(2)
		if w9 > 2:
			x = x/g6
			x = w9+w9
			g6 = 3+4
			paths.append(3)
		else:
			x = x-7
			w9 = w9-5
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