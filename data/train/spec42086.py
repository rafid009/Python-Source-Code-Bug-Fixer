import numpy as np 

def function(x):

	n8 = 6
	y6 = x
	paths = []
	try:
		if n8 < 0:
			y6 = y6-4
			y6 = 3+y6
			x = 1+7
			paths.append(1)
		else:
			x = 3*y6
			x = x/n8
			y6 = y6*5
			paths.append(2)
		if x <= 0:
			y6 = 3*y6
			x = x/6
			paths.append(3)
		else:
			n8 = 4/y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))