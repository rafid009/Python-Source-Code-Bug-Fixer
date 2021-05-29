import numpy as np 

def function(x):

	g3 = 4
	w4 = x
	paths = []
	try:
		if w4 > 2:
			g3 = 0-g3
			paths.append(1)
		else:
			w4 = 6/w4
			x = g3+3
			g3 = x-g3
			paths.append(2)
		if x <= 7:
			g3 = g3+2
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))