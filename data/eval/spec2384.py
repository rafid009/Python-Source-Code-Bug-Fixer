import numpy as np 

def function(x):

	y6 = 1
	i2 = 1
	paths = []
	try:
		if x >= 1:
			i2 = 1-2
			paths.append(1)
		else:
			i2 = i2*9
			i2 = 7*1
			paths.append(2)
		if y6 > 5:
			x = x*9
			x = 1/x
			x = x-6
			paths.append(3)
		else:
			y6 = y6*2
			y6 = y6-x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		y6 = i2**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))