import numpy as np 

def function(x):

	y7 = x
	i2 = 6
	paths = []
	try:
		if x > 2:
			y7 = y7-x
			i2 = i2-4
			paths.append(1)
		else:
			y7 = 2-i2
			x = x+i2
			x = x/8
			paths.append(2)
		if i2 < 5:
			y7 = 5+y7
			paths.append(3)
		else:
			i2 = i2*y7
			i2 = y7/8
			i2 = i2-3
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		i2 = y7**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))