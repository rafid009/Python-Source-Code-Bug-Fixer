import numpy as np 

def function(x):

	y0 = 2
	o7 = x
	paths = []
	try:
		if x <= 2:
			x = 8+x
			o7 = 1*o7
			y0 = 0+5
			paths.append(1)
		else:
			y0 = y0*6
			y0 = y0*y0
			o7 = x/o7
			paths.append(2)
		if y0 < 9:
			x = 8-x
			x = x*7
			y0 = y0-4
			paths.append(3)
		else:
			o7 = 7/8
			y0 = y0/x
			y0 = o7*8
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))