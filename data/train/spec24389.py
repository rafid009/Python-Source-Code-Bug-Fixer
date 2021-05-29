import numpy as np 

def function(x):

	y7 = 3
	y1 = 9
	x = x
	paths = []
	try:
		if y7 >= 6:
			y7 = y7*4
			y7 = y1/5
			paths.append(1)
		else:
			y1 = 2+y1
			y1 = y1-5
			x = 2*x
			paths.append(2)
		if x < 3:
			y7 = y7/y7
			y7 = 5+y7
			paths.append(3)
		else:
			x = 5+y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))