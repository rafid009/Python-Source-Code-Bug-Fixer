import numpy as np 

def function(x):

	o8 = 4
	h5 = x
	paths = []
	try:
		if x <= 0:
			x = x-9
			o8 = 4/o8
			paths.append(1)
		else:
			h5 = h5*h5
			paths.append(2)
		if o8 < 4:
			o8 = 2/o8
			x = x*7
			paths.append(3)
		else:
			h5 = 7-h5
			h5 = h5-o8
			h5 = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))