import numpy as np 

def function(x):

	y0 = x
	k4 = x
	paths = []
	try:
		if k4 < 3:
			y0 = 1+3
			paths.append(1)
		else:
			y0 = 5+y0
			k4 = y0/k4
			x = 5-x
			paths.append(2)
		if x < 9:
			k4 = 3+5
			x = 6/x
			paths.append(3)
		else:
			k4 = 0/7
			k4 = 4+y0
			y0 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))