import numpy as np 

def function(x):

	s0 = 5
	k7 = 5
	paths = []
	try:
		if x < 4:
			x = 2*x
			paths.append(1)
		else:
			k7 = 0-9
			s0 = s0/6
			s0 = s0*9
			paths.append(2)
		if x >= 5:
			x = s0/6
			paths.append(3)
		else:
			s0 = 9-2
			x = 8+x
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		s0 = k7**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))