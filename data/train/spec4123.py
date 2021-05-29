import numpy as np 

def function(x):

	s6 = x
	o4 = 2
	x = 5
	paths = []
	try:
		if x >= 0:
			o4 = o4/8
			s6 = 8*9
			o4 = o4-1
			paths.append(1)
		else:
			s6 = s6-2
			o4 = o4/s6
			paths.append(2)
		if x > 1:
			s6 = o4+o4
			x = o4/x
			paths.append(3)
		else:
			s6 = 1-1
			s6 = 3+s6
			o4 = 5*o4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))