import numpy as np 

def function(x):

	w0 = x
	g8 = x
	x = 5
	paths = []
	try:
		if w0 < 8:
			x = 1+x
			x = x/9
			x = w0*w0
			paths.append(1)
		else:
			w0 = w0-9
			g8 = 1/g8
			paths.append(2)
		if g8 >= 2:
			x = x/9
			w0 = 5/w0
			x = x-4
			paths.append(3)
		else:
			g8 = x*g8
			w0 = 5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))