import numpy as np 

def function(x):

	s8 = x
	y4 = 8
	paths = []
	try:
		if y4 < 6:
			s8 = s8/8
			y4 = y4/x
			paths.append(1)
		else:
			x = y4+x
			paths.append(2)
		if s8 >= 9:
			y4 = s8-x
			s8 = 9*s8
			paths.append(3)
		else:
			s8 = x/3
			s8 = x+s8
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