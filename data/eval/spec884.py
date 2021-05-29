import numpy as np 

def function(x):

	x4 = x
	x3 = 2
	paths = []
	try:
		if x3 >= 7:
			x3 = 4-3
			paths.append(1)
		else:
			x4 = x4-4
			x3 = 5+4
			x3 = x3*9
			paths.append(2)
		if x4 < 3:
			x4 = x4*2
			x = x3*4
			x4 = x+x4
			paths.append(3)
		else:
			x4 = 7-x4
			x3 = 8+x3
			x4 = 4+x4
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))