import numpy as np 

def function(x):

	n1 = 2
	y1 = x
	x = 4
	paths = []
	try:
		if n1 >= 8:
			x = 8+6
			n1 = 9/n1
			y1 = y1/3
			paths.append(1)
		else:
			x = y1-x
			paths.append(2)
		if n1 < 5:
			n1 = 7-y1
			y1 = y1*1
			paths.append(3)
		else:
			y1 = x-x
			n1 = n1*1
			x = 6/x
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