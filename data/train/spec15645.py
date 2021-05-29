import numpy as np 

def function(x):

	k5 = 7
	a3 = 6
	paths = []
	try:
		if x <= 0:
			a3 = a3-6
			a3 = a3-1
			paths.append(1)
		else:
			k5 = k5/a3
			paths.append(2)
		if x < 5:
			a3 = a3-0
			paths.append(3)
		else:
			k5 = k5-1
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