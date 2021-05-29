import numpy as np 

def function(x):

	w0 = 2
	o0 = 6
	paths = []
	try:
		if w0 >= 0:
			o0 = 3*4
			o0 = o0-6
			paths.append(1)
		else:
			o0 = o0*5
			paths.append(2)
		if w0 < 4:
			w0 = 7*w0
			paths.append(3)
		else:
			x = x-3
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