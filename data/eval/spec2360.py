import numpy as np 

def function(x):

	u8 = x
	y1 = 6
	paths = []
	try:
		if u8 <= 5:
			y1 = 7/y1
			y1 = 6/y1
			x = x+8
			paths.append(1)
		else:
			x = 1*x
			u8 = u8+u8
			u8 = 4/u8
			paths.append(2)
		if y1 < 6:
			x = x*1
			y1 = y1+9
			paths.append(3)
		else:
			u8 = u8+1
			u8 = 0+7
			u8 = u8-6
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