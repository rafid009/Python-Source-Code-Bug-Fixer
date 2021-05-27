import numpy as np 

def function(x):

	w3 = 4
	w0 = x
	paths = []
	try:
		if w0 > 9:
			w0 = w0+4
			w3 = w3+w3
			paths.append(1)
		else:
			w0 = 0+w0
			paths.append(2)
		if x >= 9:
			w0 = 2*2
			w0 = w0*x
			w0 = 6*w0
			paths.append(3)
		else:
			w3 = w3/x
			w3 = 9/x
			x = x-w0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))