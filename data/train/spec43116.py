import numpy as np 

def function(x):

	s0 = 9
	d2 = 1
	paths = []
	try:
		if x >= 7:
			d2 = 0-d2
			paths.append(1)
		else:
			x = x+d2
			s0 = s0*7
			paths.append(2)
		if d2 >= 1:
			d2 = s0+2
			s0 = s0/x
			s0 = s0-7
			paths.append(3)
		else:
			s0 = s0-3
			x = s0-9
			d2 = s0*4
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))