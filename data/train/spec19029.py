import numpy as np 

def function(x):

	o8 = 1
	y5 = x
	paths = []
	try:
		if o8 <= 5:
			y5 = o8/x
			paths.append(1)
		else:
			o8 = 9*o8
			o8 = o8+6
			y5 = y5*5
			paths.append(2)
		if y5 < 8:
			y5 = o8+7
			y5 = y5-1
			o8 = 6-5
			paths.append(3)
		else:
			o8 = o8*5
			x = x/2
			y5 = 6*y5
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