import numpy as np 

def function(x):

	h8 = x
	s4 = 8
	x = 5
	paths = []
	try:
		if h8 > 4:
			s4 = x/h8
			x = x-6
			paths.append(1)
		else:
			h8 = 4-h8
			h8 = x-h8
			x = x+8
			paths.append(2)
		if s4 >= 4:
			h8 = x+h8
			x = x-s4
			h8 = 8/h8
			paths.append(3)
		else:
			x = 7/x
			h8 = 1/9
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