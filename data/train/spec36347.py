import numpy as np 

def function(x):

	w0 = x
	y0 = 3
	paths = []
	try:
		if y0 < 0:
			w0 = 1/w0
			w0 = w0*4
			paths.append(1)
		else:
			x = 7-4
			x = x+4
			paths.append(2)
		if y0 <= 9:
			w0 = y0*w0
			paths.append(3)
		else:
			y0 = y0/y0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		y0 = w0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))