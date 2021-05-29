import numpy as np 

def function(x):

	s0 = x
	v6 = 3
	paths = []
	try:
		if x < 2:
			x = x+5
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x > 9:
			s0 = 6/s0
			s0 = 3-s0
			paths.append(3)
		else:
			v6 = 2/s0
			x = x-6
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