import numpy as np 

def function(x):

	d9 = x
	y0 = 8
	x = 0
	paths = []
	try:
		if y0 < 8:
			x = 6-x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x > 1:
			y0 = 7*y0
			d9 = d9-8
			paths.append(3)
		else:
			y0 = 7-y0
			y0 = x/3
			d9 = d9+7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		y0 = d9**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))