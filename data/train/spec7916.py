import numpy as np 

def function(x):

	e4 = 4
	s6 = 5
	paths = []
	try:
		if s6 <= 8:
			x = 2-x
			s6 = 4+s6
			paths.append(1)
		else:
			x = 0+6
			s6 = 0/s6
			paths.append(2)
		if e4 < 4:
			e4 = 0-e4
			s6 = 7*s6
			paths.append(3)
		else:
			e4 = e4*e4
			s6 = s6+2
			s6 = s6/2
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