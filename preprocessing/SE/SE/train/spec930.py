import numpy as np 

def function(x):

	h3 = 5
	s8 = x
	paths = []
	try:
		if x >= 3:
			h3 = 5-6
			h3 = 5-h3
			x = x-h3
			paths.append(1)
		else:
			s8 = 8*8
			paths.append(2)
		if h3 > 9:
			s8 = x/s8
			x = 8+x
			paths.append(3)
		else:
			h3 = h3+2
			x = 6/x
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