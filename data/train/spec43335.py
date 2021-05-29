import numpy as np 

def function(x):

	o6 = x
	h5 = x
	paths = []
	try:
		if h5 < 9:
			h5 = h5-h5
			paths.append(1)
		else:
			o6 = o6+h5
			x = o6-9
			h5 = 1*h5
			paths.append(2)
		if h5 >= 9:
			h5 = x+2
			x = 6-7
			h5 = 6+h5
			paths.append(3)
		else:
			h5 = h5+3
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))