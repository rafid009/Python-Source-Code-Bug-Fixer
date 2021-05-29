import numpy as np 

def function(x):

	w0 = 7
	y4 = 7
	paths = []
	try:
		if x <= 1:
			w0 = w0*w0
			y4 = w0/8
			paths.append(1)
		else:
			y4 = y4*y4
			x = 5+2
			paths.append(2)
		if x >= 4:
			x = 2-x
			paths.append(3)
		else:
			w0 = y4/w0
			w0 = 3-w0
			y4 = w0*y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))