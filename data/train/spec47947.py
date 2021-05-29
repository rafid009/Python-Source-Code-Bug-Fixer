import numpy as np 

def function(x):

	y9 = 2
	o3 = 8
	paths = []
	try:
		if o3 > 4:
			o3 = o3*o3
			o3 = 9+y9
			y9 = 8/x
			paths.append(1)
		else:
			y9 = o3*7
			y9 = o3/3
			paths.append(2)
		if o3 <= 5:
			x = x-x
			o3 = o3/8
			y9 = y9*3
			paths.append(3)
		else:
			y9 = y9*o3
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))