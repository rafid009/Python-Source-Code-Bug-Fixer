import numpy as np 

def function(x):

	e9 = x
	w0 = 3
	paths = []
	try:
		if x < 2:
			e9 = 2*x
			w0 = w0*6
			paths.append(1)
		else:
			w0 = 1/1
			paths.append(2)
		if w0 > 7:
			e9 = e9+e9
			e9 = e9+6
			paths.append(3)
		else:
			x = 5/e9
			x = w0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))