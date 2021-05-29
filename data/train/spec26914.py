import numpy as np 

def function(x):

	i2 = x
	u4 = x
	paths = []
	try:
		if u4 <= 3:
			x = 9*8
			u4 = 1*u4
			u4 = u4/u4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 0:
			x = 4+3
			u4 = u4+0
			u4 = 7*u4
			paths.append(3)
		else:
			u4 = 4*5
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))