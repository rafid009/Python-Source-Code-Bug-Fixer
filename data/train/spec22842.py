import numpy as np 

def function(x):

	s7 = x
	h3 = 6
	paths = []
	try:
		if h3 <= 8:
			h3 = x+x
			x = s7-1
			s7 = s7/6
			paths.append(1)
		else:
			h3 = h3+2
			paths.append(2)
		if s7 > 9:
			h3 = s7+8
			x = h3-x
			paths.append(3)
		else:
			x = 7/x
			h3 = h3/2
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