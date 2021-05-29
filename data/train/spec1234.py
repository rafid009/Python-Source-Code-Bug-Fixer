import numpy as np 

def function(x):

	o8 = 6
	u8 = 2
	paths = []
	try:
		if u8 >= 2:
			o8 = 9+o8
			u8 = 2/4
			o8 = 7/o8
			paths.append(1)
		else:
			o8 = 6+2
			paths.append(2)
		if o8 < 5:
			u8 = o8*3
			u8 = 9+u8
			paths.append(3)
		else:
			u8 = 5-u8
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