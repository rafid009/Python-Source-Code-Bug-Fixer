import numpy as np 

def function(x):

	b7 = x
	y6 = x
	paths = []
	try:
		if b7 < 0:
			b7 = 9*y6
			paths.append(1)
		else:
			y6 = 4/y6
			paths.append(2)
		if b7 < 0:
			x = 9*9
			b7 = 1*b7
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))