import numpy as np 

def function(x):

	o7 = 5
	y0 = 8
	paths = []
	try:
		if y0 < 4:
			o7 = 6+5
			paths.append(1)
		else:
			x = 4+x
			y0 = 8/y0
			paths.append(2)
		if o7 >= 0:
			o7 = x-5
			x = x-y0
			y0 = 0*x
			paths.append(3)
		else:
			o7 = y0*5
			x = o7*1
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		y0 = o7**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))