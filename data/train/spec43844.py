import numpy as np 

def function(x):

	y7 = x
	x9 = x
	x = x
	paths = []
	try:
		if x9 <= 5:
			x = x/8
			paths.append(1)
		else:
			x = x*x9
			y7 = 3/y7
			x = x-1
			paths.append(2)
		if x9 <= 4:
			x9 = 0-x9
			paths.append(3)
		else:
			x9 = 4+7
			x = 7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))