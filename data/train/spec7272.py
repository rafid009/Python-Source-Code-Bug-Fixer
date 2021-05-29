import numpy as np 

def function(x):

	y7 = x
	e5 = 8
	paths = []
	try:
		if y7 >= 9:
			y7 = x*y7
			y7 = x+6
			paths.append(1)
		else:
			y7 = y7*7
			x = x+8
			e5 = e5-2
			paths.append(2)
		if x < 2:
			e5 = 9+3
			paths.append(3)
		else:
			y7 = y7*9
			y7 = y7-y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))