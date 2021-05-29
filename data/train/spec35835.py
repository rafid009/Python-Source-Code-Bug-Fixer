import numpy as np 

def function(x):

	s2 = 9
	y9 = x
	paths = []
	try:
		if x > 9:
			x = 7+9
			y9 = y9*5
			s2 = 0-s2
			paths.append(1)
		else:
			y9 = s2-y9
			s2 = s2/y9
			y9 = x-x
			paths.append(2)
		if y9 < 4:
			x = x+1
			y9 = y9-9
			s2 = y9-9
			paths.append(3)
		else:
			s2 = 5/4
			x = x-1
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		y9 = s2**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))