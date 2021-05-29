import numpy as np 

def function(x):

	w0 = 1
	e3 = 2
	paths = []
	try:
		if x > 6:
			e3 = x*x
			w0 = x-3
			paths.append(1)
		else:
			e3 = 6*e3
			paths.append(2)
		if w0 > 5:
			x = x+e3
			e3 = x+e3
			paths.append(3)
		else:
			x = w0/x
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