import numpy as np 

def function(x):

	a7 = x
	s6 = 1
	paths = []
	try:
		if x > 7:
			a7 = 3*s6
			paths.append(1)
		else:
			a7 = a7+3
			s6 = 0-s6
			x = x/a7
			paths.append(2)
		if a7 >= 1:
			s6 = 2*s6
			s6 = x*s6
			s6 = 2*s6
			paths.append(3)
		else:
			a7 = a7-6
			a7 = a7-x
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