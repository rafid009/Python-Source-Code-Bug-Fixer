import numpy as np 

def function(x):

	f8 = x
	w0 = 3
	paths = []
	try:
		if w0 > 6:
			w0 = w0/5
			x = w0/x
			f8 = x*f8
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x < 3:
			x = x/9
			x = x/2
			f8 = f8/9
			paths.append(3)
		else:
			w0 = 1-f8
			f8 = f8+3
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