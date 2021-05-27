import numpy as np 

def function(x):

	d7 = x
	y9 = 0
	paths = []
	try:
		if d7 < 8:
			y9 = x*y9
			paths.append(1)
		else:
			y9 = y9-y9
			y9 = y9*1
			y9 = y9-0
			paths.append(2)
		if d7 >= 1:
			x = 6+x
			x = x+9
			paths.append(3)
		else:
			y9 = y9/x
			y9 = 8*4
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