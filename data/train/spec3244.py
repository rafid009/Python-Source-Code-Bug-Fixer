import numpy as np 

def function(x):

	e4 = x
	y6 = 8
	paths = []
	try:
		if e4 >= 9:
			y6 = y6*y6
			y6 = y6*3
			paths.append(1)
		else:
			y6 = 0/y6
			paths.append(2)
		if e4 <= 7:
			e4 = x-3
			e4 = x/8
			x = e4/8
			paths.append(3)
		else:
			e4 = x*e4
			e4 = 5/x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))