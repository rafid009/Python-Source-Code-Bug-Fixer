import numpy as np 

def function(x):

	s8 = 6
	h8 = 4
	paths = []
	try:
		if h8 <= 8:
			h8 = 0-s8
			x = x-h8
			paths.append(1)
		else:
			h8 = h8/5
			h8 = 0/x
			h8 = 9*h8
			paths.append(2)
		if x >= 6:
			s8 = 2*x
			paths.append(3)
		else:
			x = x*3
			x = 9/x
			s8 = s8/2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))