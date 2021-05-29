import numpy as np 

def function(x):

	z0 = x
	j8 = 3
	paths = []
	try:
		if z0 > 5:
			j8 = j8*7
			x = x-0
			paths.append(1)
		else:
			x = x/5
			j8 = j8/j8
			paths.append(2)
		if x < 2:
			x = x*5
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))