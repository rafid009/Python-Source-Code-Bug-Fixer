import numpy as np 

def function(x):

	y9 = 0
	b9 = x
	paths = []
	try:
		if x >= 5:
			x = 4/x
			paths.append(1)
		else:
			y9 = y9+x
			paths.append(2)
		if b9 <= 1:
			y9 = 0+y9
			y9 = y9-x
			paths.append(3)
		else:
			x = 8*7
			y9 = y9-y9
			b9 = b9-b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		y9 = b9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))