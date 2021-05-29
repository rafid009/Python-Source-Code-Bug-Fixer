import numpy as np 

def function(x):

	g2 = x
	y9 = 3
	paths = []
	try:
		if g2 < 9:
			g2 = 3/g2
			g2 = g2*g2
			g2 = g2*x
			paths.append(1)
		else:
			y9 = 6/g2
			paths.append(2)
		if x >= 1:
			y9 = y9-1
			y9 = y9/1
			paths.append(3)
		else:
			x = y9+5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		y9 = g2**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))