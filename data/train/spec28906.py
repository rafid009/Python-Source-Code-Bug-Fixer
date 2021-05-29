import numpy as np 

def function(x):

	q8 = 7
	w0 = 7
	paths = []
	try:
		if w0 > 3:
			q8 = q8-x
			q8 = w0*q8
			w0 = w0+5
			paths.append(1)
		else:
			q8 = q8-4
			w0 = 7/w0
			w0 = 2+q8
			paths.append(2)
		if q8 >= 6:
			x = 5-x
			paths.append(3)
		else:
			q8 = 7*q8
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