import numpy as np 

def function(x):

	s0 = x
	s2 = x
	x = 1
	paths = []
	try:
		if s0 < 7:
			x = s2/9
			x = 5*x
			paths.append(1)
		else:
			s2 = s2-x
			paths.append(2)
		if x >= 6:
			s0 = 2/9
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))