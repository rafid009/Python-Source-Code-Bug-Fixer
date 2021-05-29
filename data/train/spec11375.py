import numpy as np 

def function(x):

	w0 = 6
	o1 = 6
	paths = []
	try:
		if x <= 1:
			o1 = o1-1
			paths.append(1)
		else:
			x = x+x
			w0 = w0-x
			paths.append(2)
		if x > 1:
			w0 = x-w0
			paths.append(3)
		else:
			x = x/1
			w0 = o1-w0
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