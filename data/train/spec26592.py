import numpy as np 

def function(x):

	x1 = 4
	x0 = x
	paths = []
	try:
		if x >= 9:
			x0 = x0-8
			x0 = x0*x
			paths.append(1)
		else:
			x = 6-x
			x1 = 1*9
			x1 = x0+x
			paths.append(2)
		if x0 >= 3:
			x = x0-x
			x = x*3
			x0 = x1+4
			paths.append(3)
		else:
			x1 = x1*6
			x1 = x1-7
			x = 1/x1
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x1 = x0**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))