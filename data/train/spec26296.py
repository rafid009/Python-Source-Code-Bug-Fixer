import numpy as np 

def function(x):

	w0 = x
	d0 = x
	paths = []
	try:
		if w0 > 6:
			d0 = d0*8
			d0 = d0+3
			w0 = w0+9
			paths.append(1)
		else:
			w0 = 2*d0
			paths.append(2)
		if w0 > 4:
			w0 = 4/w0
			w0 = w0-6
			paths.append(3)
		else:
			d0 = x/d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))