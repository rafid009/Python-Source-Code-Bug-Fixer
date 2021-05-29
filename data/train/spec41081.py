import numpy as np 

def function(x):

	k2 = x
	y1 = 1
	paths = []
	try:
		if y1 <= 5:
			y1 = y1*8
			x = 4+x
			paths.append(1)
		else:
			k2 = 9*k2
			y1 = x-y1
			paths.append(2)
		if x >= 3:
			x = 9*y1
			paths.append(3)
		else:
			x = 0-8
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))