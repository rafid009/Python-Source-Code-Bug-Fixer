import numpy as np 

def function(x):

	y7 = 6
	d4 = x
	paths = []
	try:
		if x <= 4:
			y7 = 7-3
			d4 = 1/y7
			paths.append(1)
		else:
			d4 = 7+d4
			d4 = 7-d4
			x = x+d4
			paths.append(2)
		if d4 > 4:
			d4 = 9*d4
			y7 = y7/2
			d4 = 0/x
			paths.append(3)
		else:
			d4 = 7+d4
			d4 = d4*y7
			y7 = x/9
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		y7 = d4**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))