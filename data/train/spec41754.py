import numpy as np 

def function(x):

	k9 = 5
	y9 = 7
	paths = []
	try:
		if k9 >= 5:
			x = x-7
			paths.append(1)
		else:
			x = x*7
			k9 = k9+k9
			x = x/7
			paths.append(2)
		if y9 < 5:
			k9 = 6+k9
			k9 = k9+2
			paths.append(3)
		else:
			y9 = y9/4
			y9 = y9-k9
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