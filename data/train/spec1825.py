import numpy as np 

def function(x):

	y7 = x
	e8 = 2
	paths = []
	try:
		if y7 <= 1:
			e8 = e8-9
			paths.append(1)
		else:
			e8 = e8+8
			y7 = y7-7
			paths.append(2)
		if y7 < 0:
			e8 = e8/7
			y7 = y7/x
			paths.append(3)
		else:
			e8 = x+1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))