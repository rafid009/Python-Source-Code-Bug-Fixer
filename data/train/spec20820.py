import numpy as np 

def function(x):

	u8 = x
	g6 = 9
	x = x
	paths = []
	try:
		if u8 < 8:
			g6 = 3/x
			u8 = u8/1
			g6 = 9/g6
			paths.append(1)
		else:
			u8 = x*u8
			x = x/u8
			g6 = 3-g6
			paths.append(2)
		if u8 <= 9:
			u8 = u8/g6
			g6 = 6*7
			g6 = 0-g6
			paths.append(3)
		else:
			x = x*1
			g6 = 0*g6
			u8 = u8/3
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))