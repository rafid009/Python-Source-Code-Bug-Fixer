import numpy as np 

def function(x):

	h3 = 0
	r7 = x
	paths = []
	try:
		if r7 < 6:
			x = x-7
			x = 9-3
			paths.append(1)
		else:
			r7 = r7-h3
			paths.append(2)
		if r7 >= 0:
			h3 = h3-2
			paths.append(3)
		else:
			x = 4-x
			h3 = x*r7
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