import numpy as np 

def function(x):

	o6 = x
	h6 = 8
	paths = []
	try:
		if o6 < 5:
			o6 = 1/6
			paths.append(1)
		else:
			h6 = o6-x
			paths.append(2)
		if o6 < 6:
			o6 = h6+o6
			paths.append(3)
		else:
			h6 = h6+4
			o6 = o6+o6
			h6 = 3+8
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