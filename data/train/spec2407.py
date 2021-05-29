import numpy as np 

def function(x):

	y9 = 0
	x8 = 0
	paths = []
	try:
		if y9 < 5:
			x8 = x8+x
			paths.append(1)
		else:
			x8 = 3+9
			x8 = x8*3
			paths.append(2)
		if x8 >= 9:
			y9 = y9-y9
			paths.append(3)
		else:
			y9 = x8+y9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x8 = y9**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))