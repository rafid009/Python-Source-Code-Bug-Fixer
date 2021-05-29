import numpy as np 

def function(x):

	g1 = x
	y9 = 9
	paths = []
	try:
		if y9 < 9:
			y9 = x-y9
			paths.append(1)
		else:
			x = y9/3
			x = 4/y9
			paths.append(2)
		if g1 < 3:
			y9 = y9-6
			g1 = 4+g1
			x = 4/x
			paths.append(3)
		else:
			x = g1-x
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