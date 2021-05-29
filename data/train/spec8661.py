import numpy as np 

def function(x):

	y8 = x
	n3 = 5
	paths = []
	try:
		if y8 > 0:
			y8 = y8/3
			paths.append(1)
		else:
			x = 7+x
			y8 = y8*4
			paths.append(2)
		if y8 < 1:
			x = x+2
			y8 = y8/6
			paths.append(3)
		else:
			x = x-5
			y8 = 2-y8
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