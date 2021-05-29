import numpy as np 

def function(x):

	y9 = 4
	s6 = 9
	paths = []
	try:
		if y9 >= 6:
			s6 = 6+y9
			y9 = y9-x
			x = x+5
			paths.append(1)
		else:
			y9 = y9-7
			x = x/5
			y9 = 7-y9
			paths.append(2)
		if s6 > 6:
			y9 = s6*x
			s6 = 9-y9
			paths.append(3)
		else:
			s6 = s6/s6
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))