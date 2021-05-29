import numpy as np 

def function(x):

	y5 = 9
	a5 = 4
	paths = []
	try:
		if a5 < 3:
			y5 = y5+1
			y5 = 7/y5
			paths.append(1)
		else:
			a5 = a5*7
			paths.append(2)
		if x >= 1:
			x = 7-x
			paths.append(3)
		else:
			x = 3*3
			y5 = y5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))