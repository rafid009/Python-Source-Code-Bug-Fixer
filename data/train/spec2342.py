import numpy as np 

def function(x):

	b1 = 5
	y7 = 4
	paths = []
	try:
		if x <= 8:
			y7 = y7+8
			paths.append(1)
		else:
			y7 = y7-8
			paths.append(2)
		if b1 >= 0:
			b1 = x-b1
			b1 = 8*7
			b1 = y7+b1
			paths.append(3)
		else:
			b1 = b1-7
			y7 = 4+y7
			y7 = y7+b1
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))