import numpy as np 

def function(x):

	g8 = x
	y9 = x
	paths = []
	try:
		if y9 > 3:
			y9 = g8/5
			x = x/1
			y9 = x/y9
			paths.append(1)
		else:
			g8 = g8+9
			g8 = g8/x
			paths.append(2)
		if x < 7:
			y9 = y9-4
			y9 = 6-y9
			g8 = g8+2
			paths.append(3)
		else:
			y9 = 3+y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))