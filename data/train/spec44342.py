import numpy as np 

def function(x):

	w0 = 5
	h9 = 4
	x = 2
	paths = []
	try:
		if h9 < 4:
			w0 = 3*1
			h9 = 0-h9
			paths.append(1)
		else:
			h9 = h9-9
			x = w0-8
			paths.append(2)
		if h9 <= 7:
			h9 = w0-h9
			h9 = h9-x
			paths.append(3)
		else:
			x = 3+x
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