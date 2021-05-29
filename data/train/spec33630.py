import numpy as np 

def function(x):

	n0 = 5
	s1 = x
	paths = []
	try:
		if n0 > 8:
			x = n0+5
			n0 = 5-4
			paths.append(1)
		else:
			s1 = 6*s1
			s1 = 1-s1
			x = x-n0
			paths.append(2)
		if s1 <= 0:
			n0 = n0/s1
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		s1 = n0**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))