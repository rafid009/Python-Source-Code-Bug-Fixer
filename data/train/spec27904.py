import numpy as np 

def function(x):

	y2 = x
	o4 = 9
	paths = []
	try:
		if y2 >= 9:
			y2 = y2+7
			x = x+o4
			paths.append(1)
		else:
			o4 = 9-x
			paths.append(2)
		if o4 <= 9:
			o4 = o4-0
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))