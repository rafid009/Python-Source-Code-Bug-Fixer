import numpy as np 

def function(x):

	a1 = 6
	o8 = x
	paths = []
	try:
		if x < 4:
			x = o8+8
			paths.append(1)
		else:
			x = x-5
			a1 = 1-o8
			paths.append(2)
		if x <= 9:
			x = 0-a1
			o8 = 9+o8
			paths.append(3)
		else:
			o8 = o8-1
			x = 4-x
			x = x-o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))