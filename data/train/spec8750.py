import numpy as np 

def function(x):

	y9 = 9
	s8 = 6
	paths = []
	try:
		if y9 < 5:
			x = 1/x
			x = x*9
			paths.append(1)
		else:
			y9 = y9/8
			s8 = s8+s8
			paths.append(2)
		if s8 > 8:
			x = x-y9
			y9 = y9/9
			s8 = 6+s8
			paths.append(3)
		else:
			x = s8-7
			y9 = 6/y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s8 = x**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))