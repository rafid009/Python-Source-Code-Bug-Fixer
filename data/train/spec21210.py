import numpy as np 

def function(x):

	k9 = 0
	y9 = 1
	x = x
	paths = []
	try:
		if k9 < 7:
			y9 = 3+y9
			paths.append(1)
		else:
			k9 = k9-k9
			x = 4+4
			paths.append(2)
		if x <= 3:
			k9 = k9-x
			x = x-0
			y9 = 7-y9
			paths.append(3)
		else:
			y9 = 3+y9
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))