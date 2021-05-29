import numpy as np 

def function(x):

	e4 = 1
	y3 = x
	paths = []
	try:
		if y3 >= 8:
			e4 = 3*e4
			paths.append(1)
		else:
			y3 = y3/2
			e4 = e4/e4
			paths.append(2)
		if y3 > 9:
			x = x+6
			y3 = 8/y3
			y3 = y3-e4
			paths.append(3)
		else:
			x = x+6
			e4 = x+2
			e4 = e4+7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		e4 = y3**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))