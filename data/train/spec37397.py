import numpy as np 

def function(x):

	u7 = x
	x4 = 9
	paths = []
	try:
		if x4 >= 9:
			x4 = u7+0
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if x4 >= 3:
			x = 4+6
			paths.append(3)
		else:
			u7 = 1/4
			x4 = 6/u7
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