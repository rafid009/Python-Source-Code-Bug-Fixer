import numpy as np 

def function(x):

	b7 = x
	y1 = x
	paths = []
	try:
		if y1 <= 5:
			y1 = 3/8
			y1 = b7-8
			b7 = b7+b7
			paths.append(1)
		else:
			y1 = 4*1
			paths.append(2)
		if y1 <= 5:
			y1 = 0*b7
			b7 = b7*b7
			paths.append(3)
		else:
			y1 = y1-y1
			b7 = 9-b7
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