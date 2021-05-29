import numpy as np 

def function(x):

	y9 = x
	v3 = 8
	paths = []
	try:
		if x < 0:
			x = x+4
			y9 = 4/y9
			paths.append(1)
		else:
			y9 = y9/y9
			paths.append(2)
		if v3 > 5:
			v3 = v3-1
			paths.append(3)
		else:
			y9 = y9*x
			x = 9-v3
			x = x/5
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