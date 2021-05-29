import numpy as np 

def function(x):

	o1 = 2
	h9 = 8
	paths = []
	try:
		if h9 > 6:
			h9 = h9-7
			x = x/6
			h9 = 2*h9
			paths.append(1)
		else:
			x = x-7
			h9 = h9*3
			paths.append(2)
		if x > 7:
			o1 = o1/o1
			x = x/9
			paths.append(3)
		else:
			o1 = o1*x
			o1 = h9+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))