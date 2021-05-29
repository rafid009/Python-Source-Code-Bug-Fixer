import numpy as np 

def function(x):

	j4 = 7
	w0 = 6
	paths = []
	try:
		if x < 2:
			w0 = 3-8
			paths.append(1)
		else:
			x = w0-j4
			paths.append(2)
		if w0 >= 8:
			w0 = 3*w0
			paths.append(3)
		else:
			w0 = 6+x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))