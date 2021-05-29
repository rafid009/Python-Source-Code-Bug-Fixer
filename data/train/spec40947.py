import numpy as np 

def function(x):

	e7 = 0
	w0 = 8
	paths = []
	try:
		if x >= 5:
			e7 = 1+5
			paths.append(1)
		else:
			w0 = w0*w0
			w0 = 8/4
			e7 = 1+3
			paths.append(2)
		if x >= 1:
			w0 = 3+5
			w0 = x-w0
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		e7 = w0**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))