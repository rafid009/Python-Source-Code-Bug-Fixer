import numpy as np 

def function(x):

	y8 = 1
	e4 = x
	x = x
	paths = []
	try:
		if y8 < 3:
			y8 = y8*9
			paths.append(1)
		else:
			e4 = 1*3
			e4 = 2*1
			e4 = 2-6
			paths.append(2)
		if e4 > 0:
			e4 = 7+e4
			paths.append(3)
		else:
			y8 = x/x
			e4 = e4/1
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