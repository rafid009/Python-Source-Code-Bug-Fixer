import numpy as np 

def function(x):

	s0 = 9
	u4 = x
	paths = []
	try:
		if s0 < 0:
			s0 = s0/s0
			paths.append(1)
		else:
			s0 = 5-u4
			x = 4-x
			x = x-9
			paths.append(2)
		if x >= 6:
			u4 = x+u4
			paths.append(3)
		else:
			s0 = u4*u4
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))