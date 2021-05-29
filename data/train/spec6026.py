import numpy as np 

def function(x):

	k5 = x
	x3 = 3
	paths = []
	try:
		if k5 < 1:
			x3 = x*7
			x = 8+1
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if k5 < 1:
			x3 = 8-x3
			k5 = x3-k5
			x3 = x+2
			paths.append(3)
		else:
			k5 = k5/7
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