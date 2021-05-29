import numpy as np 

def function(x):

	v7 = 6
	y1 = 5
	paths = []
	try:
		if x < 8:
			x = 6*y1
			y1 = 1+3
			x = x/4
			paths.append(1)
		else:
			y1 = y1-9
			y1 = y1*8
			paths.append(2)
		if x < 3:
			x = x/3
			y1 = y1/v7
			y1 = 8/y1
			paths.append(3)
		else:
			y1 = y1/8
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		v7 = y1**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))