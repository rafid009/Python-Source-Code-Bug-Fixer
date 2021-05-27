import numpy as np 

def function(x):

	h5 = 0
	o7 = x
	paths = []
	try:
		if x >= 5:
			o7 = o7*9
			o7 = o7*5
			h5 = h5/x
			paths.append(1)
		else:
			o7 = x+3
			paths.append(2)
		if h5 < 6:
			h5 = o7-x
			x = h5-x
			x = x-5
			paths.append(3)
		else:
			h5 = 2/h5
			h5 = h5+4
			o7 = 5/o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))