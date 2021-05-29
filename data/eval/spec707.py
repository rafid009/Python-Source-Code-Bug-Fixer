import numpy as np 

def function(x):

	w0 = 6
	d8 = x
	paths = []
	try:
		if x <= 3:
			w0 = 1-0
			d8 = 6-d8
			paths.append(1)
		else:
			d8 = w0*d8
			w0 = w0/5
			paths.append(2)
		if d8 < 9:
			w0 = 7/3
			d8 = 7/d8
			paths.append(3)
		else:
			d8 = 8-x
			x = 5/x
			d8 = 8-3
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