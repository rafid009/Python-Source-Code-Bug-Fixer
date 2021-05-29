import numpy as np 

def function(x):

	e3 = 8
	w0 = 8
	paths = []
	try:
		if e3 <= 8:
			x = 7+x
			w0 = 0+w0
			paths.append(1)
		else:
			e3 = w0+e3
			paths.append(2)
		if x > 0:
			x = 0*x
			paths.append(3)
		else:
			w0 = w0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))