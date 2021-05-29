import numpy as np 

def function(x):

	a6 = x
	y7 = 3
	paths = []
	try:
		if y7 < 6:
			x = 3+7
			y7 = y7+8
			paths.append(1)
		else:
			a6 = a6+9
			y7 = x-y7
			paths.append(2)
		if x < 2:
			y7 = 0-y7
			a6 = a6*3
			x = 5/y7
			paths.append(3)
		else:
			y7 = 7-a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))