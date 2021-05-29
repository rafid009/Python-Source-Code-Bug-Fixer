import numpy as np 

def function(x):

	y9 = x
	g1 = x
	paths = []
	try:
		if x >= 7:
			y9 = 2/y9
			y9 = y9*3
			paths.append(1)
		else:
			g1 = g1-g1
			x = x/2
			paths.append(2)
		if x > 8:
			g1 = y9-5
			paths.append(3)
		else:
			y9 = y9+5
			x = x*6
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))