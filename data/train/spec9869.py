import numpy as np 

def function(x):

	g0 = 6
	y9 = x
	paths = []
	try:
		if x <= 2:
			x = g0-x
			paths.append(1)
		else:
			x = x+4
			x = y9/4
			g0 = g0-4
			paths.append(2)
		if x < 5:
			y9 = y9-3
			y9 = x*y9
			g0 = 5/y9
			paths.append(3)
		else:
			x = 9-5
			y9 = y9-9
			g0 = 7*g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		y9 = g0**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))