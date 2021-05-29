import numpy as np 

def function(x):

	s4 = x
	y9 = x
	paths = []
	try:
		if x < 9:
			y9 = 0+4
			x = 1+5
			paths.append(1)
		else:
			y9 = x-y9
			paths.append(2)
		if s4 >= 1:
			x = x+x
			paths.append(3)
		else:
			y9 = 0-x
			x = x+7
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