import numpy as np 

def function(x):

	n7 = 0
	w0 = x
	paths = []
	try:
		if w0 > 2:
			x = 9*x
			paths.append(1)
		else:
			w0 = n7-w0
			x = x-8
			n7 = n7-w0
			paths.append(2)
		if n7 > 9:
			w0 = 1*x
			x = 7/w0
			paths.append(3)
		else:
			n7 = w0+5
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