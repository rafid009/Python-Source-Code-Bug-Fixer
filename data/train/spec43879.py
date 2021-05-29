import numpy as np 

def function(x):

	i0 = x
	h6 = 3
	x = x
	paths = []
	try:
		if i0 >= 0:
			h6 = h6*8
			paths.append(1)
		else:
			x = x-h6
			h6 = h6*1
			paths.append(2)
		if i0 <= 7:
			i0 = h6-i0
			i0 = x+x
			paths.append(3)
		else:
			x = 2*3
			i0 = i0-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		h6 = i0**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))