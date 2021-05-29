import numpy as np 

def function(x):

	y9 = 7
	v3 = 4
	paths = []
	try:
		if x <= 6:
			v3 = v3/v3
			v3 = 5+0
			paths.append(1)
		else:
			y9 = y9/1
			v3 = y9-4
			paths.append(2)
		if v3 >= 5:
			v3 = y9-5
			paths.append(3)
		else:
			y9 = 6-y9
			v3 = 7-8
			v3 = 5*v3
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