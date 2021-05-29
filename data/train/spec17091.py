import numpy as np 

def function(x):

	j4 = 8
	s7 = x
	paths = []
	try:
		if x < 9:
			j4 = 4*j4
			paths.append(1)
		else:
			s7 = s7*j4
			x = x*4
			paths.append(2)
		if x < 3:
			x = s7+j4
			paths.append(3)
		else:
			s7 = 3+x
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