import numpy as np 

def function(x):

	h4 = 7
	s5 = 8
	paths = []
	try:
		if x >= 9:
			s5 = 1-0
			paths.append(1)
		else:
			h4 = h4/s5
			h4 = h4+3
			s5 = 6/s5
			paths.append(2)
		if x < 8:
			h4 = 0-s5
			h4 = h4*2
			x = h4*x
			paths.append(3)
		else:
			h4 = h4*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))