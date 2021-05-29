import numpy as np 

def function(x):

	o9 = 5
	h4 = x
	paths = []
	try:
		if x < 8:
			h4 = o9/h4
			x = x-x
			paths.append(1)
		else:
			h4 = h4+o9
			x = x-x
			o9 = 9*o9
			paths.append(2)
		if h4 >= 3:
			h4 = h4-7
			paths.append(3)
		else:
			x = x*4
			x = h4+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))