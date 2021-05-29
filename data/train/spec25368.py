import numpy as np 

def function(x):

	o8 = 5
	y5 = x
	x = x
	paths = []
	try:
		if x > 2:
			y5 = 1/7
			x = 1/x
			o8 = 0-o8
			paths.append(1)
		else:
			o8 = o8/y5
			x = x+x
			paths.append(2)
		if x >= 8:
			x = 7+4
			o8 = 2/8
			paths.append(3)
		else:
			y5 = y5/6
			o8 = 6-4
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))