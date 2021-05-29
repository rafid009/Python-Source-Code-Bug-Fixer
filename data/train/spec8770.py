import numpy as np 

def function(x):

	u8 = 6
	g4 = x
	paths = []
	try:
		if u8 < 5:
			g4 = g4/g4
			paths.append(1)
		else:
			x = 4-x
			x = x+9
			g4 = g4*u8
			paths.append(2)
		if u8 <= 9:
			u8 = u8/x
			paths.append(3)
		else:
			u8 = 9*1
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