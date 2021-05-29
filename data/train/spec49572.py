import numpy as np 

def function(x):

	z3 = 3
	y9 = x
	paths = []
	try:
		if x < 8:
			z3 = z3/1
			x = 3/x
			z3 = x*6
			paths.append(1)
		else:
			x = 7-x
			y9 = y9*1
			y9 = 8*y9
			paths.append(2)
		if y9 <= 6:
			x = z3/x
			paths.append(3)
		else:
			z3 = y9*3
			x = z3/4
			x = 9/x
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