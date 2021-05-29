import numpy as np 

def function(x):

	i2 = 5
	u4 = x
	paths = []
	try:
		if x > 1:
			i2 = x/x
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x >= 2:
			u4 = u4+u4
			u4 = x/u4
			i2 = i2/x
			paths.append(3)
		else:
			i2 = i2*u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))