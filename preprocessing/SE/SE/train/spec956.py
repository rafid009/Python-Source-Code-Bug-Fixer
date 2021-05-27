import numpy as np 

def function(x):

	b8 = 4
	h6 = 9
	paths = []
	try:
		if b8 < 3:
			h6 = b8/h6
			b8 = 0+b8
			paths.append(1)
		else:
			h6 = b8*h6
			x = 8+x
			paths.append(2)
		if b8 < 6:
			h6 = h6-x
			h6 = h6-b8
			x = b8-x
			paths.append(3)
		else:
			x = 1/3
			b8 = 2+b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))