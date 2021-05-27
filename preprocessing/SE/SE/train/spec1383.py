import numpy as np 

def function(x):

	s9 = x
	y9 = x
	paths = []
	try:
		if s9 < 0:
			s9 = s9-3
			paths.append(1)
		else:
			x = x/2
			y9 = 9+y9
			s9 = 0/y9
			paths.append(2)
		if s9 < 1:
			x = x/8
			paths.append(3)
		else:
			x = y9/y9
			y9 = y9-1
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))