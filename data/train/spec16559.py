import numpy as np 

def function(x):

	b3 = x
	h9 = 1
	paths = []
	try:
		if x < 8:
			h9 = 8/9
			paths.append(1)
		else:
			x = h9-x
			paths.append(2)
		if h9 <= 8:
			x = x-8
			h9 = b3/8
			paths.append(3)
		else:
			x = 1*x
			b3 = x*b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))