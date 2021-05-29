import numpy as np 

def function(x):

	s8 = x
	y6 = x
	x = x
	paths = []
	try:
		if s8 >= 2:
			x = 9/x
			s8 = s8*4
			paths.append(1)
		else:
			x = x-8
			s8 = s8+7
			paths.append(2)
		if s8 <= 1:
			s8 = s8+4
			paths.append(3)
		else:
			y6 = 2*s8
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))