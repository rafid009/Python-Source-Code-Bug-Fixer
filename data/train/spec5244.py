import numpy as np 

def function(x):

	n8 = 2
	u1 = 6
	x = x
	paths = []
	try:
		if x >= 6:
			x = u1*n8
			x = u1*7
			u1 = u1-2
			paths.append(1)
		else:
			u1 = x*u1
			u1 = 1/u1
			n8 = 4/n8
			paths.append(2)
		if x < 7:
			x = 1/u1
			paths.append(3)
		else:
			x = 0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))