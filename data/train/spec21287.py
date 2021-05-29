import numpy as np 

def function(x):

	e7 = x
	o8 = x
	x = 6
	paths = []
	try:
		if x > 9:
			o8 = 7/o8
			o8 = o8-3
			o8 = o8+4
			paths.append(1)
		else:
			x = 2-x
			x = 4*5
			o8 = o8/1
			paths.append(2)
		if x <= 1:
			e7 = e7*7
			e7 = e7-x
			paths.append(3)
		else:
			e7 = 2/e7
			e7 = 1+o8
			e7 = 2-e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))