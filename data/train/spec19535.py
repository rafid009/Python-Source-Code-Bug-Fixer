import numpy as np 

def function(x):

	y9 = x
	g5 = x
	paths = []
	try:
		if y9 < 2:
			x = 0-x
			x = x*4
			y9 = y9+9
			paths.append(1)
		else:
			x = g5+4
			y9 = 4-y9
			paths.append(2)
		if g5 < 5:
			x = x-g5
			x = x/6
			paths.append(3)
		else:
			y9 = y9/3
			g5 = g5*7
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		g5 = y9**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))