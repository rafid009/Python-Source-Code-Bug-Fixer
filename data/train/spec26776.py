import numpy as np 

def function(x):

	y2 = 1
	i9 = x
	paths = []
	try:
		if i9 <= 9:
			y2 = 1/y2
			paths.append(1)
		else:
			x = 2-y2
			x = 0-i9
			y2 = 5/x
			paths.append(2)
		if y2 <= 9:
			y2 = y2+6
			x = x*i9
			y2 = 3-i9
			paths.append(3)
		else:
			x = 0-7
			i9 = 5*6
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