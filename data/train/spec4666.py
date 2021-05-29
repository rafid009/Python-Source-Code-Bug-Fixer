import numpy as np 

def function(x):

	h7 = 7
	s5 = x
	x = x
	paths = []
	try:
		if s5 > 3:
			x = 0-7
			paths.append(1)
		else:
			s5 = h7/3
			s5 = h7+s5
			s5 = x-6
			paths.append(2)
		if h7 < 3:
			s5 = s5+2
			h7 = h7-8
			paths.append(3)
		else:
			h7 = 4*x
			h7 = 7*h7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		s5 = h7**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))