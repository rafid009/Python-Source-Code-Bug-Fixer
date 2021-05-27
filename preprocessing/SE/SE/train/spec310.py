import numpy as np 

def function(x):

	h7 = x
	s1 = 8
	x = 3
	paths = []
	try:
		if s1 < 0:
			s1 = s1-1
			paths.append(1)
		else:
			s1 = h7+s1
			s1 = 0/s1
			paths.append(2)
		if h7 < 2:
			s1 = s1+6
			s1 = h7+6
			paths.append(3)
		else:
			h7 = 6/h7
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))