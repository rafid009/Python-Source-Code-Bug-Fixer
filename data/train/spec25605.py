import numpy as np 

def function(x):

	h3 = 0
	o2 = x
	paths = []
	try:
		if o2 <= 2:
			h3 = h3-5
			paths.append(1)
		else:
			x = x*3
			h3 = h3+x
			x = 0+6
			paths.append(2)
		if x <= 2:
			h3 = h3*o2
			o2 = 8-o2
			h3 = h3-6
			paths.append(3)
		else:
			h3 = 4*h3
			x = h3-h3
			h3 = h3*h3
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