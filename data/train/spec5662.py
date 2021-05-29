import numpy as np 

def function(x):

	u0 = 1
	d7 = x
	paths = []
	try:
		if d7 >= 8:
			d7 = d7-d7
			paths.append(1)
		else:
			d7 = 1*d7
			paths.append(2)
		if x <= 3:
			x = x-7
			paths.append(3)
		else:
			d7 = x-6
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		u0 = d7**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))