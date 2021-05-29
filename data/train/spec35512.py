import numpy as np 

def function(x):

	x0 = 6
	i2 = 7
	paths = []
	try:
		if x0 > 0:
			x0 = x0-x0
			x0 = x0/x
			i2 = i2-3
			paths.append(1)
		else:
			x = i2-5
			paths.append(2)
		if x <= 5:
			i2 = i2/3
			paths.append(3)
		else:
			x0 = 2-x0
			i2 = i2*x
			x0 = x0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))