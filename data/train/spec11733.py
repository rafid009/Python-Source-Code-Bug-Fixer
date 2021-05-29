import numpy as np 

def function(x):

	y1 = 0
	o4 = 2
	paths = []
	try:
		if y1 > 8:
			y1 = 8*y1
			paths.append(1)
		else:
			y1 = y1-o4
			paths.append(2)
		if x > 7:
			o4 = o4+4
			x = 1-x
			y1 = y1+0
			paths.append(3)
		else:
			y1 = 8+y1
			x = x-0
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