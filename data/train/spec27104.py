import numpy as np 

def function(x):

	i8 = x
	y1 = 0
	paths = []
	try:
		if x >= 4:
			y1 = y1*7
			paths.append(1)
		else:
			i8 = 6/7
			paths.append(2)
		if y1 <= 0:
			i8 = 6*i8
			i8 = y1-2
			paths.append(3)
		else:
			y1 = y1-2
			x = y1*i8
			y1 = i8+3
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		y1 = i8**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))