import numpy as np 

def function(x):

	y7 = 2
	a8 = x
	paths = []
	try:
		if x >= 7:
			y7 = 8/6
			paths.append(1)
		else:
			a8 = a8/3
			y7 = 7-y7
			y7 = a8-0
			paths.append(2)
		if x <= 0:
			a8 = a8+1
			x = 9+7
			paths.append(3)
		else:
			y7 = 0+7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		y7 = a8**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))