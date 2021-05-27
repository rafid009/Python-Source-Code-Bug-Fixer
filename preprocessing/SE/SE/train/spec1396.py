import numpy as np 

def function(x):

	s6 = x
	n6 = 9
	paths = []
	try:
		if s6 < 1:
			n6 = 6-7
			x = x*9
			n6 = 9/s6
			paths.append(1)
		else:
			x = s6+x
			s6 = 6-5
			paths.append(2)
		if s6 >= 1:
			x = 9-x
			x = 1*6
			s6 = 8*s6
			paths.append(3)
		else:
			n6 = 3*6
			s6 = 6+s6
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