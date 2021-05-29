import numpy as np 

def function(x):

	y8 = 8
	e6 = 6
	paths = []
	try:
		if x > 7:
			e6 = 1-5
			paths.append(1)
		else:
			e6 = e6+9
			y8 = y8-4
			e6 = e6*5
			paths.append(2)
		if e6 > 4:
			e6 = y8*x
			y8 = y8+y8
			e6 = 7-0
			paths.append(3)
		else:
			y8 = 3-x
			e6 = e6+e6
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