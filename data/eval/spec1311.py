import numpy as np 

def function(x):

	y9 = x
	u7 = x
	paths = []
	try:
		if y9 > 7:
			x = x/7
			y9 = y9*1
			paths.append(1)
		else:
			x = 9/x
			u7 = 7-4
			y9 = 3-0
			paths.append(2)
		if x >= 6:
			y9 = 4-y9
			paths.append(3)
		else:
			y9 = y9*0
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