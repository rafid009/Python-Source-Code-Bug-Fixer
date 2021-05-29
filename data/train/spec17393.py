import numpy as np 

def function(x):

	o3 = x
	s0 = 7
	paths = []
	try:
		if s0 <= 2:
			s0 = s0-x
			x = s0+o3
			s0 = 6*s0
			paths.append(1)
		else:
			x = x+3
			o3 = o3-s0
			paths.append(2)
		if x > 8:
			o3 = 3/o3
			x = o3*o3
			paths.append(3)
		else:
			x = 4*o3
			s0 = 3/o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))