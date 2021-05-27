import numpy as np 

def function(x):

	h6 = x
	o4 = 9
	paths = []
	try:
		if h6 > 8:
			h6 = 5-h6
			h6 = o4*h6
			o4 = 1/o4
			paths.append(1)
		else:
			h6 = h6+h6
			o4 = o4/h6
			paths.append(2)
		if o4 > 2:
			h6 = h6+6
			o4 = o4*9
			h6 = h6/1
			paths.append(3)
		else:
			o4 = h6*o4
			o4 = o4/o4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))