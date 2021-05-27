import numpy as np 

def function(x):

	b8 = x
	y9 = 3
	paths = []
	try:
		if y9 < 9:
			b8 = 8*b8
			x = 0/7
			paths.append(1)
		else:
			b8 = x/3
			x = 2+x
			paths.append(2)
		if b8 >= 0:
			y9 = x-y9
			b8 = b8*y9
			y9 = 7*4
			paths.append(3)
		else:
			x = 6+x
			b8 = 8-b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		y9 = b8**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))