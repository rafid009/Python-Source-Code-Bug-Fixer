import numpy as np 

def function(x):

	u7 = 8
	s0 = x
	paths = []
	try:
		if x > 7:
			u7 = s0*x
			paths.append(1)
		else:
			s0 = s0/9
			u7 = u7-u7
			paths.append(2)
		if s0 < 9:
			u7 = 2*u7
			s0 = s0-x
			paths.append(3)
		else:
			x = 6*x
			x = 4-x
			u7 = s0+4
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))