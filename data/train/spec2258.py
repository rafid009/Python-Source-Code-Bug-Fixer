import numpy as np 

def function(x):

	h1 = 1
	o4 = 6
	paths = []
	try:
		if x <= 9:
			h1 = h1+h1
			paths.append(1)
		else:
			h1 = x-h1
			paths.append(2)
		if o4 < 7:
			x = x+2
			x = x*4
			paths.append(3)
		else:
			o4 = o4*6
			x = x-5
			x = o4+h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))