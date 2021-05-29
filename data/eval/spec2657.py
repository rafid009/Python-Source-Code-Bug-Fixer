import numpy as np 

def function(x):

	k5 = 3
	k1 = 7
	paths = []
	try:
		if x <= 0:
			x = x-4
			k5 = k5*x
			k1 = 9/k5
			paths.append(1)
		else:
			k5 = x*k5
			k5 = k1/k5
			k1 = 3/k1
			paths.append(2)
		if k1 < 8:
			x = x*7
			paths.append(3)
		else:
			x = 5*k1
			x = k5/3
			k1 = k1-k1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))