import numpy as np 

def function(x):

	x5 = 9
	k1 = x
	paths = []
	try:
		if x5 < 9:
			k1 = k1-x
			k1 = k1/k1
			paths.append(1)
		else:
			x5 = 7/x
			x5 = 0+x
			x5 = x5-8
			paths.append(2)
		if x <= 0:
			x5 = x5+x5
			paths.append(3)
		else:
			x5 = x5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))