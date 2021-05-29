import numpy as np 

def function(x):

	s0 = x
	x8 = 9
	x = x
	paths = []
	try:
		if x < 0:
			x8 = x8-s0
			s0 = s0*x8
			x8 = s0+3
			paths.append(1)
		else:
			s0 = s0+x8
			x8 = x8*7
			paths.append(2)
		if x < 3:
			s0 = s0+0
			paths.append(3)
		else:
			x = s0/x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		s0 = x8**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))