import numpy as np 

def function(x):

	w0 = x
	g3 = x
	paths = []
	try:
		if x >= 9:
			w0 = w0-w0
			paths.append(1)
		else:
			w0 = 9*w0
			paths.append(2)
		if x >= 2:
			g3 = 0*5
			paths.append(3)
		else:
			x = 9+x
			w0 = 4/w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))