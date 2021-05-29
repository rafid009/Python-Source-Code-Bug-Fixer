import numpy as np 

def function(x):

	y1 = 3
	a7 = x
	x = x
	paths = []
	try:
		if a7 > 9:
			x = x+1
			y1 = y1/x
			paths.append(1)
		else:
			x = 4*y1
			a7 = 2*a7
			a7 = 7+a7
			paths.append(2)
		if x >= 2:
			a7 = 1*a7
			y1 = 2-x
			paths.append(3)
		else:
			x = 9*x
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		y1 = a7**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))