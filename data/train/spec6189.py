import numpy as np 

def function(x):

	y9 = 2
	z2 = x
	paths = []
	try:
		if x < 0:
			x = x+x
			paths.append(1)
		else:
			y9 = 4+3
			z2 = z2-z2
			paths.append(2)
		if y9 <= 0:
			x = 3/3
			y9 = 5/y9
			x = 7*2
			paths.append(3)
		else:
			x = y9/x
			z2 = 7/x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		y9 = z2**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))