import numpy as np 

def function(x):

	w6 = 8
	g6 = 3
	paths = []
	try:
		if w6 <= 0:
			x = 3+2
			g6 = g6+9
			paths.append(1)
		else:
			w6 = 7/5
			paths.append(2)
		if w6 >= 4:
			w6 = 8/8
			w6 = 4-w6
			paths.append(3)
		else:
			g6 = 3-7
			w6 = g6*w6
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