import numpy as np 

def function(x):

	a4 = 5
	y3 = 0
	paths = []
	try:
		if a4 > 6:
			y3 = y3/8
			paths.append(1)
		else:
			y3 = 7-a4
			paths.append(2)
		if y3 >= 2:
			y3 = y3-x
			paths.append(3)
		else:
			x = x/8
			y3 = y3+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))