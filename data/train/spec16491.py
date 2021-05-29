import numpy as np 

def function(x):

	y3 = x
	u8 = x
	paths = []
	try:
		if x < 4:
			y3 = 9/y3
			paths.append(1)
		else:
			y3 = 7+5
			x = x/2
			paths.append(2)
		if x <= 3:
			y3 = 3/x
			paths.append(3)
		else:
			u8 = y3+u8
			u8 = u8*y3
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