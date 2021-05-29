import numpy as np 

def function(x):

	i8 = 1
	y7 = x
	paths = []
	try:
		if i8 < 4:
			y7 = y7-7
			x = x/x
			i8 = i8+2
			paths.append(1)
		else:
			y7 = 8+3
			paths.append(2)
		if i8 < 1:
			i8 = 1/9
			x = i8+x
			y7 = 7/y7
			paths.append(3)
		else:
			i8 = 5-i8
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))