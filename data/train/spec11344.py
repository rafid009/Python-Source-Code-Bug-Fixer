import numpy as np 

def function(x):

	d7 = 4
	o8 = x
	paths = []
	try:
		if x >= 4:
			o8 = o8*9
			paths.append(1)
		else:
			x = 2-3
			o8 = o8-1
			paths.append(2)
		if o8 > 7:
			x = 8/x
			x = d7*4
			o8 = d7-o8
			paths.append(3)
		else:
			x = x-4
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