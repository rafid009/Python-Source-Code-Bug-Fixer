import numpy as np 

def function(x):

	u8 = 1
	a9 = x
	paths = []
	try:
		if a9 <= 2:
			a9 = 0/u8
			u8 = u8/u8
			paths.append(1)
		else:
			x = 9*1
			u8 = u8+7
			paths.append(2)
		if x >= 2:
			u8 = u8/3
			u8 = u8-9
			x = x*a9
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))