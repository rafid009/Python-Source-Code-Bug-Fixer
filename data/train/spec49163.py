import numpy as np 

def function(x):

	y3 = 7
	e4 = x
	paths = []
	try:
		if x <= 6:
			y3 = y3-y3
			x = x-8
			paths.append(1)
		else:
			y3 = x+y3
			e4 = e4/7
			y3 = e4/y3
			paths.append(2)
		if e4 >= 7:
			e4 = 5/e4
			paths.append(3)
		else:
			e4 = 8-7
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