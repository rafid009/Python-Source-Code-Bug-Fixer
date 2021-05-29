import numpy as np 

def function(x):

	y9 = 6
	q3 = 0
	paths = []
	try:
		if y9 > 2:
			x = x+2
			q3 = q3-3
			paths.append(1)
		else:
			q3 = 0*q3
			x = x-1
			paths.append(2)
		if y9 <= 4:
			y9 = y9*6
			y9 = 6*2
			paths.append(3)
		else:
			x = x+0
			y9 = y9+y9
			y9 = 9-y9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		y9 = q3**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))