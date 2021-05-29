import numpy as np 

def function(x):

	y6 = x
	d7 = x
	paths = []
	try:
		if x <= 8:
			d7 = 2-d7
			y6 = y6-5
			paths.append(1)
		else:
			d7 = 8/d7
			paths.append(2)
		if x <= 6:
			y6 = 0+d7
			d7 = d7-5
			d7 = d7+8
			paths.append(3)
		else:
			x = 2+3
			y6 = y6+9
			x = 1+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))