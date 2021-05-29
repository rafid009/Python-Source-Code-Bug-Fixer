import numpy as np 

def function(x):

	n3 = x
	y9 = 5
	paths = []
	try:
		if x <= 6:
			y9 = 4+9
			y9 = 6+6
			paths.append(1)
		else:
			y9 = y9-2
			paths.append(2)
		if n3 > 8:
			n3 = 8*4
			n3 = n3-9
			y9 = 2*y9
			paths.append(3)
		else:
			y9 = 4+n3
			x = x*x
			x = 9*y9
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))