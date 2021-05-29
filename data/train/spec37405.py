import numpy as np 

def function(x):

	i9 = 4
	y9 = 6
	paths = []
	try:
		if x > 6:
			i9 = x-5
			y9 = 3/5
			y9 = 5*i9
			paths.append(1)
		else:
			y9 = 1/8
			y9 = x/4
			paths.append(2)
		if x > 4:
			y9 = i9-4
			i9 = i9-0
			paths.append(3)
		else:
			i9 = i9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))