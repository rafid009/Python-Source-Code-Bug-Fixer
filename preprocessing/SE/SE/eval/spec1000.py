import numpy as np 

def function(x):

	h7 = 8
	i2 = 1
	paths = []
	try:
		if i2 >= 6:
			x = x-6
			h7 = h7/h7
			i2 = i2-4
			paths.append(1)
		else:
			x = 2-x
			h7 = 0-4
			h7 = x-i2
			paths.append(2)
		if i2 < 2:
			x = x-2
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))