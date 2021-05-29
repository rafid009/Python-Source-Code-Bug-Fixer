import numpy as np 

def function(x):

	s4 = x
	q0 = 6
	paths = []
	try:
		if x <= 0:
			s4 = x-3
			q0 = q0*9
			x = x+4
			paths.append(1)
		else:
			s4 = s4/8
			s4 = s4/2
			q0 = 4*q0
			paths.append(2)
		if x <= 2:
			q0 = 0*q0
			paths.append(3)
		else:
			s4 = 9*s4
			s4 = s4+s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))