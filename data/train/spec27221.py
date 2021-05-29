import numpy as np 

def function(x):

	y7 = 1
	a4 = x
	paths = []
	try:
		if y7 < 6:
			x = x*y7
			paths.append(1)
		else:
			y7 = y7/y7
			a4 = 3-a4
			a4 = 9+a4
			paths.append(2)
		if a4 > 4:
			a4 = 4-a4
			a4 = 3*x
			paths.append(3)
		else:
			y7 = 0-x
			a4 = a4+y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		a4 = y7**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))