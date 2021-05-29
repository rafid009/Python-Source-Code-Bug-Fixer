import numpy as np 

def function(x):

	y7 = x
	f1 = 9
	paths = []
	try:
		if x > 7:
			y7 = y7-f1
			paths.append(1)
		else:
			f1 = 4*f1
			paths.append(2)
		if x <= 5:
			y7 = x/x
			y7 = y7*3
			paths.append(3)
		else:
			y7 = y7/9
			y7 = 0-f1
			f1 = 5/f1
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