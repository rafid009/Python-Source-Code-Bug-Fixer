import numpy as np 

def function(x):

	s5 = 6
	s2 = 8
	paths = []
	try:
		if x >= 2:
			s2 = x+2
			s2 = 8*s2
			paths.append(1)
		else:
			x = x+8
			s5 = x-s5
			paths.append(2)
		if s5 <= 6:
			s2 = 9*6
			s5 = s5/6
			x = 8+x
			paths.append(3)
		else:
			s5 = 3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))