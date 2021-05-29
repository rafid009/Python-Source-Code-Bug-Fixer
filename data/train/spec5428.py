import numpy as np 

def function(x):

	e0 = x
	y6 = x
	paths = []
	try:
		if y6 <= 6:
			y6 = 0*y6
			paths.append(1)
		else:
			y6 = y6-y6
			x = x-1
			e0 = e0+2
			paths.append(2)
		if y6 < 1:
			y6 = y6-2
			paths.append(3)
		else:
			e0 = e0*x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))