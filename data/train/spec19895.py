import numpy as np 

def function(x):

	s9 = 8
	y9 = x
	paths = []
	try:
		if s9 > 8:
			y9 = y9-6
			y9 = y9+5
			paths.append(1)
		else:
			s9 = y9/8
			s9 = 7+1
			paths.append(2)
		if s9 <= 9:
			x = 0-x
			paths.append(3)
		else:
			s9 = y9/y9
			y9 = y9+1
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