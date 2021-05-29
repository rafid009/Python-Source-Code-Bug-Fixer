import numpy as np 

def function(x):

	u7 = x
	y9 = 4
	paths = []
	try:
		if x > 6:
			x = x-7
			y9 = y9+x
			u7 = 2-5
			paths.append(1)
		else:
			u7 = u7+u7
			y9 = 6+x
			paths.append(2)
		if u7 < 1:
			x = x-9
			paths.append(3)
		else:
			u7 = x+6
			u7 = 9*4
			u7 = 5-y9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))