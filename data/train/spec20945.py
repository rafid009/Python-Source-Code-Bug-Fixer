import numpy as np 

def function(x):

	l1 = x
	w0 = x
	paths = []
	try:
		if w0 > 0:
			w0 = 9+6
			paths.append(1)
		else:
			w0 = w0-0
			l1 = l1/9
			paths.append(2)
		if l1 <= 3:
			x = x-2
			w0 = 7-9
			paths.append(3)
		else:
			w0 = w0*w0
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))