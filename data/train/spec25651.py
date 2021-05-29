import numpy as np 

def function(x):

	h9 = x
	n3 = 7
	paths = []
	try:
		if x <= 7:
			x = x*4
			x = x-n3
			paths.append(1)
		else:
			n3 = n3/6
			n3 = n3-h9
			paths.append(2)
		if x < 3:
			h9 = h9-n3
			paths.append(3)
		else:
			x = 8+x
			x = x*n3
			x = x-h9
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