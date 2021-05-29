import numpy as np 

def function(x):

	y1 = x
	n4 = x
	x = 9
	paths = []
	try:
		if x > 1:
			n4 = 5*y1
			paths.append(1)
		else:
			y1 = 3/1
			y1 = y1/y1
			n4 = 6/x
			paths.append(2)
		if n4 <= 8:
			y1 = 1*y1
			x = 1-5
			paths.append(3)
		else:
			y1 = y1*4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		y1 = n4**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))