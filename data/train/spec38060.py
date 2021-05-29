import numpy as np 

def function(x):

	y5 = 7
	y9 = 4
	paths = []
	try:
		if y9 > 6:
			x = x+x
			y9 = x/y9
			y5 = 5+y5
			paths.append(1)
		else:
			y9 = y9-7
			y9 = y9/9
			paths.append(2)
		if y5 >= 3:
			y9 = y9*9
			paths.append(3)
		else:
			y5 = 5+y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))