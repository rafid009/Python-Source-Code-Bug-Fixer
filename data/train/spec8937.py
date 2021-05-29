import numpy as np 

def function(x):

	y0 = x
	o5 = x
	paths = []
	try:
		if x <= 9:
			y0 = 6/y0
			x = x-o5
			paths.append(1)
		else:
			y0 = x/y0
			o5 = 2/o5
			x = 3+9
			paths.append(2)
		if x < 1:
			o5 = o5-o5
			y0 = 4*y0
			o5 = y0-o5
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))