import numpy as np 

def function(x):

	u1 = x
	n0 = x
	paths = []
	try:
		if u1 <= 6:
			n0 = n0-x
			x = x-6
			n0 = n0*7
			paths.append(1)
		else:
			n0 = n0-4
			paths.append(2)
		if x > 7:
			n0 = 0-0
			x = 9-x
			x = x*5
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))