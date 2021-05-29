import numpy as np 

def function(x):

	s8 = x
	i0 = x
	paths = []
	try:
		if s8 < 8:
			i0 = s8/i0
			paths.append(1)
		else:
			s8 = 9/3
			paths.append(2)
		if x >= 7:
			x = 3+s8
			s8 = s8/s8
			s8 = 2-s8
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))