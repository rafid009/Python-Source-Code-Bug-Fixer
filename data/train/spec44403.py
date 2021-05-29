import numpy as np 

def function(x):

	y9 = x
	g8 = 6
	paths = []
	try:
		if g8 > 5:
			g8 = 7+g8
			x = y9*x
			paths.append(1)
		else:
			x = x/8
			g8 = x-g8
			paths.append(2)
		if x >= 4:
			x = x-5
			g8 = g8*g8
			x = x/7
			paths.append(3)
		else:
			g8 = g8/4
			x = x+y9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))