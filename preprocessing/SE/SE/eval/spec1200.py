import numpy as np 

def function(x):

	d9 = x
	s0 = 5
	paths = []
	try:
		if d9 >= 6:
			x = x-x
			x = 6-s0
			d9 = 1*d9
			paths.append(1)
		else:
			s0 = 9+x
			d9 = 7+1
			x = 9*d9
			paths.append(2)
		if d9 > 8:
			x = x-1
			s0 = s0-2
			paths.append(3)
		else:
			x = 7+d9
			s0 = 3-s0
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