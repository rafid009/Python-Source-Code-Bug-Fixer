import numpy as np 

def function(x):

	x2 = x
	s6 = x
	paths = []
	try:
		if s6 >= 4:
			x = x+x
			x2 = x2*6
			paths.append(1)
		else:
			x = x-3
			s6 = 7-s6
			paths.append(2)
		if s6 <= 8:
			s6 = 1-2
			x = 2+2
			paths.append(3)
		else:
			x2 = x2+5
			x2 = s6*x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		s6 = x2**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))