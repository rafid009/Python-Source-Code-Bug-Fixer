import numpy as np 

def function(x):

	b5 = 6
	s6 = x
	paths = []
	try:
		if b5 >= 0:
			s6 = 6/s6
			b5 = 1*s6
			b5 = b5/7
			paths.append(1)
		else:
			b5 = b5-8
			paths.append(2)
		if b5 <= 0:
			s6 = s6-1
			s6 = 9+6
			paths.append(3)
		else:
			s6 = 7-s6
			s6 = x*x
			s6 = s6/s6
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