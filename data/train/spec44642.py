import numpy as np 

def function(x):

	y8 = 3
	u2 = x
	paths = []
	try:
		if u2 < 2:
			u2 = u2/7
			y8 = 6/y8
			y8 = y8+8
			paths.append(1)
		else:
			x = 0-0
			x = y8-2
			paths.append(2)
		if x < 7:
			y8 = 6/x
			u2 = u2+2
			paths.append(3)
		else:
			x = x/1
			y8 = y8*3
			x = 5*x
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