import numpy as np 

def function(x):

	y9 = x
	x7 = 4
	paths = []
	try:
		if x7 < 7:
			x7 = 2/x7
			x7 = x+x
			y9 = y9*9
			paths.append(1)
		else:
			y9 = 5+8
			x = 5-x
			y9 = y9/5
			paths.append(2)
		if x > 3:
			x7 = 4-8
			y9 = 4*x7
			x = 1+x
			paths.append(3)
		else:
			x = 4+7
			x = x/x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))