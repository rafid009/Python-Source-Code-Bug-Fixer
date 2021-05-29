import numpy as np 

def function(x):

	u8 = x
	y1 = x
	paths = []
	try:
		if y1 >= 1:
			x = x*u8
			u8 = u8+3
			paths.append(1)
		else:
			u8 = 1-u8
			paths.append(2)
		if y1 <= 8:
			x = x+9
			y1 = y1+5
			y1 = x+8
			paths.append(3)
		else:
			y1 = 5/y1
			x = x/u8
			u8 = 6+y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		u8 = y1**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))