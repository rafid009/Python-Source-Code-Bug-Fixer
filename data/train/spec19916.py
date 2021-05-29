import numpy as np 

def function(x):

	k5 = 7
	d4 = 3
	paths = []
	try:
		if x > 6:
			d4 = k5*5
			d4 = 6-d4
			x = 4-x
			paths.append(1)
		else:
			k5 = 3-9
			paths.append(2)
		if k5 < 8:
			k5 = 5/k5
			k5 = k5*x
			k5 = k5-k5
			paths.append(3)
		else:
			x = 4*x
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