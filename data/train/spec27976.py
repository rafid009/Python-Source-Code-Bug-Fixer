import numpy as np 

def function(x):

	u7 = 1
	y9 = 0
	paths = []
	try:
		if x >= 5:
			y9 = 2+y9
			paths.append(1)
		else:
			y9 = 2/7
			y9 = y9-8
			u7 = 8+u7
			paths.append(2)
		if u7 > 3:
			x = 0/x
			u7 = u7*3
			x = y9-6
			paths.append(3)
		else:
			y9 = 9+0
			y9 = u7+8
			u7 = y9*6
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		u7 = y9**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))