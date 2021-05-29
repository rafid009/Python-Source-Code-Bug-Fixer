import numpy as np 

def function(x):

	y9 = 0
	q6 = 6
	paths = []
	try:
		if y9 <= 0:
			y9 = 4+x
			y9 = 3*y9
			q6 = 3*y9
			paths.append(1)
		else:
			x = x*9
			q6 = q6/9
			paths.append(2)
		if q6 <= 1:
			q6 = q6-y9
			y9 = y9/y9
			x = x/y9
			paths.append(3)
		else:
			y9 = 5+y9
			x = 0-5
			q6 = x+q6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))