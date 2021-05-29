import numpy as np 

def function(x):

	w0 = x
	w4 = x
	paths = []
	try:
		if x <= 6:
			w0 = 7/w0
			w0 = 7*1
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x <= 1:
			w0 = 5*2
			w4 = w4-w4
			x = 4*x
			paths.append(3)
		else:
			w0 = w0+4
			x = 4-x
			x = 6*w4
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