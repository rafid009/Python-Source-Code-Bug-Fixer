import numpy as np 

def function(x):

	u7 = 0
	x4 = 4
	paths = []
	try:
		if x < 0:
			x4 = 6/x
			x4 = x4-u7
			u7 = 1*x
			paths.append(1)
		else:
			x4 = 7-x4
			paths.append(2)
		if x >= 7:
			u7 = 5+u7
			paths.append(3)
		else:
			x = u7/7
			x = x-3
			x4 = 9*x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))