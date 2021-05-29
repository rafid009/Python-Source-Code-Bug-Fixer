import numpy as np 

def function(x):

	w4 = x
	w0 = x
	paths = []
	try:
		if x >= 0:
			w4 = 4-w4
			w0 = 6/6
			w0 = x-w0
			paths.append(1)
		else:
			x = x-w0
			w4 = x/w4
			paths.append(2)
		if w4 >= 7:
			x = 6+x
			paths.append(3)
		else:
			w0 = 3-w0
			x = x-w0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w4 = w0**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))