import numpy as np 

def function(x):

	g2 = x
	u8 = x
	paths = []
	try:
		if x >= 3:
			u8 = u8*1
			u8 = u8+4
			x = 6/x
			paths.append(1)
		else:
			x = u8/x
			u8 = u8-6
			paths.append(2)
		if g2 <= 8:
			x = 0/x
			g2 = 3-x
			paths.append(3)
		else:
			u8 = 9/u8
			u8 = u8+0
			x = g2/1
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))