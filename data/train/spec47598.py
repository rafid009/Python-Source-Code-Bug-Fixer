import numpy as np 

def function(x):

	n9 = 6
	y9 = x
	paths = []
	try:
		if n9 > 8:
			x = x-6
			y9 = y9+3
			paths.append(1)
		else:
			x = 7*x
			x = n9/x
			x = x/8
			paths.append(2)
		if n9 < 5:
			y9 = y9/5
			paths.append(3)
		else:
			n9 = 2-x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))