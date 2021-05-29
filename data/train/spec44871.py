import numpy as np 

def function(x):

	s1 = x
	x7 = 6
	paths = []
	try:
		if x >= 3:
			x7 = x+x7
			s1 = x7+s1
			x7 = 5/x7
			paths.append(1)
		else:
			x7 = 4*s1
			paths.append(2)
		if x7 > 5:
			s1 = x7+7
			paths.append(3)
		else:
			s1 = 8+x
			s1 = 9*s1
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		s1 = x7**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))