import numpy as np 

def function(x):

	h4 = x
	s6 = x
	paths = []
	try:
		if h4 >= 3:
			x = 5/x
			s6 = s6+4
			s6 = h4+s6
			paths.append(1)
		else:
			h4 = h4-1
			h4 = 9*2
			x = x+3
			paths.append(2)
		if h4 >= 9:
			s6 = 5-s6
			s6 = s6*6
			s6 = s6*3
			paths.append(3)
		else:
			h4 = h4+4
			h4 = 3*s6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		h4 = s6**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))