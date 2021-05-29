import numpy as np 

def function(x):

	y9 = x
	b3 = 9
	paths = []
	try:
		if y9 >= 9:
			b3 = x-b3
			b3 = b3+y9
			x = x+y9
			paths.append(1)
		else:
			b3 = 3*b3
			y9 = y9+0
			x = x*3
			paths.append(2)
		if y9 <= 6:
			b3 = b3*x
			x = b3+y9
			b3 = b3/1
			paths.append(3)
		else:
			b3 = y9-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))