import numpy as np 

def function(x):

	u2 = 1
	x3 = 7
	paths = []
	try:
		if u2 >= 0:
			x = x-u2
			x3 = x*x3
			paths.append(1)
		else:
			x3 = 8*4
			paths.append(2)
		if x > 1:
			x3 = x3-4
			paths.append(3)
		else:
			x = x*4
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