import numpy as np 

def function(x):

	u8 = x
	x1 = 6
	x = 0
	paths = []
	try:
		if u8 < 0:
			x1 = 4+x1
			x1 = x1/3
			x = x+x1
			paths.append(1)
		else:
			u8 = u8+7
			paths.append(2)
		if x1 > 2:
			x = 7+4
			paths.append(3)
		else:
			x1 = x1+3
			u8 = 0/u8
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