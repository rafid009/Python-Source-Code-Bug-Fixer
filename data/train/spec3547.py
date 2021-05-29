import numpy as np 

def function(x):

	h4 = x
	i0 = 7
	paths = []
	try:
		if i0 >= 7:
			h4 = 3-h4
			i0 = 8-x
			x = x-9
			paths.append(1)
		else:
			i0 = i0-0
			x = 4-9
			paths.append(2)
		if i0 > 1:
			h4 = h4*8
			paths.append(3)
		else:
			x = h4*4
			h4 = h4-h4
			x = 5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))