import numpy as np 

def function(x):

	d4 = 0
	k5 = 5
	paths = []
	try:
		if x > 4:
			k5 = 3-5
			paths.append(1)
		else:
			k5 = 4*3
			x = 9*3
			k5 = 7-k5
			paths.append(2)
		if k5 >= 0:
			d4 = d4-x
			d4 = d4*x
			paths.append(3)
		else:
			x = d4-x
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