import numpy as np 

def function(x):

	n4 = 3
	y7 = 7
	paths = []
	try:
		if x <= 2:
			x = y7*5
			n4 = y7*n4
			paths.append(1)
		else:
			y7 = n4-x
			y7 = 4/y7
			paths.append(2)
		if y7 < 2:
			y7 = n4/y7
			y7 = 2-y7
			x = 5-2
			paths.append(3)
		else:
			n4 = 9/y7
			x = 9-x
			y7 = y7*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))