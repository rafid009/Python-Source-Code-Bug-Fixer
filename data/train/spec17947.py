import numpy as np 

def function(x):

	y0 = 5
	o4 = x
	paths = []
	try:
		if x <= 2:
			o4 = o4-6
			x = 4+x
			y0 = y0+2
			paths.append(1)
		else:
			y0 = y0+4
			y0 = y0-7
			paths.append(2)
		if y0 > 4:
			o4 = 0/o4
			o4 = x-5
			y0 = x*y0
			paths.append(3)
		else:
			x = x-x
			y0 = y0+y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		o4 = y0**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))