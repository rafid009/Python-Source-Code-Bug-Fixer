import numpy as np 

def function(x):

	i2 = 9
	w0 = 2
	paths = []
	try:
		if w0 < 2:
			w0 = w0*i2
			paths.append(1)
		else:
			w0 = w0+6
			paths.append(2)
		if x > 7:
			w0 = w0/7
			w0 = w0*9
			paths.append(3)
		else:
			x = 9*x
			i2 = 7/w0
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