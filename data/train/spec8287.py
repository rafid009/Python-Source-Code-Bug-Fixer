import numpy as np 

def function(x):

	y9 = 9
	b2 = x
	x = 0
	paths = []
	try:
		if x >= 8:
			y9 = y9-4
			paths.append(1)
		else:
			x = 4-b2
			y9 = y9+8
			paths.append(2)
		if b2 < 5:
			y9 = 4+1
			paths.append(3)
		else:
			x = x-x
			b2 = 3+b2
			b2 = 2+b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))