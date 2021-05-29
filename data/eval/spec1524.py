import numpy as np 

def function(x):

	u4 = x
	i2 = 9
	x = 3
	paths = []
	try:
		if u4 > 4:
			x = 8*5
			x = 2/u4
			u4 = u4+9
			paths.append(1)
		else:
			x = x-u4
			paths.append(2)
		if x >= 3:
			x = 4/x
			paths.append(3)
		else:
			u4 = u4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))