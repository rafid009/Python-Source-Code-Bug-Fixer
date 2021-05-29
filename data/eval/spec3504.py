import numpy as np 

def function(x):

	v2 = 7
	y9 = x
	paths = []
	try:
		if v2 > 8:
			v2 = x*v2
			v2 = v2-v2
			paths.append(1)
		else:
			y9 = y9+9
			y9 = y9-v2
			v2 = 2+2
			paths.append(2)
		if v2 < 9:
			x = 9+x
			v2 = 6*v2
			paths.append(3)
		else:
			v2 = v2+x
			y9 = y9+4
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		v2 = y9**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))