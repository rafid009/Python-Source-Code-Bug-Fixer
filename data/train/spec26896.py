import numpy as np 

def function(x):

	s8 = 4
	n4 = 5
	paths = []
	try:
		if n4 < 8:
			x = x+2
			paths.append(1)
		else:
			s8 = s8*8
			paths.append(2)
		if x > 3:
			s8 = 1-s8
			n4 = n4+n4
			paths.append(3)
		else:
			s8 = s8*s8
			n4 = n4/x
			n4 = n4/s8
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		s8 = n4**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))