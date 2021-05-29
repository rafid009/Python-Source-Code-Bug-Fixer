import numpy as np 

def function(x):

	u8 = 2
	y2 = x
	paths = []
	try:
		if x < 7:
			u8 = u8+u8
			paths.append(1)
		else:
			u8 = u8/y2
			y2 = u8-4
			paths.append(2)
		if y2 >= 3:
			y2 = u8+y2
			x = 2-0
			x = u8*x
			paths.append(3)
		else:
			u8 = y2*7
			y2 = y2+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))