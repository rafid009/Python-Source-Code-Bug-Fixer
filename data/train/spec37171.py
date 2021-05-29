import numpy as np 

def function(x):

	y1 = x
	d9 = x
	paths = []
	try:
		if y1 <= 0:
			d9 = y1+x
			y1 = y1+3
			paths.append(1)
		else:
			d9 = d9+8
			x = 2-x
			paths.append(2)
		if x <= 1:
			y1 = 8/y1
			d9 = d9-x
			d9 = d9*9
			paths.append(3)
		else:
			d9 = 2-d9
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