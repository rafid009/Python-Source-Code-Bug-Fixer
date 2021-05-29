import numpy as np 

def function(x):

	s7 = x
	s1 = 6
	paths = []
	try:
		if s1 < 1:
			x = 1/x
			x = 9-x
			paths.append(1)
		else:
			s1 = x-7
			paths.append(2)
		if s7 > 4:
			s1 = s1-0
			s1 = s7-1
			paths.append(3)
		else:
			s7 = s7+4
			x = x*8
			s7 = s7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))