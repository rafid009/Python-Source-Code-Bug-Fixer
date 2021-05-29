import numpy as np 

def function(x):

	l3 = 3
	s8 = 3
	x = x
	paths = []
	try:
		if l3 <= 0:
			s8 = 9*s8
			l3 = s8/s8
			paths.append(1)
		else:
			s8 = 9*s8
			s8 = 4-s8
			paths.append(2)
		if s8 >= 9:
			s8 = 9-6
			x = 8/x
			paths.append(3)
		else:
			l3 = 5+l3
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