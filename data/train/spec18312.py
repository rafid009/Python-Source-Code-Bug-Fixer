import numpy as np 

def function(x):

	y9 = 5
	r1 = 5
	paths = []
	try:
		if x >= 9:
			x = x-5
			y9 = 7*y9
			x = x/7
			paths.append(1)
		else:
			y9 = 4-y9
			paths.append(2)
		if y9 >= 8:
			r1 = r1*y9
			r1 = r1+8
			y9 = y9*8
			paths.append(3)
		else:
			x = 3+x
			y9 = y9-y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))