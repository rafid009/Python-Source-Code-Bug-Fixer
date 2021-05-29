import numpy as np 

def function(x):

	e8 = x
	y0 = x
	paths = []
	try:
		if y0 > 6:
			y0 = y0/6
			y0 = 8+y0
			y0 = y0+2
			paths.append(1)
		else:
			y0 = y0/1
			y0 = 5/y0
			x = 1+4
			paths.append(2)
		if y0 >= 9:
			e8 = e8*5
			y0 = y0+x
			paths.append(3)
		else:
			e8 = e8+2
			e8 = x/e8
			x = x-y0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))