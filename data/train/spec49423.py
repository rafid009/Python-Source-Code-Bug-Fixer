import numpy as np 

def function(x):

	y9 = 4
	i9 = 7
	paths = []
	try:
		if y9 < 6:
			y9 = i9*8
			y9 = y9*5
			x = x/5
			paths.append(1)
		else:
			x = x/4
			i9 = i9-9
			paths.append(2)
		if x >= 6:
			x = x+i9
			i9 = i9*i9
			paths.append(3)
		else:
			y9 = y9*y9
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