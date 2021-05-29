import numpy as np 

def function(x):

	x4 = x
	y7 = x
	paths = []
	try:
		if x < 6:
			x = 2+x
			y7 = x*y7
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if x4 > 7:
			x = 0/8
			paths.append(3)
		else:
			y7 = y7/x
			x = 4/x
			y7 = 7/2
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		y7 = x4**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))