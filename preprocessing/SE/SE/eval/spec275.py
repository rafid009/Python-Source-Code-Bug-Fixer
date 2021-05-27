import numpy as np 

def function(x):

	y9 = 6
	s6 = x
	paths = []
	try:
		if x <= 8:
			y9 = y9-7
			s6 = 5/s6
			paths.append(1)
		else:
			y9 = s6/y9
			y9 = 6*6
			paths.append(2)
		if s6 <= 1:
			x = x*2
			s6 = s6/x
			paths.append(3)
		else:
			s6 = 3+6
			x = s6/4
			x = 5*7
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))