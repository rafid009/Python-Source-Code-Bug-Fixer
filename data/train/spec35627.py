import numpy as np 

def function(x):

	g3 = 4
	u8 = 8
	paths = []
	try:
		if x < 8:
			g3 = g3+8
			g3 = 2-x
			g3 = x-x
			paths.append(1)
		else:
			g3 = g3-u8
			u8 = 6-g3
			u8 = g3+u8
			paths.append(2)
		if x < 0:
			x = 9*x
			u8 = u8*5
			g3 = 1*g3
			paths.append(3)
		else:
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))