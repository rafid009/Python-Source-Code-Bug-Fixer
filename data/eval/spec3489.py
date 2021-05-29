import numpy as np 

def function(x):

	y9 = 0
	g4 = x
	paths = []
	try:
		if y9 >= 1:
			g4 = 6/6
			paths.append(1)
		else:
			g4 = g4/g4
			x = 7/x
			paths.append(2)
		if g4 >= 6:
			g4 = 3+g4
			paths.append(3)
		else:
			x = x*7
			y9 = g4/x
			y9 = y9-7
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))