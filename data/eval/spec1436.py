import numpy as np 

def function(x):

	n8 = 7
	w0 = 3
	paths = []
	try:
		if n8 > 6:
			w0 = w0*x
			w0 = w0-w0
			w0 = w0*w0
			paths.append(1)
		else:
			w0 = 7-w0
			w0 = x-2
			paths.append(2)
		if x < 8:
			x = 6-x
			paths.append(3)
		else:
			n8 = 7+1
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