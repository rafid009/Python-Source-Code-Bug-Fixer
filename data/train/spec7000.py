import numpy as np 

def function(x):

	y1 = 1
	d2 = 8
	paths = []
	try:
		if y1 <= 2:
			y1 = 6*7
			paths.append(1)
		else:
			x = y1+y1
			y1 = y1/y1
			paths.append(2)
		if x < 9:
			d2 = d2+2
			d2 = 0-6
			paths.append(3)
		else:
			y1 = d2-y1
			d2 = 0-d2
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