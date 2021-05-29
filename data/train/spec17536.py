import numpy as np 

def function(x):

	o8 = 9
	n6 = 7
	x = 6
	paths = []
	try:
		if n6 >= 0:
			o8 = o8+2
			n6 = n6/6
			paths.append(1)
		else:
			n6 = 0-n6
			n6 = o8-5
			o8 = 5+8
			paths.append(2)
		if n6 < 9:
			o8 = 4-o8
			x = x-4
			o8 = o8+o8
			paths.append(3)
		else:
			x = x/o8
			x = x+o8
			o8 = x/6
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