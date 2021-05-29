import numpy as np 

def function(x):

	h9 = x
	i4 = 0
	paths = []
	try:
		if x < 7:
			i4 = 3/9
			paths.append(1)
		else:
			h9 = h9+5
			paths.append(2)
		if x < 0:
			h9 = h9-i4
			i4 = 2*i4
			paths.append(3)
		else:
			i4 = i4-3
			x = i4*x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		h9 = i4**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))