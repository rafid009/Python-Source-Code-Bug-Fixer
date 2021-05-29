import numpy as np 

def function(x):

	w0 = x
	w5 = x
	paths = []
	try:
		if x < 7:
			w5 = w5-w0
			x = x+2
			w5 = w5-x
			paths.append(1)
		else:
			w5 = w5/8
			paths.append(2)
		if x <= 0:
			w0 = 7/w0
			w0 = x+8
			w0 = w0*2
			paths.append(3)
		else:
			x = 9/w0
			w5 = 1/w5
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