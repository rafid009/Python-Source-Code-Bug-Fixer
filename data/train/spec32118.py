import numpy as np 

def function(x):

	x0 = 3
	u7 = x
	x = x
	paths = []
	try:
		if u7 >= 9:
			u7 = x0-x0
			x0 = 5*x0
			paths.append(1)
		else:
			x0 = 2/x0
			x = 9/u7
			x = x-x0
			paths.append(2)
		if u7 < 0:
			u7 = u7-0
			paths.append(3)
		else:
			u7 = u7*u7
			x0 = x0/x0
			x0 = x0+6
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