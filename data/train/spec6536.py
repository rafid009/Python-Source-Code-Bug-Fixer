import numpy as np 

def function(x):

	s2 = 7
	h8 = x
	paths = []
	try:
		if s2 >= 6:
			x = s2-1
			s2 = 4-s2
			x = 3-x
			paths.append(1)
		else:
			h8 = h8-6
			paths.append(2)
		if s2 <= 7:
			h8 = s2/3
			paths.append(3)
		else:
			s2 = 2*s2
			h8 = h8/2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		s2 = h8**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))