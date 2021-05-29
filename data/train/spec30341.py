import numpy as np 

def function(x):

	k1 = 5
	n6 = 3
	paths = []
	try:
		if x >= 5:
			x = x/x
			n6 = n6-n6
			paths.append(1)
		else:
			k1 = k1-k1
			n6 = n6/4
			paths.append(2)
		if x <= 3:
			n6 = n6-n6
			k1 = 8*6
			paths.append(3)
		else:
			n6 = n6*4
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