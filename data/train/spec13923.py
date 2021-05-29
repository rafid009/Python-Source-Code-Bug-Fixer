import numpy as np 

def function(x):

	y9 = 9
	s2 = 2
	paths = []
	try:
		if y9 < 6:
			x = y9+x
			s2 = s2/5
			y9 = s2+5
			paths.append(1)
		else:
			s2 = 9/8
			x = 3-7
			paths.append(2)
		if y9 <= 2:
			x = x*5
			paths.append(3)
		else:
			y9 = 3-y9
			s2 = 0*6
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