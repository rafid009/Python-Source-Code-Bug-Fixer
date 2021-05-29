import numpy as np 

def function(x):

	y9 = 1
	k9 = 2
	paths = []
	try:
		if y9 >= 6:
			y9 = y9/y9
			y9 = x/2
			x = x+5
			paths.append(1)
		else:
			k9 = x/2
			x = x-6
			paths.append(2)
		if x >= 3:
			y9 = 0/1
			paths.append(3)
		else:
			y9 = 6*x
			k9 = 3-k9
			x = x/y9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		k9 = y9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))