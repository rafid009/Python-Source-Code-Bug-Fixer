import numpy as np 

def function(x):

	l8 = x
	y5 = 5
	paths = []
	try:
		if x < 3:
			l8 = l8-8
			y5 = l8/3
			y5 = y5-9
			paths.append(1)
		else:
			x = 7-x
			l8 = 1+0
			paths.append(2)
		if x >= 9:
			y5 = 8-y5
			y5 = 2/y5
			x = 3/x
			paths.append(3)
		else:
			l8 = l8*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))