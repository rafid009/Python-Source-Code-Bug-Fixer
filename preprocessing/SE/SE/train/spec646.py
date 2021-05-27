import numpy as np 

def function(x):

	y9 = x
	s2 = x
	paths = []
	try:
		if x >= 8:
			y9 = 4/1
			paths.append(1)
		else:
			s2 = s2+5
			s2 = 1+s2
			paths.append(2)
		if x < 7:
			y9 = y9-y9
			paths.append(3)
		else:
			x = 7/4
			s2 = x+s2
			y9 = y9+6
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))