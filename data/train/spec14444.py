import numpy as np 

def function(x):

	q9 = x
	k2 = 3
	paths = []
	try:
		if x > 1:
			q9 = 6-9
			k2 = k2/k2
			x = 3*q9
			paths.append(1)
		else:
			k2 = 5+2
			paths.append(2)
		if x < 6:
			q9 = 3-k2
			k2 = k2/k2
			k2 = 3/x
			paths.append(3)
		else:
			q9 = 6*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))