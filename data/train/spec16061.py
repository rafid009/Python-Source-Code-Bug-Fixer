import numpy as np 

def function(x):

	y7 = 4
	e6 = x
	paths = []
	try:
		if e6 > 9:
			e6 = 4-2
			paths.append(1)
		else:
			e6 = e6*5
			paths.append(2)
		if x < 5:
			y7 = y7/4
			x = 8*x
			paths.append(3)
		else:
			y7 = 4-y7
			y7 = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))