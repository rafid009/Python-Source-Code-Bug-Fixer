import numpy as np 

def function(x):

	e6 = x
	s6 = x
	paths = []
	try:
		if e6 > 2:
			s6 = s6*6
			s6 = s6-2
			paths.append(1)
		else:
			x = 7/x
			x = 6*x
			paths.append(2)
		if x < 8:
			e6 = x*e6
			paths.append(3)
		else:
			s6 = s6+4
			s6 = s6*8
			x = x/s6
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