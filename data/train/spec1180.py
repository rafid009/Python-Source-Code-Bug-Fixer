import numpy as np 

def function(x):

	x5 = x
	u8 = x
	paths = []
	try:
		if x < 0:
			x5 = 7*x5
			u8 = 3+u8
			x = 4/x
			paths.append(1)
		else:
			u8 = u8/1
			u8 = u8*3
			x = u8*x
			paths.append(2)
		if x > 9:
			u8 = x/u8
			u8 = u8/1
			paths.append(3)
		else:
			x = x/4
			x5 = x5*x
			u8 = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))