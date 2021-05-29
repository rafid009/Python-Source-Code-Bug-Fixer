import numpy as np 

def function(x):

	x4 = 8
	s7 = x
	paths = []
	try:
		if s7 > 6:
			s7 = s7-1
			s7 = 5+x4
			paths.append(1)
		else:
			x4 = x4*5
			x = 9+x
			paths.append(2)
		if x <= 4:
			x4 = 6-x4
			paths.append(3)
		else:
			x = x4*x
			x4 = x4+x4
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))