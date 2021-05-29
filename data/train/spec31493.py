import numpy as np 

def function(x):

	g2 = 1
	u8 = x
	paths = []
	try:
		if u8 < 3:
			u8 = 7-u8
			paths.append(1)
		else:
			u8 = u8*u8
			x = 8+x
			paths.append(2)
		if u8 > 3:
			u8 = 6-u8
			paths.append(3)
		else:
			u8 = 7*u8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))