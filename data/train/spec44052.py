import numpy as np 

def function(x):

	q8 = x
	y9 = 5
	paths = []
	try:
		if q8 <= 1:
			q8 = 1*5
			q8 = q8/x
			y9 = y9*4
			paths.append(1)
		else:
			y9 = y9+y9
			x = x/6
			q8 = 8+q8
			paths.append(2)
		if q8 > 3:
			y9 = 1/y9
			q8 = q8*5
			paths.append(3)
		else:
			y9 = y9/2
			y9 = x+q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))