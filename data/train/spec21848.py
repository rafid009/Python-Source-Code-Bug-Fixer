import numpy as np 

def function(x):

	o8 = x
	y0 = 8
	x = x
	paths = []
	try:
		if x <= 7:
			x = x/3
			y0 = 7-y0
			paths.append(1)
		else:
			y0 = 2*y0
			o8 = 8-o8
			paths.append(2)
		if x < 7:
			y0 = 4/o8
			o8 = 1*o8
			paths.append(3)
		else:
			o8 = 5/o8
			x = y0+2
			x = x-4
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