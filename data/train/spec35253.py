import numpy as np 

def function(x):

	y4 = x
	s2 = x
	paths = []
	try:
		if x <= 9:
			s2 = y4-x
			s2 = s2-y4
			paths.append(1)
		else:
			x = 4*x
			y4 = y4-7
			paths.append(2)
		if x >= 1:
			x = 5-3
			paths.append(3)
		else:
			s2 = y4-s2
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		s2 = y4**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))