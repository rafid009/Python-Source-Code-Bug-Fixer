import numpy as np 

def function(x):

	s7 = 6
	j8 = 7
	paths = []
	try:
		if x < 3:
			x = 9/3
			s7 = 8-s7
			j8 = s7+j8
			paths.append(1)
		else:
			x = x*3
			x = 3+9
			s7 = s7/x
			paths.append(2)
		if s7 > 6:
			x = 6/x
			j8 = 1-0
			paths.append(3)
		else:
			s7 = s7-9
			j8 = j8/x
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