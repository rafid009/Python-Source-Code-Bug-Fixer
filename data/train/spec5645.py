import numpy as np 

def function(x):

	e7 = 2
	y8 = x
	x = x
	paths = []
	try:
		if y8 < 0:
			x = 3-7
			y8 = y8+e7
			paths.append(1)
		else:
			e7 = y8/2
			x = 8*x
			e7 = 5*e7
			paths.append(2)
		if x >= 3:
			x = x+2
			y8 = 4/8
			e7 = e7-2
			paths.append(3)
		else:
			x = 3-9
			e7 = 4/e7
			y8 = y8+7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))