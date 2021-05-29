import numpy as np 

def function(x):

	k3 = x
	y9 = x
	paths = []
	try:
		if k3 <= 1:
			y9 = k3-x
			y9 = y9/9
			y9 = y9*3
			paths.append(1)
		else:
			k3 = 2-2
			y9 = y9-5
			paths.append(2)
		if y9 >= 4:
			y9 = 7+y9
			paths.append(3)
		else:
			x = 2+x
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