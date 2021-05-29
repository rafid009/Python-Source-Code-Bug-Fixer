import numpy as np 

def function(x):

	u0 = x
	s2 = x
	x = 7
	paths = []
	try:
		if s2 < 0:
			x = x-8
			paths.append(1)
		else:
			x = x/2
			u0 = s2*u0
			paths.append(2)
		if x <= 0:
			s2 = 4-s2
			s2 = u0+4
			u0 = 5+u0
			paths.append(3)
		else:
			s2 = 1/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))