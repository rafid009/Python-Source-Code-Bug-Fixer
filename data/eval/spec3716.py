import numpy as np 

def function(x):

	g7 = 2
	u8 = x
	paths = []
	try:
		if g7 > 6:
			g7 = u8+9
			g7 = g7-8
			u8 = u8+u8
			paths.append(1)
		else:
			g7 = 5*g7
			paths.append(2)
		if g7 > 5:
			u8 = 4+u8
			g7 = g7/u8
			paths.append(3)
		else:
			x = 7/x
			u8 = u8+u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))