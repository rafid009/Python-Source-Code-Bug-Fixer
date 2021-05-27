import numpy as np 

def function(x):

	y8 = x
	u8 = x
	paths = []
	try:
		if u8 < 7:
			x = x+8
			paths.append(1)
		else:
			u8 = u8-7
			y8 = y8+5
			u8 = 9/y8
			paths.append(2)
		if y8 > 1:
			y8 = y8/1
			u8 = 2*7
			y8 = 2-4
			paths.append(3)
		else:
			y8 = 0/y8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		y8 = u8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))