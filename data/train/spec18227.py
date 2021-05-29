import numpy as np 

def function(x):

	h3 = x
	o0 = 9
	paths = []
	try:
		if h3 <= 9:
			o0 = 1-o0
			h3 = o0/1
			paths.append(1)
		else:
			h3 = h3-1
			x = 3*x
			paths.append(2)
		if o0 > 0:
			o0 = o0+8
			h3 = 1-h3
			h3 = 8+h3
			paths.append(3)
		else:
			x = h3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))