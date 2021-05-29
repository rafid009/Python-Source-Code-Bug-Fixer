import numpy as np 

def function(x):

	y0 = x
	o9 = x
	paths = []
	try:
		if o9 >= 8:
			y0 = 0+y0
			y0 = y0*3
			paths.append(1)
		else:
			y0 = y0/x
			paths.append(2)
		if y0 >= 7:
			o9 = y0*o9
			o9 = y0/o9
			y0 = y0-9
			paths.append(3)
		else:
			o9 = 7-o9
			o9 = o9*4
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))