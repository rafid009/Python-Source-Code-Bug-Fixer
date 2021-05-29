import numpy as np 

def function(x):

	y9 = x
	v2 = x
	paths = []
	try:
		if x <= 0:
			y9 = y9/8
			x = 9-x
			paths.append(1)
		else:
			x = x/y9
			paths.append(2)
		if x > 0:
			v2 = 5-v2
			y9 = y9-6
			y9 = y9/v2
			paths.append(3)
		else:
			x = x+7
			x = x-x
			v2 = 8-v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))