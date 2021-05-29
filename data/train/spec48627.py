import numpy as np 

def function(x):

	x0 = x
	y7 = 3
	paths = []
	try:
		if x > 1:
			x = y7*8
			y7 = y7+0
			y7 = y7/4
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if y7 < 7:
			x0 = 3-3
			paths.append(3)
		else:
			x = 7-4
			x0 = x0*5
			x = x0-9
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