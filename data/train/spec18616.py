import numpy as np 

def function(x):

	a6 = x
	y0 = x
	paths = []
	try:
		if y0 <= 9:
			y0 = y0/3
			y0 = y0-2
			a6 = 8/5
			paths.append(1)
		else:
			a6 = 8/a6
			a6 = x+y0
			paths.append(2)
		if y0 < 2:
			x = x*1
			a6 = a6-9
			paths.append(3)
		else:
			a6 = a6/4
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))