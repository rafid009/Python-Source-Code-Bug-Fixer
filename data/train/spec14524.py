import numpy as np 

def function(x):

	y9 = x
	b6 = 4
	paths = []
	try:
		if y9 > 7:
			b6 = x*y9
			paths.append(1)
		else:
			b6 = b6-8
			paths.append(2)
		if b6 <= 7:
			x = 3*3
			x = x+x
			y9 = 7-y9
			paths.append(3)
		else:
			x = y9-2
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		y9 = b6**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))