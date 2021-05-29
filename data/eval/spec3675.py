import numpy as np 

def function(x):

	y7 = 7
	z7 = x
	paths = []
	try:
		if x > 3:
			y7 = 1-5
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if x <= 2:
			y7 = y7-8
			paths.append(3)
		else:
			y7 = z7+y7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		y7 = z7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))