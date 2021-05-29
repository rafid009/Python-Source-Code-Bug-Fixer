import numpy as np 

def function(x):

	s6 = 6
	x0 = x
	x = x
	paths = []
	try:
		if x0 > 8:
			x = x/7
			s6 = s6/s6
			paths.append(1)
		else:
			x = s6/x
			x0 = x0/4
			x = x*5
			paths.append(2)
		if s6 < 0:
			s6 = 6*s6
			paths.append(3)
		else:
			x = 3/x
			s6 = x0/s6
			x0 = x0*4
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))