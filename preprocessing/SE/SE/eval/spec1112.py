import numpy as np 

def function(x):

	s0 = x
	d8 = x
	paths = []
	try:
		if s0 >= 1:
			d8 = d8*x
			d8 = 3/5
			s0 = s0*5
			paths.append(1)
		else:
			d8 = d8-5
			paths.append(2)
		if d8 <= 8:
			s0 = 8+x
			s0 = 9*d8
			paths.append(3)
		else:
			d8 = d8-x
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