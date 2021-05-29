import numpy as np 

def function(x):

	x0 = 4
	y2 = 1
	paths = []
	try:
		if y2 <= 5:
			y2 = x+2
			x0 = 4-7
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if x0 > 8:
			x = x-6
			x0 = 9/x0
			paths.append(3)
		else:
			x0 = x0*1
			y2 = y2-y2
			x0 = x0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))