import numpy as np 

def function(x):

	g8 = 9
	u8 = 5
	paths = []
	try:
		if u8 < 7:
			g8 = 1-x
			paths.append(1)
		else:
			x = x-5
			g8 = 6-7
			g8 = u8/g8
			paths.append(2)
		if g8 >= 9:
			g8 = 9-g8
			x = u8+x
			u8 = u8/g8
			paths.append(3)
		else:
			u8 = u8-3
			g8 = g8-u8
			g8 = 0/g8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		g8 = u8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))