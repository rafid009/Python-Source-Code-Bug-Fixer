import numpy as np 

def function(x):

	s2 = 1
	o6 = x
	x = x
	paths = []
	try:
		if x < 9:
			s2 = s2+4
			s2 = x-s2
			s2 = 9+o6
			paths.append(1)
		else:
			o6 = s2/o6
			x = 2-o6
			paths.append(2)
		if x >= 3:
			s2 = 4/s2
			s2 = o6*s2
			s2 = s2-x
			paths.append(3)
		else:
			s2 = 9+s2
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