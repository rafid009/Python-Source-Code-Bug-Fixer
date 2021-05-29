import numpy as np 

def function(x):

	w1 = 0
	w0 = x
	paths = []
	try:
		if w0 <= 6:
			w1 = 8+w1
			paths.append(1)
		else:
			w0 = w0+8
			x = 2-w1
			w1 = x*8
			paths.append(2)
		if w1 <= 8:
			w0 = 1*w0
			w1 = 4-w1
			paths.append(3)
		else:
			x = 2-x
			w0 = 0/w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))