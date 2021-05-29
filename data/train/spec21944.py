import numpy as np 

def function(x):

	e4 = 4
	w0 = 9
	paths = []
	try:
		if x >= 9:
			w0 = w0*9
			w0 = w0+e4
			e4 = e4*w0
			paths.append(1)
		else:
			w0 = w0/1
			x = 1/4
			x = x-x
			paths.append(2)
		if e4 < 4:
			e4 = 8-e4
			w0 = e4-w0
			w0 = w0-9
			paths.append(3)
		else:
			e4 = x-9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		w0 = e4**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))