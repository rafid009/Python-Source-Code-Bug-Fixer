import numpy as np 

def function(x):

	w0 = x
	g0 = x
	paths = []
	try:
		if g0 < 7:
			x = g0/7
			paths.append(1)
		else:
			g0 = 9-g0
			g0 = 1/6
			paths.append(2)
		if x <= 3:
			x = 9-x
			paths.append(3)
		else:
			w0 = w0-9
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))