import numpy as np 

def function(x):

	s8 = x
	a4 = x
	paths = []
	try:
		if x < 7:
			a4 = 9*a4
			a4 = a4*8
			s8 = 8+s8
			paths.append(1)
		else:
			a4 = s8*a4
			paths.append(2)
		if x < 5:
			s8 = 9+3
			a4 = 6-s8
			a4 = 4-x
			paths.append(3)
		else:
			s8 = s8+6
			a4 = a4-9
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