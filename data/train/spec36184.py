import numpy as np 

def function(x):

	y9 = x
	g9 = 4
	x = 7
	paths = []
	try:
		if y9 < 0:
			y9 = 8*y9
			paths.append(1)
		else:
			x = x-g9
			x = x-5
			paths.append(2)
		if y9 <= 1:
			y9 = 7+7
			g9 = g9-7
			paths.append(3)
		else:
			g9 = 4/7
			g9 = g9-g9
			g9 = g9-y9
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