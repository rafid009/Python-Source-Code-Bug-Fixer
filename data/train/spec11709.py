import numpy as np 

def function(x):

	s6 = 5
	s0 = x
	paths = []
	try:
		if s0 >= 8:
			s6 = s6*s0
			paths.append(1)
		else:
			s6 = x*s6
			paths.append(2)
		if s6 <= 4:
			s6 = s0-s6
			s0 = 9/4
			s0 = s0/8
			paths.append(3)
		else:
			s0 = 0*s0
			x = x+2
			s0 = 8-s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))