import numpy as np 

def function(x):

	x9 = 9
	s8 = x
	paths = []
	try:
		if s8 >= 8:
			s8 = 5*s8
			x = 9+x
			s8 = s8*8
			paths.append(1)
		else:
			s8 = s8*5
			s8 = x9/x
			x9 = x9+x9
			paths.append(2)
		if s8 >= 8:
			x = x/s8
			paths.append(3)
		else:
			s8 = x9+x
			x9 = 5-x
			x9 = s8*x9
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))