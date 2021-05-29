import numpy as np 

def function(x):

	v4 = x
	s0 = x
	paths = []
	try:
		if v4 <= 4:
			s0 = 9*9
			paths.append(1)
		else:
			s0 = 6/s0
			s0 = s0+6
			paths.append(2)
		if v4 < 7:
			s0 = s0*s0
			paths.append(3)
		else:
			x = 0-v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))