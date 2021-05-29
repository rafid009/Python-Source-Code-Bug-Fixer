import numpy as np 

def function(x):

	x4 = x
	paths = []
	try:
		if x <= 1:
			x4 = x4/9
			x4 = x4+8
			x = x/3
			paths.append(1)
		else:
			x4 = 6+6
			x = x4-x4
			x4 = x4+8
			paths.append(2)
		if x4 <= 8:
			x4 = 0-3
			x4 = x4*4
			x4 = 0+x4
			paths.append(3)
		else:
			x4 = x4-1
			x4 = x4-3
			x4 = 6-x4
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