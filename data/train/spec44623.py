import numpy as np 

def function(x):

	x9 = 9
	y4 = x
	paths = []
	try:
		if x > 7:
			y4 = y4/1
			x = x-1
			x9 = x9-x9
			paths.append(1)
		else:
			x = 0/1
			x = x+4
			paths.append(2)
		if y4 <= 6:
			x9 = x-x9
			y4 = 3+y4
			x = 1-x
			paths.append(3)
		else:
			x9 = y4*9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))