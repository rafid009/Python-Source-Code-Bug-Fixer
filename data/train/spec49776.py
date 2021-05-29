import numpy as np 

def function(x):

	h3 = 3
	o1 = 6
	paths = []
	try:
		if h3 <= 9:
			h3 = o1/x
			paths.append(1)
		else:
			o1 = h3+o1
			x = 9-h3
			h3 = h3-7
			paths.append(2)
		if x > 2:
			o1 = o1*8
			paths.append(3)
		else:
			o1 = h3+o1
			o1 = 0*o1
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