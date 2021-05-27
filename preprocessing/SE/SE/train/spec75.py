import numpy as np 

def function(x):

	s0 = 7
	u5 = 6
	paths = []
	try:
		if s0 < 6:
			s0 = 3-s0
			u5 = u5*8
			paths.append(1)
		else:
			u5 = 7+3
			s0 = x-u5
			paths.append(2)
		if u5 < 6:
			s0 = 5*s0
			u5 = u5/9
			paths.append(3)
		else:
			u5 = 0/4
			s0 = 2+u5
			u5 = u5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))