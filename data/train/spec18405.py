import numpy as np 

def function(x):

	y6 = x
	q4 = x
	x = x
	paths = []
	try:
		if x > 2:
			q4 = 1/x
			paths.append(1)
		else:
			q4 = q4-6
			paths.append(2)
		if q4 > 5:
			x = x-5
			paths.append(3)
		else:
			x = x+7
			q4 = q4-x
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