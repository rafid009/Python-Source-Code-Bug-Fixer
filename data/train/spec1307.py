import numpy as np 

def function(x):

	x0 = x
	y5 = 9
	paths = []
	try:
		if y5 >= 8:
			x = x+x
			y5 = 3*x
			x0 = x0/8
			paths.append(1)
		else:
			x = x/y5
			y5 = 7*y5
			paths.append(2)
		if y5 >= 2:
			x0 = x0-6
			x = x-y5
			paths.append(3)
		else:
			x = 6*x
			x0 = x0/1
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))