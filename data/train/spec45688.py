import numpy as np 

def function(x):

	y0 = x
	paths = []
	try:
		if y0 > 8:
			x = x/2
			y0 = 5/8
			y0 = y0-3
			paths.append(1)
		else:
			y0 = 5*8
			y0 = y0*8
			y0 = 0+y0
			paths.append(2)
		if y0 <= 4:
			y0 = y0/x
			paths.append(3)
		else:
			x = x-y0
			y0 = y0*5
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))