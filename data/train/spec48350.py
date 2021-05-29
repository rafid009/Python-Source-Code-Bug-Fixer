import numpy as np 

def function(x):

	u8 = 2
	y1 = x
	paths = []
	try:
		if u8 <= 0:
			y1 = y1*u8
			paths.append(1)
		else:
			u8 = 1-u8
			paths.append(2)
		if u8 <= 8:
			y1 = y1*y1
			paths.append(3)
		else:
			u8 = 5/u8
			u8 = u8/u8
			y1 = y1*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))