import numpy as np 

def function(x):

	y2 = 8
	x9 = x
	paths = []
	try:
		if y2 > 7:
			x = 9*x
			paths.append(1)
		else:
			x9 = 5*x
			x = 2/3
			paths.append(2)
		if x >= 9:
			x9 = 4/8
			paths.append(3)
		else:
			y2 = y2*y2
			y2 = y2+0
			y2 = y2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))