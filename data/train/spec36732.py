import numpy as np 

def function(x):

	u8 = 4
	g5 = 9
	paths = []
	try:
		if u8 < 2:
			g5 = u8+g5
			x = x*2
			x = x+1
			paths.append(1)
		else:
			x = 8-x
			u8 = 0+u8
			paths.append(2)
		if g5 > 5:
			u8 = x+2
			g5 = g5+g5
			paths.append(3)
		else:
			u8 = u8*u8
			x = u8*7
			x = x-u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		g5 = u8**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))