import numpy as np 

def function(x):

	y5 = 3
	y0 = 8
	paths = []
	try:
		if y0 <= 4:
			y0 = x+x
			y5 = x/7
			x = 7/x
			paths.append(1)
		else:
			y5 = x/y0
			x = x+x
			paths.append(2)
		if y0 >= 3:
			y5 = 4-x
			paths.append(3)
		else:
			y5 = y5*3
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