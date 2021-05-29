import numpy as np 

def function(x):

	s8 = 4
	h4 = x
	paths = []
	try:
		if h4 < 8:
			s8 = x-6
			x = x/s8
			x = x*6
			paths.append(1)
		else:
			x = x*s8
			s8 = s8-0
			h4 = s8-h4
			paths.append(2)
		if x >= 2:
			x = x/1
			h4 = h4/h4
			h4 = h4-h4
			paths.append(3)
		else:
			s8 = s8/h4
			h4 = x*h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))