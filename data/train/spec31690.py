import numpy as np 

def function(x):

	y6 = x
	e9 = x
	paths = []
	try:
		if x >= 9:
			e9 = 0/e9
			y6 = 4*y6
			x = x*3
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if e9 < 6:
			y6 = y6+8
			paths.append(3)
		else:
			y6 = y6+4
			y6 = y6*e9
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