import numpy as np 

def function(x):

	y9 = x
	k7 = 1
	paths = []
	try:
		if x >= 2:
			k7 = 4+k7
			x = 9+x
			paths.append(1)
		else:
			k7 = k7*3
			paths.append(2)
		if x <= 3:
			y9 = x*y9
			paths.append(3)
		else:
			x = x+9
			x = 2-x
			k7 = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))