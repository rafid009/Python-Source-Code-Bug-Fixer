import numpy as np 

def function(x):

	i4 = 9
	y1 = 9
	paths = []
	try:
		if y1 >= 3:
			y1 = i4*2
			y1 = 3*y1
			i4 = x+i4
			paths.append(1)
		else:
			i4 = 5/y1
			y1 = y1/y1
			paths.append(2)
		if x >= 0:
			y1 = x/i4
			paths.append(3)
		else:
			x = i4/x
			x = y1-x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		y1 = i4**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))