import numpy as np 

def function(x):

	y9 = x
	u7 = x
	paths = []
	try:
		if x < 9:
			u7 = u7-7
			paths.append(1)
		else:
			y9 = 3+u7
			paths.append(2)
		if y9 < 0:
			u7 = u7+0
			y9 = y9*2
			paths.append(3)
		else:
			y9 = 2+y9
			y9 = y9+3
			y9 = 9/9
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))