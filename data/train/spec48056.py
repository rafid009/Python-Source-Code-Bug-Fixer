import numpy as np 

def function(x):

	y8 = 3
	o8 = x
	paths = []
	try:
		if y8 >= 6:
			x = 6-5
			paths.append(1)
		else:
			o8 = o8/1
			paths.append(2)
		if o8 > 7:
			y8 = y8+y8
			paths.append(3)
		else:
			o8 = o8*6
			x = 3-2
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		y8 = o8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))