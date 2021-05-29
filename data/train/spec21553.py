import numpy as np 

def function(x):

	a0 = x
	y5 = x
	x = 9
	paths = []
	try:
		if a0 < 4:
			a0 = a0-3
			paths.append(1)
		else:
			x = 4-x
			a0 = 8*a0
			paths.append(2)
		if a0 >= 6:
			y5 = y5*a0
			y5 = y5/9
			a0 = 8*6
			paths.append(3)
		else:
			x = a0*5
			a0 = a0*3
			a0 = x/y5
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