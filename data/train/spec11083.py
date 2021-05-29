import numpy as np 

def function(x):

	i8 = 9
	y5 = x
	paths = []
	try:
		if i8 >= 7:
			y5 = 0-4
			y5 = i8*5
			y5 = y5+7
			paths.append(1)
		else:
			x = i8/y5
			i8 = i8+8
			paths.append(2)
		if y5 < 8:
			i8 = 1-i8
			i8 = i8*1
			paths.append(3)
		else:
			y5 = y5/2
			y5 = 4*x
			y5 = i8*x
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