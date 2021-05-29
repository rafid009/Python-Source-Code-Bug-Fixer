import numpy as np 

def function(x):

	k7 = x
	y9 = 6
	paths = []
	try:
		if y9 >= 5:
			x = 9/x
			y9 = 5/y9
			paths.append(1)
		else:
			k7 = 6+1
			y9 = y9-2
			y9 = k7*k7
			paths.append(2)
		if y9 >= 8:
			k7 = k7/k7
			x = x/1
			paths.append(3)
		else:
			k7 = k7-6
			k7 = k7*8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))