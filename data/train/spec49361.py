import numpy as np 

def function(x):

	w0 = x
	g0 = 1
	paths = []
	try:
		if w0 <= 2:
			g0 = g0*8
			x = x/g0
			w0 = w0-2
			paths.append(1)
		else:
			w0 = x*w0
			g0 = g0/w0
			paths.append(2)
		if x >= 3:
			g0 = g0/g0
			paths.append(3)
		else:
			g0 = 8-g0
			g0 = g0*4
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