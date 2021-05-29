import numpy as np 

def function(x):

	x3 = 1
	s8 = x
	paths = []
	try:
		if x3 <= 1:
			x3 = s8+x3
			paths.append(1)
		else:
			s8 = 3/8
			paths.append(2)
		if x3 <= 0:
			x = x-3
			x = 7*7
			paths.append(3)
		else:
			s8 = 9-s8
			x3 = x3-x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		s8 = x3**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))