import numpy as np 

def function(x):

	i2 = 2
	y0 = 8
	paths = []
	try:
		if x < 5:
			i2 = i2-5
			paths.append(1)
		else:
			y0 = 0+4
			x = i2/9
			paths.append(2)
		if x < 1:
			y0 = x/y0
			paths.append(3)
		else:
			i2 = i2-0
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		y0 = i2**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))