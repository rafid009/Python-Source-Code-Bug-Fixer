import numpy as np 

def function(x):

	y7 = 8
	x2 = 9
	paths = []
	try:
		if x2 < 0:
			x2 = y7*x2
			y7 = 9-y7
			y7 = 6*y7
			paths.append(1)
		else:
			x = 7*x
			y7 = 5-y7
			x2 = 2*x2
			paths.append(2)
		if x2 <= 0:
			y7 = 2+x
			x2 = 6/x2
			paths.append(3)
		else:
			x2 = x2/x2
			y7 = x+0
			x2 = 8/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))