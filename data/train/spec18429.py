import numpy as np 

def function(x):

	h0 = x
	i0 = x
	paths = []
	try:
		if i0 > 9:
			i0 = i0+1
			i0 = 6/8
			paths.append(1)
		else:
			i0 = h0*6
			x = i0*9
			paths.append(2)
		if h0 >= 0:
			i0 = i0/i0
			paths.append(3)
		else:
			h0 = i0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))