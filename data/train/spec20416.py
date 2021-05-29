import numpy as np 

def function(x):

	o1 = 8
	h9 = 9
	paths = []
	try:
		if o1 < 7:
			x = x*7
			paths.append(1)
		else:
			h9 = h9-2
			paths.append(2)
		if h9 < 0:
			o1 = o1-6
			h9 = h9+h9
			x = 3+8
			paths.append(3)
		else:
			x = 8+x
			h9 = o1+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))