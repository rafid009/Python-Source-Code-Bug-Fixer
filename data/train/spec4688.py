import numpy as np 

def function(x):

	i0 = 2
	y9 = 0
	paths = []
	try:
		if i0 > 8:
			x = x+2
			y9 = 1-9
			i0 = 6*i0
			paths.append(1)
		else:
			y9 = x-y9
			paths.append(2)
		if y9 <= 7:
			i0 = 8-9
			i0 = 6+i0
			paths.append(3)
		else:
			y9 = y9-5
			x = i0+x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		i0 = y9**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))