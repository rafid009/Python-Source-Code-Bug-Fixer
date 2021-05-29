import numpy as np 

def function(x):

	o4 = x
	y5 = x
	paths = []
	try:
		if y5 < 7:
			o4 = x-6
			x = 8+4
			o4 = 3-5
			paths.append(1)
		else:
			y5 = o4*y5
			o4 = 8/y5
			y5 = y5/1
			paths.append(2)
		if y5 >= 3:
			y5 = y5-y5
			x = o4*3
			o4 = y5-6
			paths.append(3)
		else:
			o4 = 8*o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		y5 = o4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))