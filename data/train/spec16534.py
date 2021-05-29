import numpy as np 

def function(x):

	s5 = x
	s7 = 9
	paths = []
	try:
		if s5 > 2:
			s5 = 9+s5
			x = 5+x
			paths.append(1)
		else:
			s7 = s7/3
			s7 = 1-s7
			paths.append(2)
		if s5 > 6:
			s5 = 1-s7
			paths.append(3)
		else:
			s5 = 9+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))