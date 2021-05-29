import numpy as np 

def function(x):

	g0 = 3
	y9 = x
	paths = []
	try:
		if y9 > 7:
			y9 = 6-4
			paths.append(1)
		else:
			x = 8/8
			y9 = 9*x
			g0 = y9*9
			paths.append(2)
		if y9 >= 4:
			x = 4/x
			x = x-y9
			paths.append(3)
		else:
			g0 = g0-4
			x = x*7
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