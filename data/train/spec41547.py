import numpy as np 

def function(x):

	s0 = 2
	y7 = x
	paths = []
	try:
		if x < 2:
			s0 = 8+6
			paths.append(1)
		else:
			s0 = 4-y7
			y7 = 0+7
			paths.append(2)
		if y7 < 6:
			s0 = 3*2
			paths.append(3)
		else:
			s0 = s0-x
			s0 = 3-7
			y7 = 7+y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))