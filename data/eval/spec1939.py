import numpy as np 

def function(x):

	s0 = 2
	s8 = 4
	paths = []
	try:
		if s0 >= 9:
			s0 = s0/x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x <= 6:
			s0 = s0+0
			s0 = s0-7
			x = 7*x
			paths.append(3)
		else:
			s8 = s0*5
			s0 = s0*6
			s8 = 9/x
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