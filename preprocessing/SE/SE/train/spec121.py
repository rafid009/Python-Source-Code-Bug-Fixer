import numpy as np 

def function(x):

	y3 = 0
	y7 = 4
	paths = []
	try:
		if y7 < 8:
			y7 = 5*y7
			x = x+2
			y7 = y7/y7
			paths.append(1)
		else:
			y3 = 4+y3
			y7 = y7+5
			paths.append(2)
		if y3 > 8:
			x = 6*x
			y3 = y3+9
			paths.append(3)
		else:
			y7 = y7/3
			y7 = 5-y7
			y3 = 4-y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))