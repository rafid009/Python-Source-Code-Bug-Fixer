import numpy as np 

def function(x):

	x0 = 8
	y8 = x
	paths = []
	try:
		if x < 7:
			y8 = y8*4
			paths.append(1)
		else:
			x = y8+x
			y8 = y8+0
			x = x/9
			paths.append(2)
		if x0 >= 2:
			x0 = x0/x0
			paths.append(3)
		else:
			y8 = 1+x
			y8 = 8-y8
			x0 = 6+x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))