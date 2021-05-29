import numpy as np 

def function(x):

	o6 = 0
	h3 = 3
	paths = []
	try:
		if o6 < 2:
			o6 = h3+h3
			h3 = 3+h3
			x = x/h3
			paths.append(1)
		else:
			h3 = x/h3
			paths.append(2)
		if h3 < 3:
			h3 = 2-x
			h3 = h3*7
			paths.append(3)
		else:
			x = x*h3
			h3 = o6/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))