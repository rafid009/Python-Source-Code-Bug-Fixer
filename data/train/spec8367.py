import numpy as np 

def function(x):

	s0 = x
	d5 = 8
	paths = []
	try:
		if d5 <= 2:
			s0 = d5+8
			paths.append(1)
		else:
			d5 = d5+7
			d5 = d5/s0
			paths.append(2)
		if s0 > 9:
			d5 = 8-6
			paths.append(3)
		else:
			x = 0/x
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		s0 = d5**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))