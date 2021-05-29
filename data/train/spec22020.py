import numpy as np 

def function(x):

	y9 = x
	g1 = x
	paths = []
	try:
		if g1 > 6:
			y9 = x+y9
			y9 = y9+6
			y9 = y9+9
			paths.append(1)
		else:
			g1 = g1+2
			paths.append(2)
		if x >= 3:
			x = x-2
			g1 = 7-1
			x = 2+3
			paths.append(3)
		else:
			x = 8+g1
			y9 = y9-2
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		g1 = y9**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))