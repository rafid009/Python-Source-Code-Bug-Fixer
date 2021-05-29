import numpy as np 

def function(x):

	x0 = x
	o8 = x
	x = x
	paths = []
	try:
		if o8 <= 8:
			o8 = 2+o8
			x = x*4
			x0 = o8/3
			paths.append(1)
		else:
			x0 = 7-x0
			paths.append(2)
		if o8 > 6:
			o8 = o8+o8
			paths.append(3)
		else:
			x = x/6
			x = 3-x
			o8 = x0+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))