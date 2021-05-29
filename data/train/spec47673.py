import numpy as np 

def function(x):

	s5 = 8
	s8 = 2
	paths = []
	try:
		if x < 0:
			x = s8-s5
			s5 = 4-s5
			paths.append(1)
		else:
			s5 = 9*7
			s5 = 7*s5
			s5 = s5+6
			paths.append(2)
		if x < 1:
			s5 = s5*5
			s5 = 1-s5
			s5 = 1-8
			paths.append(3)
		else:
			s8 = 4-s8
			s5 = 5+6
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s8 = s5**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))