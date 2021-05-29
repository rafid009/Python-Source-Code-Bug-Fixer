import numpy as np 

def function(x):

	w0 = 2
	u2 = 4
	paths = []
	try:
		if x > 2:
			u2 = w0-6
			paths.append(1)
		else:
			w0 = w0/w0
			paths.append(2)
		if w0 > 2:
			u2 = u2*3
			w0 = x/w0
			w0 = w0*5
			paths.append(3)
		else:
			w0 = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))