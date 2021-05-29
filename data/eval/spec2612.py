import numpy as np 

def function(x):

	y6 = 6
	k1 = 3
	paths = []
	try:
		if x < 2:
			k1 = 0-1
			k1 = k1-5
			k1 = 4/k1
			paths.append(1)
		else:
			k1 = y6-k1
			k1 = 5-k1
			paths.append(2)
		if k1 <= 9:
			y6 = 4/y6
			y6 = 6/k1
			paths.append(3)
		else:
			k1 = 9+k1
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