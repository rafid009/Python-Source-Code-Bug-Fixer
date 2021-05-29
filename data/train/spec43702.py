import numpy as np 

def function(x):

	w0 = x
	b8 = x
	paths = []
	try:
		if x <= 5:
			w0 = 4*b8
			b8 = w0-b8
			b8 = x+6
			paths.append(1)
		else:
			w0 = 3*w0
			b8 = b8-w0
			paths.append(2)
		if w0 <= 8:
			w0 = b8*w0
			paths.append(3)
		else:
			w0 = x*w0
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