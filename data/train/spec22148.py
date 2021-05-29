import numpy as np 

def function(x):

	b7 = 5
	y1 = 2
	paths = []
	try:
		if x > 1:
			x = 2/8
			b7 = b7*b7
			y1 = 9*y1
			paths.append(1)
		else:
			b7 = b7+8
			paths.append(2)
		if b7 >= 0:
			y1 = y1-5
			y1 = y1*9
			paths.append(3)
		else:
			x = 2/b7
			b7 = b7*b7
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