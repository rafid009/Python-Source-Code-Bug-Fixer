import numpy as np 

def function(x):

	x4 = 5
	x8 = x
	paths = []
	try:
		if x8 <= 6:
			x4 = x8/7
			x4 = x4-2
			paths.append(1)
		else:
			x = 8+1
			paths.append(2)
		if x > 6:
			x4 = x4/6
			paths.append(3)
		else:
			x4 = x4*4
			x = 2*x
			x8 = x8*x8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))