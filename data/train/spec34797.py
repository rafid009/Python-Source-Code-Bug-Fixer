import numpy as np 

def function(x):

	x3 = 2
	s0 = x
	paths = []
	try:
		if x3 >= 7:
			x3 = 0-x3
			paths.append(1)
		else:
			x3 = x3*4
			s0 = 1/s0
			s0 = 0-x
			paths.append(2)
		if x3 <= 2:
			x = 7+8
			x = 6/s0
			paths.append(3)
		else:
			s0 = s0-4
			x3 = s0-8
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))