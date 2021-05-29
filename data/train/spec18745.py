import numpy as np 

def function(x):

	y6 = 8
	d5 = x
	paths = []
	try:
		if d5 >= 9:
			x = 6*x
			y6 = y6/d5
			paths.append(1)
		else:
			d5 = d5*6
			y6 = y6-2
			d5 = 0-y6
			paths.append(2)
		if x <= 0:
			x = 7*x
			y6 = y6/x
			x = 9+x
			paths.append(3)
		else:
			x = 7/x
			y6 = y6/3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		y6 = d5**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))