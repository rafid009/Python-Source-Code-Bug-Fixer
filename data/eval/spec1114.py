import numpy as np 

def function(x):

	x4 = x
	paths = []
	try:
		if x4 <= 0:
			x4 = x4/1
			x4 = x4/x4
			x4 = x4+4
			paths.append(1)
		else:
			x4 = 8-5
			x4 = 9-0
			x = 1-4
			paths.append(2)
		if x4 < 5:
			x4 = 7-x4
			x = 1/1
			x4 = 8*x4
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))