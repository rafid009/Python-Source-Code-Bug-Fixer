import numpy as np 

def function(x):

	y7 = 1
	y8 = 0
	paths = []
	try:
		if y8 >= 3:
			y8 = y8*0
			y7 = 9-y7
			paths.append(1)
		else:
			y7 = 7*y7
			y8 = y8*y7
			y8 = 0/6
			paths.append(2)
		if y7 >= 0:
			y8 = 1-y7
			y7 = y7/y8
			paths.append(3)
		else:
			y7 = y7+y7
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))