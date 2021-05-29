import numpy as np 

def function(x):

	i2 = 9
	z5 = x
	paths = []
	try:
		if i2 >= 6:
			i2 = x+7
			x = 3+7
			paths.append(1)
		else:
			x = 1-4
			x = 0+x
			paths.append(2)
		if z5 < 0:
			x = x/4
			i2 = i2-6
			paths.append(3)
		else:
			i2 = 9-7
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