import numpy as np 

def function(x):

	y8 = x
	y9 = x
	paths = []
	try:
		if y9 >= 4:
			y9 = y8-9
			x = x*3
			x = x*9
			paths.append(1)
		else:
			x = x/8
			x = 4-x
			paths.append(2)
		if y8 < 3:
			y8 = 1+y8
			y8 = y9+y8
			y9 = 8-3
			paths.append(3)
		else:
			x = y8/3
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y8 = y9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))