import numpy as np 

def function(x):

	y9 = x
	t8 = 0
	paths = []
	try:
		if x <= 4:
			t8 = y9*x
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x < 1:
			y9 = 8/y9
			paths.append(3)
		else:
			x = t8-t8
			y9 = 8*y9
			y9 = 4*y9
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