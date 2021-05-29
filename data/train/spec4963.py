import numpy as np 

def function(x):

	s9 = 4
	s0 = x
	paths = []
	try:
		if x > 3:
			s9 = s9+s9
			s9 = 9*1
			s0 = s0+6
			paths.append(1)
		else:
			s9 = 6/s0
			paths.append(2)
		if s9 < 2:
			s0 = 6*s9
			paths.append(3)
		else:
			s9 = 1+4
			s9 = s9+x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s0 = s9**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))