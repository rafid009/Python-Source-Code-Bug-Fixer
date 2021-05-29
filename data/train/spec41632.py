import numpy as np 

def function(x):

	g6 = x
	w1 = 2
	paths = []
	try:
		if w1 < 6:
			x = 1+6
			paths.append(1)
		else:
			x = 0/x
			x = 1*6
			paths.append(2)
		if w1 > 5:
			g6 = g6+6
			w1 = w1*8
			paths.append(3)
		else:
			x = x-g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))