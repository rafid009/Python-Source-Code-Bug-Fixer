import numpy as np 

def function(x):

	s0 = 9
	b3 = 3
	paths = []
	try:
		if x >= 9:
			x = x+2
			x = 6-s0
			s0 = 9/s0
			paths.append(1)
		else:
			s0 = s0+2
			s0 = b3+2
			s0 = 9+s0
			paths.append(2)
		if x > 4:
			b3 = b3-1
			b3 = 3-s0
			s0 = x-s0
			paths.append(3)
		else:
			s0 = s0+x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		s0 = b3**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))