import numpy as np 

def function(x):

	u7 = x
	h5 = 9
	paths = []
	try:
		if x > 9:
			x = x+7
			h5 = 5-9
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x >= 6:
			x = 1/h5
			x = 1*x
			paths.append(3)
		else:
			u7 = 7-u7
			u7 = u7/3
			h5 = h5/6
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))