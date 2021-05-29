import numpy as np 

def function(x):

	w0 = 5
	v0 = 3
	paths = []
	try:
		if x <= 3:
			w0 = 1+1
			v0 = 6-v0
			x = 1-2
			paths.append(1)
		else:
			v0 = v0-1
			w0 = w0-2
			w0 = w0*4
			paths.append(2)
		if x >= 7:
			v0 = 2-6
			x = 8-x
			w0 = w0+x
			paths.append(3)
		else:
			w0 = 8-w0
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