import numpy as np 

def function(x):

	s8 = 2
	l2 = 0
	paths = []
	try:
		if s8 < 6:
			s8 = s8*9
			l2 = l2+2
			s8 = 9+s8
			paths.append(1)
		else:
			s8 = 3*s8
			s8 = s8/x
			x = 9*9
			paths.append(2)
		if l2 >= 8:
			s8 = s8-l2
			l2 = s8-3
			s8 = 9-5
			paths.append(3)
		else:
			l2 = l2+9
			s8 = l2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))