import numpy as np 

def function(x):

	y1 = x
	i4 = x
	x = 7
	paths = []
	try:
		if x >= 1:
			y1 = y1*4
			x = i4*9
			paths.append(1)
		else:
			x = x-y1
			i4 = 4*i4
			paths.append(2)
		if x <= 0:
			i4 = i4/8
			x = x/x
			paths.append(3)
		else:
			y1 = 6*y1
			i4 = 6*i4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))