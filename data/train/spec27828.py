import numpy as np 

def function(x):

	y9 = 4
	h6 = x
	paths = []
	try:
		if x <= 2:
			x = 7+0
			paths.append(1)
		else:
			y9 = 9+y9
			x = x+h6
			x = 0/3
			paths.append(2)
		if x > 0:
			y9 = y9+0
			x = x+3
			paths.append(3)
		else:
			x = 9+4
			h6 = h6*y9
			x = 8/9
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		y9 = h6**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))