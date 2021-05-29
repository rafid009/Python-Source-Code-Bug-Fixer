import numpy as np 

def function(x):

	e0 = 3
	s0 = x
	paths = []
	try:
		if e0 > 4:
			s0 = 8*6
			x = 5+x
			e0 = e0*s0
			paths.append(1)
		else:
			x = x*s0
			x = 1-7
			x = 8/x
			paths.append(2)
		if s0 < 7:
			e0 = 0-e0
			x = x/1
			s0 = 9*9
			paths.append(3)
		else:
			x = x-s0
			x = e0+4
			e0 = e0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))