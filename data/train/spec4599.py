import numpy as np 

def function(x):

	y7 = 3
	a7 = x
	paths = []
	try:
		if x >= 3:
			y7 = y7/6
			a7 = a7/a7
			y7 = y7/x
			paths.append(1)
		else:
			a7 = 1/x
			x = x-1
			a7 = a7-9
			paths.append(2)
		if x <= 1:
			y7 = 5+y7
			a7 = a7+6
			y7 = 0*1
			paths.append(3)
		else:
			y7 = y7-1
			y7 = 3*x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		y7 = a7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))