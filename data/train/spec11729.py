import numpy as np 

def function(x):

	y9 = x
	g4 = 3
	x = 0
	paths = []
	try:
		if y9 < 7:
			x = 7*x
			paths.append(1)
		else:
			g4 = g4-0
			y9 = 6/1
			g4 = g4/y9
			paths.append(2)
		if x < 8:
			x = 0*y9
			x = x+y9
			g4 = g4*4
			paths.append(3)
		else:
			x = 1-x
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