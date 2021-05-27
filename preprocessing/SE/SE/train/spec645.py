import numpy as np 

def function(x):

	y9 = x
	k8 = 2
	paths = []
	try:
		if x <= 5:
			x = 0+x
			y9 = y9+5
			paths.append(1)
		else:
			y9 = y9+4
			paths.append(2)
		if x < 2:
			x = 2/1
			k8 = k8-4
			k8 = k8+y9
			paths.append(3)
		else:
			y9 = y9-9
			y9 = y9/1
			k8 = x*x
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