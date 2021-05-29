import numpy as np 

def function(x):

	q0 = x
	s0 = x
	paths = []
	try:
		if x <= 2:
			s0 = s0-x
			paths.append(1)
		else:
			s0 = x-x
			q0 = 2-q0
			paths.append(2)
		if x >= 8:
			x = s0*5
			paths.append(3)
		else:
			s0 = s0-x
			q0 = 6+3
			x = x/3
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		s0 = q0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))