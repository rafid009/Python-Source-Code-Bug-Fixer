import numpy as np 

def function(x):

	y2 = x
	o8 = x
	x = 0
	paths = []
	try:
		if y2 <= 3:
			o8 = o8*9
			y2 = y2+6
			paths.append(1)
		else:
			y2 = y2+o8
			o8 = 2-o8
			x = o8/7
			paths.append(2)
		if x >= 2:
			o8 = 9+o8
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		y2 = o8**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))