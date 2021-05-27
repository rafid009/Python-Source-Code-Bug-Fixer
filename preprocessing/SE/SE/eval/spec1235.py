import numpy as np 

def function(x):

	y1 = x
	b7 = x
	paths = []
	try:
		if y1 > 9:
			x = x-b7
			paths.append(1)
		else:
			b7 = b7-6
			paths.append(2)
		if y1 < 1:
			b7 = x/x
			x = x+6
			x = x/8
			paths.append(3)
		else:
			x = x-7
			y1 = 9+y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))