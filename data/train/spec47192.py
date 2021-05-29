import numpy as np 

def function(x):

	u8 = x
	y3 = 3
	paths = []
	try:
		if x <= 7:
			u8 = u8/6
			y3 = 5/2
			y3 = 9*u8
			paths.append(1)
		else:
			y3 = y3+x
			y3 = 3/y3
			paths.append(2)
		if x <= 5:
			x = x+6
			paths.append(3)
		else:
			y3 = y3+y3
			x = 8+y3
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		u8 = y3**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))