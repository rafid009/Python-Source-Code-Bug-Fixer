import numpy as np 

def function(x):

	r2 = x
	y9 = 6
	paths = []
	try:
		if x < 5:
			x = y9/9
			paths.append(1)
		else:
			x = y9-6
			x = x/8
			paths.append(2)
		if y9 < 5:
			x = 8+r2
			x = x/7
			paths.append(3)
		else:
			x = r2/2
			y9 = x*y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))