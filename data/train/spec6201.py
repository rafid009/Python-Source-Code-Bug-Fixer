import numpy as np 

def function(x):

	y0 = x
	i1 = x
	paths = []
	try:
		if y0 >= 7:
			i1 = 1/y0
			i1 = i1*5
			paths.append(1)
		else:
			y0 = y0+3
			x = x/1
			paths.append(2)
		if y0 > 9:
			i1 = 7/i1
			x = x+7
			paths.append(3)
		else:
			x = 7+x
			y0 = y0-2
			i1 = i1/8
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