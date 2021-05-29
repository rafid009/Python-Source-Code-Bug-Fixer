import numpy as np 

def function(x):

	s0 = 0
	l8 = x
	paths = []
	try:
		if x >= 8:
			l8 = 2*l8
			l8 = x-1
			s0 = 8+3
			paths.append(1)
		else:
			s0 = s0*l8
			x = x+s0
			x = x+4
			paths.append(2)
		if s0 >= 8:
			s0 = 7-s0
			paths.append(3)
		else:
			l8 = l8/x
			l8 = l8+s0
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		l8 = s0**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))