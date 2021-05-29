import numpy as np 

def function(x):

	s7 = 1
	o1 = x
	x = x
	paths = []
	try:
		if o1 > 9:
			s7 = s7+4
			s7 = 6*s7
			s7 = s7-o1
			paths.append(1)
		else:
			x = x-4
			s7 = 0/x
			s7 = s7/9
			paths.append(2)
		if s7 < 0:
			s7 = s7-3
			o1 = 7*o1
			paths.append(3)
		else:
			s7 = 4-s7
			s7 = s7+x
			s7 = s7-9
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