import numpy as np 

def function(x):

	y7 = x
	e3 = 4
	paths = []
	try:
		if e3 >= 9:
			e3 = 2*e3
			paths.append(1)
		else:
			x = 1/y7
			paths.append(2)
		if x >= 4:
			y7 = 5-y7
			e3 = 6*4
			paths.append(3)
		else:
			y7 = y7+0
			y7 = y7-1
			x = 7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))