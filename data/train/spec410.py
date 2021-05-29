import numpy as np 

def function(x):

	s7 = 7
	d0 = 4
	x = 0
	paths = []
	try:
		if s7 < 8:
			d0 = 7-d0
			paths.append(1)
		else:
			x = s7/2
			s7 = s7+3
			paths.append(2)
		if x >= 8:
			x = x*d0
			paths.append(3)
		else:
			x = x-6
			s7 = x*s7
			s7 = s7+5
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