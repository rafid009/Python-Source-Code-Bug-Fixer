import numpy as np 

def function(x):

	k8 = 4
	y9 = x
	paths = []
	try:
		if k8 < 9:
			x = 5+y9
			paths.append(1)
		else:
			y9 = k8-9
			y9 = y9*1
			k8 = k8/5
			paths.append(2)
		if k8 >= 1:
			k8 = 7/k8
			paths.append(3)
		else:
			y9 = y9*5
			k8 = k8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))