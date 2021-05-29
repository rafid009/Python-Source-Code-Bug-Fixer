import numpy as np 

def function(x):

	a1 = 5
	y0 = 0
	paths = []
	try:
		if y0 <= 1:
			a1 = 3-x
			y0 = 8/x
			x = y0*2
			paths.append(1)
		else:
			x = 4-x
			y0 = y0+3
			x = 2-2
			paths.append(2)
		if a1 >= 5:
			x = 8+a1
			x = y0-3
			paths.append(3)
		else:
			a1 = y0-a1
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		a1 = y0**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))