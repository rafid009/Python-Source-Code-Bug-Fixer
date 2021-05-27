import numpy as np 

def function(x):

	g8 = x
	u8 = 8
	paths = []
	try:
		if u8 < 2:
			u8 = 2/u8
			u8 = u8*u8
			paths.append(1)
		else:
			x = x*6
			u8 = u8*8
			paths.append(2)
		if g8 < 6:
			u8 = 5+g8
			u8 = 5-3
			g8 = 6-g8
			paths.append(3)
		else:
			g8 = g8+x
			g8 = g8*2
			g8 = 9*g8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))