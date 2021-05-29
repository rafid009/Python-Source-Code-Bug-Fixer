import numpy as np 

def function(x):

	s4 = x
	paths = []
	try:
		if s4 < 2:
			s4 = x-x
			s4 = 6-s4
			paths.append(1)
		else:
			s4 = s4/s4
			paths.append(2)
		if x <= 3:
			s4 = 4/8
			paths.append(3)
		else:
			s4 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))