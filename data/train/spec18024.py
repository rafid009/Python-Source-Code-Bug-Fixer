import numpy as np 

def function(x):

	y9 = 4
	n5 = x
	paths = []
	try:
		if y9 < 3:
			x = x/5
			y9 = y9/x
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if y9 > 7:
			n5 = n5*1
			paths.append(3)
		else:
			y9 = 5/y9
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