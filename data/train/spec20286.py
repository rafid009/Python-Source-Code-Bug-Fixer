import numpy as np 

def function(x):

	a6 = 1
	y0 = 1
	paths = []
	try:
		if x < 3:
			a6 = 9/a6
			x = x+9
			y0 = 3*1
			paths.append(1)
		else:
			x = 9*6
			a6 = a6*9
			paths.append(2)
		if y0 > 1:
			a6 = 1*y0
			y0 = y0/8
			paths.append(3)
		else:
			x = a6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))