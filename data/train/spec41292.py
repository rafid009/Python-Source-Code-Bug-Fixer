import numpy as np 

def function(x):

	w0 = x
	x1 = x
	paths = []
	try:
		if x1 > 2:
			x = 0/x
			w0 = w0*w0
			w0 = x1/4
			paths.append(1)
		else:
			x1 = x1+w0
			x1 = 9-x1
			x1 = x1+7
			paths.append(2)
		if w0 >= 2:
			w0 = w0/8
			x = x-5
			paths.append(3)
		else:
			x1 = x1/5
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