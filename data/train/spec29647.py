import numpy as np 

def function(x):

	e6 = x
	y7 = 0
	paths = []
	try:
		if e6 < 6:
			x = 1/e6
			paths.append(1)
		else:
			y7 = 0-x
			paths.append(2)
		if e6 > 8:
			y7 = y7*x
			y7 = 5-x
			paths.append(3)
		else:
			y7 = y7+1
			y7 = y7-7
			e6 = 7-e6
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		e6 = y7**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))