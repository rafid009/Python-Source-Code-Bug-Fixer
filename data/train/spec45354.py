import numpy as np 

def function(x):

	y7 = 0
	x4 = 2
	paths = []
	try:
		if x4 > 6:
			x4 = x4*2
			x = x*8
			x4 = 9*6
			paths.append(1)
		else:
			x4 = x4-4
			x = x4*x
			y7 = y7/2
			paths.append(2)
		if x > 8:
			y7 = 6+x
			paths.append(3)
		else:
			y7 = y7-1
			x4 = 1/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))