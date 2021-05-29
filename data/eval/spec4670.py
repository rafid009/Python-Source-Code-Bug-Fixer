import numpy as np 

def function(x):

	x9 = x
	x2 = x
	paths = []
	try:
		if x < 9:
			x = x+8
			paths.append(1)
		else:
			x = 8-x9
			paths.append(2)
		if x2 < 9:
			x2 = x9/6
			paths.append(3)
		else:
			x9 = 7-x9
			x2 = x9-4
			x9 = x9*9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))