import numpy as np 

def function(x):

	u6 = 7
	y8 = x
	paths = []
	try:
		if x <= 9:
			u6 = 6+6
			x = 5*x
			paths.append(1)
		else:
			x = y8*1
			x = 1/x
			y8 = u6+x
			paths.append(2)
		if y8 > 8:
			y8 = 8/y8
			x = x+x
			paths.append(3)
		else:
			x = 8-x
			y8 = 9/u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))