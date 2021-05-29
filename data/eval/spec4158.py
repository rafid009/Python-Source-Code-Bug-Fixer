import numpy as np 

def function(x):

	s0 = 5
	paths = []
	try:
		if s0 < 4:
			s0 = s0*x
			s0 = s0+s0
			paths.append(1)
		else:
			x = x-s0
			s0 = s0/6
			s0 = s0*5
			paths.append(2)
		if s0 > 7:
			s0 = s0/x
			x = x*2
			paths.append(3)
		else:
			x = x+5
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