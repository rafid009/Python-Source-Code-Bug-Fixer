import numpy as np 

def function(x):

	x6 = 3
	x1 = x
	paths = []
	try:
		if x > 8:
			x6 = 8/5
			x6 = 3-x6
			x = x/8
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x6 >= 0:
			x6 = x6-x1
			x6 = 6*3
			paths.append(3)
		else:
			x = x1/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))