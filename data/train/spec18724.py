import numpy as np 

def function(x):

	y1 = x
	o4 = 6
	paths = []
	try:
		if x < 2:
			y1 = 7/y1
			paths.append(1)
		else:
			x = 6*7
			paths.append(2)
		if y1 > 1:
			o4 = 7/3
			x = 4+5
			x = 7+x
			paths.append(3)
		else:
			o4 = y1*o4
			o4 = o4+7
			x = 0/o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))