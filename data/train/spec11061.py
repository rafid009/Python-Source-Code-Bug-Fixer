import numpy as np 

def function(x):

	x8 = 9
	s0 = x
	paths = []
	try:
		if x8 < 4:
			x = 4+7
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if s0 >= 5:
			x = 4*x
			s0 = s0-0
			s0 = 7/x
			paths.append(3)
		else:
			x8 = x8/2
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