import numpy as np 

def function(x):

	x1 = x
	y9 = 4
	paths = []
	try:
		if y9 <= 8:
			x = x/8
			paths.append(1)
		else:
			y9 = y9*2
			x1 = y9/2
			y9 = 6/4
			paths.append(2)
		if x1 <= 3:
			y9 = 7-x
			paths.append(3)
		else:
			x1 = 2-x1
			x1 = 7+0
			y9 = y9+1
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))