import numpy as np 

def function(x):

	y8 = x
	f1 = x
	paths = []
	try:
		if f1 > 4:
			y8 = 9/y8
			y8 = y8-y8
			paths.append(1)
		else:
			f1 = f1*3
			y8 = 0-y8
			y8 = y8/6
			paths.append(2)
		if x > 7:
			y8 = 1/5
			y8 = 6*4
			f1 = 2-f1
			paths.append(3)
		else:
			y8 = y8-f1
			x = 4-x
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