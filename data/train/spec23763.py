import numpy as np 

def function(x):

	x3 = x
	s4 = x
	paths = []
	try:
		if s4 <= 2:
			x3 = 0*s4
			s4 = 5*s4
			s4 = 2-s4
			paths.append(1)
		else:
			x3 = 4*x
			paths.append(2)
		if x3 > 5:
			x3 = x3+x
			s4 = x3-s4
			x = s4-6
			paths.append(3)
		else:
			s4 = x3*3
			x3 = x3-x3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))