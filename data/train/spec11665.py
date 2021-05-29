import numpy as np 

def function(x):

	s7 = 1
	h9 = x
	paths = []
	try:
		if h9 >= 7:
			h9 = h9/x
			s7 = s7+6
			x = 0+4
			paths.append(1)
		else:
			h9 = h9-6
			x = 8/x
			h9 = 8*6
			paths.append(2)
		if h9 < 5:
			h9 = h9*4
			paths.append(3)
		else:
			h9 = 3*2
			x = 3+7
			h9 = s7-4
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		s7 = h9**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))