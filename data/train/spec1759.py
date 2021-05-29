import numpy as np 

def function(x):

	y4 = x
	u8 = 5
	paths = []
	try:
		if u8 > 4:
			u8 = y4-u8
			x = 9+x
			paths.append(1)
		else:
			x = 1/x
			x = 8-x
			paths.append(2)
		if y4 <= 1:
			y4 = u8/y4
			u8 = 4+u8
			u8 = 8-u8
			paths.append(3)
		else:
			y4 = y4*9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))