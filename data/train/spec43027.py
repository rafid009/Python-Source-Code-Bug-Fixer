import numpy as np 

def function(x):

	k0 = x
	y9 = 4
	paths = []
	try:
		if x <= 1:
			y9 = y9*1
			y9 = y9*x
			k0 = 3*3
			paths.append(1)
		else:
			y9 = y9+x
			paths.append(2)
		if y9 < 8:
			x = y9*6
			k0 = x/k0
			k0 = k0*3
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		y9 = k0**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))